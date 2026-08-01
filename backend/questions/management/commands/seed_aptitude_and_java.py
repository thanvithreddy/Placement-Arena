from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten Ages, Ratios, and Partnerships PDF notes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with Ages, Ratios, and Partnerships PDF notes..."))

        # ----------------------------------------------------
        # 1. PROBLEMS ON AGES - PDF MASTER NOTES
        # ----------------------------------------------------
        ages_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Problems on Ages

#### 1. Core Principles
- **Age Gap Invariance**: The age gap/difference between any two entities is **ALWAYS CONSTANT** throughout their lives.
- **Single Occurrence Rule**: Relations like double, triple, 4 times, etc. occur **ONLY ONCE** in a lifetime.

#### 2. Case 1: Age Gap & Multiple Given
- *Example 1*: Father's present age is 28 years more than son. Before 3y 5m, Father's age was double son's age.
  - Age Gap = 28. Before 3y 5m: Diff (2 - 1) = 1 part = 28.
  - Son before 3y 5m = 28y, Father = 56y.
  - Present Son = 28 + 3y 5m = **31y 5m**. Present Father = 56 + 3y 5m = **59y 5m**!
- *Example 2*: Father 27 years older than son. Before 2 years, Father was 5.5 times son's age.
  - Multiplicity 5.5 = 11/2 -> Diff = 5.5 - 1 = 4.5 parts = 27 -> 1 part = 6.
  - Son before 2y = 6y -> Present Son = **8 years**. Present Father = **35 years**!

#### 3. Case 2: Ratio Equating Method
- *Example*: Ratio of present ages of Man & Daughter is 3:1. After 12 years, ratio becomes 11:5.
  - Present 3:1 = 9:3 (multiplied by 3 to equate diff parts 11-5=6).
  - After 12 years = 11:5 -> Increase = 2 parts = 12 years -> 1 part = 6 years.
  - Present age of Man = 9 parts * 6 = **54 years**!

#### 4. Case 3: Family Average & Marriage Intervals
- Avg age of H & W 7 years ago was 25 years. Today family avg (including 1 child born during interval) is 22 years.
  - Present sum of H + W = (25 + 7) * 2 = 64.
  - Present sum of H + W + Child = 22 * 3 = 66.
  - Child Age = 66 - 64 = **2 years**!
"""

        ages_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="problems-on-ages",
            defaults={
                "order": 9,
                "name": "Problems on Ages (PDF Master Edition)",
                "description": "Master Age Gap Invariance, Multiplicity shortcuts, Ratio Equating method, & Family Marriage Interval rules.",
                "icon": "⏳",
                "formula_sheet": ages_formula_sheet
            }
        )

        # ----------------------------------------------------
        # 2. RATIOS & PROPORTIONS - PDF MASTER NOTES
        # ----------------------------------------------------
        ratios_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Ratios & Proportions

#### 1. Definitions & Formulas
- Proportion $a:b :: c:d \\implies \\frac{a}{b} = \\frac{c}{d}$
- **Product of Extremes = Product of Means**: $a \\times d = b \\times c$
- **Mean Proportional**: $b = \\sqrt{ac}$
- **Third Proportional**: $c = \\frac{b^2}{a}$ | **Fourth Proportional**: $d = \\frac{bc}{a}$
- **Compounded Ratio**: $(a:b)$ and $(c:d) \\implies (ac : bd)$
- **Duplicate Ratio**: $a^2 : b^2$ | **Sub-Duplicate**: $\\sqrt{a} : \\sqrt{b}$
- **Triplicate Ratio**: $a^3 : b^3$ | **Sub-Triplicate**: $\\sqrt[3]{a} : \\sqrt[3]{b}$

#### 2. Ratio Combining Shortcut
- If $A:B = 2:3$ and $B:C = 4:3 \\implies A:B:C = (2 \\times 4) : (3 \\times 4) : (3 \\times 3) = \\mathbf{8 : 12 : 9}$.
- If $A:B = 2:3, B:C = 4:3, C:D = 2:3 \\implies A:B:C:D = \\mathbf{16 : 24 : 18 : 27}$.

#### 3. Income, Expenditure & Savings ($I - E = S$)
- Incomes $A:B = 4:5$, Expenses $= 5:7$. Each saves Rs. 1500.
  - Multiply Income ratio by 2 $\\to 8:10$.
  - Savings $= 8 - 5 = 3 \\text{ parts} = \\text{Rs. } 1500 \\implies 1 \\text{ part} = 500$.
  - B's Income $= 10 \\times 500 = \\mathbf{\\text{Rs. } 5000}$!

#### 4. Bag Coins Value Calculation
- Bag has Rs. 1, 50p, 25p coins in ratio $5:6:7$. Total sum = Rs. 78.
  - Value Ratio $= (5 \\times 1) : (6 \\times 0.5) : (7 \\times 0.25) = 5 : 3 : 1.75 = 20 : 12 : 7$.
  - Total 39 parts $= 78 \\implies 1 \\text{ part} = 2$.
  - 50p Value $= 12 \\times 2 = \\text{Rs. } 24 \\implies \\text{No. of 50p coins} = 24 \\times 2 = \\mathbf{48 \\text{ coins}}$!
"""

        ratios_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="ratios-proportions",
            defaults={
                "order": 10,
                "name": "Ratios & Proportions (PDF Master Edition)",
                "description": "Master Proportion laws, Chain ratio merging, Income-Expenditure savings trick, & Coin bag calculations.",
                "icon": "📐",
                "formula_sheet": ratios_formula_sheet
            }
        )

        # ----------------------------------------------------
        # 3. PARTNERSHIPS - PDF MASTER NOTES
        # ----------------------------------------------------
        partnerships_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Partnerships

#### 1. Core Profit Sharing Law
$$\\text{Profit Sharing Ratio } (P_A : P_B) = (I_A \\times T_A) : (I_B \\times T_B)$$
- $\\text{Investment Ratio} = \\frac{\\text{Profit Ratio}}{\\text{Time Ratio}}$
- $\\text{Time Ratio} = \\frac{\\text{Profit Ratio}}{\\text{Investment Ratio}}$

#### 2. Managing / Working Partner vs Sleeping Partner
- Working partner gets management fee (% of total profit) first, remaining shared in investment ratio.
- *Example*: A (working) and B (sleeping) invest 5000 & 8000. A gets 22% of total profit for managing. Total profit if A's share is Rs. 2028?
  - Remaining profit = 78%. A's share from remaining = (5/13) * 78% = 30%.
  - A's total share = 22% + 30% = 52% = Rs. 2028.
  - Total Profit (100%) = (2028 / 52) * 100 = **Rs. 3900**!

#### 3. Capital Withdrawal & Re-investment Method
- *Example*: P & Q invest 150000 & 120000. After 8 months, Q withdraws 30000. Total profit if Q's share is Rs. 44000?
  - P = 150000 * 12 = 1800000.
  - Q = (120000 * 8) + (90000 * 4) = 960000 + 360000 = 1320000.
  - Ratio P:Q = 1800000 : 1320000 = 15 : 11.
  - Q's share (11 parts) = 44000 -> 1 part = 4000.
  - Total Profit (26 parts) = 26 * 4000 = **Rs. 1,04,000**!

#### 4. Charity % Deduction
- Surya & Chandu invest 85000 & 90000. After 4 months Chandu adds 56250. 20% of profit to charity. Total profit Rs. 98000. How much more does Chandu get than Surya?
  - Surya = 85000 * 12 = 1020000.
  - Chandu = (90000 * 4) + (146250 * 8) = 1530000.
  - Ratio S:C = 2 : 3.
  - After 20% charity (19600), remaining = 78400.
  - Chandu extra (1 part out of 5) = 78400 / 5 = **Rs. 15,680**!
"""

        partnerships_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="partnerships",
            defaults={
                "order": 11,
                "name": "Partnerships (PDF Master Edition)",
                "description": "Master Profit Sharing Ratio (Inv x Time), Working vs Sleeping Partner, Mid-term Withdrawals, & Charity deductions.",
                "icon": "🤝",
                "formula_sheet": partnerships_formula_sheet
            }
        )

        # Seed PDF Worked Questions
        AptitudeQuestion.objects.get_or_create(
            topic=ages_topic,
            text="The ratio of present ages of a man and his daughter is 3:1. After 12 years, the ratio of their ages would be 11:5. Find the present age of the man.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "48 years", "option_b": "54 years", "option_c": "60 years", "option_d": "45 years",
                "correct_option": "B",
                "explanation": "Ratio Equating Method: Present 3:1 = 9:3 (multiply by 3). After 12y = 11:5.\nIncrease = 2 parts = 12 years -> 1 part = 6 years.\nMan's Present Age = 9 * 6 = 54 years."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=ratios_topic,
            text="A bag contains 1 Rupee, 50 Paise, and 25 Paise coins in the ratio 5:6:7. If the total sum in the bag is Rs. 78, find the number of 50 Paise coins.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "36 coins", "option_b": "48 coins", "option_c": "60 coins", "option_d": "42 coins",
                "correct_option": "B",
                "explanation": "Value Ratio = (5*1) : (6*0.5) : (7*0.25) = 5 : 3 : 1.75 = 20 : 12 : 7.\nTotal 39 parts = 78 -> 1 part = Rs. 2.\n50p Value = 12 * 2 = Rs. 24 -> Number of 50p coins = 24 * 2 = 48 coins."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=partnerships_topic,
            text="A and B start a business with Rs. 5000 and Rs. 8000. A gets 22% of total profit for managing the business, and remaining profit is shared in capital ratio. If A's total share is Rs. 2028, find total profit.",
            defaults={
                "difficulty": "advanced",
                "option_a": "Rs. 3600", "option_b": "Rs. 3900", "option_c": "Rs. 4200", "option_d": "Rs. 4000",
                "correct_option": "B",
                "explanation": "Remaining profit = 78%. Capital ratio A:B = 5:8.\nA's share from remaining = (5/13) * 78% = 30%.\nA's total share = 22% + 30% = 52% = Rs. 2028.\nTotal Profit (100%) = (2028 / 52) * 100 = Rs. 3900."
            }
        )

        self.stdout.write(self.style.SUCCESS("Ages, Ratios, and Partnerships PDF notes & questions successfully seeded!"))
