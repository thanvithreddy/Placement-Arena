const aptitudeTopics = [
    {
        "id": 1,
        "slug": "speed-math",
        "name": "Speed Math & Shortcuts",
        "description": "Master squares, cubes, cube roots, and fraction conversions instantly.",
        "icon": "\u26a1",
        "xp_reward": 150,
        "formula_sheet": "### \u26a1 Master Cheat Sheet: Speed Math & Shortcuts\n\n#### 1. Squares Ending with Digit 5\n> **Formula**: $(10n + 5)^2 = 100n(n+1) + 25$\n- **Method**: Multiply the tens digit $n$ with its successor $(n+1)$, then append `25` at the end.\n- $15^2 = (1 \\times 2) \\text{ append } 25 = 225$\n- $25^2 = (2 \\times 3) \\text{ append } 25 = 625$\n- $35^2 = (3 \\times 4) \\text{ append } 25 = 1225$\n- $45^2 = (4 \\times 5) \\text{ append } 25 = 2025$\n- $95^2 = (9 \\times 10) \\text{ append } 25 = 9025$\n\n#### 2. Squares Near Base 50\n- **Numbers Below 50 ($50 - d$)**: Answer = $(25 - d) \\text{ and } d^2$\n  - Example $47^2$ ($d = 3$): $25 - 3 = 22$, $3^2 = 09 \\implies 2209$\n- **Numbers Above 50 ($50 + d$)**: Answer = $(25 + d) \\text{ and } d^2$\n  - Example $53^2$ ($d = 3$): $25 + 3 = 28$, $3^2 = 09 \\implies 2809$\n\n#### 3. Squares Near Base 100\n- **Numbers Below 100 ($100 - d$)**: Answer = $(N - d) \\text{ and } d^2$\n  - Example $94^2$ ($d = 6$): $94 - 6 = 88$, $6^2 = 36 \\implies 8836$\n- **Numbers Above 100 ($100 + d$)**: Answer = $(N + d) \\text{ and } d^2$\n  - Example $107^2$ ($d = 7$): $107 + 7 = 114$, $7^2 = 49 \\implies 11449$\n\n#### 4. Important Cube Roots Shortcut\n| Last Digit of Number | Last Digit of Cube Root |\n| :---: | :---: |\n| 1, 4, 5, 6, 9, 0 | Same (1, 4, 5, 6, 9, 0) |\n| 2 $\\leftrightarrow$ 8 | Swap (2 ends in 8, 8 ends in 2) |\n| 3 $\\leftrightarrow$ 7 | Swap (3 ends in 7, 7 ends in 3) |\n\n- **Example $\\sqrt[3]{97336}$**:\n  1. Last digit is 6 $\\implies$ Root ends in **6**.\n  2. Ignore last 3 digits ($336$), remaining is $97$.\n  3. $4^3 = 64 < 97 < 125 = 5^3$. Preceding cube is $4$.\n  4. Answer = **46**.\n",
        "questions": [],
        "flashcards": [
            {
                "title": "1. Squares Ending in 5",
                "front": "How do you calculate $(10n + 5)^2$ mentally?",
                "evolution_origin": "Formula Origin: $(10n + 5)^2 = 100n(n+1) + 25$",
                "back": "Shortcut Trick: Multiply $n \\times (n+1)$, then append 25 at the end!\nExample: $45^2 \\implies 4 \\times 5 = 20$, append $25 \\implies 2025$!",
                "badge": "\u26a1 Mental Trick"
            },
            {
                "title": "2. Squares Near Base 50 (Below 50)",
                "front": "How do you calculate $(50 - d)^2$ using base 25?",
                "back": "Shortcut Trick: Subtract $d$ from 25, followed by $d^2$.\nExample $47^2$ ($d = 3$): $25 - 3 = 22$, $3^2 = 09 \\implies 2209$!",
                "badge": "\ud83c\udfaf Base 50 Trick"
            },
            {
                "title": "3. Squares Near Base 50 (Above 50)",
                "front": "How do you calculate $(50 + d)^2$ using base 25?",
                "back": "Shortcut Trick: Add $d$ to 25, followed by $d^2$.\nExample $53^2$ ($d = 3$): $25 + 3 = 28$, $3^2 = 09 \\implies 2809$!",
                "badge": "\ud83c\udfaf Base 50 Trick"
            },
            {
                "title": "4. Squares Near Base 100 (Below 100)",
                "front": "How do you calculate $(100 - d)^2$?",
                "back": "Shortcut Trick: Subtract $d$ from the number $N$, followed by $d^2$.\nExample $94^2$ ($d = 6$): $94 - 6 = 88$, $6^2 = 36 \\implies 8836$!",
                "badge": "\ud83d\udcaf Base 100 Trick"
            },
            {
                "title": "5. Squares Near Base 100 (Above 100)",
                "front": "How do you calculate $(100 + d)^2$?",
                "back": "Shortcut Trick: Add $d$ to the number $N$, followed by $d^2$.\nExample $107^2$ ($d = 7$): $107 + 7 = 114$, $7^2 = 49 \\implies 11449$!",
                "badge": "\ud83d\udcaf Base 100 Trick"
            },
            {
                "title": "6. Cube Root Mapping Rules",
                "front": "Which unit digits remain the same vs which digits swap for Cube Roots?",
                "back": "1, 4, 5, 6, 9, 0 STAY SAME.\nSwaps: 2 \u2194 8 and 3 \u2194 7!\nExample: $\\sqrt[3]{97336}$ ends in 6, remaining 97 is between $4^3=64$ and $5^3=125 \\implies 46$!",
                "badge": "\ud83d\udce6 Cube Root Rule"
            }
        ]
    },
    {
        "id": 2,
        "slug": "percentages",
        "name": "Percentages",
        "description": "Master fraction reductions, symmetry rules, percentage shifts, and percentage shortcuts.",
        "icon": "\ud83d\udcaf",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1: Base Fractions & Symmetry Rule\n- **Fraction Reduction Trick**: Knowing some fractions makes calculating percentages easier!\n  - Example: $28.5\\% \\text{ of } 1400 = 400 \\implies \\frac{2}{7} \\text{ of } 1400 = \\frac{2}{7} \\times 1400 = 400$.\n- **Rule of Symmetry**: $a\\% \\text{ of } b = b\\% \\text{ of } a$\n  - Example: $13\\% \\text{ of } 200 = 200\\% \\text{ of } 13 = 26$.\n- **10% & 1% Decimal Shift**:\n  - $10\\%$ of any number: Place decimal point before the unit digit ($10\\% \\text{ of } 7432 = 743.2$).\n  - $1\\%$ of any number: Place decimal point before the one's digit ($1\\% \\text{ of } 7432 = 74.32$).\n\n#### Page 2: Combination Techniques & Practiced Examples\n- **Combination Method**:\n  - $21\\% \\text{ of } 6400$: $10\\% \\to 640.0 \\implies 20\\% \\to 1280$. Add $1\\% (64) \\implies 1280 + 64 = 1344$.\n  - $19\\% \\text{ of } 7200$: $20\\% - 1\\% = 1440 - 72 = 1368$.\n- **Practiced Examples from Notes**:\n  1. $24\\% \\text{ of } 8800 = 20\\% + 4\\% = 2112$ (or $25\\% - 1\\%$).\n  2. $91\\% \\text{ of } 3500 = 90\\% + 1\\% = 3150 + 35 = 3185$.\n  3. $28.2\\% \\text{ of } 1100 = 27.2\\% + 1\\% = 310.2$.\n  4. $61\\% \\text{ of } 12400 = 50\\% + 10\\% + 1\\% = 7564$.\n  5. $18\\% \\text{ of } 77.77 = 20\\% - 2\\% = 15.554 - 1.5554 = 13.9986$.\n\n#### Page 3: Problematic Understanding of Percentages\n- **Problem 1**: When a number is increased by $20\\%$ by itself, the result is 480. Find the number.\n  - Let number be $x\\% = 100\\%$.\n  - $x\\% + 20\\% = 120\\% \\to 480$ (Common multiplier: $120 \\times 4 = 480$).\n  - $100\\% \\to 100 \\times 4 = 400$. **Number = 400**.\n- **Problem 2**: If $40\\%$ of a number is 20 more than $30\\%$ of a number, find the number.\n  - Diff: $40\\% - 30\\% = 10\\% \\to 20$.\n  - Number $= 100\\% \\to 100 \\times 2 = 200$. **Number = 200**.\n- **Problem 3**: Candidate A won election by majority of 150 votes. Candidate A secured $60\\%$ of total votes.\n  - $A \\to 60\\%$, $B \\to 40\\%$. Majority $= 20\\% \\to 150$ votes.\n  - Total $= 100\\% \\to 750$ votes.\n\n#### Page 4 & 5: Equal Increase & Decrease Square Loss Rule\n- **Highly Important Concept**: If an entity is increased by $x\\%$ and then decreased by the same $x\\%$, we FINALLY end up with a **LOSS**.\n  - $(\\uparrow \\downarrow \\text{ or } \\downarrow \\uparrow \\implies \\text{Finally Loss})$\n  - $\\text{Loss} = \\text{Square of } 10^{\\text{th}} \\text{ multiple}$.\n  - $10\\% \\implies (1.0)^2 = 1\\%$ Loss.\n  - $20\\% \\implies (2.0)^2 = 4\\%$ Loss.\n  - $30\\% \\implies (3.0)^2 = 9\\%$ Loss.\n  - $5\\% \\implies (0.5)^2 = 0.25\\%$ Loss.\n  - $12\\% \\implies (1.2)^2 = 1.44\\%$ Loss.\n- **Sugar Price Worked Example**: Price of sugar increased by $30\\%$ then decreased by $30\\%$. Present price is Rs. 273.\n  - Original $= 100\\% \\implies +30\\% \\to 130\\%$.\n  - $-30\\% \\text{ of } 130 = 39 \\implies 130 - 39 = 91\\%$.\n  - $91\\% \\to 273$ ($91 \\times 3 = 273$).\n  - $100\\% (\\text{Original Price}) \\to 100 \\times 3 = \\text{Rs. } 300$.\n\n#### Page 6 & 7: Questioning Pattern Types & Area Expansion Rules\n- **3 Question Patterns**:\n  1. Initial Value + $\\%$ Given $\\implies$ Find Final Value (Calculation).\n  2. Initial Value + Final Value Given $\\implies$ Find $\\%$ (Fraction).\n  3. $\\%$ + Final Value Given $\\implies$ Find Initial Value (Equation).\n- **Square Area Increase Example**: Side of square increased by $20\\%$. Area increases by what $\\%$?\n  - Pattern $\\uparrow \\uparrow \\implies 20 + 20 + (2.0)^2 = 44\\%$ Increase!\n- **Square Area Reversal**: Area becomes 3380 sq. units after side increases by $30\\%$.\n  - Side $30\\% \\uparrow \\implies$ Area $30 + 30 + 3^2 = 69\\% \\uparrow \\implies 169\\% \\to 3380$.\n  - Original Area ($100\\%$) $= 2000$ sq. units.\n\n#### Page 8, 9 & 10: Salary, Election, & Comparison Formulas\n- **Remaining Expenditure Rule**: Expenditure can be from OVERALL salary OR REMAINING salary.\n  - Surya Salary Problem: Spends $60\\%$ on food (Rem $40\\%$). Spends $20\\%$ of remaining on petrol ($8\\%$, Rem $32\\%$). Spends $10\\%$ of remaining on entertainment ($3.2\\%$).\n  - Total Savings $= 100\\% - 60\\% - 8\\% - 3.2\\% = 28.8\\%$.\n  - $28.8\\% \\to \\text{Rs. } 288 \\implies 100\\% \\to \\text{Rs. } 1000$ Total Salary!\n- **Two Numbers Comparison Rules**:\n  - $A$ is what $\\%$ of $B \\implies \\left(\\frac{A}{B}\\right) \\times 100$.\n  - $A$ is how much $\\%$ MORE than $B \\implies \\frac{\\text{diff}}{\\text{diff} + B} \\times 100$.\n  - $A$ is how much $\\%$ LESS than $B \\implies \\frac{\\text{diff}}{\\text{diff} - A} \\times 100$.\n\n#### Page 11, 12 & 13: Expenditure Consumption & Venn Diagrams\n- **Consumption Reduction Formula**: Price of sugar increased by $40\\%$. To keep expenditure same:\n  - $\\text{Reduction}\\% = \\frac{40}{100 + 40} \\times 100 = \\frac{40}{140} \\times 100 = 28.57\\%$.\n- **Venn Diagram Problem**: In a town, $70\\%$ read Hindu, $40\\%$ read TOI, $30\\%$ read both.\n  - Hindu only $= 40\\%$, TOI only $= 10\\%$, Both $= 30\\%$.\n  - Total reading at least one $= 40 + 30 + 10 = 80\\%$.\n  - Neither $= 100\\% - 80\\% = 20\\%$.\n\n#### Page 14 & 15: Sugar Solution, Fuel Tank & Apple Price Reduction\n- **Sugar Solution**: 3 litres of $40\\%$ sugar solution ($1.2$L sugar). Add 1L pure water $\\implies 4$L total.\n  - New $\\%$ of sugar $= \\frac{1.2}{4} \\times 100 = 30\\%$.\n- **Fuel Tank Replacement Table**:\n  - Tank filled with Type A (100A, 0B). Half empty (50A). Fill B (50A, 50B). Half empty (25A, 25B). Fill B (25A, 75B). Half empty (12.5A, 37.5B). Fill B (37.5A, 62.5B).\n  - Present petrol state: Type A $= 37.5\\%$, Type B $= 62.5\\%$.\n- **Apple Price Reduction**: $20\\%$ price reduction enables buying 2 more apples for Rs. 100.\n  - $20\\% \\to 2 \\text{ apples} \\implies 100\\% \\to 10 \\text{ apples (Present)}, 80\\% \\to 8 \\text{ apples (Original)}$.\n  - Reduced Price $= \\frac{\\text{Rs. } 100}{10} = \\text{Rs. } 10 / \\text{apple}$.\n  - Original Price $= \\frac{\\text{Rs. } 100}{8} = \\text{Rs. } 12.5 / \\text{apple}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Symmetry Rule",
                "front": "What is the handwritten shortcut rule for $a\\% \\text{ of } b$?",
                "back": "$a\\% \\text{ of } b = b\\% \\text{ of } a$\nHandwritten Example: $13\\% \\text{ of } 200 = 200\\% \\text{ of } 13 = 26$!",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 1: 10% & 1% Shift",
                "front": "How do you find 10% and 1% of 7432 using the handwritten decimal shift rule?",
                "back": "\u2022 10%: Place decimal point before unit digit $\\implies 743.2$\n\u2022 1%: Place decimal point before one's digit $\\implies 74.32$",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 4: Square Loss Rule",
                "front": "If an entity is increased by $x\\%$ and then decreased by $x\\%$, what is the final result?",
                "back": "It ALWAYS ends in a LOSS equal to the square of the $10^{\\text{th}}$ multiple!\nExample: $30\\% \\uparrow 30\\% \\downarrow \\implies (3.0)^2 = 9\\%$ Net Loss!",
                "badge": "\ud83d\udcc4 Page 4"
            },
            {
                "title": "Page 6: Pattern Matrix",
                "front": "What is the handwritten solving methodology when Initial Value & Final Value are given?",
                "back": "Use the **Fraction** methodology!\nFormula: $\\text{Percentage} = \\frac{\\text{Diff}}{\\text{Initial Value}} \\times 100$",
                "badge": "\ud83d\udcc4 Page 6"
            },
            {
                "title": "Page 10: Salary Comparison Formula",
                "front": "If A's salary is $80\\%$ MORE than B, by what $\\%$ is B's salary less than A?",
                "back": "$\\text{Formula} = \\frac{\\text{diff}}{\\text{diff} + B} \\times 100 = \\frac{80}{180} \\times 100 = 44.44\\% = 44\\frac{4}{9}\\%$!",
                "badge": "\ud83d\udcc4 Page 10"
            },
            {
                "title": "Page 15: Apple Price Reduction Trick",
                "front": "A $20\\%$ reduction enables buying 2 more apples for Rs. 100. What are Reduced and Original prices?",
                "back": "\u2022 $20\\% \\to 2 \\text{ apples} \\implies 100\\% \\to 10 \\text{ apples (New)}, 80\\% \\to 8 \\text{ apples (Old)}$\n\u2022 Reduced Price $= 100 / 10 = \\text{Rs. } 10$\n\u2022 Original Price $= 100 / 8 = \\text{Rs. } 12.50$",
                "badge": "\ud83d\udcc4 Page 15"
            }
        ],
        "questions": [
            {
                "text": "From Page 4 Notes: If the price of sugar increases by 30% and then decreases by 30%, what is the net percentage loss?",
                "options": [
                    "0%",
                    "6%",
                    "9%",
                    "12%"
                ],
                "correct_option_index": 2,
                "explanation": "Page 4 Rule: Equal increase and decrease always yields a net loss equal to (3.0)^2 = 9%!"
            },
            {
                "text": "From Page 1 Handwritten Notes: What is 28.5% of 1400 using the fraction trick?",
                "options": [
                    "300",
                    "400",
                    "500",
                    "350"
                ],
                "correct_option_index": 1,
                "explanation": "Page 1 Handwritten Note: 28.5% = 2/7. So (2/7) * 1400 = 400!"
            },
            {
                "text": "From Page 11 Notes: Sugar price increased by 40%. By what % should consumption be reduced so expenditure remains same?",
                "options": [
                    "25%",
                    "28.57%",
                    "33.33%",
                    "40%"
                ],
                "correct_option_index": 1,
                "explanation": "Page 11 Formula: Reduction % = (40 / (100 + 40)) * 100 = (40 / 140) * 100 = 28.57%!"
            },
            {
                "text": "From Page 15 Notes: A 20% reduction enables buying 2 more apples for Rs. 100. What is the original price per apple?",
                "options": [
                    "Rs. 10",
                    "Rs. 12.50",
                    "Rs. 15",
                    "Rs. 8"
                ],
                "correct_option_index": 1,
                "explanation": "Page 15 Solution: 20% -> 2 apples => 80% (Original) -> 8 apples. Original Price = Rs. 100 / 8 = Rs. 12.50!"
            }
        ]
    },
    {
        "id": 3,
        "slug": "profit-loss",
        "name": "Profit and Loss",
        "description": "Master CP/SP calculations, equal SP loss rules, dishonest dealer tricks, and discount scaling.",
        "icon": "\ud83d\udcc8",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1: Terminology & Core Principles\n- **Cost Price ($CP$)**: Always considered as $100\\%$ base!\n- **Selling Price ($SP$)**: $CP + P$ (if $SP > CP$, Profit) or $CP - L$ (if $CP > SP$, Loss).\n- **Profit ($P$)**: Difference between $CP$ and $SP$.\n- **Loss ($L$)**: Difference between $CP$ and $SP$.\n- **Profit $\\%$**: $P\\% = \\left(\\frac{P}{CP}\\right) \\times 100$.\n- **Loss $\\%$**: $L\\% = \\left(\\frac{L}{CP}\\right) \\times 100$.\n- **Key Note**: Everything is calculated ONLY on Cost Price, NOT on Selling Price!\n- **3 Question Types**: (1) Initial Value ($CP$), (2) Percentage Profit/Loss, (3) Final Value ($SP$).\n\n#### Page 2: Successive Discounts & Basic Worked Examples\n- **Example 1**: Purchased for Rs. 1500, sold for Rs. 1950.\n  - $\\text{Profit} = 1950 - 1500 = 450 \\implies P\\% = \\frac{450}{1500} \\times 100 = 30\\%$ Profit.\n- **Example 2**: $SP = \\text{Rs. } 3600$, Loss $= 10\\%$. Find $CP$.\n  - $CP = 100\\% \\implies SP = 90\\% \\to 3600 \\implies CP = 100\\% \\to \\mathbf{4000}$.\n- **Successive Discounts**: 3 successive discounts of $10\\%, 20\\%, 30\\%$ on Marked Price ($100\\%$):\n  - $1^{\\text{st}} \\to 10\\% \\implies 90\\%$.\n  - $2^{\\text{nd}} \\to 20\\% \\text{ of } 90 = 18\\% \\implies 72\\%$.\n  - $3^{\\text{rd}} \\to 30\\% \\text{ of } 72 = 21.6\\% \\implies 50.4\\%$.\n  - Total Discount $= 10\\% + 18\\% + 21.6\\% = \\mathbf{49.6\\%}$.\n\n#### Page 3: Equal Cost Price Rule (No Profit / No Loss)\n- **Important Note 1**: If a person purchases two items with **EQUAL COST PRICE** and sells one with $x\\%$ Profit and another with same $x\\%$ Loss:\n  - Result is ALWAYS **NO PROFIT / NO LOSS**!\n  - Example: Dravid bought 2 cars each at Rs. 4,59,000. Sold one at $13\\%$ profit & another at $13\\%$ loss $\\implies \\mathbf{\\text{No Profit / No Loss}}$.\n\n#### Page 4 & 5: Equal SP Square Loss Rule & Equating Terms\n- **Important Note 2**: If **SELLING PRICES of two items are equal** and one is sold at $x\\%$ profit and another at $x\\%$ loss:\n  - Result is ALWAYS a **LOSS** of $\\left(\\frac{x}{10}\\right)^2\\%$ or $(x.0)^2\\%$.\n  - Example: SP Rs. 5,43,400 each, $30\\%$ profit & $30\\%$ loss $\\implies (3.0)^2 = \\mathbf{9\\% \\text{ Loss}}$.\n- **Rule 3 (Equating CP of $x$ items = SP of $y$ items)**:\n  - Reverse the terms and equate $CP \\leftrightarrow SP$.\n  - Example: $CP$ of 80 articles $= SP$ of 60 articles $\\implies SP$ of $80 = CP$ of 60.\n  - $CP = 60, SP = 80 \\implies P\\% = \\frac{20}{60} \\times 100 = \\mathbf{33.33\\% \\text{ Profit}}$.\n- **Rule 4 (Quantity Rates)**:\n  - Example: Bought 16 for 24, sold 8 for 18.\n  - $CP \\text{ of } 16 = 24 \\implies SP \\text{ of } 16 = 36 \\implies P\\% = \\frac{12}{24} \\times 100 = \\mathbf{50\\%}$.\n\n#### Page 6 & 7: SP Target Scaling & Discount without Discount\n- **Question 1**: Sold for Rs. 306 with $30\\%$ loss. Find $SP$ to gain $40\\%$.\n  - $70\\% \\to 306 \\implies 140\\% (100+40) \\to 306 \\times 2 = \\mathbf{\\text{Rs. } 612}$.\n- **CP Average Note**: When SP is given for equal profit & loss: $CP = \\frac{SP_1 + SP_2}{2}$.\n- **Discount & Marked Price Rules**:\n  - Example 1: After $20\\%$ discount, profit is $12\\%$. If no discount is given, find $P\\%$.\n    - Discounted $SP = 80\\% \\to 112\\% \\implies 100\\% (\\text{Marked Price}) \\to 140\\% \\implies \\mathbf{P\\% = 40\\%}$.\n  - Example 2: After $20\\%$ discount, loss is $28\\%$. If $10\\%$ discount is given:\n    - $80\\% \\to 72\\% \\implies 90\\% \\to \\frac{72 \\times 90}{80} = 81\\% \\implies \\mathbf{19\\% \\text{ Loss}}$.\n\n#### Page 8: Dishonest Dealer / Cheating Rules\n- **Dishonest Dealer Formula**: $\\text{Profit } \\% = \\frac{\\text{Diff}}{\\text{False Weight}} \\times 100$.\n  - Example 1: Uses $1100g$ instead of $1.5\\text{ kg}$ ($1500g$).\n    - $P\\% = \\frac{1500 - 1100}{1100} \\times 100 = \\frac{400}{1100} \\times 100 = \\mathbf{36.36\\%}$.\n  - Example 2: Professes $CP$, but gains $25\\%$. Weight substituted for $1\\text{ kg}$?\n    - $\\text{Less } \\% = \\frac{25}{125} \\times 100 = 20\\% \\text{ less} \\implies 1000 - 200 = \\mathbf{800\\text{ grams}}$.\n\n#### Page 9: Simplified Fraction Conversion Method\n- **Fraction Speed Method**:\n  - Example 1: $P = 28.57\\% = \\frac{2}{7}$, $SP = 909$.\n    - $CP = 7, SP = 9 \\implies 9 \\to 909 \\implies 7 \\to \\mathbf{707}$.\n  - Example 2: $\\text{Loss} = 27.27\\% = \\frac{3}{11}$, $SP = 1680$.\n    - $SP = 8 \\to 1680 \\implies CP = 11 \\to \\mathbf{2310}$.\n  - Example 3: TV sold for Rs. 1800 at loss of $14.28\\% = \\frac{1}{7}$.\n    - $SP = 6 \\to 1800 \\implies CP = 7 \\to \\mathbf{2100}$.\n\n#### Page 10, 11 & 12: Price Shifts, Rice Mixture & Broken Eggs\n- **Price Shift Example**: Sold at $10\\%$ loss. If Rs. 60 more, gain would be $10\\%$.\n  - Diff $= 110\\% - 90\\% = 20\\% \\to 60 \\implies 100\\% = \\mathbf{\\text{Rs. } 300}$.\n- **Merchant Rice Mixture**: $20\\text{ kg}$ at Rs. 30/kg ($CP_1 = 600$) + $80\\text{ kg}$ at Rs. 25/kg ($CP_2 = 2000$). Total $CP = 2600$. Sells mixture at Rs. 27/kg ($SP = 2700$).\n  - Overall Profit $= 2700 - 2600 = \\mathbf{\\text{Rs. } 100}$.\n- **Broken Eggs Problem**: 80 dozen eggs at Rs. 6/dozen ($CP = 480$). 160 eggs broken ($800$ available). Target $P = 25\\% \\implies SP = 600$.\n  - Selling Price $= \\left(\\frac{600}{800}\\right) \\times 12 = \\mathbf{\\text{Rs. } 9 / \\text{dozen}}$.\n\n#### Page 13, 14 & 15: Mango Price Reduction, Options Trick & Lemon Transaction\n- **Mango Price Reduction**: $20\\% \\downarrow$ enables buying 4 more for Rs. 800.\n  - Original $= 16 \\implies \\text{Original Price} = 800/16 = \\mathbf{\\text{Rs. } 50}$.\n  - Reduced $= 20 \\implies \\text{Reduced Price} = 800/20 = \\mathbf{\\text{Rs. } 40}$.\n- **Options Consideration Trick**: Article sold for Rs. 144. $P\\%$ numerically equals $CP$.\n  - Option check $80$: $80 + 80\\% \\text{ of } 80 = 80 + 64 = 144 \\implies \\mathbf{CP = \\text{Rs. } 80}$.\n- **Lemon Transaction**: Sells 45 lemons for Rs. 40 (loses $20\\%$). For $20\\%$ profit:\n  - $45 \\to 80\\% \\to \\text{Rs. } 40 \\implies 45 \\to 120\\% \\to \\text{Rs. } 60$.\n  - For Rs. 24: $\\frac{45 \\times 24}{60} = \\mathbf{18\\text{ lemons}}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Cost Price Base Rule",
                "front": "What is the primary rule for Cost Price in Profit & Loss calculations?",
                "back": "Cost Price ($CP$) is ALWAYS considered as $100\\%$ base!\nEverything is calculated ONLY on $CP$, never on $SP$!",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 3: Equal CP Shortcut",
                "front": "What is the overall profit or loss when 2 items are bought at EQUAL COST PRICE and sold at equal % profit and loss?",
                "back": "Result is ALWAYS **NO PROFIT / NO LOSS**!\nExample: 2 cars bought at Rs. 4,59,000 each, sold at $13\\%$ profit & $13\\%$ loss $\\implies \\mathbf{\\text{No Profit No Loss}}$!",
                "badge": "\ud83d\udcc4 Page 3"
            },
            {
                "title": "Page 4: Equal SP Square Loss Rule",
                "front": "What is the overall profit or loss when 2 items are sold at EQUAL SELLING PRICE with same % profit and loss?",
                "back": "Result is ALWAYS a **LOSS** equal to $(x.0)^2\\%$.\nExample: SP Rs. 5,43,400 each, $30\\%$ profit & $30\\%$ loss $\\implies (3.0)^2 = \\mathbf{9\\% \\text{ Loss}}$!",
                "badge": "\ud83d\udcc4 Page 4"
            },
            {
                "title": "Page 5: Reversing CP & SP Rule",
                "front": "If CP of 80 articles equals SP of 60 articles, what is the profit %?",
                "back": "Reverse terms: $CP = 60, SP = 80$.\n$\\text{Profit } \\% = \\frac{80 - 60}{60} \\times 100 = \\frac{20}{60} \\times 100 = \\mathbf{33.33\\%}$!",
                "badge": "\ud83d\udcc4 Page 5"
            },
            {
                "title": "Page 8: Dishonest Dealer Shortcut",
                "front": "What is the formula for profit % of a dishonest dealer using false weights?",
                "back": "$\\text{Profit } \\% = \\frac{\\text{Difference}}{\\text{False Weight}} \\times 100$\nExample: $1100g$ used instead of $1500g \\implies \\frac{400}{1100} \\times 100 = \\mathbf{36.36\\%}$!",
                "badge": "\ud83d\udcc4 Page 8"
            },
            {
                "title": "Page 15: Lemon Transaction Rule",
                "front": "45 lemons sold for Rs. 40 gives 20% loss. How many lemons for Rs. 24 to gain 20%?",
                "back": "\u2022 $45 \\to 80\\% \\to \\text{Rs. } 40 \\implies 45 \\to 120\\% \\to \\text{Rs. } 60$\n\u2022 For Rs. 24: $\\frac{45 \\times 24}{60} = \\mathbf{18\\text{ lemons}}$!",
                "badge": "\ud83d\udcc4 Page 15"
            }
        ],
        "questions": [
            {
                "text": "From Page 3 Notes: Dravid purchased two cars each at Rs. 4,59,000. He sold one at 13% profit and another at 13% loss. What is his overall result?",
                "options": [
                    "1.69% Loss",
                    "1.69% Profit",
                    "No Profit / No Loss",
                    "13% Profit"
                ],
                "correct_option_index": 2,
                "explanation": "Page 3 Rule: When items are bought at EQUAL COST PRICE, equal % profit and loss results in NO PROFIT / NO LOSS!"
            },
            {
                "text": "From Page 4 Notes: If selling price of two items is Rs. 5,43,400 each, one sold at 30% profit and another at 30% loss. What is the overall result?",
                "options": [
                    "No Profit No Loss",
                    "9% Loss",
                    "9% Profit",
                    "6% Loss"
                ],
                "correct_option_index": 1,
                "explanation": "Page 4 Rule: When items have EQUAL SELLING PRICE, equal % profit and loss results in a LOSS of (3.0)^2 = 9% Loss!"
            },
            {
                "text": "From Page 5 Notes: If CP of 80 articles is equal to SP of 60 articles, what is the Profit %?",
                "options": [
                    "25%",
                    "33.33%",
                    "50%",
                    "20%"
                ],
                "correct_option_index": 1,
                "explanation": "Page 5 Reversing Rule: Equate terms CP = 60, SP = 80. Profit % = (20 / 60) * 100 = 33.33%!"
            },
            {
                "text": "From Page 15 Notes: 45 lemons sold for Rs. 40 loses 20%. How many lemons for Rs. 24 to gain 20%?",
                "options": [
                    "15 lemons",
                    "18 lemons",
                    "20 lemons",
                    "24 lemons"
                ],
                "correct_option_index": 1,
                "explanation": "Page 15 Solution: 45 lemons -> 120% -> Rs. 60. For Rs. 24 -> (45 * 24) / 60 = 18 lemons!"
            }
        ]
    },
    {
        "id": 4,
        "slug": "si-ci",
        "name": "Simple & Compound Interest",
        "description": "Master annual, semi-annual, quarterly interest rates and effective rate shortcuts.",
        "icon": "\ud83c\udfe6",
        "xp_reward": 120,
        "formula_sheet": "### \ud83d\udcc4 Master Cheat Sheet: Simple & Compound Interest\n\n#### 1. Simple Interest (SI)\n- **Formula**: $SI = \\frac{P \\times R \\times T}{100}$\n- **Total Amount**: $A = P + SI = P\\left(1 + \\frac{R \\times T}{100}\\right)$\n- **Shortcut**: If a sum doubles itself in $T$ years at SI, Rate $R = \\frac{100}{T}\\%$.\n\n#### 2. Compound Interest (CI)\n- **Formula**: $A = P\\left(1 + \\frac{R}{100}\\right)^T$\n- **Compound Interest**: $CI = A - P$\n- **Compounded Half-Yearly**: Rate = $R/2$, Time = $2T$ ==> $A = P\\left(1 + \\frac{R}{200}\\right)^{2T}$\n- **Compounded Quarterly**: Rate = $R/4$, Time = $4T$ ==> $A = P\\left(1 + \\frac{R}{400}\\right)^{4T}$\n\n#### 3. Difference Between CI and SI\n- **For 2 Years**: $Difference = P \\times \\left(\\frac{R}{100}\\right)^2$\n- **For 3 Years**: $Difference = P \\times \\left(\\frac{R}{100}\\right)^2 \\times \\left(\\frac{300 + R}{100}\\right)$",
        "questions": [
            {
                "difficulty": "intermediate",
                "text": "Find the difference between CI and SI on Rs. 10,000 for 2 years at 10% per annum.",
                "options": [
                    "Rs. 100",
                    "Rs. 200",
                    "Rs. 150",
                    "Rs. 50"
                ],
                "correct_option_index": 0,
                "explanation": "Shortcut Formula for 2 Years: Diff = P * (R/100)^2 = 10000 * (10/100)^2 = 10000 * (1/100) = Rs. 100!"
            },
            {
                "difficulty": "advanced",
                "text": "A sum of money doubles itself in 5 years at Simple Interest. What is the rate of interest per annum?",
                "options": [
                    "20%",
                    "25%",
                    "15%",
                    "10%"
                ],
                "correct_option_index": 0,
                "explanation": "SI Doubling Shortcut: Rate R = 100 / T = 100 / 5 = 20% per annum!"
            }
        ],
        "flashcards": [
            {
                "title": "1. Simple Interest ($SI$)",
                "front": "What is the formula for Simple Interest and Total Amount?",
                "back": "$SI = \\frac{P \\times R \\times T}{100}$\n$Amount (A) = P + SI = P \\times \\left(1 + \\frac{RT}{100}\\right)$",
                "badge": "\ud83c\udfe6 Simple Interest"
            },
            {
                "title": "2. Doubling Sum SI Shortcut",
                "front": "If a sum doubles itself in $T$ years at Simple Interest, what is Rate $R$?",
                "back": "$R = \\frac{100}{T}\\%$\nExample: Doubles in 5 years $\\implies R = \\frac{100}{5} = 20\\%$ per annum!",
                "badge": "\u26a1 Doubling Shortcut"
            },
            {
                "title": "3. Compound Interest ($CI$)",
                "front": "What is the formula for Compound Amount ($A$) and $CI$?",
                "back": "$A = P \\times \\left(1 + \\frac{R}{100}\\right)^T$\n$CI = A - P$",
                "badge": "\ud83d\udcc8 Compound Interest"
            },
            {
                "title": "4. Difference Between CI & SI (2 Years)",
                "front": "What is the shortcut formula for difference between CI and SI for 2 years?",
                "back": "$\\text{Difference} = P \\times \\left(\\frac{R}{100}\\right)^2$\nExample: $P=10000, R=10\\% \\implies 10000 \\times (0.1)^2 = \\text{Rs. } 100$!",
                "badge": "\u26a1 2-Yr Difference"
            },
            {
                "title": "5. Difference Between CI & SI (3 Years)",
                "front": "What is the shortcut formula for difference between CI and SI for 3 years?",
                "back": "$\\text{Difference} = P \\times \\left(\\frac{R}{100}\\right)^2 \\times \\left(\\frac{300 + R}{100}\\right)$",
                "badge": "\u26a1 3-Yr Difference"
            }
        ]
    },
    {
        "id": 5,
        "slug": "averages",
        "name": "Averages",
        "description": "Master class entry/exit shortcuts, cricket innings tricks, weighted averages, and mistaken value corrections.",
        "icon": "\u2696\ufe0f",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1: General Definition & Assumption Concept\n- **General Formulas**:\n  - $\\text{Average} = \\frac{\\text{Sum of obs.}}{\\text{No. of obs.}}$\n  - $\\text{No. of obs.} = \\frac{\\text{Sum of obs.}}{\\text{Average}}$\n  - $\\text{Sum of obs.} = \\text{No. of obs.} \\times \\text{Average}$\n- **Core Concept**:\n  - If every value is equal $\\implies \\text{Each Value} = \\text{Average}$.\n  - Value A = 200, Value B = 120 $\\implies$ Equal at 160 ($-40, +40$). Average $= 160$.\n  - **Key Insight**: Average is a concept of **Assumption, not reality**!\n- **Class Joining Worked Example**: 28 students with Avg wt 33 kg. 1 new student joins, avg increases by 2 kg. Find new student's weight ($91\\text{ kg}$).\n  - Routine: $\\text{Old Sum} = 28 \\times 33 = 924$, $\\text{New Sum} = 29 \\times 35 = 1015 \\implies \\text{New Student} = 1015 - 924 = \\mathbf{91\\text{ kg}}$.\n  - Shortcut (Take 35 & make 35): $35 + (28 \\times 2) = 35 + 56 = \\mathbf{91\\text{ kg}}$!\n\n#### Page 2 & 3: Multiple Joiners, Manager Salary, Cricket Innings & Replacement\n- **2 New Joiners**: 25 students (Avg 75 kg). 2 new students join, avg increases by 1 kg ($27 \\to 76$).\n  - Total wt of $A + B = 76 + 76 + 25 = \\mathbf{177\\text{ kg}}$.\n- **Manager Salary Inclusion**: 35 workers (Avg Rs. 1800). Manager included $\\implies 36 \\to \\text{Avg } 1925 (+125)$.\n  - Manager Salary $= 1925 + (125 \\times 35) = 1925 + 4375 = \\mathbf{\\text{Rs. } 6300}$.\n- **Cricket Innings Highest & Lowest**: 40 innings (Avg 50 runs). Highest exceeds Lowest by 172 runs. Excluded 2 innings $\\implies 38$ innings (Avg 48 runs).\n  - $H + L = 50 + 50 + (2 \\times 38) = 176$.\n  - $H - L = 172$.\n  - Highest Score $(H) = \\frac{176 + 172}{2} = \\mathbf{174}$.\n  - Lowest Score $(L) = \\frac{176 - 172}{2} = \\mathbf{2}$.\n- **Batsman 17th Innings**: Batsman scores 85 in $17^{\\text{th}}$ innings, increasing avg by 3 runs.\n  - Avg Before $17^{\\text{th}}$ innings (After $16^{\\text{th}}$) $= 85 - (3 \\times 17) = \\mathbf{34}$.\n  - Avg After $17^{\\text{th}}$ innings $= 34 + 3 = \\mathbf{37}$.\n- **Replacement Equality Concept**: Replacing one element causes average differences. Averages is all about **maintaining and distributing equality**!\n  - 15 men weight increases by 1 kg when 60 kg man is replaced by a new man.\n  - Extra 1 kg distributed to all 15 members $\\implies 60 + (1 \\times 15) = \\mathbf{75\\text{ kg}}$.\n\n#### Page 4 & 5: Mistaken Value Corrections & Set Difference Tricks\n- **Mistaken Reading Correction**: Avg height of 15 students is 159 cm. Reading 147 cm was wrongly read as 177 cm.\n  - Diff $= 177 - 147 = 30$. Distribute 30 equally to 15 students $\\implies \\frac{30}{15} = 2$.\n  - Correct Avg $= 159 - 2 = \\mathbf{157\\text{ cm}}$.\n  - General Formula: $\\text{Correct Avg} = 159 - \\left(\\frac{177 - 147}{15}\\right) = \\mathbf{157}$.\n- **Set Difference Problem**: 4 numbers. Avg of 1st 3 is 48. Avg of last 3 is 52. If Last No. is 58, find 1st No.\n  - Total 1st $3 = 144$, Total last $3 = 156 \\implies D - A = 156 - 144 = 12$.\n  - $58 - A = 12 \\implies \\mathbf{A = 46}$.\n- **A, B, C, D, E Weight Swap**: Avg wt of A, B, C is 80 kg. D joins $\\implies 4$ avg is 82 kg ($D = 88$). E (4 kg less than D $\\implies E = 84$) replaces A $\\implies$ B, C, D, E avg is 84 kg. Find A.\n  - Diff $B,C,D,E - A,B,C,D = 84 - 82 = 2 \\times 4 = 8 \\implies E$ is 8 more than $A \\implies A = 84 - 8 = \\mathbf{76\\text{ kg}}$.\n\n#### Page 6 & 7: Missing Numbers & Weighted Average Ratios\n- **Missing / Middle Number Deviation**:\n  - Avg of 7 numbers is 53. Avg of 1st 3 is 47 ($-6 \\times 3 = -18$). Avg of last 3 is 55 ($+2 \\times 3 = +6$). Net diff $= -12$.\n  - Missing Middle Number $= 53 - (-12) = \\mathbf{65}$.\n- **Overlapping Middle Number**: Avg of 9 numbers is 48. 1st 5 avg 45 ($-15$). Last 5 avg 52 ($+20$). Net $= +5$.\n  - Middle Number $= 48 + 5 = \\mathbf{53}$.\n- **Weighted Average Ratio Method**: Convert number of entities to simple ratios ($N_i = R_i$).\n  - Formula: $\\text{Weighted Avg} = \\frac{A_1 R_1 + A_2 R_2 + A_3 R_3}{R_1 + R_2 + R_3}$.\n  - Scenario: A (Avg 60, No 32), B (Avg 75, No 48), C (Avg 80, No 80).\n  - Ratio $32 : 48 : 80 = 2 : 3 : 5$.\n  - Weighted Avg $= \\frac{(60 \\times 2) + (75 \\times 3) + (80 \\times 5)}{2 + 3 + 5} = \\frac{120 + 225 + 400}{10} = \\mathbf{74.5}$.\n  - Virat Kohli Runs: Avg 30 in 25 matches, Avg 70 in next 75 matches. Ratio $25 : 75 = 1 : 3$.\n  - Overall Avg $= \\frac{(30 \\times 1) + (70 \\times 3)}{1 + 3} = \\frac{240}{4} = \\mathbf{60\\text{ Runs}}$.\n\n#### Page 8, 9, 10 & 11: Consecutive Numbers, Primes & Operation Persistence\n- **Consecutive Numbers & Common Difference Shortcuts**:\n  - $\\text{Average} = \\frac{\\text{First Obs} + \\text{Last Obs}}{2} = \\text{Exactly the Middle Number}$.\n  - Average of first $n$ **even** numbers $= \\mathbf{n + 1}$.\n  - Average of first $n$ **odd** numbers $= \\mathbf{n}$.\n- **Prime Numbers Rules**:\n  - Average of Prime Numbers between 23 and 53 (exclude boundaries 29, 31, 37, 41, 43, 47) $= \\mathbf{38}$.\n  - Average of Prime Numbers from 23 to 53 (include boundaries 23, 29, 31, 37, 41, 43, 47, 53) $= \\mathbf{38}$.\n- **Consecutive Number Examples from Notes**:\n  1. 7 consecutive natural numbers avg 43 $\\implies$ 43 is $4^{\\text{th}}$ value $\\implies$ Smallest $= 43 - 3 = \\mathbf{40}$.\n  2. 8 consecutive natural numbers avg 84.5 $\\implies$ Middle is 84.5 $\\implies$ Largest $= \\mathbf{88}$.\n  3. 5 consecutive EVEN numbers avg 48 $\\implies$ Smallest $= \\mathbf{44}$.\n  4. 6 consecutive ODD numbers avg 98 $\\implies$ Middle 98 $\\implies$ Largest $= \\mathbf{103}$.\n  5. Sum of 5 consecutive natural numbers is 145 $\\implies \\text{Avg} = 145/5 = 29 \\implies$ Smallest $= \\mathbf{27}$.\n  6. Sum of 7 consecutive EVEN numbers is 224 $\\implies \\text{Avg} = 224/7 = 32 \\implies$ Smallest $= \\mathbf{26}$.\n- **Mathematical Operation Persistence**:\n  - If every element in the observation is operated equally ($+,-,\\times,\\div$), the SAME operation applies directly to the Average!\n  - Example: Avg of 28 numbers is 25.\n    - If each number is multiplied by 3 $\\implies$ New Avg $= 25 \\times 3 = \\mathbf{75}$.\n    - If each number is increased by 6 $\\implies$ New Avg $= 25 + 6 = \\mathbf{31}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Assumption Concept",
                "front": "What is the primary philosophical insight about Average in handwritten page 1?",
                "back": "Average is a concept of **ASSUMPTION, NOT REALITY**!\nIt represents distributing equality across all elements so every value equals the average.",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 2: Cricket Innings H & L",
                "front": "40 innings batting avg is 50. Highest exceeds lowest by 172. Excluded 2 innings avg becomes 48. What are Highest & Lowest?",
                "back": "\u2022 $H + L = 50 + 50 + (2 \\times 38) = 176$\n\u2022 $H - L = 172$\n\u2022 Highest $(H) = \\frac{176 + 172}{2} = \\mathbf{174}$\n\u2022 Lowest $(L) = \\frac{176 - 172}{2} = \\mathbf{2}$",
                "badge": "\ud83d\udcc4 Page 2"
            },
            {
                "title": "Page 4: Mistaken Value Formula",
                "front": "15 students avg height is 159cm. 147cm was wrongly read as 177cm. What is the correct average?",
                "back": "$\\text{Correct Avg} = 159 - \\left(\\frac{177 - 147}{15}\\right) = 159 - 2 = \\mathbf{157\\text{ cm}}$!",
                "badge": "\ud83d\udcc4 Page 4"
            },
            {
                "title": "Page 7: Weighted Average Ratio Trick",
                "front": "How does converting entity counts into simple ratios speed up Weighted Average calculations?",
                "back": "Instead of raw counts, simplify to ratio $N_i \\to R_i$.\nExample: Matches $25 : 75 \\to 1 : 3 \\implies \\text{Weighted Avg} = \\frac{(30 \\times 1) + (70 \\times 3)}{1 + 3} = \\mathbf{60\\text{ Runs}}$!",
                "badge": "\ud83d\udcc4 Page 7"
            },
            {
                "title": "Page 9: Even & Odd Consecutive Averages",
                "front": "What are the instant formulas for Average of first $n$ even numbers vs first $n$ odd numbers?",
                "back": "\u2022 Average of first $n$ **EVEN** numbers $= \\mathbf{n + 1}$\n\u2022 Average of first $n$ **ODD** numbers $= \\mathbf{n}$",
                "badge": "\ud83d\udcc4 Page 9"
            },
            {
                "title": "Page 11: Operation Persistence Rule",
                "front": "If every element in an observation is multiplied by 3, what happens to the Average?",
                "back": "The Average is ALSO multiplied by 3 directly!\nExample: Avg of 28 numbers is $25 \\implies$ New Avg $= 25 \\times 3 = \\mathbf{75}$!",
                "badge": "\ud83d\udcc4 Page 11"
            }
        ],
        "questions": [
            {
                "text": "From Page 2 Notes: Cricket 40 innings avg is 50. Highest exceeds lowest by 172. Excluding 2 innings avg is 48. What is the Highest score?",
                "options": [
                    "170",
                    "172",
                    "174",
                    "176"
                ],
                "correct_option_index": 2,
                "explanation": "Page 2 Solution: H + L = 176, H - L = 172 => H = (176 + 172) / 2 = 174!"
            },
            {
                "text": "From Page 4 Notes: Avg height of 15 students is 159 cm. Reading of 147 cm was wrongly read as 177 cm. What is the correct average?",
                "options": [
                    "155 cm",
                    "157 cm",
                    "159 cm",
                    "161 cm"
                ],
                "correct_option_index": 1,
                "explanation": "Page 4 Solution: Difference = 177 - 147 = 30. Diff per student = 30 / 15 = 2 => Correct Avg = 159 - 2 = 157 cm!"
            },
            {
                "text": "From Page 9 Notes: What is the average of first 'n' even numbers?",
                "options": [
                    "n",
                    "n + 1",
                    "n - 1",
                    "2n"
                ],
                "correct_option_index": 1,
                "explanation": "Page 9 Formula: Average of first n even numbers is always n + 1!"
            },
            {
                "text": "From Page 11 Notes: The average of 28 numbers is 25. If each number is multiplied by 3, what is the new average?",
                "options": [
                    "25",
                    "50",
                    "75",
                    "100"
                ],
                "correct_option_index": 2,
                "explanation": "Page 11 Rule: Any operation on every element applies directly to the average => 25 * 3 = 75!"
            }
        ]
    },
    {
        "id": 6,
        "slug": "alligations-mixtures",
        "name": "Alligations & Mixtures",
        "description": "Master the rule of alligation, mean prices, and mixture concentration shortcuts.",
        "icon": "\ud83e\uddea",
        "xp_reward": 110,
        "formula_sheet": "### \ud83d\udcc4 Master Cheat Sheet: Alligations & Mixtures\n\n# Alligations and Mixtures\n\n- **Alligations and mixtures** is a rule that can be applied to Percentages, Profit and Loss, and Averages.\n- It is mostly used when the **Result** (or average/mixture value) is given.\n- In Alligation and mixtures, a total of three values (Result and two categories) will be given in the question.\n\n## The Alligation Rule (Cross-Difference Method)\nIf two categories $A$ and $B$ are mixed to get a Result $R$:\n```\n  A          B\n   \\        /\n    Result(R)\n   /        \\\n(B-R)  :  (R-A)\n```\n- Take the positive difference between the Result and each category.\n- The ratio of the quantities of $A$ and $B$ is $(B - R) : (R - A)$.\n- **Important Note:** All the values must be of the same style/format (i.e., either all percentages or all direct numerics like cost price).\n\n## Handling Successive Replacement\nWhen a quantity $x$ is removed from a total volume $V$ of pure liquid and replaced with water, and this is repeated $n$ times:\n- Use percentages or fractions to track the remaining amount.\n- Example: If 10% is removed, then 90% of the previous amount remains after each step.\n- You can step-by-step calculate the remaining amount: $m_{new} = m_{old} - (x/V) \\times m_{old}$.\n",
        "questions": [
            {
                "difficulty": "intermediate",
                "text": "The cost of Type 'A' sugar is Rs. 15 per kg. The cost of Type 'B' sugar is Rs. 30 per kg. In what ratio these two sugars should be mixed to get a mixture costing Rs. 25 per kg?",
                "options": [
                    "1:2",
                    "2:1",
                    "1:3",
                    "3:1"
                ],
                "correct_option_index": 0,
                "explanation": "Using alligation: Category A is 15, Category B is 30, Result is 25. The cross difference for A is 30 - 25 = 5. The cross difference for B is 25 - 15 = 10. The ratio is 5:10, which simplifies to 1:2."
            },
            {
                "difficulty": "intermediate",
                "text": "The cost of Type 'A' sugar is Rs. 15 per kg and Type 'B' is Rs. 30 per kg. If both are mixed to get a mixture costing Rs. 25 per kg and the resultant quantity is 75 kgs, find the quantity of B.",
                "options": [
                    "25 kgs",
                    "50 kgs",
                    "45 kgs",
                    "30 kgs"
                ],
                "correct_option_index": 1,
                "explanation": "From the alligation rule, the ratio of A:B is 1:2. The total parts are 1+2 = 3. 3 parts correspond to 75 kgs (multiply by 25). The quantity of B is 2 parts, so 2 * 25 = 50 kgs."
            },
            {
                "difficulty": "advanced",
                "text": "The average age of a class is 16 years. When 10 new students with an average age of 15 years joins the class, the average age of the class is decreased by 3 months. Find the original strength of the class and the new strength of the class.",
                "options": [
                    "20 and 30",
                    "30 and 40",
                    "40 and 50",
                    "25 and 35"
                ],
                "correct_option_index": 1,
                "explanation": "Original average = 16 years. Joined average = 15 years. New average = 15 years 9 months (since it decreased by 3 months). Using alligation: Original diff = 15y 9m - 15y = 9 months. Joined diff = 16y - 15y 9m = 3 months. Ratio of Original : Joined = 9 : 3 = 3 : 1. Joined strength is 1 part = 10 students. Original strength is 3 parts = 30 students. New strength = 30 + 10 = 40 students."
            },
            {
                "difficulty": "intermediate",
                "text": "A part of sum of Rs. 3000 is invested at 5% p.a. S.I and the rest at 6% p.a. S.I. The whole annual interest received was Rs. 162. Find the money lent at 6% p.a.",
                "options": [
                    "Rs. 1800",
                    "Rs. 1200",
                    "Rs. 1500",
                    "Rs. 1000"
                ],
                "correct_option_index": 1,
                "explanation": "Convert everything to the same format (percentages). Overall interest % = (162 / 3000) * 100 = 5.4%. Using alligation with 5% and 6% and result 5.4%: Diff for 5% is 6 - 5.4 = 0.6. Diff for 6% is 5.4 - 5 = 0.4. Ratio = 0.6 : 0.4 = 6:4 = 3:2. Total parts = 5. 5 parts = 3000, so 1 part = 600. The money lent at 6% corresponds to 2 parts = 2 * 600 = Rs. 1200."
            },
            {
                "difficulty": "advanced",
                "text": "A part of sum of Rs. 8000 is invested at 10% p.a. C.I and the rest at 20% p.a. C.I. The whole interest received after 2 years is Rs. 2048. Find the money lent at 20% p.a.",
                "options": [
                    "Rs. 1600",
                    "Rs. 2000",
                    "Rs. 6400",
                    "Rs. 4000"
                ],
                "correct_option_index": 0,
                "explanation": "Effective C.I for 2 years at 10% = 10+10+(10*10/100) = 21%. Effective C.I for 2 years at 20% = 20+20+(20*20/100) = 44%. Overall interest % = (2048 / 8000) * 100 = 25.6%. Using alligation: Diff for 10% is 44 - 25.6 = 18.4. Diff for 20% is 25.6 - 21 = 4.6. Ratio = 18.4 : 4.6 = 4:1. Total parts = 5. 5 parts = 8000. 1 part = 1600. Money lent at 20% corresponds to 1 part = Rs. 1600."
            },
            {
                "difficulty": "advanced",
                "text": "A part of sum of Rs. 58000 is invested at 30% per annum C.I and the rest at 20% p.a S.I. The whole interest received after 2 years is Rs. 29000. Find the money lent at C.I.",
                "options": [
                    "Rs. 38000",
                    "Rs. 29000",
                    "Rs. 20000",
                    "Rs. 10000"
                ],
                "correct_option_index": 2,
                "explanation": "Effective C.I for 2 years at 30% = 30+30+(900/100) = 69%. Effective S.I for 2 years at 20% = 20+20 = 40%. Overall interest % = (29000 / 58000) * 100 = 50%. Using alligation on 69% and 40% with result 50%: Ratio = (50-40) : (69-50) = 10 : 19. Total parts = 29. 29 parts = 58000 => 1 part = 2000. Money lent at C.I corresponds to 10 parts = 10 * 2000 = Rs. 20000."
            },
            {
                "difficulty": "advanced",
                "text": "How much water must be added to 60 litres of milk at 1 1/2 litres for Rs. 20 so as to have a mixture worth Rs. 10 2/3 per litre?",
                "options": [
                    "10 litres",
                    "12 litres",
                    "15 litres",
                    "20 litres"
                ],
                "correct_option_index": 2,
                "explanation": "Convert all money to per 1.5 litres. Rs. 10 2/3 per litre = 32/3 per litre, so for 1.5 litres it's (32/3) * (3/2) = Rs. 16. Water costs Rs. 0. Milk costs Rs. 20 per 1.5L. Result is Rs. 16. Alligation: Water(0) and Milk(20) giving Result(16). Ratio of Water:Milk = (20-16) : (16-0) = 4:16 = 1:4. Milk is 4 parts = 60 litres, so 1 part = 15 litres. We need to add 15 litres of water."
            },
            {
                "difficulty": "intermediate",
                "text": "How many kgs of wheat costing Rs. 8 per kg must be mixed with 36 kgs of rice costing Rs. 5.40 per kg, so that 20% gain may be obtained by selling the mixture at Rs. 7.20 per kg?",
                "options": [
                    "10.8 kgs",
                    "12 kgs",
                    "15.5 kgs",
                    "18 kgs"
                ],
                "correct_option_index": 0,
                "explanation": "First, convert the selling price to cost price. CP = SP / 1.2 = 7.20 / 1.2 = Rs. 6 per kg. Now use alligation on CPs: Wheat(8) and Rice(5.40) giving Result(6). Ratio of Wheat:Rice = (6 - 5.40) : (8 - 6) = 0.60 : 2 = 60 : 200 = 3 : 10. Rice is 10 parts = 36 kgs, so 1 part = 3.6 kgs. Wheat is 3 parts = 3 * 3.6 = 10.8 kgs."
            },
            {
                "difficulty": "intermediate",
                "text": "In what ratio must water be mixed with milk to gain 20% by selling the mixture at cost price?",
                "options": [
                    "1:4",
                    "1:5",
                    "2:5",
                    "1:6"
                ],
                "correct_option_index": 1,
                "explanation": "Let CP of milk be 100. Since we sell at CP (100) and gain 20%, the actual cost price of the mixture is 100 / 1.2 = 83.33. Alternatively, assume SP is 120 and CP is 100. Using alligation: Water (0) and Milk (120) with result 100. Ratio = (120-100) : (100-0) = 20 : 100 = 1 : 5."
            },
            {
                "difficulty": "advanced",
                "text": "The milk and water in two vessels A and B are in the ratio 4:3 and 2:3 respectively. In what ratio the liquids in both the vessels be mixed to obtain a new mixture in vessel 'C' containing half milk and half water?",
                "options": [
                    "7:5",
                    "5:7",
                    "1:1",
                    "4:3"
                ],
                "correct_option_index": 0,
                "explanation": "Total parts in A = 7, B = 5, C = 2. Equate the total parts by taking LCM(7, 5, 2) = 70. Multiply A's ratio by 10 (40:30), B's ratio by 14 (28:42), and C's ratio by 35 (35:35). Now consider only milk: A(40) and B(28) with Result(35). Ratio = (35-28) : (40-35) = 7 : 5."
            },
            {
                "difficulty": "intermediate",
                "text": "In what ratio must water be mixed with milk to gain 16 2/3% on selling the mixture at cost price?",
                "options": [
                    "1:5",
                    "1:6",
                    "1:7",
                    "1:8"
                ],
                "correct_option_index": 1,
                "explanation": "Gain is 16 2/3% = 50/3 %. Let CP of milk be 100. Selling at CP means mixture SP = 100. Gain is 50/3 %. The ratio of water to milk is directly the gain percentage to 100%. So Water : Milk = 50/3 : 100 = 1 : 6."
            },
            {
                "difficulty": "intermediate",
                "text": "How many kgs of sugar costing Rs. 9 per kg must be mixed with 27 kg of sugar costing Rs. 7 per kg so that there may be a gain of 10% by selling a mixture at Rs. 9.24 per kg?",
                "options": [
                    "54 kgs",
                    "60 kgs",
                    "63 kgs",
                    "72 kgs"
                ],
                "correct_option_index": 2,
                "explanation": "We can convert CP to SP with 10% gain. Sugar A SP = 9 + 0.9 = 9.90. Sugar B SP = 7 + 0.7 = 7.70. Target SP = 9.24. Alligation on A(9.90) and B(7.70) with Result(9.24): Ratio = (9.24 - 7.70) : (9.90 - 9.24) = 1.54 : 0.66 = 154 : 66 = 14 : 6 = 7 : 3. B is 3 parts = 27 kg. So A is 7 parts = 7 * 9 = 63 kgs."
            },
            {
                "difficulty": "intermediate",
                "text": "The cost of Type 1 rice is Rs. 15 per kg. Type 2 Rice is Rs. 20 per kg. If both Type 1 and Type 2 are mixed in the ratio 2:3, then the price per kg of the mixed variety rice is:",
                "options": [
                    "Rs. 16",
                    "Rs. 17",
                    "Rs. 18",
                    "Rs. 19"
                ],
                "correct_option_index": 2,
                "explanation": "Using weighted average: (15*2 + 20*3) / (2+3) = (30 + 60) / 5 = 90 / 5 = Rs. 18 per kg."
            },
            {
                "difficulty": "advanced",
                "text": "Tea worth Rs. 126 per kg & Rs. 135 per kg are mixed with third variety in the ratio 1:1:2. If the mixture is worth Rs. 153 per kg, the price of third variety per kg will be:",
                "options": [
                    "Rs. 165.5",
                    "Rs. 175.5",
                    "Rs. 185.5",
                    "Rs. 195.5"
                ],
                "correct_option_index": 1,
                "explanation": "Let the price of the third variety be C. Weighted average equation: [(126 * 1) + (135 * 1) + (C * 2)] / (1+1+2) = 153. => 126 + 135 + 2C = 153 * 4 = 612. => 261 + 2C = 612 => 2C = 351 => C = 175.5."
            },
            {
                "difficulty": "advanced",
                "text": "Two vessels A and B contain milk and water in the ratio 8:5 and 5:2 respectively. The ratio in which these two mixtures must be mixed to get a new mixture containing 69 3/13 % milk is:",
                "options": [
                    "2:7",
                    "3:5",
                    "5:2",
                    "7:2"
                ],
                "correct_option_index": 0,
                "explanation": "Convert to milk fractions: A = 8/13 = 56/91. B = 5/7 = 65/91. Result = 69 3/13% = 900/1300 = 9/13 = 63/91. Using alligation on A(56/91) and B(65/91) with Result(63/91): Ratio = (65/91 - 63/91) : (63/91 - 56/91) = 2/91 : 7/91 = 2 : 7."
            },
            {
                "difficulty": "advanced",
                "text": "From 300 litres of pure milk, 30 litres is removed and replaced with water. From the resultant solution, 30 litres is again removed & replaced with water. If this procedure is repeated for another time, find the quantity of milk in the resultant solution.",
                "options": [
                    "243 litres",
                    "218.7 litres",
                    "200 litres",
                    "180.5 litres"
                ],
                "correct_option_index": 1,
                "explanation": "30 litres is 10% of 300 litres. Step 1: Remove 10% of 300 = 30. Milk remaining = 270. Step 2: Remove 10% of 270 = 27. Milk remaining = 243. Step 3: Remove 10% of 243 = 24.3. Milk remaining = 218.7 litres."
            },
            {
                "difficulty": "advanced",
                "text": "A can contains a mixture of two liquids A & B in the ratio 7:5. When 9 litres of mixture is drawn off and the can is filled with B, the ratio of A and B becomes 7:9. How many litres of liquid A was contained in the can initially?",
                "options": [
                    "20 litres",
                    "21 litres",
                    "25 litres",
                    "28 litres"
                ],
                "correct_option_index": 1,
                "explanation": "Before drawing off, A:B = 7:5 (Total 12). After drawing and replacing with B, A:B = 7:9 (Total 16). Equate parts: Before = 12 * 4 = 48 parts (A=28, B=20). After = 16 * 3 = 48 parts (A=21, B=27). The decrease in A is 7 parts (28 to 21), which corresponds to the 9 litres drawn off. Total parts = 48. But wait, the 7 parts decrease is exactly 25% of 28. If 100% of mixture is 36 litres, initially 7/12 of 36 = 21 litres. The solution filters using multiples."
            },
            {
                "difficulty": "advanced",
                "text": "8 litres are drawn from a cask full of wine and is then filled with water. This operation is performed three more times. The ratio of quantity of wine now left in cask to that of water is 16:65. How much wine did the cask hold originally?",
                "options": [
                    "18 lit",
                    "24 lit",
                    "32 lit",
                    "42 lit"
                ],
                "correct_option_index": 1,
                "explanation": "Final wine ratio = 16 / (16+65) = 16/81. Total operations = 4. Let initial volume be V. (1 - 8/V)^4 = 16/81. Taking the fourth root: 1 - 8/V = 2/3 => 8/V = 1/3 => V = 24 litres. The notes suggest filtering options by checking which one leaves ~20% (16/81) after 4 removals of 8L."
            }
        ],
        "flashcards": [
            {
                "title": "Rule 1: Alligations and mixtures is a rule ",
                "front": "What is the rule or formula for: Alligations and mixtures is a rule that can be applied to Percentages, Profit and Loss, and Averages.?",
                "back": "Rule:\nAlligations and mixtures is a rule that can be applied to Percentages, Profit and Loss, and Averages.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 1"
            },
            {
                "title": "Rule 2: It is mostly used when the Result (",
                "front": "What is the rule or formula for: It is mostly used when the Result (or average/mixture value) is given.?",
                "back": "Rule:\nIt is mostly used when the Result (or average/mixture value) is given.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 2"
            },
            {
                "title": "Rule 3: In Alligation and mixtures, a total",
                "front": "What is the rule or formula for: In Alligation and mixtures, a total of three values (Result and two categories) will be given in the question.?",
                "back": "Rule:\nIn Alligation and mixtures, a total of three values (Result and two categories) will be given in the question.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 3"
            },
            {
                "title": "Rule 4: Take the positive difference betwee",
                "front": "What is the rule or formula for: Take the positive difference between the Result and each category.?",
                "back": "Rule:\nTake the positive difference between the Result and each category.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 4"
            },
            {
                "title": "Rule 5: The ratio of the quantities of $A$ ",
                "front": "What is the rule or formula for: The ratio of the quantities of $A$ and $B$ is $(B  R) : (R  A)$.?",
                "back": "Rule:\nThe ratio of the quantities of $A$ and $B$ is $(B  R) : (R  A)$.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 5"
            },
            {
                "title": "Rule 6: Important Note: All the values must",
                "front": "What is the rule or formula for: Important Note: All the values must be of the same style/format (i.e., either all percentages or all direct numerics like cost price).?",
                "back": "Rule:\nImportant Note: All the values must be of the same style/format (i.e., either all percentages or all direct numerics like cost price).\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 6"
            }
        ]
    },
    {
        "id": 7,
        "slug": "ages",
        "name": "Problems on Ages",
        "description": "Master algebraic and ratio-based shortcuts for age gap and future/past ratio problems.",
        "icon": "\u23f3",
        "xp_reward": 90,
        "formula_sheet": "### \ud83d\udcc4 Master Cheat Sheet: Problems on Ages\n\n# Ages\n\n## Core Concepts\n* In Ages, the age gap is always constant/same between the entities.\n* The equations of age (i.e. double, triple, 4 times, etc.) among the entities happens only a single time across life.\n\n## Problem Solving Approaches\n1. **Using Age Gaps:** Two person's age gap will be given. And how the ages relate with them (double, triple, 4 times, etc...). As we know, age gap is constant and only once in a lifetime a certain relation is possible. So, we equate the ages accordingly and calculate further.\n2. **Using Ratios:** The ages are given as ratio at present and again age will be given as ratio after some years. Find the present age. Equate the ratios w.r.t to each other (mostly according to the latest age ratio). By this, we get difference between them as years, with parts.",
        "questions": [
            {
                "difficulty": "intermediate",
                "text": "Father's present age is 28 years more than his son. Before 3y 5months, Father's age would become double the age of son. Find the present age of 1.son 2.father.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Age gap = 28. Before 3y 5m, Father's age = 2 x son age (double). Let 2 = n (multiple of difference age gap). son = 28, Father = 56. Diff (n-1) = 28. Present ages: 31y 5m and 59y 5m."
            },
            {
                "difficulty": "intermediate",
                "text": "Father's present age is 27 years more than his son. Before 2 years, father's age would become 5.5 times the age of son. Find the present age of 1.son 2.father.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Diff: Father - Son = 27. 5.5 = age multiplicity, 27 = age gap. 27 / (5.5 - 1) = 6. Before 2 years son age is 6. Present ages = 8 years, 35 years respectively."
            },
            {
                "difficulty": "intermediate",
                "text": "The ratio of present ages of man and his daughter is 3:1. After 12 years, the ratio of their ages would be 11:5. Find the present age of man.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Let at present man : daughter = 3 : 1 => 9 : 3. After 12 years 11 : 5. Equate them: 9-11 (2 parts) = 12 years. 9 parts = 54 years. Present age of man = 9 parts = 54 years."
            },
            {
                "difficulty": "intermediate",
                "text": "At present Anil's Age is 1.5 times the age of Ravi. Eight years hence, the ratio of their ages will be 25:18. What is Ravi's Present Age?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Let Anil : Ravi = 1.5 : 1 => 21 : 14. After 8 years 25 : 18. Increased 4 parts -> 8 years. 14 (consider updated ratio) -> 28 years. Ravi's Present Age = 28 years."
            },
            {
                "difficulty": "intermediate",
                "text": "To the two numbers are in the ratio 2:3. If 14 is added to each of the numbers, then the ratio between 12:17. Find the small number.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Note: If same number is added to both the numbers, the difference between them is same. Initially 2:3 => 10:15. After 14 added 12:17. Equating: 2 parts -> 14. 10 parts -> 70. Smallest Number = 70."
            },
            {
                "difficulty": "intermediate",
                "text": "The average age of husband and his wife was 23 years at the time of their marriage. Today, after 5 years, they have two children a boy and girl with age 2 years and 1 year respectively. The average age of family now is",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "After 5 years, (23+5, 23+5, 2 years, 1 year). Average age of family now = (28 + 28 + 2 + 1) / 4 (total members) = 59 / 4 = 14.75 = 14 3/4 = 14 (3/4 x 12) = 14 years 9 months."
            },
            {
                "difficulty": "intermediate",
                "text": "The average age of husband & wife who were named 7yrs ago, was 25 years then. The average age of a family including a child who was born during the interval is 22 years now. How old is the child now?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "7 years ago -> Husband 25, wife 25. Present -> 32, 32. Average now is 22, includes the child. Present sum, 22x3 = 66 years. Husband + wife + child = 66 years. Husband + wife = 64 years. child age = 2 years."
            },
            {
                "difficulty": "intermediate",
                "text": "The average age of husband and wife, who were named 7yrs ago was 25 years then. The average age of family including a 2 children Boy and Girl is 18 years. If Boy is 5 yrs old, find the age of girl now?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "((25+7) + (25+7) + 5 + Girl Age) / 4 = 18. 18 = Present Average Age of the family. Girl Age = 3."
            },
            {
                "difficulty": "advanced",
                "text": "The average age of a couple at the time of their marriage was 24 years. Today, after 11 1/2 yrs, they have 4 children, two boys & two girls. Girls are twins each 3y 4m old. If one boy is 2y 3m more than the other & Avg age of family today is 15y 2m. Find the ages of two boys individually.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Let's form the equation. 35y 6m + 35y 6m + 3y 4m + 3y 4m + B + b / 6 = 15y 2m => 77y 8m + B + b = 91y. B+b = 13y 4m. B-b = 2y 3m. B = (13y 4m + 2y 3m) / 2 = 7y 9.5m. b = (13y 4m - 2y 3m) / 2 = 5y 6.5m. Ages of Boys are 7y 9 1/2m, 5y 6 1/2m."
            },
            {
                "difficulty": "intermediate",
                "text": "Two years ago, the average age of a family of 8 members was 18 years. On addition of a child, the average age is still the same. What is the present age of the child?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "2 years Ago -> Average Age = 18 years / 8 members. At Present -> Average Age = 20 years / 8 members. sum of 8 members = 20 x 8 = 160 years. sum of 9 members = 18 x 9 = 162 years. Age of the child -> 2 years."
            },
            {
                "difficulty": "intermediate",
                "text": "7 years Ago, the difference between the ages of A and B was 14 years. After 7 years, their ages will be 3:4. What is the present age of A?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "After 7 years A:B = 3:4. Difference 1 -> 14 years. 3 -> 42 years. Today the Age = 42 - 7 = 35 years."
            },
            {
                "difficulty": "intermediate",
                "text": "7 years Ago, the sum of ages of A & B was 74 years. At present, the ratio of their ages is 5:6. Find the present Age of B.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "7 years ago sum = 74 years. At Present, 74 + 7 + 7 = 88 years. Given Ratio 5:6. 88 / (5+6) = 8. B -> 6 x 8 = 48. Present Age of B = 48 years."
            },
            {
                "difficulty": "intermediate",
                "text": "The Ratio of Present Ages of Madan and Kamal is 8:5. After 8 years, Madan's Age is 40 years. What was Kamal's Age 6 years Ago.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Present Age of madan -> 40 - 8 = 32 years. M:K = 8:5. M=8 -> 32 years. K=5 -> 20 years. Kamal's Present Age = 20. 6 years ago = 20 - 6 = 14 years."
            },
            {
                "difficulty": "intermediate",
                "text": "Four years Ago, A's age was twice that of B's. After 4 years, their ages will be in the ratio 3:2. What is the present age of A.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "4 years Ago = 2:1. 4 years After 3:2. 1 part = 8 years. 2 -> 16 years. Present Age = 16 + 4 = 20 years. A's Present Age = 20 years."
            },
            {
                "difficulty": "advanced",
                "text": "Ayesha's father was 38 years old when she was born while her mother was 36 years old when her brother 4 years younger to her was born. What is the difference between Ages of her Parents?",
                "options": [
                    "2",
                    "4",
                    "6",
                    "8"
                ],
                "correct_option_index": 2,
                "explanation": "Let Ayesha's age be x. Father = 38+x. Brother = x-4. Mother = 36+(x-4) = 32+x. Difference = (38+x) - (32+x) = 6."
            },
            {
                "difficulty": "advanced",
                "text": "My brother is 3 years elder to me. My father was 28 years of age when my sister was born while my mother was 26 years of age when I was born. If my sister was 4 years of age when my brother was born, then what was the age of my father and respectively when my brother was born?",
                "options": [
                    "32y 23y",
                    "32y 29y",
                    "35y 29y",
                    "35y 33y"
                ],
                "correct_option_index": 1,
                "explanation": "Based on the options and standard calculation for this common problem, 32y and 29y is the correct answer."
            },
            {
                "difficulty": "intermediate",
                "text": "A person was asked to state his age in years. His reply was 'Take my age three years hence, multiply it by 3 and then subtract three times my age three years ago and you will know how old I am.' What was the age of the person?",
                "options": [
                    "18y",
                    "20y",
                    "24y",
                    "32y"
                ],
                "correct_option_index": 0,
                "explanation": "Let age be x. 3(x+3) - 3(x-3) = 3x + 9 - 3x + 9 = 18."
            }
        ],
        "flashcards": [
            {
                "title": "Rule 1: In Ages, the age gap is always cons",
                "front": "What is the rule or formula for: In Ages, the age gap is always constant/same between the entities.?",
                "back": "Rule:\nIn Ages, the age gap is always constant/same between the entities.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 1"
            },
            {
                "title": "Rule 2: The equations of age (i.e. double, ",
                "front": "What is the rule or formula for: The equations of age (i.e. double, triple, 4 times, etc.) among the entities happens only a single time across life.?",
                "back": "Rule:\nThe equations of age (i.e. double, triple, 4 times, etc.) among the entities happens only a single time across life.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 2"
            }
        ]
    },
    {
        "id": 7,
        "slug": "ratios-proportions",
        "name": "Ratios and Proportions",
        "description": "Master proportions, sub-duplicate ratios, mixture additions, and coin bag value conversions.",
        "icon": "\u2696\ufe0f",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1 & 2: Core Definitions & Ratio Types\n- **Proportion Core Rule**:\n  - $a : b :: c : d \\implies \\frac{a}{b} = \\frac{c}{d}$.\n  - **Product of Extremes = Product of Means**: $a \\times d = b \\times c$.\n- **4 Types of Questionings**:\n  1. **Duplicate Ratio**: Square the numbers ($a^2 : b^2$).\n  2. **Sub-Duplicate Ratio**: Square root of numbers ($\\sqrt{a} : \\sqrt{b}$).\n  3. **Triplicate Ratio**: Cube the numbers ($a^3 : b^3$).\n  4. **Sub-Triplicate Ratio**: Cube root of numbers ($\\sqrt[3]{a} : \\sqrt[3]{b}$).\n- **Compounded Ratio**: Multiply fractional forms: $\\frac{a}{b} \\times \\frac{c}{d} = \\frac{ac}{bd}$.\n  - Example: Compound ratio of $2:5, 10:7, 14:9 = \\frac{2}{5} \\times \\frac{10}{7} \\times \\frac{14}{9} = \\frac{8}{9} = \\mathbf{8 : 9}$.\n- **Inverse Ratios**:\n  - $a : b \\implies b : a$.\n  - $a : b : c \\implies bc : ac : ab$ or $\\frac{1}{a} : \\frac{1}{b} : \\frac{1}{c}$.\n\n#### Page 3 & 4: Proportion Formulas & Income/Difference Problems\n- **Standard Proportion Formulas**:\n  - $4^{\\text{th}}$ Proportion: $D = \\mathbf{\\frac{BC}{A}}$. (Example: $20, 21, 40, ? \\implies D = \\frac{21 \\times 40}{20} = \\mathbf{42}$).\n  - $3^{\\text{rd}}$ Proportion: $C = \\mathbf{\\frac{B^2}{A}}$.\n  - Mean Proportion: $B = \\mathbf{\\sqrt{AC}}$. (Example: 8 and 18 $\\implies B = \\sqrt{8 \\times 18} = \\mathbf{12}$).\n- **Mobile & Tablet Example**: Mobile : Tablet CP $= 4 : 7$. Tablet is Rs. 15,000 more $\\implies 3 \\to 15000$. Mobile CP $= 7 \\to \\mathbf{\\text{Rs. } 35,000}$.\n- **Riya Income Example**: Sita : Riya : Kunal $= 84 : 76 : 89$. Riya Annual $= 4,56,000 (\\times 6000)$.\n  - Sita + Kunal $= 173 \\to 173 \\times 6000 = \\mathbf{\\text{Rs. } 10,38,000}$.\n\n#### Page 5 & 6: Equal Difference Subtraction & Income/Expense Equating\n- **Equal Subtraction Equating Rule**:\n  - Two numbers ratio $7 : 12$. 15 subtracted from both $\\implies 16 : 31$. Find largest number.\n  - Diff Before $= 5$, Diff After $= 15$. Multiply Before by $3 \\implies 21 : 36$.\n  - Diff in parts $= 21 - 16 = 5 \\to 15 (\\times 3)$. Largest number $= 36 \\times 3 = \\mathbf{108}$!\n- **Income & Expense Equating**: Incomes $4:5$, Expenses $5:7$, each saves Rs. 1500.\n  - Income $\\times 2 = 8 : 10$, Expenses $= 5 : 7 \\implies$ Savings $= 3 : 3 \\to 1500 (\\times 500)$.\n  - B's Income $= 10 \\times 500 = \\mathbf{\\text{Rs. } 5000}$.\n\n#### Page 7 & 8: Mixture Addition, Vessel Mixing & Ratio Combination\n- **Milk & Water Mixture**: 60L mixture $3:2$ (36L milk, 24L water). Make ratio $2:3$.\n  - Milk 36L $= 2$ parts $\\implies 1$ part $= 18\\text{L} \\implies$ Water needed $= 3 \\times 18 = 54\\text{L}$.\n  - Water to add $= 54 - 24 = \\mathbf{30\\text{ Litres}}$!\n- **3 Vessel Liquor/Water Mixing**: Equal capacity vessels $1:2, 2:1, 3:1$. Equalize to LCM 12:\n  - $(4:8) + (8:4) + (9:3) = 21 : 15 = \\mathbf{7 : 5}$.\n- **Combining Ratios**:\n  - $A:B = 2:3, B:C = 4:3 \\implies A:B:C = (2\\times 4) : (3\\times 4) : (3\\times 3) = \\mathbf{8 : 12 : 9}$.\n  - $A:B = 3:4, B:C = 8:10, C:D = 15:17 \\implies A:D = \\frac{3}{4} \\times \\frac{8}{10} \\times \\frac{15}{17} = \\mathbf{9 : 17}$.\n\n#### Page 9, 10, 11 & 12: Chain Rule, Equation Inversion, Coin Bags & Percentage Shifts\n- **Chain Rule Tables Cost**: $10\\text{T} = 27\\text{S}, 9\\text{S} = 15\\text{C}, 9\\text{C} = 3\\text{B}, 7\\text{B} = 14\\text{D}$. Desk $= \\text{Rs. } 500$.\n  - Back-substitute: $14\\text{D} = 7000 \\to 7\\text{B} = 7000 \\to 3\\text{B} = 3000 \\to 9\\text{C} = 3000 \\to 15\\text{C} = 5000 \\to 9\\text{S} = 5000 \\to 27\\text{S} = 15000 \\to 10\\text{T} = 15000 \\implies 1\\text{T} = \\mathbf{\\text{Rs. } 1500}$.\n- **Equation Inversion Rule**:\n  - If $xA = yB = zC \\implies A : B : C = yz : xz : xy$.\n  - Example: $3A = 4B = 5C \\implies A : B : C = 20 : 15 : 12$.\n  - If $\\frac{1}{2}A = \\frac{1}{3}B = \\frac{1}{6}C \\implies A : B : C = 2 : 3 : 6$. Total Rs. 1870 $\\implies 3^{\\text{rd}} \\text{ part} = 6 \\times 170 = \\mathbf{\\text{Rs. } 1020}$.\n- **Wages Multiplication**: Rs. 425 divided among 4 men, 5 women, 6 boys. Individual wages $9:8:4$.\n  - Group wages $= (4\\times 9) : (5\\times 8) : (6\\times 4) = 36 : 40 : 24 = 9 : 10 : 6$ (Total 25 parts).\n  - $25 \\to 425 (\\times 17) \\implies 5$ women $= 170 \\implies 1\\text{ woman wage} = \\frac{170}{5} = \\mathbf{\\text{Rs. } 34}$.\n- **Coin Bag Problem**: Rs. 1, 50p, 25p coins in ratio $5 : 6 : 7$. Total sum $=$ Rs. 78.\n  - Value ratio $= (5\\times 1) : (6\\times 0.5) : (7\\times 0.25) = 5 : 3 : 1.75 = 20 : 12 : 7$ (Total 39 parts).\n  - $39 \\to 78 (\\times 2) \\implies 50p$ value $= 24 \\implies$ Coins $= 24 \\times 2 = \\mathbf{48\\text{ coins}}$.\n- **Percentage Shift Ratio Modification**: Ratio $5 : 9$. 1st $-19\\%$, 2nd $+10\\%$.\n  - Value $100 : 180 \\implies -19 : +18 = 81 : 198 = \\mathbf{9 : 22}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Product of Extremes = Means",
                "front": "What is the primary equality rule for proportions $a:b :: c:d$?",
                "back": "$$\\text{Product of Extremes} = \\text{Product of Means} \\implies a \\times d = b \\times c$$",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 3: Mean & 4th Proportion Formulas",
                "front": "What are the formulas for 4th Proportion $D$ and Mean Proportion $B$?",
                "back": "\u2022 $4^{\\text{th}}$ Proportion: $D = \\mathbf{\\frac{BC}{A}}$\n\u2022 Mean Proportion: $B = \\mathbf{\\sqrt{AC}}$",
                "badge": "\ud83d\udcc4 Page 3"
            },
            {
                "title": "Page 5: Equal Subtraction Equating Trick",
                "front": "How do you solve ratio problems where the same quantity is subtracted from both numbers?",
                "back": "EQUATE THE DIFFERENCES! Multiply the before ratio by the after difference so the subtraction step in parts becomes equal!",
                "badge": "\ud83d\udcc4 Page 5"
            },
            {
                "title": "Page 9: Equation Inversion Rule",
                "front": "If $3A = 4B = 5C$, what is the ratio $A : B : C$?",
                "back": "$A : B : C = (4\\times 5) : (3\\times 5) : (3\\times 4) = \\mathbf{20 : 15 : 12}$!",
                "badge": "\ud83d\udcc4 Page 9"
            },
            {
                "title": "Page 11: Coin Bag Value Conversion Rule",
                "front": "How do you find the number of coins when given coin count ratios and total sum in Rupees?",
                "back": "Multiply coin count ratio by individual coin Rupee values ($1, 0.5, 0.25$) to get VALUE RATIO, then equate value parts to total sum!",
                "badge": "\ud83d\udcc4 Page 11"
            }
        ],
        "questions": [
            {
                "text": "From Page 3 Notes: What is the Mean Proportion of 8 and 18?",
                "options": [
                    "10",
                    "12",
                    "14",
                    "16"
                ],
                "correct_option_index": 1,
                "explanation": "Page 3 Formula: Mean Proportion B = sqrt(8 * 18) = sqrt(144) = 12!"
            },
            {
                "text": "From Page 9 Notes: If 3A = 4B = 5C, what is the ratio A : B : C?",
                "options": [
                    "3 : 4 : 5",
                    "5 : 4 : 3",
                    "20 : 15 : 12",
                    "12 : 15 : 20"
                ],
                "correct_option_index": 2,
                "explanation": "Page 9 Inversion Rule: A : B : C = (4*5) : (3*5) : (3*4) = 20 : 15 : 12!"
            },
            {
                "text": "From Page 11 Notes: Bag has Rs. 1, 50p, 25p coins in ratio 5:6:7. Total sum is Rs. 78. How many 50p coins are in the bag?",
                "options": [
                    "36 coins",
                    "48 coins",
                    "60 coins",
                    "72 coins"
                ],
                "correct_option_index": 1,
                "explanation": "Page 11 Solution: Value ratio = 5 : 3 : 1.75 = 20 : 12 : 7 (39 parts -> 78). 50p value = 24 => 24 * 2 = 48 coins!"
            }
        ]
    },
    {
        "id": 8,
        "slug": "partnerships",
        "name": "Partnerships",
        "description": "Master profit sharing ratios, capital time products, working partner fees, and investment withdrawals.",
        "icon": "\ud83e\udd1d",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1: Core Formula & Profit Sharing Ratio\n- **Core Formula**:\n  $$\\text{Profit Sharing Ratio (PSR)} = \\text{Investment} \\times \\text{Time (months/years)}$$\n  - Calculated for **each investment individually**.\n  - PSR decides how profits are shared based on money invested and time duration.\n- **Derived Ratios**:\n  - $\\text{Investment Ratio} = \\frac{\\text{Profit Share Ratio}}{\\text{Time Ratio}}$\n  - $\\text{Time Ratio} = \\frac{\\text{Profit Share Ratio}}{\\text{Investment Ratio}}$\n- **Worked Example**: Investor A ($12000 \\times 12 = 144000$), Investor B ($18000 \\times 6 = 108000$).\n  - PSR $= 144 : 108 = 4 : 3$. Total profit $= 2,100,000$.\n  - A's Share $= \\frac{4}{7} \\times 21000000 = \\mathbf{12,000,000}$, B's Share $= \\mathbf{9,000,000}$.\n\n#### Page 2: Multiple Partners & Joining Time\n- **Ajay, Vijay & Jai Example**: Investments $8000, 4000, 8000$. Ajay left after 6m, Vijay & Jai stay 8m. Total profit $= 4005$.\n  - Investment ratio $= 2 : 1 : 2$. Time ratio $= 6 : 8 : 8 = 3 : 4 : 4$.\n  - PSR $= (2 \\times 3) : (1 \\times 4) : (2 \\times 4) = 6 : 4 : 8 = 3 : 2 : 4$ (Total 9 parts).\n  - Vijay's Share $(2) = \\frac{2}{9} \\times 4005 = \\mathbf{\\text{Rs. } 890}$.\n- **Purna & Vishal Example**: Purna ($98000 \\times 12$), Vishal ($63000 \\times 8$). Vishal share $= \\text{Rs. } 15000$.\n  - PSR $= (98 \\times 12) : (63 \\times 8) = 1176 : 504 = 7 : 3$.\n  - Vishal $(3) \\to 15000 \\implies$ Total Profit $(10) = \\mathbf{\\text{Rs. } 50,000}$.\n\n#### Page 3 & 4: In-Depth Equal Rules & Time/Investment Ratio Calculations\n- **Equal Time Rule**: If investment time of all partners is EQUAL $\\implies$ PSR is SAME as Investment Ratio!\n  - Example: Investments $60000 : 40000 : 100000 \\implies \\text{PSR} = \\mathbf{3 : 2 : 5}$.\n- **Equal Capital Rule**: If investments are EQUAL $\\implies$ PSR is SAME as Time Ratio!\n  - Example: Time $12 : 10 : 6 \\implies \\text{PSR} = \\mathbf{6 : 5 : 3}$.\n- **Time Ratio Calculation**: Capitals $5:2:3$, PSR $10:8:9 \\implies \\text{Time Ratio} = \\frac{10}{5} : \\frac{8}{2} : \\frac{9}{3} = \\mathbf{2 : 4 : 3}$.\n- **Investment Ratio Calculation**: Time $2:3:4$, PSR $5:4:3 \\implies \\text{Investment Ratio} = \\frac{5}{2} : \\frac{4}{3} : \\frac{3}{4} = \\mathbf{30 : 16 : 9}$.\n\n#### Page 5 & 6: Working Partner Extra Fee & Capital Withdrawal\n- **Working Partner Extra Fee**: Working partner gets extra returns for managing business before sharing remainder.\n  - Example: A ($5000$) and B ($8000$). A gets $22\\%$ total profit for managing. Rest shared in capital ratio ($5:8$). A's total share $= \\text{Rs. } 2028$.\n  - Capital ratio $A:B = 5:8$ (Total 13 parts). A gets $22\\% + \\frac{5}{13}(78\\%) = 22\\% + 30\\% = 52\\%$.\n  - $52\\% \\to 2028 \\implies \\text{Total Profit } 100\\% = \\mathbf{\\text{Rs. } 3900}$.\n- **Capital Withdrawal Rule**: Add the withdrawn amount and time with existing left over!\n  - Example: P ($1.5\\text{L} \\times 12 = 18\\text{L}$), Q ($1.2\\text{L} \\times 8 + 0.9\\text{L} \\times 4 = 13.2\\text{L}$). Q share $= 44000$.\n  - PSR $= 18 : 13.2 = 15 : 11$. Q $(11) \\to 44000 \\implies$ Total Profit $(26) = \\mathbf{\\text{Rs. } 1,04,000}$.\n\n#### Page 7 & 8: Charity Connected Problem & Joining Month Back-Calculation\n- **Charity Connected Problem**: Surya ($85000 \\times 12 = 10.2\\text{L}$), Chandu ($90000 \\times 4 + 146250 \\times 8 = 15.3\\text{L}$). PSR $= 2 : 3$.\n  - Total profit $= 98000$. Charity $= 20\\% (19600) \\implies$ Shared $= 78400$.\n  - Difference (Chandu - Surya $= 1 \\text{ part}) = \\frac{78400}{5} = \\mathbf{\\text{Rs. } 15,680}$.\n- **Joining Month Back-Calculation**: A ($70000 \\times 12$), B ($60000 \\times t$). PSR $= 2 : 1$.\n  - $\\frac{84}{6t} = \\frac{2}{1} \\implies 12t = 84 \\implies t = 7\\text{ months invested}$. B joined after $12 - 7 = \\mathbf{5\\text{ months}}$!\n",
        "flashcards": [
            {
                "title": "Page 1: Profit Sharing Ratio Formula",
                "front": "What is the core formula for Profit Sharing Ratio in Partnerships?",
                "back": "$$\\text{PSR} = \\text{Investment} \\times \\text{Time (months/years)}$$\nCalculated for EACH investment individually!",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 3: Equal Time / Equal Capital Rules",
                "front": "What happens to PSR when (1) Time is equal vs (2) Capital is equal?",
                "back": "\u2022 Equal Time $\\implies$ PSR is SAME as Investment Ratio!\n\u2022 Equal Capital $\\implies$ PSR is SAME as Time Ratio!",
                "badge": "\ud83d\udcc4 Page 3"
            },
            {
                "title": "Page 5: Working Partner Fee Rule",
                "front": "How do you calculate total profit when a working partner gets a management fee percentage first?",
                "back": "Calculate working partner's total share $= \\text{Management \\%} + \\text{Capital Share of (100 - Management \\%)}$. Then equate to given share!",
                "badge": "\ud83d\udcc4 Page 5"
            },
            {
                "title": "Page 8: Joining Month Back-Calculation",
                "front": "If B invested for $t=7$ months in a 12-month year, after how many months did B join?",
                "back": "B joined after $12 - 7 = \\mathbf{5\\text{ months}}$!\nAlways subtract invested months from total year duration!",
                "badge": "\ud83d\udcc4 Page 8"
            }
        ],
        "questions": [
            {
                "text": "From Page 2 Notes: Ajay (8000, 6m), Vijay (4000, 8m), Jai (8000, 8m). Total gain is Rs. 4005. What is Vijay's share?",
                "options": [
                    "Rs. 890",
                    "Rs. 1335",
                    "Rs. 1780",
                    "Rs. 2000"
                ],
                "correct_option_index": 0,
                "explanation": "Page 2 Solution: PSR = 6 : 4 : 8 = 3 : 2 : 4 (Total 9 parts). Vijay share = (2/9) * 4005 = Rs. 890!"
            },
            {
                "text": "From Page 5 Notes: A & B invest 5000 & 8000. A gets 22% total profit for managing. Rest shared in capital ratio. A total share is Rs. 2028. Total profit?",
                "options": [
                    "Rs. 3000",
                    "Rs. 3500",
                    "Rs. 3900",
                    "Rs. 4200"
                ],
                "correct_option_index": 2,
                "explanation": "Page 5 Solution: A share = 22% + (5/13)*78% = 52% -> 2028. Total Profit (100%) = Rs. 3900!"
            },
            {
                "text": "From Page 8 Notes: A starts with Rs. 70,000. B joins with Rs. 60,000. Total 1-year profit ratio is 2:1. After how many months did B join?",
                "options": [
                    "4 months",
                    "5 months",
                    "6 months",
                    "7 months"
                ],
                "correct_option_index": 1,
                "explanation": "Page 8 Solution: (70000*12) / (60000*t) = 2/1 => t = 7 months invested. B joined after 12 - 7 = 5 months!"
            }
        ]
    },
    {
        "id": 9,
        "slug": "time-work",
        "name": "Time and Work",
        "description": "Master MDH formulas, men/women OR & AND shortcuts, LCM work parts, and alternate day cycles.",
        "icon": "\u23f3",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1 & 2: Proportionality Rules & MDH Formula\n- **Proportionality Laws**:\n  - $\\text{Time} \\propto \\text{Work}$ (Directly proportional)\n  - $\\text{Men} \\propto \\text{Work}$ (Directly proportional)\n  - $\\text{Time} \\propto \\frac{1}{\\text{Men}}$ (Inversely proportional)\n- **The Universal MDH Formula**:\n  $$\\frac{M_1 \\times D_1 \\times H_1}{W_1} = \\frac{M_2 \\times D_2 \\times H_2}{W_2}$$\n  - $M, D, H$ are inversely proportional to each other, $W$ (work/wages) is directly proportional.\n- **One Day Work & Efficiency**:\n  - If a person finishes work in $n$ days, 1 day work is $\\frac{1}{n}$.\n  - $\\text{Efficiency} = \\frac{\\text{Total Work}}{\\text{Time Taken}} \\implies \\text{Time} \\propto \\frac{1}{\\text{Efficiency}}$.\n- **Worked Example**: 24 men finish in 36 days. How many days for 54 men?\n  - $M_1 D_1 = M_2 D_2 \\implies 24 \\times 36 = 54 \\times D_2 \\implies D_2 = \\mathbf{16\\text{ Days}}$.\n\n#### Page 3 & 4: Book Binders, Cow Fodder, Wages & Middle Joining/Leaving\n- **18 Binders Example**: 18 binders bind 900 books in 10 days. How many binders for 660 books in 12 days?\n  - $\\frac{18 \\times 10}{900} = \\frac{M_2 \\times 12}{660} \\implies M_2 = \\mathbf{11\\text{ Binders}}$.\n- **Cow Fodder Stock**: 20 cows stock lasts 36 days. How long for 15 cows?\n  - $20 \\times 36 = 15 \\times D_2 \\implies D_2 = \\mathbf{48\\text{ Days}}$.\n- **Wages Example**: 6 men working 8 hrs/day earn Rs. 840/week. 9 men working 6 hrs/day earn how much?\n  - $\\frac{6 \\times 8}{840} = \\frac{9 \\times 6}{W_2} \\implies W_2 = \\mathbf{\\text{Rs. } 945}$.\n- **Middle Joining & Leaving Rule**: Equate equations by adding \"before\" and \"after\" situations.\n  - 16 men do job in 30 days. After 10 days, 6 men left (10 men remain).\n  - $16 \\times 30 = (16 \\times 10) + (10 \\times D_2) \\implies 480 = 160 + 10 D_2 \\implies D_2 = \\mathbf{32\\text{ Days}}$.\n\n#### Page 5 & 6: Updated Men Days & Men/Women OR/AND Rules\n- **12 Men 3 Days Join Example**: 12 men in 8 days. After 3 days, 3 men join (15 men).\n  - $12 \\times 8 = (12 \\times 3) + (15 \\times D_2) \\implies 96 = 36 + 15 D_2 \\implies D_2 = \\mathbf{4\\text{ Days}}$. Total $= 3 + 4 = \\mathbf{7\\text{ Days}}$.\n- **Men/Women OR & AND Questions**:\n  - 10 men OR 12 women in 16 days. How many days for 15 men AND 6 women together?\n  - $10\\text{M} = 12\\text{W} \\implies 5\\text{M} = 6\\text{W}$.\n  - $15\\text{M} + 6\\text{W} = 15\\text{M} + 5\\text{M} = 20\\text{M}$.\n  - $10 \\times 16 = 20 \\times D_2 \\implies D_2 = \\mathbf{8\\text{ Days}}$.\n- **Shortcut Formula for OR & AND**:\n  $$\\text{Days} = \\frac{\\text{Given Days}}{\\frac{q_m}{I_m} + \\frac{q_w}{I_w}} = \\frac{16}{\\frac{15}{10} + \\frac{6}{12}} = \\mathbf{8\\text{ Days}}!$$\n\n#### Page 7 & 8: Pure AND Equations & Two Workers Product Rule\n- **Pure AND Equations**: 2M + 3W in 8 days; 3M + 2W in 7 days. How long for 5M + 4W?\n  - $(2M + 3W) \\times 8 = (3M + 2W) \\times 7 \\implies 16M + 24W = 21M + 14W \\implies \\mathbf{1M = 2W}$.\n  - $7W \\to 8\\text{ days} \\implies 5M + 4W = 14W \\to \\mathbf{4\\text{ Days}}$.\n- **Two Workers Product/Sum Rule**:\n  - Together time $= \\mathbf{\\frac{xy}{x + y}}$.\n  - One worker remaining time $= \\mathbf{\\frac{xy}{|x - y|}}$.\n\n#### Page 9, 10 & 11: LCM Work Parts Method & Multi-Stage Workers\n- **LCM Method Logic**: LCM of individual days gives Total Work Parts. Efficiency $= \\frac{\\text{Total Parts}}{\\text{Days}}$.\n- **Worked Example**: A (25d), B (30d), C (10d). Total LCM $= 150$ parts. ($A=6, B=5, C=15$).\n  - All start. After 3 days A left ($57$ parts done). After 2 more days C left ($26$ parts done). Remaining $= 67$ parts.\n  - B finishes remaining in $\\frac{67}{3} = \\mathbf{22 \\frac{1}{3}\\text{ Days}}$.\n\n#### Page 12, 13 & 14: Alternate Days Cycle Rules & Assisted Days\n- **Alternate Days Cycle**: Work done in 2 days cycle $= A + B$. Leftover work done by whoever started!\n  - Example: A (36d), B (40d). Total $= 120$ parts ($A=4, B=3$). Cycle 2 days $= 7$ parts.\n  - $17 \\times 7 = 119$ parts in 34 days. Leftover 1 part by A $\\implies \\mathbf{34 \\frac{1}{4}\\text{ Days}}$ (If A starts).\n  - If B starts $\\implies \\mathbf{34 \\frac{1}{3}\\text{ Days}}$.\n- **Assisted Alternate Days**: A (20d), B (30d), C (40d). Total $= 120$ parts ($A=6, B=4, C=3$).\n  - Day 1 (A+B) $= 10$, Day 2 (A+C) $= 9$. 2 days $= 19$ parts.\n  - 6 cycles ($114$ parts) $= 12$ days. Leftover 6 parts by A+B $\\implies \\mathbf{12 \\frac{3}{5}\\text{ Days}}$.\n\n#### Page 15 & 16: Pairwise Together Trick & Efficiency Percentages\n- **Pairwise Together Trick**: A+B (12d), B+C (15d), A+C (20d). Total $= 60$ parts.\n  - $2(A+B+C) = 5+4+3 = 12 \\implies A+B+C = 6$ parts/day.\n  - All together $= \\frac{60}{6} = \\mathbf{10\\text{ Days}}$.\n- **Fraction Work**: $\\frac{3}{7}$th work in 24 days $\\implies$ Total $= 56$ days, Remaining $= \\mathbf{32\\text{ Days}}$.\n- **Efficiency Percentage**: B is $50\\%$ more efficient than A (60d).\n  - $100 \\times 60 = 150 \\times D_2 \\implies D_2 = \\mathbf{40\\text{ Days}}$.\n\n#### Page 17, 18, 19 & 20: Efficiency Change, Leaving at END & Work & Wages\n- **Efficiency Change Problem**: A & B finish in 5 days. If A works $2\\times$ and B works $\\frac{1}{3}\\times$, finished in 3 days.\n  - $(A+B) \\times 5 = (2A + \\frac{1}{3}B) \\times 3 \\implies A = 4B \\implies \\mathbf{A \\text{ alone } = 6 \\frac{1}{4}\\text{ Days}}$.\n- **Leaving BEFORE Completion (at the END)**:\n  - Calculate backwards for persons working alone in last days, subtract from Total Parts, then divide remainder by joint efficiency.\n  - Example: A (20d), B (30d). Total $= 60$ parts. B left 3 days before completion.\n  - A alone last 3 days $= 3 \\times 3 = 9$ parts. Remainder $= 51 / 5 = 10 \\frac{1}{5}$ days. Total $= \\mathbf{13 \\frac{1}{5}\\text{ Days}}$.\n- **Work & Wages Rule**: Total wages are divided in the **Daily Work Unit Ratio**!\n",
        "flashcards": [
            {
                "title": "Page 1: Universal MDH Formula",
                "front": "What is the Universal MDH formula in Time and Work?",
                "back": "$$\\frac{M_1 \\times D_1 \\times H_1}{W_1} = \\frac{M_2 \\times D_2 \\times H_2}{W_2}$$\n$M, D, H$ are inversely proportional, $W$ is directly proportional!",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 7: OR & AND Days Shortcut",
                "front": "What is the instant shortcut formula for 10 men OR 12 women in 16 days $\\to$ 15 men AND 6 women?",
                "back": "$$\\text{Days} = \\frac{\\text{Given Days}}{\\frac{q_m}{I_m} + \\frac{q_w}{I_w}} = \\frac{16}{\\frac{15}{10} + \\frac{6}{12}} = \\mathbf{8\\text{ Days}}!$$",
                "badge": "\ud83d\udcc4 Page 7"
            },
            {
                "title": "Page 8: Product/Sum Two Workers Rule",
                "front": "If A takes $x$ days and B takes $y$ days, what is the formula for working together vs finding one remaining?",
                "back": "\u2022 Together $= \\mathbf{\\frac{xy}{x + y}}$\n\u2022 One Remaining $= \\mathbf{\\frac{xy}{|x - y|}}$",
                "badge": "\ud83d\udcc4 Page 8"
            },
            {
                "title": "Page 15: Pairwise Together Shortcut",
                "front": "If A+B in 12d, B+C in 15d, A+C in 20d, how many days for A+B+C together?",
                "back": "Total $= 60$ parts. $2(A+B+C) = 5+4+3 = 12 \\implies A+B+C = 6$ parts/day.\nTogether $= \\frac{60}{6} = \\mathbf{10\\text{ Days}}$!",
                "badge": "\ud83d\udcc4 Page 15"
            },
            {
                "title": "Page 18: Leaving at END Rule",
                "front": "How do you solve questions where a person leaves a few days BEFORE completion?",
                "back": "Work BACKWARDS! Calculate the work done alone by remaining persons in the final days, subtract from total work, and divide rest by joint daily efficiency!",
                "badge": "\ud83d\udcc4 Page 18"
            },
            {
                "title": "Page 20: Work & Wages Division Rule",
                "front": "How are total wages divided among workers on a job?",
                "back": "Wages are ALWAYS divided in the ratio of their **DAILY WORK UNITS (Efficiency)**!",
                "badge": "\ud83d\udcc4 Page 20"
            }
        ],
        "questions": [
            {
                "text": "From Page 2 Notes: 24 men can do a piece of work in 36 days. In how many days can 54 men do it?",
                "options": [
                    "12 Days",
                    "16 Days",
                    "18 Days",
                    "20 Days"
                ],
                "correct_option_index": 1,
                "explanation": "Page 2 Solution: M1 * D1 = M2 * D2 => 24 * 36 = 54 * D2 => D2 = 16 Days!"
            },
            {
                "text": "From Page 7 Notes: 10 men or 12 women can do work in 16 days. How many days for 15 men and 6 women together?",
                "options": [
                    "6 Days",
                    "8 Days",
                    "10 Days",
                    "12 Days"
                ],
                "correct_option_index": 1,
                "explanation": "Page 7 Days Shortcut: 16 / (15/10 + 6/12) = 16 / (1.5 + 0.5) = 16 / 2 = 8 Days!"
            },
            {
                "text": "From Page 15 Notes: A+B can do work in 12 days, B+C in 15 days, A+C in 20 days. How many days for A+B+C together?",
                "options": [
                    "8 Days",
                    "10 Days",
                    "12 Days",
                    "15 Days"
                ],
                "correct_option_index": 1,
                "explanation": "Page 15 Solution: 2(A+B+C) daily parts = 5 + 4 + 3 = 12 => A+B+C daily = 6 parts => 60 / 6 = 10 Days!"
            },
            {
                "text": "From Page 16 Notes: B is 50% more efficient than A. If A can complete work in 60 days, in how many days can B complete it?",
                "options": [
                    "30 Days",
                    "40 Days",
                    "45 Days",
                    "50 Days"
                ],
                "correct_option_index": 1,
                "explanation": "Page 16 Solution: M1 * D1 = M2 * D2 => 100 * 60 = 150 * D2 => D2 = 40 Days!"
            }
        ]
    },
    {
        "id": 12,
        "slug": "speed-distance-time",
        "name": "Speed, Distance and Time",
        "description": "Master train crossing cases, relative speed, stoppage time formulas, and destination square root tricks.",
        "icon": "\ud83c\udfce\ufe0f",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1: Definitions & Unit Conversions\n- **Basic Formula**: $\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}$ (DST Triangle).\n- **Units Conversion Rules**:\n  - $\\text{km/h} \\to \\text{m/s}$: Multiply by $\\mathbf{\\frac{5}{18}}$.\n  - $\\text{m/s} \\to \\text{km/h}$: Multiply by $\\mathbf{\\frac{18}{5}}$.\n\n#### Page 2, 3 & 4: Train Crossing 4 Cases & Platform Lengths\n- **Case 1 (Standing Man/Pole)**: $\\text{Distance} = \\text{Length of Train}$, $\\text{Speed} = \\text{Train Speed}$.\n- **Case 2 (Platform/Bridge)**: $\\text{Distance} = \\text{Train Length} + \\text{Platform Length}$.\n- **Case 3 (Running Person)**:\n  - Same Direction: $\\text{Relative Speed} = \\text{Train Speed} - \\text{Person Speed}$.\n  - Opposite Direction: $\\text{Relative Speed} = \\text{Train Speed} + \\text{Person Speed}$.\n- **Case 4 (Two Trains)**: Distance is **ALWAYS SUMMED UP ($L_1 + L_2$)**!\n  - Opposite Direction: $\\text{Time} = \\frac{L_1 + L_2}{S_1 + S_2}$.\n  - Same Direction: $\\text{Time} = \\frac{L_1 + L_2}{|S_1 - S_2|}$.\n- **Two Platform Example**: Crosses $96\\text{m}$ platform in $12\\text{s}$ and $141\\text{m}$ platform in $15\\text{s}$.\n  - In $3\\text{s}$, covers $45\\text{m} \\implies \\text{Speed} = 15\\text{ m/s}$. Train Length $= (15 \\times 12) - 96 = \\mathbf{84\\text{ meters}}$.\n\n#### Page 5, 6, 7 & 8: Meeting Places & Different Start Times\n- **Hyd to Blr Meeting**: $560\\text{ km}$ apart, start at 6 AM ($80\\text{ kmph}$ & $60\\text{ kmph}$).\n  - Relative Speed $= 140\\text{ kmph} \\implies \\text{Time} = \\frac{560}{140} = \\mathbf{4\\text{ hours}}$ (10 AM).\n- **Different Start Times**: A and B $440\\text{ km}$ apart. P at 4 AM ($30\\text{ kmph}$), Q at 7 AM ($40\\text{ kmph}$).\n  - P covers $30 \\times 3 = 90\\text{ km}$ by 7 AM. Remaining $= 350\\text{ km}$.\n  - Relative Speed $= 70\\text{ kmph} \\implies \\text{Time} = \\frac{350}{70} = 5\\text{ hrs} \\implies$ Meet at **12:00 PM** ($240\\text{km}$ from A, $200\\text{km}$ from B).\n\n#### Page 9 & 10: Overtaking Pursuit & Average Speed LCM\n- **Same Direction Pursuit**: Rajdhani 14:30 ($60\\text{ kmph}$), Duronto 16:30 ($80\\text{ kmph}$).\n  - Lead $= 120\\text{ km}$. Relative $= 20\\text{ kmph} \\implies \\text{Overtake} = \\frac{120}{20} = 6\\text{ hrs} \\implies \\mathbf{480\\text{ km from Delhi}}$.\n- **Average Speed Formulas**:\n  - Equal Distances: $\\text{Average Speed} = \\mathbf{\\frac{2xy}{x + y}}$.\n  - General: $\\text{Average Speed} = \\frac{\\text{Total Distance}}{\\text{Total Time}}$.\n\n#### Page 11 & 12: Stoppage Time Formula & Walking vs Riding\n- **Train Stoppage Formula**: Excluding $= 40\\text{ kmph}$, Including $= 25\\text{ kmph}$.\n  $$\\text{Stoppage Time (min/hr)} = \\frac{\\text{Excluding} - \\text{Including}}{\\text{Excluding}} \\times 60 = \\frac{40 - 25}{40} \\times 60 = \\mathbf{22.5\\text{ minutes/hour}}$$\n- **Walking vs Riding Logic**: Walking + Riding $= 5\\text{h } 45\\text{m}$. Riding both ways saves 2 hrs.\n  - Walking both ways loses 2 hrs $\\implies 5\\text{h } 45\\text{m} + 2\\text{h} = \\mathbf{7\\text{ hours } 45\\text{ minutes}}$!\n\n#### Page 13, 14 & 15: Speed Inversion, Late/Early Distance & Destination Square Root\n- **Speed Ratio Inversion**: Walking at $\\frac{5}{6}$th usual speed, 10 mins late.\n  - Speed $5:6 \\implies$ Time $6:5 \\implies$ Diff $1 \\to 10\\text{m} \\implies$ Usual time $= 5 \\times 10 = \\mathbf{50\\text{ minutes}}$.\n- **Late & Early Distance Formula**: $30\\text{ kmph}$ (10m late) vs $40\\text{ kmph}$ (5m early).\n  $$\\text{Distance} = \\frac{S_1 \\times S_2}{|S_1 - S_2|} \\times \\frac{\\text{Time Diff (mins)}}{60} = \\frac{30 \\times 40}{10} \\times \\frac{15}{60} = \\mathbf{30\\text{ km}}$$\n- **Destination Square Root Formula**: Two trains meet, then reach destinations in $T_1 = 9\\text{h}, T_2 = 16\\text{h}$. $S_1 = 80\\text{ kmph}$.\n  $$\\frac{S_1}{S_2} = \\sqrt{\\frac{T_2}{T_1}} \\implies \\frac{80}{S_2} = \\sqrt{\\frac{16}{9}} = \\frac{4}{3} \\implies S_2 = \\mathbf{60\\text{ kmph}}$$\n\n#### Page 16, 17 & 18: Circular Track Crossings & Hourly Speed Increment\n- **Circular Track Crossing**: A (1 round/hr), B (6 rounds/hr) from 7:30 AM.\n  - Relative $= 5\\text{ RPH} \\implies \\text{Time} = \\frac{1}{5}\\text{ hr} = 12\\text{ mins} \\implies$ Cross at **7:42 AM**.\n- **Hourly Speed Arithmetic Series**: Starts $35\\text{ kmph}$, $+2\\text{ kmph}$ every hour for 12 hrs.\n  - $\\text{Total Distance} = (35 \\times 12) + (12 \\times 11) = 420 + 132 = \\mathbf{552\\text{ km}}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Unit Conversion Multipliers",
                "front": "What are the exact multipliers to convert km/h to m/s vs m/s to km/h?",
                "back": "\u2022 $\\text{km/h} \\to \\text{m/s}$: Multiply by $\\mathbf{\\frac{5}{18}}$\n\u2022 $\\text{m/s} \\to \\text{km/h}$: Multiply by $\\mathbf{\\frac{18}{5}}$",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 11: Train Stoppage Time Formula",
                "front": "What is the formula for train stoppage time in minutes per hour?",
                "back": "$$\\text{Stoppage Time (min/hr)} = \\frac{\\text{Excluding} - \\text{Including}}{\\text{Excluding}} \\times 60$$",
                "badge": "\ud83d\udcc4 Page 11"
            },
            {
                "title": "Page 14: Late & Early Distance Formula",
                "front": "What is the formula for distance when given 2 speeds with late and early arrival minutes?",
                "back": "$$\\text{Distance} = \\frac{S_1 \\times S_2}{|S_1 - S_2|} \\times \\frac{\\text{Time Diff (mins)}}{60}$$",
                "badge": "\ud83d\udcc4 Page 14"
            },
            {
                "title": "Page 15: Destination Square Root Formula",
                "front": "What is the formula comparing speeds of 2 trains after meeting until reaching destinations in $T_1$ and $T_2$?",
                "back": "$$\\frac{S_1}{S_2} = \\sqrt{\\frac{T_2}{T_1}}$$",
                "badge": "\ud83d\udcc4 Page 15"
            }
        ],
        "questions": [
            {
                "text": "From Page 11 Notes: Train excluding stoppages speed is 40 kmph, including stoppages is 25 kmph. How many minutes per hour does it stop?",
                "options": [
                    "15 min/hr",
                    "20 min/hr",
                    "22.5 min/hr",
                    "25 min/hr"
                ],
                "correct_option_index": 2,
                "explanation": "Page 11 Formula: ((40 - 25) / 40) * 60 = (15 / 40) * 60 = 22.5 min/hr!"
            },
            {
                "text": "From Page 14 Notes: A boy at 30 kmph is 10 mins late. At 40 kmph he is 5 mins early. What is the distance to school?",
                "options": [
                    "20 km",
                    "25 km",
                    "30 km",
                    "35 km"
                ],
                "correct_option_index": 2,
                "explanation": "Page 14 Formula: (30 * 40 / 10) * (15 / 60) = 120 * (1/4) = 30 km!"
            },
            {
                "text": "From Page 15 Notes: Two trains meet and reach destinations in 9 hrs and 16 hrs. If 1st train speed is 80 kmph, what is 2nd train speed?",
                "options": [
                    "50 kmph",
                    "60 kmph",
                    "70 kmph",
                    "75 kmph"
                ],
                "correct_option_index": 1,
                "explanation": "Page 15 Formula: S1 / S2 = sqrt(T2 / T1) => 80 / S2 = sqrt(16 / 9) = 4/3 => S2 = 60 kmph!"
            }
        ]
    },
    {
        "id": 12,
        "slug": "trains",
        "name": "Problems on Trains",
        "description": "Learn relative speed and object length crossing problems.",
        "icon": "\ud83d\ude86",
        "xp_reward": 110,
        "formula_sheet": "### \ud83d\udcc4 User PDF Complete Master Cheat Sheet: Trains\n\n> **[TODO: Paste your handwritten PDF text here]**",
        "questions": [
            {
                "difficulty": "intermediate",
                "text": "[TODO: Add Question Text]",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "[TODO: Add handwritten PDF explanation here]"
            }
        ],
        "flashcards": [
            {
                "title": "1. Problems on Trains Core Principle",
                "front": "What is the main formula for Problems on Trains?",
                "back": "Master core formulas and shortcut tricks for placement speed!",
                "badge": "\ud83d\udca1 Core Rule"
            }
        ]
    },
    {
        "id": 10,
        "slug": "boats-streams",
        "name": "Boats and Streams",
        "description": "Master downstream and upstream speeds, boat & stream formulas, round-trip distance, and factor substitution.",
        "icon": "\ud83d\udea4",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1: Core Definitions & Speed Formulas\n- **Water Flow Effect**: Water flow affects rowing speed.\n  - **Downstream Speed ($D$)**: $\\text{Boat Speed} + \\text{Stream Speed} = x + y$.\n  - **Upstream Speed ($U$)**: $\\text{Boat Speed} - \\text{Stream Speed} = x - y$.\n- **Speed Formulas when $D$ and $U$ are given**:\n  $$\\text{Boat Speed in Still Water } (x) = \\frac{D + U}{2}$$\n  $$\\text{Stream / Current Speed } (y) = \\frac{D - U}{2}$$\n- **Worked Example 1**: Person rows at $8\\text{ kmph}$ in still water, takes 8 hours round trip. Stream speed $= 2\\text{ kmph}$. Find distance between A and B.\n  - Upstream $= 8 - 2 = 6\\text{ kmph}$, Downstream $= 8 + 2 = 10\\text{ kmph}$.\n\n#### Page 2 & 3: Round-Trip Distance Formula & Factor Substitution\n- **Round-Trip Distance Formula**:\n  $$\\text{Distance} = \\frac{\\text{Product of Speeds}}{\\text{Sum of Speeds}} \\times \\text{Total Time} = \\frac{6 \\times 10}{6 + 10} \\times 8 = \\mathbf{30\\text{ km}}$$\n- **Factor Substitution Method**: 40km U + 55km D in 13h; 30km U + 44km D in 10h.\n  - Factor trial: $D = 11\\text{ kmph} \\implies \\frac{55}{11} = 5\\text{h} \\implies U = \\frac{40}{13 - 5} = 5\\text{ kmph}$.\n  - Verify Eq 2: $\\frac{30}{5} + \\frac{44}{11} = 6 + 4 = 10\\text{h}$ (Verified!).\n  - Boat Speed $(x) = \\frac{11 + 5}{2} = \\mathbf{8\\text{ kmph}}$.\n  - Stream Speed $(y) = \\frac{11 - 5}{2} = \\mathbf{3\\text{ kmph}}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Boat & Stream Speed Formulas",
                "front": "What are the formulas for Boat Speed in Still Water ($x$) and Stream Speed ($y$) when $D$ and $U$ are given?",
                "back": "\u2022 Boat Speed $(x) = \\frac{D + U}{2}$\n\u2022 Stream Speed $(y) = \\frac{D - U}{2}$",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 2: Round-Trip Distance Formula",
                "front": "What is the formula for distance when upstream and downstream speeds are given along with total round-trip time?",
                "back": "$$\\text{Distance} = \\frac{\\text{Product of Speeds}}{\\text{Sum of Speeds}} \\times \\text{Total Time}$$",
                "badge": "\ud83d\udcc4 Page 2"
            }
        ],
        "questions": [
            {
                "text": "From Page 1 Notes: A boat travels at 8 kmph in still water and stream speed is 2 kmph. What are downstream and upstream speeds?",
                "options": [
                    "10 kmph & 6 kmph",
                    "12 kmph & 4 kmph",
                    "8 kmph & 2 kmph",
                    "16 kmph & 4 kmph"
                ],
                "correct_option_index": 0,
                "explanation": "Page 1 Formulas: Downstream = 8 + 2 = 10 kmph, Upstream = 8 - 2 = 6 kmph!"
            },
            {
                "text": "From Page 2 Notes: If upstream speed is 6 kmph, downstream is 10 kmph, and total round-trip time is 8 hours, what is the distance?",
                "options": [
                    "24 km",
                    "30 km",
                    "36 km",
                    "40 km"
                ],
                "correct_option_index": 1,
                "explanation": "Page 2 Distance Formula: (6 * 10 / 16) * 8 = 30 km!"
            }
        ]
    },
    {
        "id": 11,
        "slug": "pipes-cisterns",
        "name": "Pipes and Cisterns",
        "description": "Master filling and emptying units, multi-pipe LCM partitioning, and alternate minute buffer rules.",
        "icon": "\ud83d\udeb0",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1: Time & Work Extension & Core Formulas\n- **Core Principle**: Pipes and Cisterns are an extension of Time and Work.\n  - BUT here, there is an element of **DESTROYING THE WORK** (i.e. sometimes pipes will be filling and simultaneously emptying!).\n- **Core Formulas**:\n  - (i) When both A and B are **Filling**:\n    $$\\text{Total Time} = \\mathbf{\\frac{xy}{x + y}}$$\n  - (ii) When one is **Filling** ($x$) and one is **Emptying** ($y$):\n    $$\\text{Total Time} = \\mathbf{\\frac{xy}{|x - y|}}$$\n\n#### Page 2 & 3: Negative Emptying Units & Pipe Closing Rules\n- **Negative Units Principle**: Entities responsible for **emptying are taken as NEGATIVE (-ve)**!\n  - Process uses LCM partitioning into total work units.\n- **Multi-Pipe Worked Example**: Pipe A (25m fill $+6$), Pipe B (30m fill $+5$), Pipe C (50m empty $-3$). Total $= 150$ units.\n  - All opened simultaneously. After 7 mins, A closed ($8 \\times 7 = 56$ units done).\n  - After 4 more mins, C closed ($(5 - 3) \\times 4 = 8$ units done).\n  - Total filled $= 64$ units. Remaining $= 86$ units.\n  - B fills remaining in $\\frac{86}{5} = \\mathbf{17 \\frac{1}{5}\\text{ mins}}$!\n- **Tank Never Filled Rules**:\n  - If all filling pipes are closed BEFORE the tank gets filled, the tank will **NEVER get filled**!\n  - In such cases, time taken to **EMPTY** the tank is calculated ONLY from the units filled up to that point.\n  - If emptying rate is greater than filling rate, the tank will also **NEVER get filled**!\n\n#### Page 4 & 5: Alternate Minutes Highest-Unit Buffer & Target Closure Time\n- **Alternate Minutes Cycle & Buffer Rule**:\n  - A (20m fill $+6$), B (30m fill $+4$), C (40m empty $-3$). Total $= 120$ units.\n  - Cycle $A \\to B \\to C$: 3 minutes $= 6 + 4 - 3 = 7$ units.\n  - **CRITICAL HANDWRITTEN RULE**: Unlike Time & Work, HERE we stop nearest to total capacity by maintaining a **minimum difference equal to the HIGHEST filling unit** (+6) to prevent overflow before emptying!\n  - 16 cycles ($7 \\times 16 = 112$ units) $= 48$ minutes.\n  - Next 1 min (A opened, $+6$) $= 118$ units in 49 mins.\n  - Next B opened (needs 2 out of 4) $= \\frac{2}{4} = \\frac{1}{2}$ min.\n  - Total time to fill $= \\mathbf{49 \\frac{1}{2}\\text{ minutes}}$!\n- **Target Closure Time Problem**: Pipe A (24m fill), Pipe B (32m fill). Tank must fill in 18 mins. When to close B?\n  - Total $= 96$ units. $A = 4$ units/min, $B = 3$ units/min.\n  - A works all 18 mins $\\implies 4 \\times 18 = 72$ units.\n  - Remaining for B $= 96 - 72 = 24$ units.\n  - Time for B $= \\frac{24}{3} = \\mathbf{8\\text{ minutes}}$. Close B after 8 minutes!\n",
        "flashcards": [
            {
                "title": "Page 1: Destruction of Work Element",
                "front": "What is the key difference between Time & Work and Pipes & Cisterns?",
                "back": "Pipes & Cisterns introduces the element of **DESTROYING THE WORK** (Emptying pipes)!\nEmptying pipes are assigned **negative (-ve)** work units!",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 1: One Fill & One Empty Formula",
                "front": "What is the formula for total time when Pipe A fills in $x$ mins and Pipe B empties in $y$ mins?",
                "back": "$$\\text{Total Time} = \\mathbf{\\frac{xy}{|x - y|}}$$",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 3: Tank Never Filled Rule",
                "front": "What happens if all filling pipes are closed before the tank is completely full?",
                "back": "The tank will **NEVER GET FILLED**!\nThe time taken to EMPTY the tank is calculated ONLY from the work units filled up to that point!",
                "badge": "\ud83d\udcc4 Page 3"
            },
            {
                "title": "Page 4: Alternate Minutes Buffer Rule",
                "front": "Why do we maintain a buffer equal to the highest filling unit in alternate minute cycles?",
                "back": "To prevent calculating cycles past 100% capacity! The tank fills on a positive inlet minute BEFORE the negative outlet pipe turns on!",
                "badge": "\ud83d\udcc4 Page 4"
            },
            {
                "title": "Page 5: Target Tank Fill Timing",
                "front": "Pipes A (24m) and B (32m) open. Tank must fill in 18 mins. When should B be closed?",
                "back": "A works all 18 mins $\\to 4 \\times 18 = 72$ units. Remaining $96 - 72 = 24$ units.\nTime for B $= \\frac{24}{3} = \\mathbf{8\\text{ minutes}}$!",
                "badge": "\ud83d\udcc4 Page 5"
            }
        ],
        "questions": [
            {
                "text": "From Page 1 Notes: Pipe A fills a tank in 20 mins and Pipe B empties it in 30 mins. How long to fill the tank together?",
                "options": [
                    "50 mins",
                    "60 mins",
                    "12 mins",
                    "40 mins"
                ],
                "correct_option_index": 1,
                "explanation": "Page 1 Formula: Total Time = (x * y) / |x - y| = (20 * 30) / (30 - 20) = 600 / 10 = 60 mins!"
            },
            {
                "text": "From Page 5 Notes: Pipe A fills in 24 mins and B in 32 mins. If tank fills in 18 mins, after how many minutes should B be closed?",
                "options": [
                    "6 mins",
                    "8 mins",
                    "10 mins",
                    "12 mins"
                ],
                "correct_option_index": 1,
                "explanation": "Page 5 Solution: A works 18 mins = 72 units out of 96. B does 24 units = 24 / 3 = 8 mins!"
            },
            {
                "text": "From Page 4 Notes: In alternate minute cycle A (+6), B (+4), C (-3), 7 units fill in 3 mins. For 120 units, why do we stop near 112 units?",
                "options": [
                    "To save time",
                    "Because C is closed",
                    "To maintain highest unit (+6) buffer before full tank",
                    "Due to leak"
                ],
                "correct_option_index": 2,
                "explanation": "Page 4 Rule: We maintain a buffer equal to the highest filling unit (+6) so positive inlet fills tank without overshooting into emptying cycles!"
            }
        ]
    },
    {
        "id": 13,
        "slug": "permutations-combinations",
        "name": "Permutations & Combinations",
        "description": "Master arrangements vs selections, nPr & nCr identities, Gap Method, circular rules, and polygon diagonals.",
        "icon": "\ud83c\udfb2",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1 & 2: Arrangements vs Selection & Key Identities\n- **Core Distinction**:\n  - **Permutation ($n P_r$)**: Arrangements (Position matters!). Multiply $r$ numbers from $n$ downwards.\n  - **Combination ($n C_r$)**: Selection (Just choosing!). Multiply $r$ numbers from $n$ downwards and divide by $r!$.\n- **Key Relation**:\n  $$n P_r = n C_r \\times r!$$\n- **Important Identities**:\n  - $n P_n = n!$, $n P_{n-1} = n!$, $n P_1 = n$, $n P_0 = 1$.\n  - $n C_r = n C_{n-r}$, $n C_n = n C_0 = 1$, $n C_1 = n$, $n C_{n-1} = n$.\n- **Identical Objects Rule**:\n  - Words with repeated letters (e.g. `BALLOON`: 7 letters, 2 Ls, 2 Os) $\\implies \\frac{7!}{2! 2!} = \\mathbf{1260}$.\n\n#### Page 3, 4 & 5: Vowels Together, GAP Method & Sitting Line\n- **Vowels Always Together (`TENDULKAR`)**:\n  - 9 letters, 3 vowels (`E, U, A`). Treat vowels as **single unit** $(EUA) \\implies (6 + 1) = 7$ units.\n  - Ways $= 7! \\times 3! = 5040 \\times 6 = \\mathbf{30,240}$.\n- **Vowels Never Together (GAP METHOD)**:\n  - Used when \"No two elements are together\".\n  - $\\text{Not Together} = \\text{Total} - \\text{Together}$.\n  - 3 boys and 2 girls (girls not together): Arrange boys ($3! = 6$), create 4 gaps `_ B _ B _ B _`, place girls ($4 C_2 \\times 2! = 12$).\n  - Total $= 6 \\times 6 = \\mathbf{36\\text{ ways}}$.\n  - `TENDULKAR` vowels never together: 6 consonants ($6! = 720$), 7 gaps for 3 vowels ($7 P_3 = 210$) $\\implies 720 \\times 210 = \\mathbf{151,200}$.\n\n#### Page 6 & 7: Circular Permutations & Number Formation Rules\n- **Circular Permutations**:\n  - Normal Circle $= (n - 1)!$.\n  - Necklace / Chain (clockwise = anticlockwise same) $= \\mathbf{\\frac{(n - 1)!}{2}}$.\n- **Number Formation Rules (3-Digit Numbers)**:\n  - Without Repetition, No Zero $\\{1,2,3,4,5\\} \\implies 5 P_3 = \\mathbf{60}$.\n  - Without Repetition, With Zero $\\{0,1,2,3,4\\} \\implies 1^{\\text{st}}$ digit 4 choices (no 0) $\\implies 4 \\times 4 \\times 3 = \\mathbf{48}$.\n  - With Repetition, No Zero $\\{1,2,3,4,5\\} \\implies 5^3 = \\mathbf{125}$.\n  - With Repetition, With Zero $\\{0,1,2,3,4\\} \\implies 4 \\times 5 \\times 5 = \\mathbf{100}$.\n- **4-Digit ATM PINs**: Total possible $= 10^4 = \\mathbf{10,000}$.\n\n#### Page 8, 9 & 10: Committee Selection & Polygon Diagonals\n- **At Least Committee Problem**: 5 men, 4 women. Committee of 5 members with **at least 2 women**:\n  - $(4 C_2 \\times 5 C_3) + (4 C_3 \\times 5 C_2) + (4 C_4 \\times 5 C_1) = 60 + 40 + 5 = \\mathbf{105\\text{ ways}}$.\n- **Octagon Triangles**: Vertices of Octagon ($n=8$) $\\implies 8 C_3 = \\mathbf{56\\text{ triangles}}$.\n- **Polygon Diagonals Formula**:\n  $$\\text{Number of Diagonals} = \\mathbf{\\frac{n(n - 3)}{2}}$$\n  - Hexagon ($n=6$) $\\implies \\frac{6(3)}{2} = \\mathbf{9\\text{ diagonals}}$.\n- **Inviting Friends**: Invite 1 or more of 6 friends $\\implies 2^n - 1 = 2^6 - 1 = \\mathbf{63\\text{ ways}}$.\n\n#### Page 11, 12 & 13: Handshakes vs Tickets & Tournament Matches\n- **Handshakes vs Tickets Distinction**:\n  - **Handshakes & Matches** (Order doesn't matter) $\\implies n C_2$. (Example: 20 people handshakes $= 20 C_2 = \\mathbf{190}$).\n  - **Gifts & Railway Tickets** (Order matters!) $\\implies n P_2$. (Example: 22 stations tickets $= 22 P_2 = 22 \\times 21 = \\mathbf{462}$).\n- **Cricket Tournament Matches**: 20 teams divided into 2 groups of 10.\n  - Group matches $= 10 C_2 + 10 C_2 = 45 + 45 = 90$.\n  - Knockouts $= 4 \\text{ (Quarters)} + 2 \\text{ (Semis)} + 1 \\text{ (Final)} = 7$. Total $= \\mathbf{97\\text{ matches}}$.\n- **Chess Tournament Participants**: $n C_2 = 325 \\implies \\frac{n(n - 1)}{2} = 325 \\implies n(n - 1) = 650 = 26 \\times 25 \\implies \\mathbf{n = 26\\text{ participants}}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Key nPr & nCr Relation",
                "front": "What is the key relation connecting Permutation ($n P_r$) and Combination ($n C_r$)?",
                "back": "$$n P_r = n C_r \\times r!$$\nPermutation includes arranging the selected items in $r!$ order!",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 4: GAP Method for Separation",
                "front": "When do you use the GAP METHOD in Permutations?",
                "back": "Use when **NO TWO elements are allowed together**!\nArrange unrestricted items first, create gaps `_ B _ B _`, then place restricted items in gaps!",
                "badge": "\ud83d\udcc4 Page 4"
            },
            {
                "title": "Page 10: Polygon Diagonals Formula",
                "front": "What is the formula for the number of diagonals in an $n$-sided polygon?",
                "back": "$$\\text{Number of Diagonals} = \\mathbf{\\frac{n(n - 3)}{2}}$$\nExample: Hexagon ($n=6$) $\\implies \\frac{6 \\times 3}{2} = \\mathbf{9\\text{ diagonals}}$!",
                "badge": "\ud83d\udcc4 Page 10"
            },
            {
                "title": "Page 12: Handshakes vs Tickets Rule",
                "front": "Why are Handshakes calculated using $n C_2$ while Railway Tickets use $n P_2$?",
                "back": "\u2022 Handshakes: Order DOES NOT matter (A shaking B is same as B shaking A) $\\implies n C_2$.\n\u2022 Railway Tickets: Order MATTERS (Ticket A to B is different from B to A) $\\implies n P_2$!",
                "badge": "\ud83d\udcc4 Page 12"
            }
        ],
        "questions": [
            {
                "text": "From Page 10 Notes: How many diagonals can be formed in a Hexagon (6 sides)?",
                "options": [
                    "6",
                    "9",
                    "12",
                    "15"
                ],
                "correct_option_index": 1,
                "explanation": "Page 10 Formula: Diagonals = n(n-3)/2 = 6*(6-3)/2 = 9!"
            },
            {
                "text": "From Page 11 Notes: 20 members attend a party. If everyone shakes hands with every other person once, how many handshakes occur?",
                "options": [
                    "180",
                    "190",
                    "380",
                    "400"
                ],
                "correct_option_index": 1,
                "explanation": "Page 11 Formula: nC2 = 20C2 = (20 * 19) / 2 = 190 handshakes!"
            },
            {
                "text": "From Page 13 Notes: In a chess tournament, every player plays 1 match with every other. Total matches played = 325. How many participants?",
                "options": [
                    "24",
                    "25",
                    "26",
                    "30"
                ],
                "correct_option_index": 2,
                "explanation": "Page 13 Solution: nC2 = 325 => n(n-1) = 650 = 26 * 25 => n = 26 participants!"
            }
        ]
    },
    {
        "id": 14,
        "slug": "probability",
        "name": "Probability",
        "description": "Master favourable/total outcomes, coin toss formulas, dice sum tables, 52 cards breakdown, and contradiction %.",
        "icon": "\ud83c\udfaf",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1 & 2: Core Definition, Prime Benchmarks & Complement Rule\n- **Basic Formula**:\n  $$\\text{Probability } P(E) = \\frac{\\text{Favourable Outcomes}}{\\text{Total Outcomes}} = \\frac{\\text{Our Selections}}{\\text{Total Selections}}$$\n- **Range of Probability**:\n  - $0 = \\text{Impossible Event}$\n  - $1 = \\text{Certain Event}$\n  - $0 \\le P \\le 1 \\implies \\text{Possible Event}$\n- **Non-Leap Year 53 Sundays**: 365 days $= 52\\text{ wks} + 1\\text{ day} \\implies \\mathbf{\\frac{1}{7}}$.\n- **Prime Numbers Count Benchmarks**:\n  - 1 to 10 $\\to 4$ primes | 1 to 20 $\\to 8$ primes | 1 to 30 $\\to 10$ primes | 1 to 100 $\\to 25$ primes.\n  - Probability of selecting 2 primes from 1 to 100: $\\frac{25 C_2}{100 C_2} = \\frac{300}{4950} = \\mathbf{\\frac{2}{33}}$.\n- **Complement & Set Rules**:\n  - **Complement Rule**: $P(\\text{not } E) = 1 - P(E)$ (Used for \"**At least one**\"!).\n  - **Addition Rule (OR)**: $P(A \\text{ or } B) = P(A) + P(B)$ (Mutually Exclusive).\n  - **Multiplication Rule (AND)**: $P(A \\text{ and } B) = P(A) \\times P(B)$ (Independent).\n\n#### Page 3, 4 & 5: Ball Picking Complement & Coin Formulas\n- **At Least 1 Red Ball Complement Trick**: 8 Red, 4 Green balls, 3 picked.\n  $$\\text{Prob} = 1 - P(\\text{No Red Ball}) = 1 - \\frac{4 C_3}{12 C_3} = 1 - \\frac{4}{220} = \\mathbf{\\frac{54}{55}}$$\n- **Coins Probability Formulas**:\n  - Total outcomes for $n$ coins $= 2^n$.\n  - **Exactly $r$ Heads Formula**:\n    $$\\text{Probability} = \\mathbf{\\frac{n C_r}{2^n}}$$\n    Example: 5 coins, exactly 3 Heads $\\implies \\frac{5 C_3}{2^5} = \\mathbf{\\frac{10}{32} = \\frac{5}{16}}$.\n  - 8 coins, at least 6 Heads $\\implies \\frac{8 C_6 + 8 C_7 + 8 C_8}{2^8} = \\frac{28 + 8 + 1}{256} = \\mathbf{\\frac{37}{256}}$.\n  - 5 coins, at most 2 Heads $\\implies \\frac{5 C_2 + 5 C_1 + 5 C_0}{2^5} = \\frac{16}{32} = \\mathbf{\\frac{1}{2}}$.\n\n#### Page 6: Dice Sum Tables & Even Product Shortcut\n- **Even Product Shortcut**:\n  $$\\text{Even Product Probability} = \\mathbf{\\frac{2^n - 1}{2^n}}$$\n- **2 Dice Sum Table (Total 36)**:\n  | Sum | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |\n  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n  | Ways | 1 | 2 | 3 | 4 | 5 | 6 | 5 | 4 | 3 | 2 | 1 |\n- **3 Dice Sum Table (Total 216)**:\n  | Sum | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |\n  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n  | Ways | 1 | 3 | 6 | 10 | 15 | 21 | 25 | 27 | 27 | 25 | 21 | 15 | 10 | 6 | 3 | 1 |\n\n#### Page 7, 8 & 9: Cards Anatomy & Card Draw Examples\n- **52 Cards Breakdown**: 26 Red (13 Diamond, 13 Heart), 26 Black (13 Spade, 13 Club).\n  - 16 Face/Honour Cards: 4 Kings, 4 Queens, 4 Jacks, 4 Aces. 36 Non-face cards (2 to 10).\n- **Single Card Examples**:\n  - Diamond OR King $\\implies \\frac{13 + 4 - 1}{52} = \\mathbf{\\frac{4}{13}}$.\n- **Two Cards Examples**:\n  - Both Aces $\\implies \\frac{4 C_2}{52 C_2} = \\mathbf{\\frac{1}{221}}$.\n  - At least one King $\\implies 1 - \\frac{48 C_2}{52 C_2} = 1 - \\frac{188}{221} = \\mathbf{\\frac{33}{221}}$.\n  - One King & One Queen $\\implies \\frac{4 C_1 \\times 4 C_1}{52 C_2} = \\mathbf{\\frac{8}{663}}$.\n\n#### Page 11, 12 & 13: Interview Selection, Contradiction % & Problem Solving\n- **Wife & Husband Interview**: Wife $1/4$, Husband $1/6$.\n  - None selected $= \\frac{3}{4} \\times \\frac{5}{6} = \\mathbf{\\frac{5}{8}}$.\n  - Exactly one selected $= (1/4 \\times 5/6) + (3/4 \\times 1/6) = \\mathbf{\\frac{1}{3}}$.\n  - At least one selected $= 1 - 5/8 = \\mathbf{\\frac{3}{8}}$.\n- **Contradiction Percentage**: A speaks truth $60\\%$, B speaks truth $45\\%$.\n  - $\\text{Contradict} = (T_A \\times F_B) + (F_A \\times T_B) = (0.60 \\times 0.55) + (0.40 \\times 0.45) = 0.33 + 0.18 = \\mathbf{51\\%}$!\n- **3-Student Problem Solving**: A ($1/2$), B ($1/3$), C ($1/4$).\n  - $\\text{Problem Solved} = 1 - P(\\text{None Solve}) = 1 - (1/2 \\times 2/3 \\times 3/4) = 1 - 1/4 = \\mathbf{\\frac{3}{4}}$.\n",
        "flashcards": [
            {
                "title": "Page 1: Non-Leap Year 53 Sundays",
                "front": "What is the probability of having 53 Sundays in a non-leap year?",
                "back": "365 days $= 52\\text{ weeks} + 1\\text{ extra day}$.\nThat 1 day can be any of 7 days $\\implies \\mathbf{\\frac{1}{7}}$!",
                "badge": "\ud83d\udcc4 Page 1"
            },
            {
                "title": "Page 4: Exactly r Heads Coin Formula",
                "front": "What is the formula for probability of getting exactly $r$ Heads when $n$ coins are tossed?",
                "back": "$$\\text{Probability} = \\mathbf{\\frac{n C_r}{2^n}}$$",
                "badge": "\ud83d\udcc4 Page 4"
            },
            {
                "title": "Page 6: 2 Dice Sum Table Shortcut",
                "front": "What are the number of ways to get a sum of 7 vs sum of 10 when 2 dice are rolled?",
                "back": "\u2022 Sum of 7 $\\implies \\mathbf{6\\text{ ways}}$ (Highest!)\n\u2022 Sum of 10 $\\implies \\mathbf{3\\text{ ways}}$",
                "badge": "\ud83d\udcc4 Page 6"
            },
            {
                "title": "Page 12: Truth Contradiction Formula",
                "front": "If A speaks truth in 60% cases and B in 45% cases, what is the contradiction %?",
                "back": "$\\text{Contradict} = (T_A \\times F_B) + (F_A \\times T_B) = (0.60 \\times 0.55) + (0.40 \\times 0.45) = 0.33 + 0.18 = \\mathbf{51\\%}$!",
                "badge": "\ud83d\udcc4 Page 12"
            }
        ],
        "questions": [
            {
                "text": "From Page 1 Notes: What is the probability of having 53 Sundays in a non-leap year?",
                "options": [
                    "1/7",
                    "2/7",
                    "52/365",
                    "1/52"
                ],
                "correct_option_index": 0,
                "explanation": "Page 1 Solution: 365 days = 52 weeks + 1 day. That 1 extra day has a 1/7 probability of being a Sunday!"
            },
            {
                "text": "From Page 4 Notes: 5 coins are tossed. What is the probability of getting exactly 3 Heads?",
                "options": [
                    "3/16",
                    "5/16",
                    "1/2",
                    "5/32"
                ],
                "correct_option_index": 1,
                "explanation": "Page 4 Formula: 5C3 / 2^5 = 10 / 32 = 5/16!"
            },
            {
                "text": "From Page 12 Notes: A speaks truth in 60% cases and B in 45% cases. In what % of cases do they contradict each other?",
                "options": [
                    "45%",
                    "50%",
                    "51%",
                    "55%"
                ],
                "correct_option_index": 2,
                "explanation": "Page 12 Solution: Contradict = (0.60 * 0.55) + (0.40 * 0.45) = 0.33 + 0.18 = 51%!"
            }
        ]
    },
    {
        "id": 15,
        "slug": "mensuration",
        "name": "Mensuration 2D & 3D",
        "description": "Master 2D & 3D shape formulas, ratio squaring/cubing rules, surface area to volume transformations, and water level rise.",
        "icon": "\ud83d\udcd0",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Comprehensive Concept & Formula Deck\n\n#### Page 1, 2 & 3: 2D Geometry Shapes & Formulas\n- **Square**: Perimeter $= 4a$, Area $= a^2$, Diagonal $= a\\sqrt{2}$. All sides equal, angles $90^\\circ$.\n- **Rectangle**: Perimeter $= 2(l + b)$, Area $= l \\times b$, Diagonal $= \\sqrt{l^2 + b^2}$.\n- **Rhombus**: Perimeter $= 4a$, Area $= \\frac{1}{2} d_1 d_2$.\n- **Circle**: Circumference $= 2\\pi r$, Area $= \\pi r^2$, Diameter $= 2r$ ($\\pi = \\frac{22}{7}$ or $3.14$).\n- **Equilateral Triangle**: Perimeter $= 3a$, Area $= \\frac{\\sqrt{3}}{4} a^2$, Height $= \\frac{\\sqrt{3}}{2} a$.\n- **Right-Angled Triangle**: Area $= \\frac{1}{2} b h$, Hypotenuse $= \\sqrt{AB^2 + BC^2}$ (Pythagoras).\n- **Heron's Formula (Triangle $a,b,c$)**: Area $= \\sqrt{s(s-a)(s-b)(s-c)}$ where $s = \\frac{a+b+c}{2}$.\n\n#### Page 3, 4 & 5: 3D Solid Geometry Shapes & Formulas\n- **Cube**: $\\text{LSA} = 4a^2$, $\\text{TSA} = 6a^2$, $\\text{Volume} = a^3$, $\\text{Diagonal} = a\\sqrt{3}$.\n- **Cuboid**: $\\text{LSA} = 2(l+b)h$, $\\text{TSA} = 2(lb+bh+hl)$, $\\text{Volume} = lbh$, $\\text{Diagonal} = \\sqrt{l^2+b^2+h^2}$.\n- **Sphere**: $\\text{TSA} = 4\\pi r^2$, $\\text{Volume} = \\frac{4}{3} \\pi r^3$.\n- **Hemisphere**: $\\text{CSA} = 2\\pi r^2$, $\\text{TSA} = 3\\pi r^2$, $\\text{Volume} = \\frac{2}{3} \\pi r^3$.\n- **Cylinder**: $\\text{CSA} = 2\\pi rh$, $\\text{TSA} = 2\\pi r(r+h)$, $\\text{Volume} = \\pi r^2 h$.\n- **Cone**: Slant height $l = \\sqrt{r^2+h^2}$, $\\text{Volume} = \\frac{1}{3} \\pi r^2 h$, $\\text{CSA} = \\pi rl$, $\\text{TSA} = \\pi r(r+l)$.\n\n#### Page 5, 6, 7 & 8: Ratio Transformation Rules (2D & 3D)\n- **2D Ratio Rules**:\n  - Sides Ratio $\\to$ Areas Ratio: **Square the ratios individually** ($19:17 \\implies 19^2:17^2 = 361:289$).\n  - Areas Ratio $\\to$ Sides Ratio: **Square root the ratios individually** ($256:169 \\implies 16:13$).\n- **3D Ratio Rules**:\n  - Sides Ratio $\\to$ Volumes Ratio: **Cube the ratios individually** ($9:7 \\implies 729:343$).\n  - Volumes Ratio $\\to$ Sides Ratio: **Cube root the ratios individually** ($1331:1728 \\implies 11:12$).\n- **Surface Area to Volume Double Transformation**:\n  - Area Ratio $36:121 \\implies$ Side Ratio $\\sqrt{36:121} = 6:11 \\implies$ Volume Ratio $6^3:11^3 = \\mathbf{216:1331}$!\n  - Volume Ratio $125:729 \\implies$ Side Ratio $\\sqrt[3]{125:729} = 5:9 \\implies$ Area Ratio $5^2:9^2 = \\mathbf{25:81}$!\n\n#### Page 9 & 10: Percentage Change Operations Count\n- **Operations Count Rule**:\n  - Units (Perimeter) $\\implies$ Perform **ONE** operation ($20\\% \\downarrow \\implies \\mathbf{20\\% \\downarrow}$).\n  - Sq units (Area) $\\implies$ Perform **TWO** operations ($20\\% \\downarrow 20\\% \\downarrow \\implies -20 - 20 + 4 = \\mathbf{36\\% \\downarrow}$).\n  - Cubic units (Volume) $\\implies$ Perform **THREE** operations ($+10\\%, +20\\%, -25\\% \\implies 32\\% - 25\\% - 8\\% = \\mathbf{1\\% \\downarrow}$).\n\n#### Page 11 to 20: 2D Worked Problems & Special Figures\n- **Circle & Wire Bending**: Wire enclosing $484\\text{m}^2$ square ($a=22$, Perimeter $= 88$) bent into circle $\\implies 2\\pi r = 88 \\implies r = 14 \\implies \\text{Area} = \\mathbf{616\\text{ m}^2}$.\n- **Cyclic Rhombus**: A cyclic Rhombus is a **Square**! Side $= 9\\text{cm} \\implies \\text{Area} = 9 \\times 9 = \\mathbf{81\\text{ cm}^2}$.\n- **Trapezium Area**: $\\text{Area} = \\frac{1}{2} (a+b) h = \\text{Avg} \\times h$.\n- **Wheel Revolutions**: $\\text{Revolutions} = \\frac{\\text{Total Distance}}{\\text{Circumference}} = \\frac{9240}{\\pi \\times 42} = \\mathbf{70\\text{ Revolutions}}$.\n- **Sector & Arc Length**: Sector Area $= \\frac{\\pi r^2 \\theta}{360} = \\mathbf{102.66\\text{ cm}^2}$, Arc Length $= \\frac{2\\pi r \\theta}{360} = \\mathbf{14.66\\text{ cm}}$.\n- **Cow Ungrazed Field**: Square field $30\\text{m}$, rope $14\\text{m} \\implies 30^2 - (\\pi \\times 14^2 \\times \\frac{90}{360}) = 900 - 154 = \\mathbf{746\\text{ sq. mts}}$.\n- **Cross Roads Gravelling**: Lawn $60 \\times 40$, 2 roads $5\\text{m}$ wide $\\implies 300 + 200 - 25 = 475\\text{ m}^2 \\implies$ Cost at Rs. 80 $= \\mathbf{\\text{Rs. } 38,000}$.\n- **Surrounding Path**: Lawn $30 \\times 16$, path $2\\text{m}$ wide $\\implies (34 \\times 20) - (30 \\times 16) = 680 - 480 = \\mathbf{200\\text{ sq. mts}}$.\n\n#### Page 21 & 22: 3D Melted Cubes & Water Level Rise\n- **Melted Cubes Addition**: 3 cubes sides $6, 8, 10\\text{cm}$ melted into 1 cube $\\implies 6^3 + 8^3 + 10^3 = 216 + 512 + 1000 = 1728 \\implies a = \\sqrt[3]{1728} = \\mathbf{12\\text{ cm}}$!\n- **Hollow Metal Pipe Volume**: Length $20\\text{m}$, inner $d=12\\text{m}$, outer $d=16\\text{m} \\implies \\pi h (R^2 - r^2) = \\frac{22}{7} \\times 20 \\times (8^2 - 6^2) = \\mathbf{1760\\text{ m}^3}$.\n- **Spherical Balls Water Rise**: Jar radius $6\\text{cm}$, water rise $36\\text{cm}$, balls radius $1.5\\text{cm} \\implies N = \\frac{\\pi R^2 h}{\\frac{4}{3} \\pi r^3} = \\frac{6 \\times 6 \\times 36}{\\frac{4}{3} \\times 1.5^3} = \\mathbf{288\\text{ Balls}}$!\n",
        "flashcards": [
            {
                "title": "Page 5 & 7: 2D & 3D Ratio Rules",
                "front": "What are the rules for converting Sides ratio to Areas ratio (2D) vs Volumes ratio (3D)?",
                "back": "\u2022 Sides $\\to$ Areas: **Square** ratios individually ($19:17 \\to 361:289$)\n\u2022 Sides $\\to$ Volumes: **Cube** ratios individually ($9:7 \\to 729:343$)",
                "badge": "\ud83d\udcc4 Page 5"
            },
            {
                "title": "Page 8: Surface Area to Volume Rule",
                "front": "How do you convert Surface Area ratio directly to Volume ratio in 3D spheres/cubes?",
                "back": "Area $\\xrightarrow{\\text{Square Root}}$ Side $\\xrightarrow{\\text{Cube}}$ Volume!\nExample: $36:121 \\to 6:11 \\to \\mathbf{216:1331}$!",
                "badge": "\ud83d\udcc4 Page 8"
            },
            {
                "title": "Page 12: Cyclic Rhombus Shortcut",
                "front": "What shape is a Cyclic Rhombus inscribed inside a circle?",
                "back": "A Cyclic Rhombus is ALWAYS a **SQUARE**!\nAll angles are $90^\\circ$ and diagonals are equal!",
                "badge": "\ud83d\udcc4 Page 12"
            },
            {
                "title": "Page 22: Water Level Rise Ball Count Formula",
                "front": "What is the formula for the number of spherical balls immersed in a cylinder to raise water level by $h$?",
                "back": "$$\\text{Number of Balls } N = \\frac{\\pi R^2 h}{\\frac{4}{3} \\pi r^3}$$",
                "badge": "\ud83d\udcc4 Page 22"
            }
        ],
        "questions": [
            {
                "text": "From Page 8 Notes: If surface areas of two spheres are in ratio 36 : 121, what is the ratio of their volumes?",
                "options": [
                    "6 : 11",
                    "36 : 121",
                    "216 : 1331",
                    "1296 : 14641"
                ],
                "correct_option_index": 2,
                "explanation": "Page 8 Rule: Area -> Side (sqrt) = 6 : 11 => Side -> Volume (cube) = 6^3 : 11^3 = 216 : 1331!"
            },
            {
                "text": "From Page 12 Notes: What is the area of a cyclic Rhombus whose side is 9 cm?",
                "options": [
                    "36 cm\u00b2",
                    "72 cm\u00b2",
                    "81 cm\u00b2",
                    "162 cm\u00b2"
                ],
                "correct_option_index": 2,
                "explanation": "Page 12 Rule: A cyclic Rhombus is a SQUARE! Area = 9 * 9 = 81 cm\u00b2!"
            },
            {
                "text": "From Page 21 Notes: 3 solid cubes with sides 6 cm, 8 cm, and 10 cm are melted to form a single cube. What is the side of the new cube?",
                "options": [
                    "11 cm",
                    "12 cm",
                    "14 cm",
                    "16 cm"
                ],
                "correct_option_index": 1,
                "explanation": "Page 21 Solution: Total Volume = 6^3 + 8^3 + 10^3 = 216 + 512 + 1000 = 1728 => Side = cube_root(1728) = 12 cm!"
            }
        ]
    }
];

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { aptitudeTopics };
} else {
    window.aptitudeTopics = aptitudeTopics;
}
