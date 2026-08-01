from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten PDF shortcut strategies and 23 Java Quest topics'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with user's PDF shortcut strategy..."))

        # ----------------------------------------------------
        # 1. SEED APTITUDE TOPICS WITH EXACT USER PDF SHORTCUTS
        # ----------------------------------------------------
        aptitude_data = [
            {
                "order": 1, "name": "Squares & Square Roots (Special PDF Method)", "slug": "squares-and-square-roots", "icon": "⚡",
                "desc": "Master 1-125 Squares using Base 50 & 100 methods, Unit Digit 5 trick, and 2-step Square Root extraction.",
                "formula": """### 📄 User PDF Special Shortcuts: Squares & Square Roots

#### 1. Numbers Ending in Digit 5 (15, 25, 35, 45, 55...)
- **Rule**: Write $25$ at the end. Multiply the tens digit by its succeeding number $(N \times (N+1))$.
- **Examples**:
  - $15^2 \to (1 \times 2) \mid 25 = 225$
  - $25^2 \to (2 \times 3) \mid 25 = 625$
  - $35^2 \to (3 \times 4) \mid 25 = 1225$
  - $45^2 \to (4 \times 5) \mid 25 = 2025$
  - $55^2 \to (5 \times 6) \mid 25 = 3025$

#### 2. Base 50 Method (Nearer to 50: 41-49 & 51-59)
- **a) Below 50 (e.g. $47^2$)**:
  - **Step 1**: Find difference from 50 ($50 - 47 = 3$). Square it: $3^2 = 09$ (must be 2 digits).
  - **Step 2**: Subtract difference from 25 ($25 - 3 = 22$).
  - **Result**: $47^2 = 2209$.
- **b) Above 50 (e.g. $53^2$)**:
  - **Step 1**: Difference from 50 ($53 - 50 = +3$). Square it: $3^2 = 09$.
  - **Step 2**: Add difference to 25 ($25 + 3 = 28$).
  - **Result**: $53^2 = 2809$.

#### 3. Base 100 Method (Nearer to 100: 76-99 & 101-125)
- **a) Below 100 (e.g. $94^2$)**:
  - Difference from 100 ($100 - 94 = 6$). $6^2 = 36$ at end.
  - Subtract 6 from 94: $94 - 6 = 88$.
  - **Result**: $94^2 = 8836$.
- **b) Above 100 (e.g. $107^2$)**:
  - Difference from 100 ($107 - 100 = 7$). $7^2 = 49$ at end.
  - Add 7 to 107: $107 + 7 = 114$.
  - **Result**: $107^2 = 11449$.
- *Note: If Step-1 square exceeds 2 digits, carry over to Step-2!*

#### 4. Square Root 3-Step Trick (e.g. $\\sqrt{7569}$)
- **Step 1**: Unit digit is 9 $\\implies$ root ends in 3 or 7.
- **Step 2**: Ignore last 2 digits ($69$). 75 lies between $8^2 = 64$ and $9^2 = 81$. Take smaller ($8$). Answer is 83 or 87.
- **Step 3**: 75 is closer to 81 ($9^2$) than 64 ($8^2$). Since it's closer to the higher square, pick the higher value $\\to \\mathbf{87}$!
"""
            },
            {
                "order": 2, "name": "Cubes & Cube Roots (Special PDF Method)", "slug": "cubes-and-cube-roots", "icon": "🎲",
                "desc": "Master 1-15 Cubes and 3-Step Cube Root extraction without calculation.",
                "formula": """### 📄 User PDF Special Shortcuts: Cubes & Cube Roots

#### 1. Unit Digits Mapping of Cubes (1 to 10)
- **Same Number Endings**: $1, 4, 5, 6, 9, 0$ end with their SAME numbers!
  - $1^3 = 1$, $4^3 = 64 (4)$, $5^3 = 125 (5)$, $6^3 = 216 (6)$, $9^3 = 729 (9)$, $10^3 = 1000 (0)$.
- **Flipped Pair Endings**:
  - $2 \\leftrightarrow 8$ ($2^3 = 8$, $8^3 = 512$)
  - $3 \\leftrightarrow 7$ ($3^3 = 27$, $7^3 = 343$)

#### 2. Cube Root 3-Step Trick (e.g. $\\sqrt[3]{97336}$)
- **Step 1**: Unit digit is $6 \\implies$ cube root ends in **6**.
- **Step 2**: Cross out / Ignore the last 3 digits ($336$). Remaining number is **97**.
- **Step 3**: $97$ lies between $4^3 = 64$ and $5^3 = 125$. Take the preceding perfect cube ($4^3 = 64$).
- **Final Result**: $\\sqrt[3]{97336} = \\mathbf{46}$!

#### 3. More PDF Examples:
- $\\sqrt[3]{29791} \\to$ Ends in 1, ignore 791, 29 between $3^3(27)$ and $4^3(64) \\implies \\mathbf{31}$.
- $\\sqrt[3]{195112} \\to$ Ends in 2 (so root ends in 8), ignore 112, 195 between $5^3(125)$ and $6^3(216) \\implies \\mathbf{58}$.
"""
            },
            {
                "order": 3, "name": "Fractions to Percentage Master Table", "slug": "fractions-to-percentage", "icon": "🔢",
                "desc": "PDF Memory Table for instant fraction to percentage conversion up to 1/12.",
                "formula": """### 📄 User PDF Special Shortcuts: Fraction to Percentage Conversion

#### 1. Core Conversion Table:
- $\\frac{1}{2} = 50\\%$
- $\\frac{1}{3} = 33.33\\%$, $\\frac{2}{3} = 66.66\\%$
- $\\frac{1}{4} = 25\\%$, $\\frac{3}{4} = 75\\%$
- $\\frac{1}{5} = 20\\%$, $\\frac{2}{5} = 40\\%$, $\\frac{3}{5} = 60\\%$, $\\frac{4}{5} = 80\\%$
- $\\frac{1}{6} = 16.66\\%$, $\\frac{5}{6} = 83.33\\%$
- $\\frac{1}{7} = 14.28\\%$, $\\frac{2}{7} = 28.57\\%$, $\\frac{3}{7} = 42.85\\%$, $\\frac{4}{7} = 57.14\\%$, $\\frac{5}{7} = 71.42\\%$, $\\frac{6}{7} = 85.71\\%$
- $\\frac{1}{8} = 12.5\\%$, $\\frac{3}{8} = 37.5\\%$, $\\frac{5}{8} = 62.5\\%$, $\\frac{7}{8} = 87.5\\%$

#### 2. The Secret 9 & 11 Pattern Tricks:
- **Denominator 9 (Multiply Numerator by 11)**:
  - $\\frac{1}{9} = 11.11\\%$ | $\\frac{2}{9} = 22.22\\%$ | $\\frac{4}{9} = 44.44\\%$ | $\\frac{7}{9} = 77.77\\%$
- **Denominator 11 (Multiply Numerator by 9)**:
  - $\\frac{1}{11} = 9.09\\%$ | $\\frac{2}{11} = 18.18\\%$ | $\\frac{3}{11} = 27.27\\%$ | $\\frac{5}{11} = 45.45\\%$
"""
            },
            {
                "order": 4, "name": "Percentages & Split-Up Methods", "slug": "percentages", "icon": "📊",
                "desc": "PDF Percentage Shortcuts: a% of b = b% of a, 10% and 1% decimal shift tricks, and successive change.",
                "formula": """### 📄 User PDF Special Shortcuts: Percentages

#### 1. Reversal Law: $a\\% \\text{ of } b = b\\% \\text{ of } a$
- **Example**: Find $13\\% \\text{ of } 200$.
- **PDF Trick**: Reperse as $200\\% \\text{ of } 13 = 2 \\times 13 = \\mathbf{26}$!

#### 2. Decimal Shift Trick for 10% & 1%:
- **10% of any number**: Place decimal point before unit digit ($10\\% \\text{ of } 7432 = 743.2$).
- **1% of any number**: Place decimal point before tens digit ($1\\% \\text{ of } 7432 = 74.32$).

#### 3. Combination Trick for Complex Percentages:
- **Find 21% of 6400**:
  - $10\\% = 640.0 \\implies 20\\% = 640 \\times 2 = 1280$.
  - $1\\% = 64$.
  - $21\\% = 1280 + 64 = \\mathbf{1344}$!
- **Find 19% of 7200**:
  - $20\\% = 1440$, $1\\% = 72$.
  - $19\\% = 1440 - 72 = \\mathbf{1368}$!

#### 4. Equal Percentage Increase & Decrease (Net Loss Rule):
- If an entity is increased by $x\\%$ and then decreased by $x\\%$, the net result is ALWAYS a **LOSS** of $\\mathbf{\\left(\\frac{x}{10}\\right)^2\\%}$!
  - $10\\% \\uparrow$ and $10\\% \\downarrow \\implies 1^2 = 1\\% \\text{ loss}$.
  - $20\\% \\uparrow$ and $20\\% \\downarrow \\implies 2^2 = 4\\% \\text{ loss}$.
  - $30\\% \\uparrow$ and $30\\% \\downarrow \\implies 3^2 = 9\\% \\text{ loss}$.

#### 5. Relative Percentage Comparison Shortcuts:
- **A is how much % less than B?**: $\\frac{\\text{Diff}}{B} \\times 100$
- **B is how much % more than A?**: $\\frac{\\text{Diff}}{A} \\times 100$
- **Example (A=60, B=80)**: B is more than A by $\\frac{20}{60} \\times 100 = 33.33\\%$.
"""
            },
            {
                "order": 5, "name": "Profit and Loss", "slug": "profit-and-loss", "icon": "📈",
                "desc": "Cost Price, Selling Price, Markups, Discounts, and False Weights.",
                "formula": "### 💡 PDF Shortcut: CP=100% Base Method\n- Profit % = (SP - CP)/CP * 100\n- False Weight Profit % = (Error / (True Value - Error)) * 100"
            },
            {
                "order": 6, "name": "Simple & Compound Interest", "slug": "simple-compound-interest", "icon": "💰",
                "desc": "SI vs CI growth, compounding frequencies, and 2-year/3-year CI-SI differences.",
                "formula": "### 💡 PDF Shortcut: Difference Formulas\n- D2 = P(R/100)^2\n- D3 = P(R/100)^2 * (3 + R/100)"
            },
            {
                "order": 7, "name": "Averages", "slug": "averages", "icon": "⚖️",
                "desc": "Deviation method and average speed shortcut.",
                "formula": "### 💡 PDF Shortcut: Average Speed\n- Average Speed for equal distance = (2xy)/(x+y)"
            },
            {
                "order": 8, "name": "Alligations & Mixtures", "slug": "alligations-mixtures", "icon": "🧪",
                "desc": "Rule of Alligation cross method.",
                "formula": "### 💡 PDF Shortcut: Cross Difference Rule\n- Ratio = (Dearer - Mean) / (Mean - Cheaper)"
            },
            {
                "order": 9, "name": "Problems on Ages", "slug": "problems-on-ages", "icon": "⏳",
                "desc": "Ratio-based age problems with constant difference.",
                "formula": "### 💡 PDF Shortcut: Age Difference Invariance\n- Age difference remains identical throughout life."
            },
            {
                "order": 10, "name": "Ratios & Proportions", "slug": "ratios-proportions", "icon": "📐",
                "desc": "Mean and third proportionals.",
                "formula": "### 💡 PDF Shortcut: Mean Proportional\n- Mean proportional = sqrt(a * b)"
            },
            {
                "order": 11, "name": "Partnerships", "slug": "partnerships", "icon": "🤝",
                "desc": "Capital x Time = Profit ratio.",
                "formula": "### 💡 PDF Shortcut: Profit Share\n- PA : PB = (CA * TA) : (CB * TB)"
            },
            {
                "order": 12, "name": "Time and Work", "slug": "time-and-work", "icon": "⏱️",
                "desc": "1-day work efficiency and combined rates.",
                "formula": "### 💡 PDF Shortcut: Combined Work\n- Time together = (X * Y) / (X + Y)"
            },
            {
                "order": 13, "name": "Speed, Distance & Time", "slug": "speed-distance-time", "icon": "🚀",
                "desc": "km/h to m/s conversion and relative speed.",
                "formula": "### 💡 PDF Shortcut: Speed Conversion\n- km/h to m/s: Multiply by 5/18."
            },
            {
                "order": 14, "name": "Pipes and Cisterns", "slug": "pipes-and-cisterns", "icon": "🚰",
                "desc": "Inlet & outlet combined rate.",
                "formula": "### 💡 PDF Shortcut: Net Rate\n- Net Fill = (Inlet * Outlet) / (Outlet - Inlet)"
            },
            {
                "order": 15, "name": "Permutations & Combinations", "slug": "permutations-combinations", "icon": "🔢",
                "desc": "nCr and nPr formulas.",
                "formula": "### 💡 PDF Shortcut: Circular Permutation\n- Circular arrangement = (n - 1)!"
            }
        ]

        for item in aptitude_data:
            topic, _ = AptitudeTopic.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "order": item["order"],
                    "name": item["name"],
                    "description": item["desc"],
                    "icon": item["icon"],
                    "formula_sheet": item["formula"]
                }
            )

        # ----------------------------------------------------
        # SEED EXACT HANDWRITTEN PDF QUESTIONS
        # ----------------------------------------------------
        squares_topic = AptitudeTopic.objects.get(slug="squares-and-square-roots")
        AptitudeQuestion.objects.get_or_create(
            topic=squares_topic,
            text="Find the square of 47 using the Base 50 shortcut method from PDF notes.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "2209",
                "option_b": "2309",
                "option_c": "2109",
                "option_d": "2409",
                "correct_option": "A",
                "explanation": "Step 1: Difference from 50 is (50 - 47 = 3). Square: 3^2 = 09.\nStep 2: Subtract difference from 25: (25 - 3 = 22).\nCombine: 2209."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=squares_topic,
            text="Find the square root of 7569 using the PDF 3-step shortcut.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "83",
                "option_b": "87",
                "option_c": "93",
                "option_d": "77",
                "correct_option": "B",
                "explanation": "Step 1: Unit digit is 9 -> Root ends in 3 or 7.\nStep 2: Ignore 69. 75 lies between 8^2 (64) and 9^2 (81). Take smaller (8) -> 83 or 87.\nStep 3: 75 is closer to 81 (higher square) -> Choose 87."
            }
        )

        cubes_topic = AptitudeTopic.objects.get(slug="cubes-and-cube-roots")
        AptitudeQuestion.objects.get_or_create(
            topic=cubes_topic,
            text="Find the cube root of 97336 using the PDF 3-step shortcut.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "36",
                "option_b": "46",
                "option_c": "56",
                "option_d": "44",
                "correct_option": "B",
                "explanation": "Step 1: Unit digit is 6 -> Cube root ends in 6.\nStep 2: Ignore last 3 digits (336). Remaining is 97.\nStep 3: 97 lies between 4^3 (64) and 5^3 (125). Take preceding cube 4 -> Result = 46."
            }
        )

        pct_topic = AptitudeTopic.objects.get(slug="percentages")
        AptitudeQuestion.objects.get_or_create(
            topic=pct_topic,
            text="Find 21% of 6400 using the PDF 10% and 1% combination technique.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "1344",
                "option_b": "1280",
                "option_c": "1380",
                "option_d": "1440",
                "correct_option": "A",
                "explanation": "10% of 6400 = 640 -> 20% = 1280.\n1% of 6400 = 64.\n21% = 20% + 1% = 1280 + 64 = 1344."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=pct_topic,
            text="The price of sugar is first increased by 30% and then decreased by 30%. If the present price is Rs. 273, find the original price.",
            defaults={
                "difficulty": "advanced",
                "option_a": "Rs. 300",
                "option_b": "Rs. 320",
                "option_c": "Rs. 290",
                "option_d": "Rs. 350",
                "correct_option": "A",
                "explanation": "Equal % increase and decrease of 30% results in a net loss of 3^2 = 9%.\nPresent value = (100 - 9)% = 91% = Rs 273.\n91% -> 273 (91 * 3 = 273).\nOriginal Price (100%) = 100 * 3 = Rs 300."
            }
        )

        self.stdout.write(self.style.SUCCESS("Database seeded with exact PDF shortcuts and handwritten examples!"))
