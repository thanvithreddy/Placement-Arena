from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten Profit and Loss PDF shortcuts and 23 Java Quest topics'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with user's complete Profit & Loss PDF notes..."))

        # ----------------------------------------------------
        # PROFIT AND LOSS - COMPLETE HANDWRITTEN PDF NOTES
        # ----------------------------------------------------
        pnl_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Profit & Loss

#### 1. Fundamental Terminology & Rules
- **Cost Price (C.P)**: Base value, **ALWAYS considered as 100%**.
- **Selling Price (S.P)**: 
  - $S.P = C.P + P$ (if Profit)
  - $S.P = C.P - L$ (if Loss)
- **Profit (P)**: Difference between C.P and S.P ($S.P - C.P$) when $S.P > C.P$.
- **Loss (L)**: Difference between C.P and S.P ($C.P - S.P$) when $C.P > S.P$.
- **Profit %**: $P\\% = \\frac{P}{C.P} \\times 100$
- **Loss %**: $L\\% = \\frac{L}{C.P} \\times 100$
- **GOLDEN RULE**: Everything is calculated ONLY on **Cost Price**, NOT on Selling Price!

---

#### 2. Successive Discounts & Marked Price (M.P)
- **Discount is ALWAYS calculated on Marked Price (M.P)**: $S.P = M.P - \\text{Discount}$.
- **Successive Discounts Trick (e.g. 10%, 20%, 30%)**:
  - Start at $M.P = 100\\%$.
  - After 1st discount ($10\\%$) $\\to 90\\%$.
  - After 2nd discount ($20\\% \\text{ of } 90 = 18\\%$) $\\to 72\\%$.
  - After 3rd discount ($30\\% \\text{ of } 72 = 21.6\\%$) $\\to 50.4\\%$.
  - **Single Equivalent Discount** = $100\\% - 50.4\\% = \\mathbf{49.6\\%}$!

---

#### 3. Special Case 1: Equal Cost Price Rule ($CP_1 = CP_2$)
- If two items are bought at **EQUAL Cost Price**, and one is sold at $x\\%$ Profit and another at $x\\%$ Loss:
- **RESULT**: **NO PROFIT / NO LOSS** ($0\\%$ net change)!
- *Example*: Dravid bought 2 cars each for Rs. 4,59,000. Sold one at 13% Profit and another at 13% Loss $\\implies$ **No Profit / No Loss**!

---

#### 4. Special Case 2: Equal Selling Price Rule ($SP_1 = SP_2$)
- If two items are sold at **EQUAL Selling Price**, one at $x\\%$ Profit and another at $x\\%$ Loss:
- **RESULT**: ALWAYS a **LOSS** of $\\mathbf{\\left(\\frac{x}{10}\\right)^2\\%}$!
- *Example*: SP of two items is Rs. 5,43,400 each. One sold at 30% Profit, another at 30% Loss $\\implies \\left(\\frac{30}{10}\\right)^2 = 3^2 = \\mathbf{9\\% \\text{ Loss}}$!

---

#### 5. Special Case 3: $CP \\text{ of } x \\text{ items} = SP \\text{ of } y \\text{ items}$
- Reverse the terms to solve: Set $C.P = y$ and $S.P = x$.
- *Example*: CP of 80 articles = SP of 60 articles.
  - $C.P = 60, S.P = 80 \\implies Profit = 20$.
  - $Profit \\% = \\frac{20}{60} \\times 100 = \\mathbf{33.33\\% \\text{ Profit}}$!

---

#### 6. Special Case 4: Quantity Equating Trick (Buying at Rate A, Selling at Rate B)
- Equate the number of articles bought and sold!
- *Example*: A man buys 16 fruits for Rs. 24, and sells 8 fruits for Rs. 18.
  - $C.P \\text{ of } 16 = \\text{Rs. } 24$.
  - $S.P \\text{ of } 8 = \\text{Rs. } 18 \\implies S.P \\text{ of } 16 = \\mathbf{\\text{Rs. } 36}$.
  - $Profit = 36 - 24 = 12 \\implies Profit \\% = \\frac{12}{24} \\times 100 = \\mathbf{50\\%}$!

---

#### 7. Special Case 5: Dishonest Dealer & Cheating Weight Trick
- **Formula**: $Profit \\% = \\left(\\frac{\\text{Difference in Weight}}{\\text{False Weight Used}}\\right) \\times 100$
- *Example 1*: Uses $1100\\text{g}$ instead of $1.5\\text{kg} (1500\\text{g})$:
  - $Profit \\% = \\frac{1500 - 1100}{1100} \\times 100 = \\frac{400}{1100} \\times 100 = \\mathbf{36.36\\%}$.
- *Example 2*: Dealer cheats 10% while buying AND 10% while selling:
  - $Overall \\% = 10 + 10 + \\frac{10 \\times 10}{100} = \\mathbf{21\\% \\text{ Profit}}$!

---

#### 8. Special Case 6: Fraction Conversion Trick for CP & SP
- Convert % into simplified fractions ($P \\% = \\frac{\\text{Num}}{\\text{Denom}}$ where Denom = C.P):
  - $28.57\\% = \\frac{2}{7} \\implies C.P = 7, Profit = 2 \\implies S.P = 9$.
  - $27.27\\% = \\frac{3}{11} \\implies C.P = 11, Loss = 3 \\implies S.P = 8$.
  - $14.28\\% = \\frac{1}{7} \\implies C.P = 7, Loss = 1 \\implies S.P = 6$.

---

#### 9. Special Case 7: Double Assumption Method
- *Example*: Article sold at 20% profit. If bought for 10% less and sold for Rs. 63 less, profit is 30%. Find original CP.
  - Original: $C.P_1 = 100\\% \\implies S.P_1 = 120\\%$.
  - New: $C.P_2 = 90\\%$. New Profit $= 30\\% \\text{ of } 90 = 27\\% \\implies S.P_2 = 117\\%$.
  - Difference in $S.P = 120\\% - 117\\% = 3\\% = \\text{Rs. } 63$.
  - $100\\% \\text{ (Original CP)} = \\frac{63}{3} \\times 100 = \\mathbf{\\text{Rs. } 2100}$!

---

#### 10. Special Case 8: Price Reduction vs More Quantity Purchase Trick
- *Example*: 20% price reduction enables buying 4 more mangoes for Rs. 800.
  - Reduced Price $= \\frac{800 \\times 20\\%}{4} = \\frac{160}{4} = \\mathbf{\\text{Rs. } 40}$.
  - Original Price $= \\frac{800}{\\text{Original Qty}} = \\mathbf{\\text{Rs. } 50}$.

---

#### 11. Special Case 9: Lemons / Articles Rate Conversion
- *Example*: Selling 45 lemons for Rs. 40 loses 20%. How many to sell for Rs. 24 to gain 20%?
  - Loss 20% $\\to S.P_1 = 80\\% = \\text{Rs. } 40$.
  - Gain 20% $\\to S.P_2 = 120\\% = \\text{Rs. } 60$ for 45 lemons.
  - For Rs. 24, number of lemons $= \\frac{45}{60} \\times 24 = \\mathbf{18 \\text{ lemons}}$!
"""

        pnl_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="profit-and-loss",
            defaults={
                "order": 5,
                "name": "Profit and Loss (PDF Master Edition)",
                "description": "Complete master guide on CP, SP, MP, Successive Discounts, Equal CP/SP rules, Dishonest Dealer & Price Reduction tricks.",
                "icon": "📈",
                "formula_sheet": pnl_formula_sheet
            }
        )

        # Seed All PDF Worked Questions into Database
        questions_data = [
            {
                "text": "Rahul purchased an article for Rs. 1500 and sold it for Rs. 1950. Find his Profit %.",
                "a": "25%", "b": "30%", "c": "35%", "d": "20%", "ans": "B",
                "exp": "Profit = SP - CP = 1950 - 1500 = 450.\nProfit % = (450 / 1500) * 100 = 30%."
            },
            {
                "text": "Find the CP of a dining table if SP is Rs. 3600 and loss is 10%.",
                "a": "Rs. 4000", "b": "Rs. 3800", "c": "Rs. 4200", "d": "Rs. 3900", "ans": "A",
                "exp": "Let CP = 100%. Loss = 10% -> SP = 90% = 3600.\nCP (100%) = (3600 / 90) * 100 = Rs. 4000."
            },
            {
                "text": "Three successive discounts of 10%, 20% and 30% are equal to a single discount of what %?",
                "a": "60%", "b": "49.6%", "c": "50.4%", "d": "45%", "ans": "B",
                "exp": "MP = 100%. 1st disc (10%) -> 90%. 2nd disc (20% of 90 = 18%) -> 72%. 3rd disc (30% of 72 = 21.6%) -> 50.4%.\nSingle Equivalent Discount = 100 - 50.4 = 49.6%."
            },
            {
                "text": "Amrutesh marked an article for Rs. 400. He sold it after giving a discount of 10%. If CP is Rs. 300, find Profit %.",
                "a": "15%", "b": "20%", "c": "25%", "d": "30%", "ans": "B",
                "exp": "MP = 400. Discount = 10% of 400 = 40 -> SP = 360.\nCP = 300 -> Profit = 360 - 300 = 60.\nProfit % = (60 / 300) * 100 = 20%."
            },
            {
                "text": "Dravid purchased two cars each at Rs. 4,59,000. He sold one at 13% Profit and another at 13% Loss. Find his overall Profit or Loss %.",
                "a": "1.69% Loss", "b": "1.69% Profit", "c": "No Profit / No Loss", "d": "2.5% Loss", "ans": "C",
                "exp": "Equal Cost Price Rule: When two items are bought at equal CP and sold at same % profit and loss, net result is No Profit / No Loss (0%)."
            },
            {
                "text": "The Selling Price of two items is Rs. 5,43,400 each. One is sold at 30% Profit and another at 30% Loss. Find overall Profit/Loss %.",
                "a": "9% Loss", "b": "9% Profit", "c": "No Loss No Profit", "d": "6% Loss", "ans": "A",
                "exp": "Equal Selling Price Rule: Net result is ALWAYS a Loss of (x/10)^2% = (30/10)^2 = 3^2 = 9% Loss."
            },
            {
                "text": "If CP of 80 articles is equal to SP of 60 articles, find Profit or Loss %.",
                "a": "25% Profit", "b": "33.33% Profit", "c": "20% Loss", "d": "33.33% Loss", "ans": "B",
                "exp": "CP * 80 = SP * 60 -> CP = 60, SP = 80.\nProfit = 20 -> Profit % = (20 / 60) * 100 = 33.33% Profit."
            },
            {
                "text": "A man bought fruits at a rate of 16 for Rs. 24, and sold them at a rate of 8 for Rs. 18. What is his Profit %?",
                "a": "40%", "b": "50%", "c": "60%", "d": "45%", "ans": "B",
                "exp": "Equate quantities: CP of 16 = Rs. 24.\nSP of 8 = Rs. 18 -> SP of 16 = Rs. 36.\nProfit % = ((36 - 24) / 24) * 100 = (12 / 24) * 100 = 50%."
            },
            {
                "text": "If an article is sold for Rs. 306, a trader loses 30%. What should be the SP to gain 40%?",
                "a": "Rs. 510", "b": "Rs. 612", "c": "Rs. 600", "d": "Rs. 620", "ans": "B",
                "exp": "30% Loss -> SP1 = 70% = 306.\n40% Profit -> Target SP2 = 140%.\nSince 140% is double of 70%, SP2 = 306 * 2 = Rs. 612."
            },
            {
                "text": "A dishonest dealer professes to sell goods at CP, but uses 1100g instead of 1.5kg (1500g). Find his Profit %.",
                "a": "30%", "b": "36.36%", "c": "40%", "d": "25%", "ans": "B",
                "exp": "Diff in weight = 1500 - 1100 = 400g.\nProfit % = (400 / 1100) * 100 = 36.36%."
            },
            {
                "text": "A TV set was sold for Rs. 1800 at a loss of 14.28%. Find its CP.",
                "a": "Rs. 2000", "b": "Rs. 2100", "c": "Rs. 2200", "d": "Rs. 2400", "ans": "B",
                "exp": "14.28% = 1/7 -> CP = 7, Loss = 1 -> SP = 6.\n6 units = 1800 -> 1 unit = 300.\nCP = 7 * 300 = Rs. 2100."
            },
            {
                "text": "By selling 45 lemons for Rs. 40, a man loses 20%. How many should he sell for Rs. 24 to gain 20%?",
                "a": "15 lemons", "b": "18 lemons", "c": "20 lemons", "d": "16 lemons", "ans": "B",
                "exp": "Loss 20% -> SP1 = 80% = Rs. 40.\nGain 20% -> SP2 = 120% = Rs. 60 for 45 lemons.\nFor Rs. 24: (45 / 60) * 24 = 18 lemons!"
            }
        ]

        for q_data in questions_data:
            AptitudeQuestion.objects.get_or_create(
                topic=pnl_topic,
                text=q_data["text"],
                defaults={
                    "difficulty": "intermediate",
                    "option_a": q_data["a"],
                    "option_b": q_data["b"],
                    "option_c": q_data["c"],
                    "option_d": q_data["d"],
                    "correct_option": q_data["ans"],
                    "explanation": q_data["exp"]
                }
            )

        self.stdout.write(self.style.SUCCESS("All handwritten Profit and Loss PDF notes & questions successfully embedded!"))
