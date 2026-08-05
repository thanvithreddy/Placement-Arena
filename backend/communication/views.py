import re
import logging
import requests as http_requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import SpeechTopic, SpeechAttempt
from .serializers import SpeechTopicSerializer, SpeechAttemptSerializer, SpeechAttemptCreateSerializer

logger = logging.getLogger('placement_arena')


# ════════════════════════════════════════════════════════════════════════════════
#  GEMINI AI HELPER
# ════════════════════════════════════════════════════════════════════════════════

def _call_gemini(prompt: str, temperature: float = 0.3) -> str:
    """
    Call Gemini REST API with multi-model fallback (gemini-1.5-flash, gemini-1.5-pro, gemini-pro).
    """
    api_key = getattr(settings, 'GEMINI_API_KEY', '')
    if not api_key:
        raise ValueError('GEMINI_API_KEY not configured')

    models = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    last_err = None
    for model in models:
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}'
        payload = {
            'contents': [{'parts': [{'text': prompt}]}],
            'generationConfig': {
                'temperature': temperature,
                'maxOutputTokens': 2048,
            }
        }
        try:
            resp = http_requests.post(url, json=payload, timeout=25)
            if resp.status_code == 200:
                data = resp.json()
                candidates = data.get('candidates', [])
                if candidates and 'content' in candidates[0]:
                    parts = candidates[0]['content'].get('parts', [])
                    if parts and 'text' in parts[0]:
                        return parts[0]['text'].strip()
            else:
                last_err = f"{resp.status_code}: {resp.text[:200]}"
        except Exception as e:
            last_err = str(e)

    raise RuntimeError(f"Gemini API call failed across models: {last_err}")


# ════════════════════════════════════════════════════════════════════════════════
#  ENGLISH SPEECH ANALYSIS ENGINE
# ════════════════════════════════════════════════════════════════════════════════

# Filler words (for detection — this is still rule-based, fast, reliable)
FILLER_WORDS = [
    'you know what', 'i mean like', 'sort of like', 'kind of like',
    'you know', 'i mean', 'sort of', 'kind of', 'so yeah', 'okay so',
    'right so', 'and so', 'so basically', 'so actually', 'so like',
    'um', 'uh', 'umm', 'uhh', 'er', 'err', 'hmm', 'hm',
    'basically', 'literally', 'honestly', 'obviously',
]


def _detect_fillers(text: str):
    text_lower = text.lower()
    found, count = [], 0
    for fw in FILLER_WORDS:
        pattern = r'\b' + re.escape(fw) + r'\b'
        matches = re.findall(pattern, text_lower)
        if matches:
            found.append(fw)
            count += len(matches)
    return found, count


def _gemini_analyze_speech(transcript: str) -> dict:
    """
    Use Gemini to produce grammar corrections, vocabulary upgrades, and a
    placement-grade rewritten version of the candidate's speech.
    Returns a dict with keys: corrected_transcript, grammar_errors, vocabulary_upgrades, tips_extra
    """
    prompt = f"""You are an expert HR interviewer and English language coach for Indian engineering students preparing for placement interviews.

A candidate spoke the following text during a practice session:

CANDIDATE SPEECH:
\"\"\"{transcript}\"\"\"

Your task:
1. Identify ALL grammar errors (verb tense, subject-verb agreement, article errors, wrong prepositions, informal constructs, etc.)
2. Identify informal words/phrases that should be upgraded to professional vocabulary
3. Rewrite the entire speech in formal, placement-ready English — fix ALL issues, not just the patterns — make it sound like a confident engineering graduate

Respond ONLY in this exact JSON format (no markdown, no extra text):
{{
  "corrected_transcript": "Full formal rewrite of the speech",
  "grammar_errors": [
    {{"original": "original wrong phrase", "corrected": "corrected phrase", "type": "explanation of error"}}
  ],
  "vocabulary_upgrades": [
    {{"original": "informal word", "upgrade": "professional word", "reason": "why this upgrade"}}
  ],
  "extra_tips": ["specific tip 1", "specific tip 2"]
}}"""

    try:
        raw = _call_gemini(prompt, temperature=0.2)
        # Strip markdown code fences if present
        raw = re.sub(r'^```(?:json)?\s*', '', raw, flags=re.MULTILINE)
        raw = re.sub(r'\s*```$', '', raw, flags=re.MULTILINE)
        import json
        result = json.loads(raw.strip())
        return result
    except Exception as e:
        return {
            'corrected_transcript': '',
            'grammar_errors': [],
            'vocabulary_upgrades': [],
            'extra_tips': [],
            '_error': str(e),
        }


def _rule_based_correct(text: str):
    """
    Comprehensive rule-based grammar corrector — covers 80+ common Indian English errors.
    Used as fallback when Gemini API key is not configured.
    """
    PHRASE_REWRITES = [
        # ── Tense errors (very common in Indian English) ──────────────────────────
        (r'\byesterday I go\b', 'yesterday I went', 'Past tense error: "go" → "went"'),
        (r'\byesterday I goes\b', 'yesterday I went', 'Past tense error: "goes" → "went"'),
        (r'\byesterday I come\b', 'yesterday I came', 'Past tense error: "come" → "came"'),
        (r'\byesterday I see\b', 'yesterday I saw', 'Past tense error: "see" → "saw"'),
        (r'\byesterday I eat\b', 'yesterday I ate', 'Past tense error: "eat" → "ate"'),
        (r'\byesterday I buy\b', 'yesterday I bought', 'Past tense error: "buy" → "bought"'),
        (r'\byesterday I give\b', 'yesterday I gave', 'Past tense error: "give" → "gave"'),
        (r'\byesterday I take\b', 'yesterday I took', 'Past tense error: "take" → "took"'),
        (r'\byesterday I make\b', 'yesterday I made', 'Past tense error: "make" → "made"'),
        (r'\byesterday I tell\b', 'yesterday I told', 'Past tense error: "tell" → "told"'),
        (r'\byesterday I speak\b', 'yesterday I spoke', 'Past tense error: "speak" → "spoke"'),
        (r'\byesterday I write\b', 'yesterday I wrote', 'Past tense error: "write" → "wrote"'),
        (r'\byesterday I run\b', 'yesterday I ran', 'Past tense error: "run" → "ran"'),
        (r'\byesterday I do\b', 'yesterday I did', 'Past tense error: "do" → "did"'),
        (r'\byesterday I meet\b', 'yesterday I met', 'Past tense error: "meet" → "met"'),
        (r'\byesterday I find\b', 'yesterday I found', 'Past tense error: "find" → "found"'),
        (r'\bmy day start\b', 'my day started', 'Past tense: "day start" → "day started"'),
        (r'\bday start\b', 'day started', 'Past tense: "day start" → "day started"'),
        (r'\bI am wake up\b', 'I woke up', 'Verb tense: "am wake up" → "woke up"'),
        (r'\bI am woke up\b', 'I woke up', 'Verb tense: "am woke up" → "woke up"'),
        (r'\bI wake up at\b', 'I woke up at', 'Past tense: "wake up" → "woke up"'),
        (r'\bworked up very late\b', 'woke up very late', 'Word choice: "worked up" → "woke up"'),
        (r'\bworked up at\b', 'woke up at', 'Word choice: "worked up" → "woke up"'),
        (r'\beat to egg\b', 'ate eggs', 'Preposition & tense error: "eat to egg" → "ate eggs"'),
        (r'\beat egg\b', 'ate an egg', 'Article & tense error: "eat egg" → "ate an egg"'),
        (r'\beat to\b', 'ate', 'Preposition error: "eat to" → "ate"'),
        (r'\bI go to kitchen\b', 'I went to the kitchen', 'Tense & article error: "go to kitchen" → "went to the kitchen"'),
        (r'\bI go to\b', 'I went to', 'Past tense: "go to" → "went to"'),
        (r'\bI goes to\b', 'I went to', 'Subject-verb agreement + tense error'),
        (r'\bhe go to\b', 'he went to', 'Past tense: "go" → "went"'),
        (r'\bshe go to\b', 'she went to', 'Past tense: "go" → "went"'),
        (r'\bwe go to\b', 'we went to', 'Past tense: "go" → "went"'),
        (r'\bthey go to\b', 'they went to', 'Past tense: "go" → "went"'),

        # ── Workplace & Spoken English errors ──────────────────────────────────────
        (r'\bmy boss look\b', 'my boss looked', 'Subject-verb & tense error: "boss look" → "boss looked"'),
        (r'\bboss look\b', 'boss looked', 'Past tense: "boss look" → "boss looked"'),
        (r'\blook very angry to me\b', 'looked very angry with me', 'Preposition & tense: "angry to me" → "angry with me"'),
        (r'\bangry to me\b', 'angry with me', 'Preposition error: "angry to me" → "angry with me"'),
        (r'\bangry on me\b', 'angry with me', 'Preposition error: "angry on me" → "angry with me"'),
        (r'\bwhen I arrive at my office\b', 'when I arrived at my office', 'Past tense: "arrive" → "arrived"'),
        (r'\bwhen I arrive at\b', 'when I arrived at', 'Past tense: "arrive at" → "arrived at"'),
        (r'\barrive at my office\b', 'arrived at my office', 'Past tense: "arrive" → "arrived"'),
        (r'\barrive at office\b', 'arrived at the office', 'Past tense & article error'),
        (r'\bclock do not ring\b', "clock didn't ring", 'Past tense & auxiliary error'),
        (r'\bdo not ring\b', "didn't ring", 'Past tense: "do not" → "didn\'t"'),
        (r'\bdoes not ring\b', "didn't ring", 'Past tense: "does not" → "didn\'t"'),
        (r'\bhe look\b', 'he looked', 'Past tense: "look" → "looked"'),
        (r'\bshe look\b', 'she looked', 'Past tense: "look" → "looked"'),
        (r'\bthey look\b', 'they looked', 'Past tense: "look" → "looked"'),
        (r'\bhe say\b', 'he said', 'Past tense: "say" → "said"'),
        (r'\bshe say\b', 'she said', 'Past tense: "say" → "said"'),
        (r'\bthey say\b', 'they said', 'Past tense: "say" → "said"'),
        (r'\bboss say\b', 'boss said', 'Past tense: "say" → "said"'),

        # ── "for + verb" → "to + verb" (very common Indian error) ───────────────
        (r'\bfor buy\b', 'to buy', 'Preposition error: "for buy" → "to buy"'),
        (r'\bfor get\b', 'to get', 'Preposition error: "for get" → "to get"'),
        (r'\bfor eat\b', 'to eat', 'Preposition error: "for eat" → "to eat"'),
        (r'\bfor go\b', 'to go', 'Preposition error: "for go" → "to go"'),
        (r'\bfor see\b', 'to see', 'Preposition error: "for see" → "to see"'),
        (r'\bfor take\b', 'to take', 'Preposition error: "for take" → "to take"'),
        (r'\bfor study\b', 'to study', 'Preposition error: "for study" → "to study"'),
        (r'\bfor do\b', 'to do', 'Preposition error: "for do" → "to do"'),
        (r'\bfor make\b', 'to make', 'Preposition error: "for make" → "to make"'),
        (r'\bfor learn\b', 'to learn', 'Preposition error: "for learn" → "to learn"'),
        (r'\bfor work\b', 'to work', 'Preposition error: "for work" → "to work"'),
        (r'\bfor help\b', 'to help', 'Preposition error: "for help" → "to help"'),
        (r'\bfor come\b', 'to come', 'Preposition error: "for come" → "to come"'),
        (r'\bfor tell\b', 'to tell', 'Preposition error: "for tell" → "to tell"'),
        (r'\bfor give\b', 'to give', 'Preposition error: "for give" → "to give"'),

        # ── Subject-verb agreement errors ─────────────────────────────────────────
        (r'\bthey was\b', 'they were', 'Subject-verb agreement: "they was" → "they were"'),
        (r'\bwe was\b', 'we were', 'Subject-verb agreement: "we was" → "we were"'),
        (r'\byou was\b', 'you were', 'Subject-verb agreement: "you was" → "you were"'),
        (r'\bhe were\b', 'he was', 'Subject-verb agreement: "he were" → "he was"'),
        (r'\bshe were\b', 'she was', 'Subject-verb agreement: "she were" → "she was"'),
        (r'\bI are\b', 'I am', 'Subject-verb agreement: "I are" → "I am"'),
        (r'\bI has\b', 'I have', 'Subject-verb agreement: "I has" → "I have"'),
        (r'\bhe have\b', 'he has', 'Subject-verb agreement: "he have" → "he has"'),
        (r'\bshe have\b', 'she has', 'Subject-verb agreement: "she have" → "she has"'),
        (r'\bI goes\b', 'I go', 'Subject-verb agreement: "I goes" → "I go"'),
        (r'\bI comes\b', 'I come', 'Subject-verb agreement: "I comes" → "I come"'),

        # ── "already" misuse (common in Indian English) ──────────────────────────
        (r'\bwas closed already\b', 'was already closed', 'Word order: "closed already" → "already closed"'),
        (r'\bwas opened already\b', 'was already open', 'Word order: "opened already" → "already open"'),
        (r'\bhas done already\b', 'has already done', 'Word order fix'),
        (r'\bdone already\b', 'already done', 'Word order: move "already" before verb'),
        (r'\bcompleted already\b', 'already completed', 'Word order fix'),
        (r'\bleft already\b', 'already left', 'Word order fix'),
        (r'\barrived already\b', 'already arrived', 'Word order fix'),
        (r'\bfinished already\b', 'already finished', 'Word order fix'),

        # ── Double auxiliary / wrong form ─────────────────────────────────────────
        (r'\bI have went\b', 'I have gone', '"Have went" is incorrect → "have gone"'),
        (r'\bI have did\b', 'I have done', '"Have did" is incorrect → "have done"'),
        (r'\bI have came\b', 'I have come', '"Have came" is incorrect → "have come"'),
        (r'\bI have ate\b', 'I have eaten', '"Have ate" is incorrect → "have eaten"'),
        (r'\bI have ran\b', 'I have run', '"Have ran" is incorrect → "have run"'),
        (r'\bI am knowing\b', 'I know', '"Am knowing" is incorrect → "know"'),
        (r'\bI am having\b', 'I have', '"Am having" is incorrect → "I have"'),
        (r'\bI am understanding\b', 'I understand', '"Am understanding" is incorrect → "understand"'),
        (r'\bI am wanting\b', 'I want', '"Am wanting" is incorrect → "want"'),
        (r'\bI am liking\b', 'I like', '"Am liking" is incorrect → "like"'),
        (r'\bI am thinking\b', 'I think', '"Am thinking" is incorrect in simple context → "think"'),
        (r'\bI done\b', 'I did', '"I done" is incorrect → "I did"'),

        # ── Preposition errors ─────────────────────────────────────────────────────
        (r'\bmarried with\b', 'married to', 'Preposition error: "married with" → "married to"'),
        (r'\bdiscuss about\b', 'discuss', '"Discuss" doesn\'t need "about"'),
        (r'\bexplain about\b', 'explain', '"Explain" doesn\'t need "about"'),
        (r'\benter into\b', 'enter', '"Enter" doesn\'t need "into"'),
        (r'\bsince (\d+) years\b', r'for \1 years', 'Use "for" with duration, not "since"'),
        (r'\bsince long time\b', 'for a long time', '"Since" needs a point in time; use "for" with duration'),

        # ── Article errors ─────────────────────────────────────────────────────────
        (r'\ban university\b', 'a university', 'Article: "university" takes "a" (consonant sound)'),
        (r'\ba hour\b', 'an hour', 'Article: "hour" takes "an" (vowel sound)'),
        (r'\ba honest\b', 'an honest', 'Article: "honest" takes "an" (vowel sound)'),
        (r'\ba MBA\b', 'an MBA', 'Article: abbreviation starting with vowel sound takes "an"'),
        (r'\ba MCA\b', 'an MCA', 'Article: abbreviation starting with vowel sound takes "an"'),

        # ── Double negatives ───────────────────────────────────────────────────────
        (r"\bdon't know nothing\b", "don't know anything", 'Double negative error'),
        (r"\bcan't do nothing\b", "can't do anything", 'Double negative error'),
        (r"\bdidn't go nowhere\b", "didn't go anywhere", 'Double negative error'),

        # ── Placement/self-intro errors ────────────────────────────────────────────
        (r'^hey hello\b', 'Hello,', 'Informal opening: use "Hello," or "Good morning,"'),
        (r'^hey\b', 'Hello,', 'Informal opening'),
        (r'\bI am currently pursuing a\b', 'I am currently in my', 'Rephrase for formality'),
        (r'\bBTech\b', 'B.Tech', 'Write as "B.Tech"'),
        (r'\bBtech\b', 'B.Tech', 'Write as "B.Tech"'),
        (r'\bfinal year industry of\b', 'final year in the field of', '"industry of" → "field of"'),
        (r'\bindustry of\b', 'field of', '"industry of" → "field of"'),
        (r'\bI have done certification\b', 'I have completed a certification', '"done" → "completed"'),
        (r'\bhave done certification\b', 'have completed a certification', '"done" → "completed"'),
        (r'\bdone project related to\b', 'completed a project related to', '"done" → "completed"'),
        (r'\balso done project\b', 'also completed a project', '"done" → "completed"'),
        (r'\bhave done\b', 'have completed', '"have done" → "have completed"'),
        (r'\brelated to Ai\b', 'related to Artificial Intelligence', 'Expand "AI"'),
        (r'\brelated to ai\b', 'related to Artificial Intelligence', 'Expand "AI"'),
        (r"\bthat'?s all about myself\b", 'That is a brief overview of my background.', 'Formal closing'),
        (r"\bthat'?s all about me\b", 'That is a brief introduction about myself.', 'Formal closing'),
        (r'\bcomputer science engineering and artificial intelligence and machine learning\b',
         'Computer Science Engineering with a specialization in Artificial Intelligence and Machine Learning',
         'Expand and format degree title'),
        (r'\bartificial intelligence and machine learning\b',
         'Artificial Intelligence and Machine Learning', 'Capitalize subject name'),
        (r'\bcomputer science engineering\b', 'Computer Science Engineering', 'Capitalize'),
        (r'\bcomputer science\b', 'Computer Science', 'Capitalize'),

        # ── Informal → formal ──────────────────────────────────────────────────────
        (r'\bwanna\b', 'want to', 'Informal: "wanna" → "want to"'),
        (r'\bgonna\b', 'going to', 'Informal: "gonna" → "going to"'),
        (r'\bgotta\b', 'have to', 'Informal: "gotta" → "have to"'),
        (r'\bkinda\b', 'somewhat', 'Informal: "kinda" → "somewhat"'),
        (r'\bsorta\b', 'somewhat', 'Informal: "sorta" → "somewhat"'),
        (r'\blots of\b', 'numerous', 'Informal: "lots of" → "numerous"'),
        (r'\ba lot of\b', 'numerous', 'Informal: "a lot of" → "numerous"'),
        (r'\bgot opportunity\b', 'had the opportunity', 'Formal: "got opportunity" → "had the opportunity"'),
        (r'\bgot chance\b', 'had the opportunity', 'Formal phrasing'),
    ]

    # Vocabulary upgrades (whole word replacements)
    VOCAB_UPGRADES = [
        (r'\bgood at\b', 'proficient in', 'More professional than "good at"'),
        (r'\btalk about\b', 'elaborate on', 'More formal than "talk about"'),
        (r'\bwork on\b', 'contribute to', 'More formal than "work on"'),
        (r'\bliked\b', 'appreciated', 'More professional than "liked"'),
        (r'\bi think\b', 'I believe', 'More confident than "I think"'),
        (r'\bstuff\b', 'aspects', 'More formal than "stuff"'),
        (r'\bthings\b', 'elements', 'More formal than "things"'),
        (r'\bmaybe\b', 'potentially', 'More formal than "maybe"'),
        (r'\bfix\b', 'resolve', 'More formal than "fix"'),
        (r'\bshow\b', 'demonstrate', 'More formal than "show"'),
        (r'\bfast\b', 'efficient', 'More professional than "fast"'),
    ]

    errors = []
    vocab_applied = []
    result = text

    for pattern, replacement, desc in PHRASE_REWRITES:
        matches = re.findall(pattern, result, flags=re.IGNORECASE)
        if matches:
            orig = matches[0] if isinstance(matches[0], str) else matches[0]
            errors.append({'original': orig, 'corrected': replacement, 'type': desc})
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

    for pattern, replacement, reason in VOCAB_UPGRADES:
        m = re.search(pattern, result, flags=re.IGNORECASE)
        if m:
            vocab_applied.append({'original': m.group(0), 'upgrade': replacement, 'reason': reason})
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

    # Fix capitalization
    result = result.strip()
    if result and result[0].islower():
        result = result[0].upper() + result[1:]
    result = re.sub(r'(?<=[.!?]\s)([a-z])', lambda m: m.group(1).upper(), result)
    result = re.sub(r'(?<![A-Za-z])\bi\b(?![A-Za-z])', 'I', result)

    return result, errors, vocab_applied


def analyze_speech(transcript: str, duration_seconds: int) -> dict:
    """
    Main analysis: uses Gemini AI for high-quality correction + rule-based fallback.
    """
    if not transcript or not transcript.strip():
        return _empty_result()

    text = transcript.strip()
    words = text.split()
    word_count = len(words)
    duration_minutes = max(duration_seconds / 60, 0.01)
    wpm = round(word_count / duration_minutes, 1)

    # Filler detection (always rule-based — fast and reliable)
    filler_words_found, filler_count = _detect_fillers(text)

    # Try Gemini first
    gemini_result = _gemini_analyze_speech(text)
    using_gemini = bool(gemini_result.get('corrected_transcript') and not gemini_result.get('_error'))

    if using_gemini:
        corrected_transcript = gemini_result.get('corrected_transcript', text)
        grammar_errors = gemini_result.get('grammar_errors', [])
        vocabulary_upgrades = gemini_result.get('vocabulary_upgrades', [])
        extra_tips = gemini_result.get('extra_tips', [])
    else:
        # Fallback to comprehensive rule-based engine
        corrected_transcript, grammar_errors, vocabulary_upgrades = _rule_based_correct(text)
        extra_tips = []

    # ── Scoring ────────────────────────────────────────────────────────────
    grammar_score = max(0, min(100, 100 - len(grammar_errors) * 7))

    if 120 <= wpm <= 150:
        pace_score = 100
    elif 100 <= wpm < 120 or 150 < wpm <= 170:
        pace_score = 85
    elif 80 <= wpm < 100 or 170 < wpm <= 200:
        pace_score = 70
    elif wpm < 80:
        pace_score = max(40, int(wpm / 80 * 70))
    else:
        pace_score = max(50, int(200 / wpm * 70))

    filler_penalty = min(40, filler_count * 5)
    fluency_score = max(0, min(100, pace_score - filler_penalty))

    vocab_base = 70
    if using_gemini and vocabulary_upgrades:
        vocab_base = max(65, 90 - len(vocabulary_upgrades) * 4)
    vocab_score = min(100, vocab_base + (5 if word_count > 60 else 0))

    if duration_seconds < 15:
        fluency_score = max(0, fluency_score - 25)
        grammar_score = max(0, grammar_score - 10)

    overall_raw = grammar_score * 0.40 + fluency_score * 0.35 + vocab_score * 0.25
    overall_score = round(overall_raw / 10, 1)

    # ── Tips ───────────────────────────────────────────────────────────────
    tips = []
    if filler_count > 0:
        tips.append(f"You used {filler_count} filler word(s) ({', '.join(filler_words_found[:4])}). Pause silently instead.")
    if wpm < 100:
        tips.append(f"Your pace is {wpm} WPM — slightly slow. Aim for 120–150 WPM.")
    elif wpm > 180:
        tips.append(f"Your pace is {wpm} WPM — too fast. Slow down for clarity.")
    else:
        tips.append(f"Good pace at {wpm} WPM — within ideal 120–150 WPM range!")
    if len(grammar_errors) > 0:
        tips.append(f"{len(grammar_errors)} grammar/phrasing issue(s) found. Review the corrections and practise aloud.")
    else:
        tips.append("No significant grammar issues — well done!")
    if len(vocabulary_upgrades) > 0:
        tips.append(f"Upgrade {len(vocabulary_upgrades)} word(s) to formal vocabulary for a stronger impression in HR rounds.")
    if word_count < 50:
        tips.append("Your answer was brief. Aim for 100–150 words: Background → Skills → Projects → Goal.")
    tips.extend(extra_tips)
    if overall_score >= 8.0:
        tips.append("🌟 Excellent! You are at placement-readiness level.")
    elif overall_score >= 6.0:
        tips.append("📈 Good effort! A few more sessions will make you fully placement-ready.")
    else:
        tips.append("💪 Keep practising. Focus on removing fillers and using formal vocabulary.")

    # Rating label
    if overall_score >= 9.0:
        rating_label = "Exceptional"
    elif overall_score >= 8.0:
        rating_label = "Placement Ready"
    elif overall_score >= 6.5:
        rating_label = "Good — Minor Polish Needed"
    elif overall_score >= 5.0:
        rating_label = "Average — Practice Required"
    else:
        rating_label = "Needs Significant Improvement"

    return {
        'word_count': word_count,
        'wpm': wpm,
        'filler_count': filler_count,
        'filler_words_found': filler_words_found,
        'grammar_errors': grammar_errors,
        'vocabulary_upgrades': vocabulary_upgrades,
        'corrected_transcript': corrected_transcript,
        'grammar_score': grammar_score,
        'fluency_score': fluency_score,
        'vocabulary_score': vocab_score,
        'overall_score': overall_score,
        'rating_label': rating_label,
        'tips': tips,
        'engine': 'gemini' if using_gemini else 'rule_based',
    }


def _empty_result():
    return {
        'word_count': 0, 'wpm': 0, 'filler_count': 0,
        'filler_words_found': [], 'grammar_errors': [], 'vocabulary_upgrades': [],
        'corrected_transcript': '', 'grammar_score': 0, 'fluency_score': 0,
        'vocabulary_score': 0, 'overall_score': 0, 'rating_label': 'No speech detected',
        'tips': ['No transcript received. Please try again.'],
        'engine': 'none',
    }


# ════════════════════════════════════════════════════════════════════════════════
#  API VIEWS — SPEECH LAB
# ════════════════════════════════════════════════════════════════════════════════

class TopicListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        topics = SpeechTopic.objects.filter(is_active=True)
        serializer = SpeechTopicSerializer(topics, many=True)
        return Response(serializer.data)


class AnalyzeSpeechView(APIView):
    """POST /api/communication/analyze/"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SpeechAttemptCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        transcript = data['transcript'].strip()
        duration_seconds = data['duration_seconds']

        if not transcript:
            return Response({'error': 'Transcript is empty.'}, status=status.HTTP_400_BAD_REQUEST)

        analysis = analyze_speech(transcript, duration_seconds)

        topic = None
        topic_id = data.get('topic_id')
        if topic_id:
            try:
                topic = SpeechTopic.objects.get(id=topic_id, is_active=True)
            except SpeechTopic.DoesNotExist:
                pass

        attempt = SpeechAttempt.objects.create(
            user=request.user,
            topic=topic,
            custom_topic=data.get('custom_topic', ''),
            transcript=transcript,
            duration_seconds=duration_seconds,
            word_count=analysis['word_count'],
            wpm=analysis['wpm'],
            grammar_score=analysis['grammar_score'],
            fluency_score=analysis['fluency_score'],
            vocabulary_score=analysis['vocabulary_score'],
            overall_score=analysis['overall_score'],
            filler_count=analysis['filler_count'],
            filler_words_found=analysis['filler_words_found'],
            corrected_transcript=analysis['corrected_transcript'],
            grammar_errors=analysis['grammar_errors'],
            vocabulary_upgrades=analysis['vocabulary_upgrades'],
            tips=analysis['tips'],
        )

        return Response({
            'attempt_id': attempt.id,
            **analysis,
            'topic': SpeechTopicSerializer(topic).data if topic else None,
        }, status=status.HTTP_201_CREATED)


class SpeechHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = SpeechAttempt.objects.filter(user=request.user).order_by('-created_at')[:20]
        serializer = SpeechAttemptSerializer(attempts, many=True)
        return Response(serializer.data)


# ════════════════════════════════════════════════════════════════════════════════
#  TRANSLATOR VIEW
# ════════════════════════════════════════════════════════════════════════════════

class TranslateView(APIView):
    """
    POST /api/communication/translate/
    Body: { text, source_language, target_language }
    Engine priority: Gemini AI → Sarvam AI → MyMemory
    """
    permission_classes = [IsAuthenticated]

    LANG_NAMES = {
        'te-IN': 'Telugu',
        'en-IN': 'English',
        'hi-IN': 'Hindi',
        'te': 'Telugu',
        'en': 'English',
        'hi': 'Hindi',
    }
    SARVAM_MAP = {
        'te': 'te-IN', 'en': 'en-IN', 'hi': 'hi-IN',
        'te-IN': 'te-IN', 'en-IN': 'en-IN', 'hi-IN': 'hi-IN'
    }
    MYMEMORY_MAP = {
        'te-IN': 'te', 'en-IN': 'en', 'hi-IN': 'hi',
        'te': 'te', 'en': 'en', 'hi': 'hi'
    }

    # ── Gemini translation ────────────────────────────────────────────────
    def _translate_gemini(self, text: str, source: str, target: str) -> str:
        src_name = self.LANG_NAMES.get(source, source)
        tgt_name = self.LANG_NAMES.get(target, target)

        prompt = f"""You are an ultra-powerful multi-lingual AI translator specialized in Indian languages (Telugu, Hindi, and English).

Translate the following input text from {src_name} to {tgt_name}.

CRITICAL INSTRUCTIONS FOR INPUT TRANSLATION:
1. The input text may be written in:
   - Native script (e.g. Telugu script "ఎలా ఉన్నారు", Hindi Devanagari script "आप कैसे हैं")
   - Phonetic/Romanized typing using English keyboard letters (e.g., Phonetic Telugu: "ela unnaru", "vellandi", "namaskaram" | Phonetic Hindi: "aap kaise ho", "namaste", "dhanyawad", "main thik hoon", "khana khaya kya")
   - Standard English or a mix
2. AUTOMATICALLY RECOGNIZE Phonetic Romanized Telugu or Phonetic Romanized Hindi and translate it accurately to fluent {tgt_name}!
3. Produce natural, grammatically flawless, context-aware {tgt_name}.
4. Return ONLY the translated text, with no extra conversational filler, labels, quotes, or markdown wrappers.

Input text:
{text}"""

        return _call_gemini(prompt, temperature=0.1)

    # ── Sarvam fallback ───────────────────────────────────────────────────
    def _translate_sarvam(self, text: str, source: str, target: str) -> str:
        api_key = getattr(settings, 'SARVAM_API_KEY', '')
        if not api_key:
            raise ValueError('No Sarvam key')
        src = self.SARVAM_MAP.get(source, source)
        tgt = self.SARVAM_MAP.get(target, target)
        chunks = self._chunk(text, 1900)
        parts = []
        for chunk in chunks:
            r = http_requests.post(
                'https://api.sarvam.ai/translate',
                headers={'api-subscription-key': api_key, 'Content-Type': 'application/json'},
                json={'input': chunk, 'source_language_code': src,
                      'target_language_code': tgt, 'model': 'sarvam-translate:v1',
                      'enable_preprocessing': True},
                timeout=20,
            )
            r.raise_for_status()
            parts.append(r.json().get('translated_text', ''))
        return ' '.join(parts)

    # ── MyMemory fallback ─────────────────────────────────────────────────
    def _translate_mymemory(self, text: str, source: str, target: str) -> str:
        src = self.MYMEMORY_MAP.get(source, source.split('-')[0])
        tgt = self.MYMEMORY_MAP.get(target, target.split('-')[0])
        langpair = f'{src}|{tgt}'
        chunks = self._chunk(text, 480)
        parts = []
        for chunk in chunks:
            r = http_requests.get(
                'https://api.mymemory.translated.net/get',
                params={'q': chunk, 'langpair': langpair},
                timeout=15,
            )
            r.raise_for_status()
            parts.append(r.json()['responseData']['translatedText'])
        return ' '.join(parts)

    def _chunk(self, text: str, max_len: int):
        if len(text) <= max_len:
            return [text]
        sentences = re.split(r'(?<=[.!?\n])\s+', text)
        chunks, cur = [], ''
        for s in sentences:
            if len(cur) + len(s) + 1 <= max_len:
                cur = (cur + ' ' + s).strip()
            else:
                if cur:
                    chunks.append(cur)
                cur = s[:max_len] if len(s) > max_len else s
        if cur:
            chunks.append(cur)
        return chunks or [text]

    def post(self, request):
        text = request.data.get('text', '').strip()
        source = request.data.get('source_language', 'te-IN')
        target = request.data.get('target_language', 'en-IN')

        if not text:
            return Response({'error': 'No text provided.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(text) > 10000:
            return Response({'error': 'Text too long. Max 10,000 characters.'}, status=status.HTTP_400_BAD_REQUEST)

        # Engine priority: Gemini → Sarvam → MyMemory
        for engine_name, engine_fn in [
            ('gemini',   lambda: self._translate_gemini(text, source, target)),
            ('sarvam',   lambda: self._translate_sarvam(text, source, target)),
            ('mymemory', lambda: self._translate_mymemory(text, source, target)),
        ]:
            try:
                translated = engine_fn()
                if translated and translated.strip():
                    return Response({
                        'translated_text': translated.strip(),
                        'source_language': source,
                        'target_language': target,
                        'engine': engine_name,
                        'char_count': len(text),
                    })
            except ValueError:
                continue  # Key not configured — try next
            except Exception:
                continue  # API error — try next

        return Response(
            {'error': 'All translation engines failed. Please check your API keys on Render.'},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )


class VoiceRoboConversationView(APIView):
    """
    POST /api/communication/robo-speak/
    Interactive Conversational AI Robo for Speaking Lab.
    Returns:
      - robo_reply: conversational response
      - corrected_user_speech: formal English rewrite
      - verbal_correction_phrase: spoken audio feedback tip
      - grammar_fixes: list of errors fixed
      - turn_score: 1-100 rating
    """
    permission_classes = [IsAuthenticated]

    PERSONA_PROMPTS = {
        'hr': "You are an expert HR Placement Interviewer named Robo. You are conducting a professional mock interview for campus placement. Ask insightful HR questions, evaluate candidate's speech, and keep the interview flowing professionally.",
        'technical': "You are a Senior Technical Lead & Coding Recruiter named Robo. You evaluate technical English, problem-solving explanations, DBMS, Data Structures, and Software Engineering skills.",
        'buddy': "You are a friendly, encouraging English Speaking Buddy named Robo. Help the candidate build natural English speaking confidence, correct their grammar gently, and keep casual placement conversation fun.",
    }

    def _fallback_robo_reply(self, transcript, persona_key, history):
        text_lower = transcript.lower()
        corrected_transcript, raw_fixes, _ = _rule_based_correct(transcript)

        fixes = []
        for err in raw_fixes:
            fixes.append({
                'error': err.get('original', ''),
                'fix': err.get('corrected', ''),
                'rule': err.get('type', 'Grammar correction')
            })

        words = transcript.split()
        if len(fixes) > 0:
            score = max(55, min(88, 92 - len(fixes) * 10))
        elif len(words) < 5:
            score = 75
        else:
            score = 88

        # Word boundary helper to prevent matching 'ok' inside 'look'
        def has_word(w):
            return bool(re.search(r'\b' + re.escape(w) + r'\b', text_lower))

        if persona_key == 'buddy':
            if any(has_word(w) for w in ['boss', 'office', 'manager', 'work', 'colleague', 'job', 'company']):
                if any(has_word(w) for w in ['angry', 'mad', 'upset', 'scolded', 'late', 'traffic', 'delay', 'clock', 'alarm']):
                    reply = "Oh no! That sounds really stressful. Dealing with an angry boss or a late morning can be tough. What happened next? Did you get a chance to explain?"
                else:
                    reply = "I understand. Work environments can be fast-paced. How are things going at your workplace or internship overall?"
            elif any(has_word(w) for w in ['angry', 'mad', 'upset', 'sad', 'scolded', 'fight']):
                reply = "I'm sorry to hear that you had a difficult situation. How did you handle it, and is everything okay now?"
            elif any(has_word(w) for w in ['breakfast', 'wake', 'woke', 'morning', 'eat', 'food', 'day', 'kitchen', 'egg', 'alarm']):
                reply = "That sounds like a busy morning! What are your main plans or tasks for the rest of today?"
            elif any(has_word(w) for w in ['fine', 'good', 'great', 'okay', 'ok', 'happy', 'awesome']):
                reply = "Glad to hear that you're doing well! What topics or projects have you been working on recently?"
            elif any(has_word(w) for w in ['project', 'python', 'java', 'code', 'college', 'exam', 'class', 'study']):
                reply = "That sounds interesting! What did you enjoy most while working on that?"
            else:
                reply = "I see! Tell me more about what happened next or what else is on your mind today."

            verbal = f"Good effort! A quick tip: try saying '{corrected_transcript}'." if fixes else "Good attempt! Keep practicing natural English sentences."

        elif persona_key == 'technical':
            if any(has_word(w) for w in ['boss', 'office', 'project', 'team', 'deadline', 'client']):
                reply = "In professional tech environments, managing deadlines and expectations is key. How do you handle workplace pressure or project delays?"
            elif any(has_word(w) for w in ['python', 'java', 'cpp', 'c++', 'sql', 'db', 'database', 'code', 'api']):
                reply = "Good technical context! How do you handle error handling, edge cases, and optimization in your code?"
            else:
                reply = "Understood. As a Tech Lead, I'd love to know: what is your primary technical project or favorite programming language?"

            verbal = f"For technical interviews, phrase it like: '{corrected_transcript}'." if fixes else "Clear technical response!"

        else: # HR recruiter
            if any(has_word(w) for w in ['boss', 'office', 'work', 'conflict', 'angry', 'late']):
                reply = "Handling workplace challenges professionally is an important HR metric. How do you resolve conflicts or miscommunications in a team?"
            elif any(has_word(w) for w in ['strengths', 'strength', 'good', 'hardworking', 'learn', 'team']):
                reply = "Thank you for sharing your strength. Can you give me a real-life example where you demonstrated that?"
            else:
                reply = "Thank you for sharing. Could you please tell me about your background and why you are interested in joining our company?"

            verbal = f"In an HR interview, state it formally like: '{corrected_transcript}'." if fixes else "Professional response!"

        return {
            'robo_reply': reply,
            'corrected_user_speech': corrected_transcript,
            'verbal_correction_phrase': verbal,
            'grammar_fixes': fixes,
            'turn_score': score
        }

    def post(self, request):
        transcript = request.data.get('transcript', '').strip()
        persona_key = request.data.get('persona', 'hr').lower()
        history = request.data.get('history', [])
        user_name = request.data.get('user_name', '')
        if not user_name:
            user_name = getattr(request.user, 'display_name', '') or request.user.username

        if not transcript:
            return Response({'error': 'No transcript provided.'}, status=status.HTTP_400_BAD_REQUEST)

        persona_context = self.PERSONA_PROMPTS.get(persona_key, self.PERSONA_PROMPTS['hr'])

        history_text = ""
        if history:
            history_text = "CONVERSATION HISTORY:\n" + "\n".join(
                f"{turn.get('role', 'user').upper()}: {turn.get('text', '')}"
                for turn in history[-6:]
            )

        prompt = f"""{persona_context}

Candidate Name: {user_name}
The candidate ({user_name}) just said: "{transcript}"

{history_text}

Task:
1. Formulate an intelligent, highly natural, conversational next response as Robo to keep the interview/chat flowing. Naturally address the candidate by name ({user_name}) when appropriate. Ask insightful follow-up questions tailored to your persona.
2. Rewrite the candidate's speech into formal, placement-ready, grammatically flawless English.
3. Provide a short verbal correction phrase for text-to-speech feedback (e.g., "A better way to say that is: ...").
4. Identify 1-3 specific grammar errors if present.
5. Provide 1-2 native professional vocabulary upgrades (e.g., "think" -> "firmly believe", "worked on" -> "architected").
6. Score the turn out of 100 based on grammar, clarity, and vocabulary richness.
7. Provide a short 1-sentence actionable tip for confidence/delivery.

Respond ONLY in this exact JSON format (no markdown, no extra text):
{{
  "robo_reply": "Natural conversational response as Robo",
  "corrected_user_speech": "Formal, perfect English rewrite of candidate's speech",
  "verbal_correction_phrase": "Short spoken tip for audio voice feedback",
  "grammar_fixes": [
    {{"error": "wrong phrase", "fix": "correct phrase", "rule": "explanation"}}
  ],
  "vocabulary_upgrades": [
    {{"original": "informal word", "upgrade": "professional word", "reason": "why upgrade"}}
  ],
  "turn_score": 92,
  "confidence_tip": "One clear tip for better placement delivery"
}}"""

        try:
            raw = _call_gemini(prompt, temperature=0.3)
            import json
            match = re.search(r'\{.*\}', raw, re.DOTALL)
            if match:
                data = json.loads(match.group(0))
                if 'robo_reply' in data and 'corrected_user_speech' in data:
                    return Response(data, status=status.HTTP_200_OK)
            
            data = json.loads(raw.strip())
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error("Robo AI View error: %s", e)
            fallback_data = self._fallback_robo_reply(transcript, persona_key, history)
            return Response(fallback_data, status=status.HTTP_200_OK)


# ════════════════════════════════════════════════════════════════════════════════
#  ADMIN VIEWS
# ════════════════════════════════════════════════════════════════════════════════

class AdminTopicView(APIView):
    permission_classes = [IsAuthenticated]

    def _is_admin(self, req):
        return req.user.is_staff or (hasattr(req.user, 'role') and req.user.role == 'admin')

    def get(self, request):
        if not self._is_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        return Response(SpeechTopicSerializer(SpeechTopic.objects.all(), many=True).data)

    def post(self, request):
        if not self._is_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        s = SpeechTopicSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminTopicDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def _is_admin(self, req):
        return req.user.is_staff or (hasattr(req.user, 'role') and req.user.role == 'admin')

    def put(self, request, pk):
        if not self._is_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        try:
            topic = SpeechTopic.objects.get(pk=pk)
        except SpeechTopic.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        s = SpeechTopicSerializer(topic, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not self._is_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        try:
            SpeechTopic.objects.get(pk=pk).delete()
        except SpeechTopic.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminAttemptsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_staff and not (hasattr(request.user, 'role') and request.user.role == 'admin'):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        attempts = SpeechAttempt.objects.all().order_by('-created_at')[:100]
        return Response(SpeechAttemptSerializer(attempts, many=True).data)


class PurgeHistoryView(APIView):
    """DELETE /api/communication/history/purge/ — delete all speech attempts for the current user"""
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        deleted_count, _ = SpeechAttempt.objects.filter(user=request.user).delete()
        return Response({'deleted': deleted_count, 'message': f'{deleted_count} attempt(s) purged successfully.'})
