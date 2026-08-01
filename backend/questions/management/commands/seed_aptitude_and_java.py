from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten Permutations/Combinations and Probability PDF notes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with P&C and Probability PDF notes..."))

        # ----------------------------------------------------
        # 1. PERMUTATIONS AND COMBINATIONS - PDF MASTER NOTES
        # ----------------------------------------------------
        pnc_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Permutations & Combinations

#### 1. Fundamental Definitions & Identities
- **Permutation ($^nP_r$)**: Arrangements where **Position/Order Matters**!
  - $^nP_r = \\frac{n!}{(n-r)!}$ | $^nP_n = n!$ | $^nP_{n-1} = n!$ | $^nP_1 = n$ | $^nP_0 = 1$
- **Combination ($^nC_r$)**: Selection where **Position Does NOT Matter**!
  - $^nC_r = \\frac{n!}{r!(n-r)!}$ | $^nC_r = ^nC_{n-r}$ | $^nC_n = ^nC_0 = 1$ | $^nC_1 = n$
- **Key Relation**: $^nP_r = ^nC_r \\times r!$

#### 2. Word Arrangements & Identical Objects Rule
- **Distinct Letters**: `YUVRAJ` (6 letters) $\\to 6P_6 = 6! = \\mathbf{720 \\text{ ways}}$.
- **Identical Objects (Repetitions)**: Formula $\\frac{n!}{p! \\, q!}$
  - `BALLOON` (7 letters, L=2, O=2) $\\to \\frac{7!}{2! \\, 2!} = \\mathbf{1260 \\text{ ways}}$.

#### 3. Vowels Together vs NEVER Together (Unit Method & Gap Method)
- **Vowels Always Together (Unit Method)**: Treat all vowels as a single unit!
  - `TENDULKAR` (9 letters: Vowels E, U, A = 3; Consonants = 6).
  - Total units $= 6 + 1 = 7 \\implies 7! \\times 3! = 5040 \\times 6 = \\mathbf{30,240 \\text{ ways}}$!
- **Never Together**: $\\text{Total Arrangements} - \\text{Together Arrangements}$.
- **GAP METHOD (No two elements together)**:
  - Arrange 3 boys ($3! = 6$). Creates 4 gaps `_ B _ B _ B _`. Choose 2 gaps for 2 girls ($^4C_2 \\times 2! = 12$) $\\implies 6 \\times 12 = \\mathbf{36 \\text{ ways}}$!

#### 4. Circular Permutations & Number Formation
- **Normal Circle**: $(n-1)!$ | **Necklace/Garland**: $\\frac{(n-1)!}{2}$
- **Number Formation (Digits 0-4 without repetition)**:
  - 1st digit cannot be 0 (4 choices), 2nd (4 choices), 3rd (3 choices) $\\implies 4 \\times 4 \\times 3 = \\mathbf{48}$.

#### 5. Handshakes, Matches, Tickets & Geometric Shapes
- **Handshakes (Order doesn't matter $\\to ^nC_2$)**: 20 people $\\to ^20C_2 = \\frac{20 \\times 19}{2} = \\mathbf{190 \\text{ handshakes}}$.
- **Railway Tickets (Order matters $\\to ^nP_2$)**: 20 stations $\\to 22P_2 = 22 \\times 21 = \\mathbf{462 \\text{ ticket types}}$.
- **Polygon Diagonals**: $\\frac{n(n-3)}{2}$ | Octagon Triangles $= ^8C_3 = \\mathbf{56}$.
"""

        pnc_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="permutations-combinations",
            defaults={
                "order": 12,
                "name": "Permutations & Combinations (PDF Master Edition)",
                "description": "Master nPr vs nCr, Identical letters, Vowels Together / Gap method, Circular permutations, Handshakes & Diagonals.",
                "icon": "🔢",
                "formula_sheet": pnc_formula_sheet
            }
        )

        # ----------------------------------------------------
        # 2. PROBABILITY - PDF MASTER NOTES
        # ----------------------------------------------------
        prob_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Probability

#### 1. Core Rules & Range
- $P(E) = \\frac{\\text{Favorable Outcomes}}{\\text{Total Outcomes}} = \\frac{\\text{Our Selections}}{\\text{Total Selections}}$
- **Range**: $0 \\le P(E) \\le 1$ ($0 =$ Impossible, $1 =$ Certain).
- **Complement Rule**: $P(\\text{not } E) = 1 - P(E)$ (Used for "At least one").
- **Addition Rule (OR)**: $P(A \\text{ or } B) = P(A) + P(B) - P(A \\cap B)$.
- **Multiplication Rule (AND)**: $P(A \\text{ and } B) = P(A) \\times P(B)$.

#### 2. Coins & Dice Shortcuts
- **Coins Probability ($2^n$ total outcomes)**:
  - Probability of exactly $r$ heads: $P = \\frac{^nC_r}{2^n}$
  - *Example*: 5 coins tossed, exactly 3 heads $\\implies \\frac{^5C_3}{2^5} = \\frac{10}{32} = \\mathbf{\\frac{5}{16}}$!
- **2 Dice Sum Shortcut Table**:
  - Sum 2/12 $\\to 1/36$ | Sum 3/11 $\\to 2/36$ | Sum 4/10 $\\to 3/36$ | Sum 5/9 $\\to 4/36$ | Sum 6/8 $\\to 5/36$ | Sum 7 $\\to 6/36$

#### 3. Cards & Bag Ball Selection
- **Deck of 52 Cards**: 26 Red, 26 Black, 16 Face Cards (4 Kings, 4 Queens, 4 Jacks, 4 Aces).
  - *Example*: Diamond OR King $= \\frac{13 + 4 - 1}{52} = \\mathbf{\\frac{4}{13}}$ (Subtract 1 overlap).

#### 4. Contradict Each Other & Problem Solving Laws
- **Contradiction Rule**: $P(\\text{Contradict}) = P(A_{\\text{true}} \\cap B_{\\text{false}}) + P(A_{\\text{false}} \\cap B_{\\text{true}})$
  - *PDF Ex*: A (60% true), B (45% true) $\\implies (0.6 \\times 0.55) + (0.4 \\times 0.45) = 0.33 + 0.18 = \\mathbf{51\\%}$!
- **Problem Solved by Students**: $P(\\text{Solved}) = 1 - P(\\text{None solve})$
  - *PDF Ex*: A (1/2), B (1/3), C (1/4) solve $\\implies 1 - (1/2 \\times 2/3 \\times 3/4) = 1 - 1/4 = \\mathbf{3/4}$!
"""

        prob_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="probability",
            defaults={
                "order": 13,
                "name": "Probability (PDF Master Edition)",
                "description": "Master Coins nCr/2^n trick, 2 Dice Sum Table, Cards Overlap rule, Contradiction law, & Problem Solving Complement.",
                "icon": "🎲",
                "formula_sheet": prob_formula_sheet
            }
        )

        # Seed PDF Worked Questions
        AptitudeQuestion.objects.get_or_create(
            topic=pnc_topic,
            text="In how many ways can the letters of the word 'TENDULKAR' be arranged such that all vowels are always together?",
            defaults={
                "difficulty": "intermediate",
                "option_a": "15,120", "option_b": "30,240", "option_c": "5,040", "option_d": "40,320",
                "correct_option": "B",
                "explanation": "PDF Unit Method: Vowels (E, U, A = 3) treated as 1 unit. Consonants = 6.\nTotal units = 7 -> Arrangements = 7! * 3! = 5040 * 6 = 30,240 ways!"
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=pnc_topic,
            text="20 members attended a party. If each person shakes hands with every other person once, find the total number of handshakes.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "380", "option_b": "190", "option_c": "400", "option_d": "200",
                "correct_option": "B",
                "explanation": "PDF Handshake Combination Formula: 20C2 = (20 * 19) / (2 * 1) = 190 handshakes!"
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=prob_topic,
            text="A speaks truth in 60% cases and B speaks truth in 45% cases. In what percentage of cases are they likely to contradict each other?",
            defaults={
                "difficulty": "advanced",
                "option_a": "45%", "option_b": "51%", "option_c": "55%", "option_d": "48%",
                "correct_option": "B",
                "explanation": "PDF Contradiction Formula: P(Contradict) = (A_true * B_false) + (A_false * B_true) = (0.60 * 0.55) + (0.40 * 0.45) = 0.33 + 0.18 = 0.51 = 51%!"
            }
        )

        self.stdout.write(self.style.SUCCESS("P&C and Probability PDF notes & worked problems successfully seeded!"))
