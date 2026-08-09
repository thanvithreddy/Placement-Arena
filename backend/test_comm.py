import sys, os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'placement_arena.settings'
import django
django.setup()

from communication.views import _rule_based_correct, analyze_speech

# Test 1: the exact failing sentence from the screenshot
t1 = "yesterday I go to the store for buy some milk but the shop was closed already"
corrected, errors, vocab = _rule_based_correct(t1)
print("=== TEST 1: Tense + preposition + word order ===")
print("IN: ", t1)
print("OUT:", corrected)
print("ERRORS:", len(errors))
for e in errors:
    print(f"  [{e['original']}] -> [{e['corrected']}]: {e['type']}")
print()

# Test 2: Thanvith's self intro
t2 = "hey hello my name is tanvith I am currently pursuing a BTech final year industry of computer science engineering and artificial Intelligence and machine learning I have done certification program in Java and also done project related to Ai and that's all about myself"
corrected2, errors2, vocab2 = _rule_based_correct(t2)
print("=== TEST 2: Self-intro ===")
print("IN: ", t2[:80], "...")
print("OUT:", corrected2[:120], "...")
print("ERRORS:", len(errors2))
print("VOCAB:", len(vocab2))
print()

# Test 3: full analyze_speech (no Gemini key, uses rule-based)
result = analyze_speech(t1, 10)
print("=== TEST 3: Full analysis on test 1 ===")
print("Corrected:", result['corrected_transcript'])
print("Grammar errors:", len(result['grammar_errors']))
print("Engine:", result['engine'])
print("Score:", result['overall_score'])
