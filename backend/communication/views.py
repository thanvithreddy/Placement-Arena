import re
import requests as http_requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import SpeechTopic, SpeechAttempt
from .serializers import SpeechTopicSerializer, SpeechAttemptSerializer, SpeechAttemptCreateSerializer

# ─── Filler words (ordered: multi-word first to avoid partial overlaps) ───────
FILLER_WORDS = [
    'you know what', 'i mean like', 'sort of like', 'kind of like',
    'you know', 'i mean', 'sort of', 'kind of', 'so yeah', 'okay so',
    'right so', 'and so', 'so basically', 'so actually', 'so like',
    'um', 'uh', 'umm', 'uhh', 'er', 'err', 'hmm', 'hm',
    'basically', 'literally', 'honestly', 'obviously',
]

# ─── Sentence-level phrase rewrites (ordered: longest/most-specific first) ────
# Each entry: (regex_pattern, replacement, error_description)
# Applied BEFORE vocabulary upgrades to handle multi-word constructs.
PHRASE_REWRITES = [

    # ── Opening/Greeting cleanup ──────────────────────────────────────────
    (r'^hey hello\b', 'Hello,', 'Informal opening: Remove "hey hello"; use "Hello,"'),
    (r'^hey\b', 'Hello,', 'Informal: Replace "hey" with "Hello,"'),
    (r'^hi hello\b', 'Hello,', 'Redundant greeting: Use "Hello,"'),
    (r'^hii+\b', 'Hello,', 'Replace informal "hii" with "Hello,"'),
    (r'^so,?\s+', '', 'Remove filler opener "so"'),
    (r'^okay so,?\s+', '', 'Remove filler opener "okay so"'),

    # ── Self-introduction ─────────────────────────────────────────────────
    (r'\bI am currently pursuing a\b', 'I am currently in my', 'Rephrase for formality'),
    (r'\bpursuing a BTech\b', 'pursuing a B.Tech', 'Use abbreviated period form "B.Tech"'),
    (r'\bpursuing BTech\b', 'pursuing B.Tech', 'Use abbreviated period form "B.Tech"'),
    (r'\bBTech\b', 'B.Tech', 'Use abbreviated period form "B.Tech"'),
    (r'\bBtech\b', 'B.Tech', 'Use abbreviated period form "B.Tech"'),
    (r'\bB\.?Tech final year industry of\b', 'B.Tech final year in the field of', 'Fix: "industry of" → "field of"'),
    (r'\bfinal year industry of\b', 'final year in the field of', 'Fix: "industry of" → "field of"'),
    (r'\bindustry of computer science\b', 'stream of Computer Science', 'Fix: "industry of" → "stream of"'),
    (r'\bindustry of\b', 'field of', 'Fix informal: "industry of" → "field of"'),

    # ── "have done" → "have completed" ───────────────────────────────────
    (r'\bI have done certification program\b', 'I have completed a certification program', 'Add article "a" and use "completed"'),
    (r'\bhave done a certification\b', 'have completed a certification', 'Replace "done" with "completed"'),
    (r'\bhave done certification\b', 'have completed a certification', 'Replace "done" and add article "a"'),
    (r'\bhave done a course\b', 'have completed a course', 'Replace "done" with "completed"'),
    (r'\bhave done course\b', 'have completed a course', 'Add article "a" and replace "done"'),
    (r'\bhave done a project\b', 'have completed a project', 'Replace "done" with "completed"'),
    (r'\bhave done project\b', 'have completed a project', 'Add article "a" and replace "done"'),
    (r'\bhave done the project\b', 'have completed the project', 'Replace "done" with "completed"'),
    (r'\bdone project related to\b', 'completed a project related to', 'Add article and use "completed"'),
    (r'\bdone a project related to\b', 'completed a project related to', 'Use "completed" for formal context'),
    (r'\balso done project\b', 'also completed a project', 'Add article "a" and use "completed"'),
    (r'\balso done a project\b', 'also completed a project', 'Use "completed" for formal context'),
    (r'\bhave done\b', 'have completed', 'Replace informal "have done" with "have completed"'),
    (r'\bI done\b', 'I have done', '"Done" requires auxiliary verb: use "I have done"'),
    (r'\bI did\b(?!\s+not)', 'I completed', 'Use "completed" for formal past tense in self-intro context'),

    # ── "related to AI/Ai/ai" ─────────────────────────────────────────────
    (r'\brelated to Ai\b', 'related to Artificial Intelligence', 'Expand abbreviation: "AI" → "Artificial Intelligence"'),
    (r'\brelated to ai\b', 'related to Artificial Intelligence', 'Expand abbreviation'),
    (r'\brelated to AI\b', 'related to Artificial Intelligence', 'Expand "AI" in formal context'),
    (r'\bAi\b', 'AI', 'Capitalize: "Ai" → "AI"'),

    # ── Closing phrases ───────────────────────────────────────────────────
    (r"\bthat'?s all about myself\b", 'That is a brief overview of my academic and professional background.', 'Replace informal closing with formal one'),
    (r"\bthat'?s all about me\b", 'That is a brief introduction about myself.', 'Replace informal closing'),
    (r"\bthat'?s it\b", 'That summarizes my background.', 'Replace informal closing'),
    (r'\bthank you\b', 'Thank you.', 'Capitalize for formal tone'),

    # ── Degree / Education ────────────────────────────────────────────────
    (r'\bcomputer science engineering and artificial intelligence and machine learning\b',
     'Computer Science Engineering with a specialization in Artificial Intelligence and Machine Learning',
     'Expand and formalize degree title'),
    (r'\bartificial intelligence and machine learning\b',
     'Artificial Intelligence and Machine Learning',
     'Capitalize subject names properly'),
    (r'\bcomputer science engineering\b', 'Computer Science Engineering', 'Capitalize subject name'),
    (r'\bcomputer science\b', 'Computer Science', 'Capitalize subject name'),

    # ── Common verb/phrase mistakes ───────────────────────────────────────
    (r'\bI go to\b', 'I went to', 'Verb tense error: use past tense "went"'),
    (r'\bgiven presentation\b', 'gave a presentation', 'Verb form error: use "gave a presentation"'),
    (r'\bgiving presentation\b', 'delivered a presentation', 'Use formal "delivered a presentation"'),
    (r'\bI am knowing\b', 'I know', 'Incorrect progressive: "knowing" → "know"'),
    (r'\bI am having\b', 'I have', 'Incorrect progressive: "am having" → "have"'),
    (r'\bI am understanding\b', 'I understand', 'Incorrect progressive: use simple present'),
    (r'\bdiscuss about\b', 'discuss', '"Discuss" does not need "about"'),
    (r'\bexplain about\b', 'explain', '"Explain" does not need "about"'),
    (r'\bmy name is\b', 'My name is', 'Capitalize the start of self-introduction'),

    # ── Subject-verb agreement ────────────────────────────────────────────
    (r'\bthey was\b', 'they were', 'Subject-verb agreement error'),
    (r'\bhe were\b', 'he was', 'Subject-verb agreement error'),
    (r'\bshe were\b', 'she was', 'Subject-verb agreement error'),
    (r'\bwe was\b', 'we were', 'Subject-verb agreement error'),
    (r'\byou was\b', 'you were', 'Subject-verb agreement error'),
    (r'\bI are\b', 'I am', 'Subject-verb agreement error'),
    (r'\bI has\b', 'I have', 'Subject-verb agreement error'),
    (r'\bhe have\b', 'he has', 'Subject-verb agreement error'),
    (r'\bshe have\b', 'she has', 'Subject-verb agreement error'),

    # ── Articles ───────────────────────────────────────────────────────────
    (r'\ban university\b', 'a university', 'Article error: use "a" (consonant sound)'),
    (r'\ba hour\b', 'an hour', 'Article error: use "an" (vowel sound)'),
    (r'\ba honest\b', 'an honest', 'Article error: use "an" (vowel sound)'),

    # ── Double negatives ───────────────────────────────────────────────────
    (r"\bdon't know nothing\b", "don't know anything", 'Double negative error'),
    (r"\bcan't do nothing\b", "can't do anything", 'Double negative error'),

    # ── Common informal → formal swaps ─────────────────────────────────────
    (r'\bgot opportunity\b', 'had the opportunity', 'Use "had the opportunity" for formal tone'),
    (r'\bgot chance\b', 'had the opportunity', 'Use "had the opportunity" for formal tone'),
    (r'\bwanna\b', 'want to', 'Replace informal "wanna" with "want to"'),
    (r'\bgonna\b', 'going to', 'Replace informal "gonna" with "going to"'),
    (r'\bgotta\b', 'have to', 'Replace informal "gotta" with "have to"'),
    (r'\bkinda\b', 'somewhat', 'Replace informal "kinda" with "somewhat"'),
    (r'\bsorta\b', 'somewhat', 'Replace informal "sorta" with "somewhat"'),
    (r'\blots of\b', 'numerous', 'Replace informal "lots of" with "numerous"'),
    (r'\ba lot of\b', 'numerous', 'Replace informal "a lot of" with "numerous"'),
]

# ─── Word-level vocabulary upgrade map ───────────────────────────────────────
# Applied AFTER phrase rewrites. Only matches whole words.
VOCABULARY_UPGRADES = [
    # (original_word_or_phrase, upgrade, reason)
    ('good at',         'proficient in',        'More professional than "good at"'),
    ('bad at',          'less experienced in',  'More professional than "bad at"'),
    ('very good',       'excellent',            'Stronger than "very good"'),
    ('very bad',        'significantly poor',   'More formal than "very bad"'),
    ('really good',     'exceptional',          'Stronger than "really good"'),
    ('really bad',      'critically poor',      'More formal than "really bad"'),
    ('hard problem',    'complex challenge',    'More professional phrasing'),
    ('easy task',       'straightforward task', 'More professional phrasing'),
    ('talk about',      'elaborate on',         'More formal than "talk about"'),
    ('work on',         'contribute to',        'More formal than "work on"'),
    ('liked it',        'found it valuable',    'More professional than "liked it"'),
    ('liked',           'appreciated',          'More professional than "liked"'),
    ('stuff',           'aspects',              'More formal than "stuff"'),
    ('things',          'elements',             'More formal than "things"'),
    ('big',             'substantial',          'More formal than "big"'),
    ('small',           'minimal',              'More formal than "small"'),
    ('nice',            'commendable',          'More professional than "nice"'),
    ('i think',         'I believe',            'More confident than "I think"'),
    ('maybe',           'potentially',          'More formal than "maybe"'),
    ('help',            'facilitate',           'More formal than "help"'),
    ('fix',             'resolve',              'More formal than "fix"'),
    ('try to',          'endeavor to',          'More formal than "try to"'),
    ('show',            'demonstrate',          'More formal than "show"'),
    ('fast',            'efficient',            'More professional than "fast"'),
    ('slow',            'inefficient',          'More professional than "slow"'),
    ('make',            'develop',              'More formal in technical context'),
    ('build',           'engineer',             'More professional in technical context'),
]


def _apply_rewrites(text):
    """
    Apply phrase-level rewrites. Returns (rewritten_text, list_of_errors_detected).
    """
    errors = []
    result = text

    for pattern, replacement, description in PHRASE_REWRITES:
        matches = re.findall(pattern, result, flags=re.IGNORECASE)
        if matches:
            orig = matches[0] if isinstance(matches[0], str) else matches[0]
            errors.append({
                'original': orig,
                'corrected': replacement,
                'type': description,
            })
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

    return result, errors


def _apply_vocab_upgrades(text):
    """
    Apply word-level vocabulary upgrades.
    Returns (upgraded_text, list_of_upgrades_applied).
    """
    upgrades_applied = []
    result = text

    for original, upgrade, reason in VOCABULARY_UPGRADES:
        pattern = r'\b' + re.escape(original) + r'\b'
        if re.search(pattern, result, flags=re.IGNORECASE):
            upgrades_applied.append({
                'original': original,
                'upgrade': upgrade,
                'reason': reason,
            })
            result = re.sub(pattern, upgrade, result, flags=re.IGNORECASE)

    return result, upgrades_applied


def _detect_fillers(text):
    """Detect filler words. Returns (filler_words_found, total_count)."""
    text_lower = text.lower()
    found = []
    count = 0
    for fw in FILLER_WORDS:
        pattern = r'\b' + re.escape(fw) + r'\b'
        matches = re.findall(pattern, text_lower)
        if matches:
            found.append(fw)
            count += len(matches)
    return found, count


def _fix_capitalization(text):
    """
    Capitalize first letter of each sentence, fix common capitalization.
    """
    # Capitalize first character overall
    if text:
        text = text[0].upper() + text[1:]

    # Capitalize after '. ', '! ', '? '
    text = re.sub(r'([.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)

    # Fix "i " at sentence start or standalone
    text = re.sub(r'\bI\b', 'I', text)  # already capital, but ensure
    text = re.sub(r'(?<![A-Z])\bi\b', 'I', text)  # lowercase 'i' → 'I'

    return text.strip()


def analyze_speech(transcript: str, duration_seconds: int) -> dict:
    """
    Smart AI analysis engine — applies phrase rewrites, vocabulary upgrades,
    filler detection, WPM calculation and scoring.
    """
    if not transcript or not transcript.strip():
        return _empty_result()

    text = transcript.strip()
    words = text.split()
    word_count = len(words)
    duration_minutes = max(duration_seconds / 60, 0.01)
    wpm = round(word_count / duration_minutes, 1)

    # ── Step 1: Detect fillers on ORIGINAL text ───────────────────────────
    filler_words_found, filler_count = _detect_fillers(text)

    # ── Step 2: Phrase-level corrections ─────────────────────────────────
    rewritten, grammar_errors = _apply_rewrites(text)

    # ── Step 3: Vocabulary upgrades on rewritten text ─────────────────────
    final_text, vocabulary_upgrades = _apply_vocab_upgrades(rewritten)

    # ── Step 4: Fix capitalization ────────────────────────────────────────
    corrected_transcript = _fix_capitalization(final_text)

    # ── Step 5: Scoring ───────────────────────────────────────────────────
    # Grammar: start at 100, -7 per detected error
    grammar_score = max(0, min(100, 100 - len(grammar_errors) * 7))

    # Fluency: based on WPM + filler penalty
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

    # Vocabulary: base 65, bonus for improvement opportunities found
    vocab_boost = min(25, len(vocabulary_upgrades) * 4)
    vocab_score = min(100, 65 + vocab_boost + (5 if word_count > 60 else 0))

    # Short attempt penalty
    if duration_seconds < 15:
        fluency_score = max(0, fluency_score - 25)
        grammar_score = max(0, grammar_score - 10)

    # Overall score out of 10
    overall_raw = grammar_score * 0.40 + fluency_score * 0.35 + vocab_score * 0.25
    overall_score = round(overall_raw / 10, 1)

    # ── Step 6: Actionable tips ───────────────────────────────────────────
    tips = []

    if filler_count > 0:
        tips.append(
            f"You used {filler_count} filler word(s) ({', '.join(filler_words_found[:4])}). "
            "Try pausing silently instead of saying 'um' or 'basically'."
        )

    if wpm < 100:
        tips.append(f"Your pace is {wpm} WPM — slightly slow. Aim for 120–150 WPM for engaging delivery.")
    elif wpm > 180:
        tips.append(f"Your pace is {wpm} WPM — a bit fast. Slowing down improves clarity.")
    else:
        tips.append(f"Good speaking pace at {wpm} WPM — within the ideal 120–150 WPM range!")

    if len(grammar_errors) > 0:
        tips.append(
            f"{len(grammar_errors)} phrasing/grammar issue(s) found. "
            "See the corrections below and practise the corrected versions aloud."
        )
    else:
        tips.append("No significant grammar issues detected — well done!")

    if len(vocabulary_upgrades) > 0:
        tips.append(
            f"{len(vocabulary_upgrades)} vocabulary upgrade(s) available. "
            "Using formal vocabulary creates a stronger impression in HR rounds."
        )

    if word_count < 50:
        tips.append(
            "Your answer was quite brief. In HR interviews aim for 100–150 words "
            "with a clear structure: Background → Skills → Projects → Goal."
        )

    if overall_score >= 8.0:
        tips.append("🌟 Excellent! You are at placement-readiness level for HR rounds and GD sessions.")
    elif overall_score >= 6.0:
        tips.append("📈 Good effort! A few more practice sessions will make you fully placement-ready.")
    else:
        tips.append("💪 Keep practising daily. Focus on removing fillers and using formal vocabulary.")

    # ── Rating label ──────────────────────────────────────────────────────
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
    }


def _empty_result():
    return {
        'word_count': 0, 'wpm': 0, 'filler_count': 0,
        'filler_words_found': [], 'grammar_errors': [], 'vocabulary_upgrades': [],
        'corrected_transcript': '', 'grammar_score': 0, 'fluency_score': 0,
        'vocabulary_score': 0, 'overall_score': 0, 'rating_label': 'No speech detected',
        'tips': ['No transcript received. Please try again and speak clearly into the microphone.'],
    }


# ─── API Views ────────────────────────────────────────────────────────────────

class TopicListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        topics = SpeechTopic.objects.filter(is_active=True)
        serializer = SpeechTopicSerializer(topics, many=True)
        return Response(serializer.data)


class AnalyzeSpeechView(APIView):
    """
    POST /api/communication/analyze/
    Accepts: { topic_id, custom_topic, transcript, duration_seconds }
    Returns: full AI analysis + saves attempt to DB
    """
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

        # Run analysis engine
        analysis = analyze_speech(transcript, duration_seconds)

        # Resolve topic
        topic = None
        topic_id = data.get('topic_id')
        if topic_id:
            try:
                topic = SpeechTopic.objects.get(id=topic_id, is_active=True)
            except SpeechTopic.DoesNotExist:
                pass

        # Save attempt
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
    """GET /api/communication/history/ — returns candidate's attempt history"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempts = SpeechAttempt.objects.filter(user=request.user).order_by('-created_at')[:20]
        serializer = SpeechAttemptSerializer(attempts, many=True)
        return Response(serializer.data)


class AdminTopicView(APIView):
    """Admin: GET/POST /api/communication/admin/topics/"""
    permission_classes = [IsAuthenticated]

    def _check_admin(self, request):
        return request.user.is_staff or (hasattr(request.user, 'role') and request.user.role == 'admin')

    def get(self, request):
        if not self._check_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        topics = SpeechTopic.objects.all()
        serializer = SpeechTopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not self._check_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        serializer = SpeechTopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminTopicDetailView(APIView):
    """Admin: PUT/DELETE /api/communication/admin/topics/{id}/"""
    permission_classes = [IsAuthenticated]

    def _check_admin(self, request):
        return request.user.is_staff or (hasattr(request.user, 'role') and request.user.role == 'admin')

    def put(self, request, pk):
        if not self._check_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        try:
            topic = SpeechTopic.objects.get(pk=pk)
        except SpeechTopic.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SpeechTopicSerializer(topic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not self._check_admin(request):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        try:
            topic = SpeechTopic.objects.get(pk=pk)
        except SpeechTopic.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminAttemptsView(APIView):
    """Admin: GET /api/communication/admin/attempts/ — all candidates' speech attempts"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_staff and not (hasattr(request.user, 'role') and request.user.role == 'admin'):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        attempts = SpeechAttempt.objects.all().order_by('-created_at')[:100]
        serializer = SpeechAttemptSerializer(attempts, many=True)
        return Response(serializer.data)


class TranslateView(APIView):
    """
    POST /api/communication/translate/
    Body: { text, source_language, target_language }
      source_language / target_language: 'te-IN' or 'en-IN'
    Uses Sarvam AI (primary) with MyMemory as automatic fallback.
    """
    permission_classes = [IsAuthenticated]

    # Map our short codes to Sarvam language codes
    LANG_MAP = {
        'te': 'te-IN',
        'en': 'en-IN',
        'te-IN': 'te-IN',
        'en-IN': 'en-IN',
    }
    # MyMemory uses different codes
    MYMEMORY_MAP = {
        'te-IN': 'te',
        'en-IN': 'en',
        'te': 'te',
        'en': 'en',
    }

    def _translate_sarvam(self, text, source, target):
        """
        Call Sarvam AI translate API.
        Returns translated string or raises exception.
        """
        api_key = getattr(settings, 'SARVAM_API_KEY', '')
        if not api_key:
            raise ValueError('No Sarvam API key configured')

        src = self.LANG_MAP.get(source, source)
        tgt = self.LANG_MAP.get(target, target)

        # Split into chunks of 1900 chars to stay under 2000 char limit
        chunks = self._chunk_text(text, 1900)
        translated_parts = []

        for chunk in chunks:
            resp = http_requests.post(
                'https://api.sarvam.ai/translate',
                headers={
                    'api-subscription-key': api_key,
                    'Content-Type': 'application/json',
                },
                json={
                    'input': chunk,
                    'source_language_code': src,
                    'target_language_code': tgt,
                    'model': 'sarvam-translate:v1',
                    'enable_preprocessing': True,
                },
                timeout=20,
            )
            resp.raise_for_status()
            data = resp.json()
            translated_parts.append(data.get('translated_text', ''))

        return ' '.join(translated_parts)

    def _translate_mymemory(self, text, source, target):
        """
        Fallback: MyMemory free translation API.
        Splits into 500-char chunks automatically.
        """
        src = self.MYMEMORY_MAP.get(source, source.split('-')[0])
        tgt = self.MYMEMORY_MAP.get(target, target.split('-')[0])
        langpair = f'{src}|{tgt}'

        chunks = self._chunk_text(text, 480)
        translated_parts = []

        for chunk in chunks:
            resp = http_requests.get(
                'https://api.mymemory.translated.net/get',
                params={'q': chunk, 'langpair': langpair},
                timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()
            translated_parts.append(data['responseData']['translatedText'])

        return ' '.join(translated_parts)

    def _chunk_text(self, text, max_len):
        """Split text into chunks at sentence boundaries, max max_len chars each."""
        if len(text) <= max_len:
            return [text]
        # Split at period/newline boundaries
        sentences = re.split(r'(?<=[.!?\n])\s+', text)
        chunks = []
        current = ''
        for sentence in sentences:
            if len(current) + len(sentence) + 1 <= max_len:
                current = (current + ' ' + sentence).strip()
            else:
                if current:
                    chunks.append(current)
                # If single sentence is too long, split at word boundary
                if len(sentence) > max_len:
                    words = sentence.split()
                    current = ''
                    for word in words:
                        if len(current) + len(word) + 1 <= max_len:
                            current = (current + ' ' + word).strip()
                        else:
                            if current:
                                chunks.append(current)
                            current = word
                else:
                    current = sentence
        if current:
            chunks.append(current)
        return chunks if chunks else [text]

    def post(self, request):
        text = request.data.get('text', '').strip()
        source = request.data.get('source_language', 'te-IN')
        target = request.data.get('target_language', 'en-IN')

        if not text:
            return Response({'error': 'No text provided.'}, status=status.HTTP_400_BAD_REQUEST)

        if len(text) > 10000:
            return Response({'error': 'Text too long. Maximum 10,000 characters.'}, status=status.HTTP_400_BAD_REQUEST)

        src_norm = self.LANG_MAP.get(source, source)
        tgt_norm = self.LANG_MAP.get(target, target)

        # Try Sarvam AI first
        engine_used = 'sarvam'
        try:
            translated = self._translate_sarvam(text, src_norm, tgt_norm)
        except ValueError:
            # No API key - use MyMemory
            engine_used = 'mymemory'
            try:
                translated = self._translate_mymemory(text, src_norm, tgt_norm)
            except Exception as e:
                return Response(
                    {'error': f'Translation failed: {str(e)}'},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )
        except Exception as e:
            # Sarvam failed (rate limit / error) - fallback to MyMemory
            engine_used = 'mymemory_fallback'
            try:
                translated = self._translate_mymemory(text, src_norm, tgt_norm)
            except Exception as e2:
                return Response(
                    {'error': f'All translation engines failed. Sarvam: {str(e)} | MyMemory: {str(e2)}'},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )

        return Response({
            'translated_text': translated,
            'source_language': src_norm,
            'target_language': tgt_norm,
            'engine': engine_used,
            'char_count': len(text),
        })
