import re
import math
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from .models import SpeechTopic, SpeechAttempt
from .serializers import SpeechTopicSerializer, SpeechAttemptSerializer, SpeechAttemptCreateSerializer

# ─── Filler words dictionary ────────────────────────────────────────────────
FILLER_WORDS = [
    'um', 'uh', 'umm', 'uhh', 'er', 'err', 'hmm',
    'like', 'basically', 'actually', 'literally',
    'you know', 'i mean', 'sort of', 'kind of',
    'so yeah', 'right', 'okay so', 'and so',
]

# ─── Vocabulary upgrade map ──────────────────────────────────────────────────
VOCABULARY_UPGRADES = {
    'good at': 'proficient in',
    'bad at': 'less experienced in',
    'very good': 'exceptional',
    'very bad': 'significantly poor',
    'a lot': 'considerably',
    'lots of': 'numerous',
    'big': 'substantial',
    'small': 'minimal',
    'nice': 'commendable',
    'hard': 'challenging',
    'hard problem': 'complex challenge',
    'easy': 'straightforward',
    'use': 'utilize',
    'make': 'develop',
    'build': 'engineer',
    'help': 'facilitate',
    'fix': 'resolve',
    'try': 'endeavor',
    'show': 'demonstrate',
    'talk about': 'elaborate on',
    'work on': 'contribute to',
    'do': 'execute',
    'fast': 'efficient',
    'slow': 'inefficient',
    'liked': 'appreciated',
    'liked it': 'found it valuable',
    'i think': 'I believe',
    'maybe': 'potentially',
    'stuff': 'aspects',
    'things': 'elements',
    'get': 'obtain',
    'got': 'acquired',
}

# ─── Grammar correction rules ────────────────────────────────────────────────
GRAMMAR_RULES = [
    # Past tense corrections
    (r'\bI go to\b', 'I went to', 'Verb tense error: Use past tense "went" instead of "go"'),
    (r'\bI goes to\b', 'I went to', 'Subject-verb agreement error'),
    (r'\bgiven presentation\b', 'gave a presentation', 'Verb form error: Use "gave" with article "a"'),
    (r'\bdone the work\b', 'completed the work', 'Use "completed" for formal context'),
    (r'\bI am come\b', 'I have come', 'Auxiliary verb error'),
    (r'\bI have went\b', 'I have gone', '"Have went" is incorrect; use "have gone"'),
    (r'\bI have did\b', 'I have done', '"Have did" is incorrect; use "have done"'),
    (r'\bI was went\b', 'I went', 'Remove auxiliary "was" before past tense verb'),
    (r'\bthey was\b', 'they were', 'Subject-verb agreement: use "were" with plural subject'),
    (r'\bhe were\b', 'he was', 'Subject-verb agreement: use "was" with singular subject'),
    (r'\bshe were\b', 'she was', 'Subject-verb agreement: use "was" with singular subject'),
    (r'\bwe was\b', 'we were', 'Subject-verb agreement: use "were" with "we"'),
    (r'\byou was\b', 'you were', 'Subject-verb agreement: use "were" with "you"'),
    (r'\bI are\b', 'I am', 'Subject-verb agreement: use "am" with "I"'),
    (r'\bi done\b', 'I did', '"Done" requires auxiliary verb; use "I did"'),
    (r'\bI has\b', 'I have', 'Subject-verb agreement: use "have" with "I"'),
    (r'\bhe have\b', 'he has', 'Subject-verb agreement: use "has" with singular third-person'),
    (r'\bshe have\b', 'she has', 'Subject-verb agreement: use "has" with singular third-person'),
    (r'\bmy self\b', 'myself', '"My self" should be one word: "myself"'),
    (r'\bour self\b', 'ourselves', '"Our self" should be "ourselves"'),
    # Article errors
    (r'\ban university\b', 'a university', 'Article error: "university" starts with a consonant sound, use "a"'),
    (r'\ba hour\b', 'an hour', 'Article error: "hour" starts with a vowel sound, use "an"'),
    (r'\ba honest\b', 'an honest', 'Article error: "honest" starts with vowel sound, use "an"'),
    # Double negatives
    (r"\bdon't know nothing\b", "don't know anything", 'Double negative error'),
    (r"\bcan't do nothing\b", "can't do anything", 'Double negative error'),
    # Preposition fixes
    (r'\bdiscuss about\b', 'discuss', '"Discuss" does not take "about" — it is redundant'),
    (r'\bexplain about\b', 'explain', '"Explain" does not take "about" — it is redundant'),
    (r'\benter into\b', 'enter', '"Enter" does not need "into"'),
    # Tense mismatches
    (r'\byesterday I (\w+)ing\b', 'yesterday I was {verb}ing', 'Use "was/were + verb+ing" for past progressive'),
]


def analyze_speech(transcript: str, duration_seconds: int) -> dict:
    """
    Core unlimited AI analysis engine.
    Analyzes grammar, vocabulary, fillers, WPM and returns structured feedback.
    """
    if not transcript or not transcript.strip():
        return _empty_result()

    text = transcript.strip()
    text_lower = text.lower()
    words = text.split()
    word_count = len(words)
    duration_minutes = max(duration_seconds / 60, 0.01)
    wpm = round(word_count / duration_minutes, 1)

    # ── Filler word detection ──────────────────────────────────────────────
    filler_words_found = []
    filler_count = 0
    for fw in FILLER_WORDS:
        pattern = r'\b' + re.escape(fw) + r'\b'
        matches = re.findall(pattern, text_lower)
        if matches:
            filler_words_found.append(fw)
            filler_count += len(matches)

    # ── Grammar analysis ───────────────────────────────────────────────────
    grammar_errors = []
    corrected = text
    for pattern, replacement, explanation in GRAMMAR_RULES:
        matches = re.findall(pattern, corrected, flags=re.IGNORECASE)
        if matches:
            grammar_errors.append({
                'original': matches[0] if isinstance(matches[0], str) else matches[0][0],
                'corrected': replacement,
                'type': explanation
            })
            corrected = re.sub(pattern, replacement, corrected, flags=re.IGNORECASE)

    # ── Vocabulary upgrades ────────────────────────────────────────────────
    vocabulary_upgrades = []
    vocab_corrected = corrected
    for original, upgrade in VOCABULARY_UPGRADES.items():
        pattern = r'\b' + re.escape(original) + r'\b'
        if re.search(pattern, vocab_corrected, flags=re.IGNORECASE):
            vocabulary_upgrades.append({
                'original': original,
                'upgrade': upgrade,
                'reason': f'Replace "{original}" with "{upgrade}" for professional communication'
            })
            vocab_corrected = re.sub(pattern, upgrade, vocab_corrected, flags=re.IGNORECASE)

    corrected_final = vocab_corrected

    # ── Scoring ───────────────────────────────────────────────────────────
    # Grammar score: starts at 100, -8 per error
    grammar_score = max(0, min(100, 100 - (len(grammar_errors) * 8)))

    # Fluency score: based on WPM (ideal: 120-150 WPM) and filler words
    if 120 <= wpm <= 150:
        pace_score = 100
    elif 100 <= wpm < 120 or 150 < wpm <= 180:
        pace_score = 85
    elif 80 <= wpm < 100 or 180 < wpm <= 200:
        pace_score = 70
    elif wpm < 80:
        pace_score = max(40, int(wpm / 80 * 70))
    else:
        pace_score = max(50, int(200 / wpm * 70))

    filler_penalty = min(40, filler_count * 5)
    fluency_score = max(0, min(100, pace_score - filler_penalty))

    # Vocabulary score: starts at 70, +5 per upgrade opportunity found, -3 per grade-boosted word still basic
    vocab_base = 70
    vocab_bonus = min(20, len(vocabulary_upgrades) * 3)  # Found opportunities (better to find them)
    vocab_score = min(100, vocab_base + vocab_bonus + (5 if word_count > 50 else 0))

    # Duration: penalize very short attempts
    if duration_seconds < 20:
        fluency_score = max(0, fluency_score - 20)
        grammar_score = max(0, grammar_score - 10)

    # Overall score (weighted average, out of 10)
    overall_raw = (grammar_score * 0.4 + fluency_score * 0.35 + vocab_score * 0.25)
    overall_score = round(overall_raw / 10, 1)

    # ── Actionable tips ────────────────────────────────────────────────────
    tips = []
    if filler_count > 3:
        tips.append(f"You used {filler_count} filler words ({', '.join(filler_words_found[:4])}). Practice pausing silently instead of using fillers.")
    if wpm < 100:
        tips.append(f"Your speaking pace is {wpm} WPM — slightly slow. Aim for 120-150 WPM for engaging delivery.")
    elif wpm > 180:
        tips.append(f"Your speaking pace is {wpm} WPM — slightly fast. Slow down a bit to improve clarity and comprehension.")
    else:
        tips.append(f"Great speaking pace at {wpm} WPM — right in the ideal zone for professional communication!")
    if len(grammar_errors) > 0:
        tips.append(f"Found {len(grammar_errors)} grammar error(s). Review subject-verb agreement and verb tenses carefully.")
    if len(vocabulary_upgrades) > 0:
        tips.append(f"Upgrade {len(vocabulary_upgrades)} word(s) from informal to professional vocabulary for a stronger impression.")
    if word_count < 50:
        tips.append("Your response was brief. In HR interviews, aim for 100-150 words for most answers.")
    if grammar_score >= 90 and filler_count == 0:
        tips.append("Excellent grammar and zero filler words — you sound highly professional!")
    if overall_score >= 8.0:
        tips.append("Outstanding! You are at placement-readiness level for HR rounds and GD sessions.")

    # ── Rating label ───────────────────────────────────────────────────────
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
        'corrected_transcript': corrected_final,
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


# ─── API Views ───────────────────────────────────────────────────────────────

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

    def get(self, request):
        if not request.user.is_staff and not (hasattr(request.user, 'role') and request.user.role == 'admin'):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        topics = SpeechTopic.objects.all()
        serializer = SpeechTopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff and not (hasattr(request.user, 'role') and request.user.role == 'admin'):
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
