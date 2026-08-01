from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten Averages & Alligations PDF notes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with Averages and Alligations PDF notes..."))

        # ----------------------------------------------------
        # 1. AVERAGES - COMPLETE HANDWRITTEN PDF NOTES
        # ----------------------------------------------------
        avg_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Averages

#### 1. Core Formulas & Equal Distribution Concept
- $\\text{Average} = \\frac{\\text{Sum of Observations}}{\\text{No. of Observations}}$
- $\\text{Sum} = \\text{No. of Observations} \\times \\text{Average}$
- **Core Concept**: Average is an **Assumption of Equality**, NOT reality! Every value is assumed equal to the Average.

#### 2. Joiner / Inclusion Shortcut
- **1 New Joiner**: $\\text{New Value} = \\text{New Avg} + (\\text{Old Count} \\times \\Delta \\text{Avg})$
  - *PDF Example*: 28 students avg = 33kg. 1 new student joins $\\implies$ avg increases by 2kg.
  - Weight $= 35 + (28 \\times 2) = \\mathbf{91\\text{kg}}$!
- **Manager / Extra Joiner**:
  - 35 workers avg = Rs. 1800. Manager included $\\implies$ avg increases by Rs. 125.
  - Manager Salary $= 1925 + (35 \\times 125) = \\mathbf{\\text{Rs. } 6300}$!

#### 3. Cricket Innings Highest & Lowest Score Shortcut
- Batting average of 40 innings = 50. Highest score exceeds lowest by 172. Excluding these 2, avg of 38 innings = 48.
  - $H + L = (40 \\times 50) - (38 \\times 48) = 176$.
  - $H - L = 172 \\implies H = \\frac{176 + 172}{2} = \\mathbf{174 \\text{ runs}}$, $L = \\mathbf{2 \\text{ runs}}$.

#### 4. Batsman Inning Increment Shortcut
- Batsman in 17th inning scores 85, increasing avg by 3 runs.
  - Avg Before 17th inning $= 85 - (3 \\times 17) = \\mathbf{34 \\text{ runs}}$.
  - Avg After 17th inning $= 34 + 3 = \\mathbf{37 \\text{ runs}}$.

#### 5. Replacement & Mistaken Value Tricks
- **Replacement**: $\\text{New Weight} = \\text{Replaced Weight} + (\\text{Total Members} \\times \\Delta \\text{Avg})$.
  - *Example*: 15 men, 1 weighing 60kg replaced $\\implies$ avg increases by 1kg. New man $= 60 + 15 = \\mathbf{75\\text{kg}}$.
- **Mistaken Value**: $\\text{Correct Avg} = \\text{Mistaken Avg} + \\frac{\\text{Correct Value} - \\text{Mistaken Value}}{\\text{Total Count}}$.
  - *Example*: 15 students avg = 159cm. 147cm read as 177cm $\\implies$ Correct Avg $= 159 - \\frac{30}{15} = \\mathbf{157\\text{cm}}$.

#### 6. Overlapping & Missing Middle Number Rules
- **Missing Number**: $\\text{Total Sum} - (\\text{Sum of 1st set} + \\text{Sum of last set})$.
- **Overlapping Number**: $(\\text{Sum of 1st set} + \\text{Sum of last set}) - \\text{Total Sum}$.

#### 7. Consecutive Numbers & Uniform Operations
- If common difference is constant $\\implies \\text{Average} = \\frac{\\text{First} + \\text{Last}}{2} = \\text{Middle Number}$.
- Avg of first $n$ even numbers $= n + 1$ | Avg of first $n$ odd numbers $= n$.
- **Uniform Change Rule**: If every element is changed by $K$, new average becomes $\\text{Old Avg} \\pm / \\times / \\div K$.
"""

        avg_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="averages",
            defaults={
                "order": 7,
                "name": "Averages (PDF Master Edition)",
                "description": "Complete master guide on Equal Distribution, Joiners, Cricket Innings, Replacements, Mistaken Values & Consecutive numbers.",
                "icon": "⚖️",
                "formula_sheet": avg_formula_sheet
            }
        )

        # ----------------------------------------------------
        # 2. ALLIGATIONS & MIXTURES - COMPLETE HANDWRITTEN PDF NOTES
        # ----------------------------------------------------
        alligation_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Alligations & Mixtures

#### 1. The Rule of Alligation Cross Method
$$\\frac{\\text{Quantity A}}{\\text{Quantity B}} = \\frac{|\\text{Mean} - \\text{Price B}|}{|\\text{Mean} - \\text{Price A}|}$$
- Applied when **Two Categories** and **Mean Result** are given in Percentages, Profit/Loss, Averages, or Simple Interest.

#### 2. Simple & Compound Interest Split
- *Example*: Rs. 3000 invested at 5% and 6% SI. Total annual interest = Rs. 162.
  - Overall $\% = \\frac{162}{3000} \\times 100 = 5.4\\%$.
  - Ratio $(5\\% \\text{ vs } 6\\% \\text{ around } 5.4\\%) = |5.4 - 6| : |5.4 - 5| = 0.6 : 0.4 = 3 : 2$.
  - Amount at $6\\% = \\frac{2}{5} \\times 3000 = \\mathbf{\\text{Rs. } 1200}$.

#### 3. Free Water Milk Shortcut
- Ratio of Water to Milk to gain $X\\%$ profit by selling mixture at Cost Price:
  $$\\text{Water} : \\text{Milk} = X : 100$$
  - *Example*: To gain 20% profit $\\implies \\text{Water} : \\text{Milk} = 20 : 100 = \\mathbf{1 : 5}$!

#### 4. Two Vessels Mixing Rule (LCM Equating Method)
- Vessel A milk:water $= 4:3$ (Total 7). Vessel B milk:water $= 2:3$ (Total 5). Mixed to get 1:1 (Total 2).
  - LCM of $7, 5, 2 = 70$.
  - Milk in A $= 40$, B $= 28$, Target $= 35$.
  - Ratio $= |35 - 28| : |35 - 40| = \\mathbf{7 : 5}$!

#### 5. Repeated Removal Formula
$$\\text{Remaining Liquid} = X \\left(1 - \\frac{Y}{X}\\right)^n$$
- *Example*: 300L milk, 30L removed and replaced with water, repeated 3 times total:
  - $10\\%$ removal each step $\\implies 300 \\to 270 \\to 243 \\to \\mathbf{218.7 \\text{ litres}}$!

#### 6. Cask of Wine Formula (Finding Capacity)
- 8L drawn from cask, filled with water, repeated 3 more times (4 times total). Ratio of wine left to water is $16:65$.
  - Fraction of wine remaining $= \\frac{16}{16 + 65} = \\frac{16}{81} = \\left(\\frac{2}{3}\\right)^4$.
  - $1 - \\frac{8}{X} = \\frac{2}{3} \\implies \\frac{8}{X} = \\frac{1}{3} \\implies X = \\mathbf{24 \\text{ litres}}$!
"""

        alligation_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="alligations-mixtures",
            defaults={
                "order": 8,
                "name": "Alligations & Mixtures (PDF Master Edition)",
                "description": "Complete master guide on Cross Rule, SI/CI Split, Free Water Trick, Two Vessel LCM Equating, & Repeated Removal Cask formula.",
                "icon": "🧪",
                "formula_sheet": alligation_formula_sheet
            }
        )

        # Seed PDF Worked Questions for Averages & Alligations
        AptitudeQuestion.objects.get_or_create(
            topic=avg_topic,
            text="There are 28 students in a class with average weight 33kg. If one new student joins, the average weight increases by 2kg. Find the weight of the new student.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "88kg", "option_b": "91kg", "option_c": "85kg", "option_d": "93kg",
                "correct_option": "B",
                "explanation": "Shortcut Method: New Student Weight = New Avg (35) + (Old Count 28 * 2) = 35 + 56 = 91kg."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=avg_topic,
            text="A batsman in his 17th innings makes a score of 85, thereby increasing his average by 3 runs. What is his average after the 17th innings?",
            defaults={
                "difficulty": "intermediate",
                "option_a": "34 runs", "option_b": "37 runs", "option_c": "40 runs", "option_d": "35 runs",
                "correct_option": "B",
                "explanation": "Shortcut Method: Avg Before 17th = 85 - (3 * 17) = 85 - 51 = 34 runs.\nAvg After 17th = 34 + 3 = 37 runs."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=alligation_topic,
            text="In what ratio must water be mixed with milk to gain 20% by selling the mixture at Cost Price?",
            defaults={
                "difficulty": "intermediate",
                "option_a": "1 : 4", "option_b": "1 : 5", "option_c": "1 : 6", "option_d": "2 : 5",
                "correct_option": "B",
                "explanation": "Free Water Shortcut: Ratio of Water to Milk = Profit % : 100 = 20 : 100 = 1 : 5."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=alligation_topic,
            text="8 litres are drawn from a cask full of wine and then filled with water. This operation is performed three more times. The ratio of quantity of wine left to water is 16:65. How much wine did the cask hold originally?",
            defaults={
                "difficulty": "advanced",
                "option_a": "18 litres", "option_b": "24 litres", "option_c": "32 litres", "option_d": "42 litres",
                "correct_option": "B",
                "explanation": "Remaining Wine Fraction = 16 / (16 + 65) = 16 / 81 = (2/3)^4.\nSince operation performed 4 times: (1 - 8/X)^4 = (2/3)^4 -> 1 - 8/X = 2/3 -> 8/X = 1/3 -> X = 24 litres."
            }
        )

        self.stdout.write(self.style.SUCCESS("Averages and Alligations PDF notes & worked problems successfully seeded!"))
