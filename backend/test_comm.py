import sys, os
sys.path.insert(0, '.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'placement_arena.settings'
import django
django.setup()

from communication.views import analyze_speech

transcript = "hey hello my name is tanvith I am currently pursuing a BTech final year industry of computer science engineering and artificial Intelligence and machine learning I have done certification program in Java and also done project related to Ai and that's all about myself"
result = analyze_speech(transcript, 45)

print("=== CORRECTED VERSION ===")
print(result['corrected_transcript'])
print()
print("=== GRAMMAR ERRORS DETECTED ===")
for e in result['grammar_errors']:
    print(f"  ORIG: {e['original']}")
    print(f"  FIX:  {e['corrected']}")
    print(f"  WHY:  {e['type']}")
    print()
print("=== VOCAB UPGRADES ===")
for v in result['vocabulary_upgrades']:
    print(f"  {v['original']} -> {v['upgrade']}")
print()
print(f"Grammar: {result['grammar_score']}%  Fluency: {result['fluency_score']}%  Vocab: {result['vocabulary_score']}%  Overall: {result['overall_score']}/10")
print(f"Rating: {result['rating_label']}")
