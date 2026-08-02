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
        "name": "Percentages (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 15 Handwritten PDF pages: Fraction Tricks, Symmetry Rule, 10% & 1% Decimal Shift, Equal Increase/Decrease Square Loss, Venn Diagrams, Sugar Solutions, Election & Salary Problems.",
        "icon": "\ud83d\udcaf",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Percentages (15 Pages Transcribed)\n\n#### Page 1: Base Fractions & Symmetry Rule\n- **Fraction Reduction Trick**: Knowing some fractions makes calculating percentages easier!\n  - Example: $28.5\\% \\text{ of } 1400 = 400 \\implies \\frac{2}{7} \\text{ of } 1400 = \\frac{2}{7} \\times 1400 = 400$.\n- **Rule of Symmetry**: $a\\% \\text{ of } b = b\\% \\text{ of } a$\n  - Example: $13\\% \\text{ of } 200 = 200\\% \\text{ of } 13 = 26$.\n- **10% & 1% Decimal Shift**:\n  - $10\\%$ of any number: Place decimal point before the unit digit ($10\\% \\text{ of } 7432 = 743.2$).\n  - $1\\%$ of any number: Place decimal point before the one's digit ($1\\% \\text{ of } 7432 = 74.32$).\n\n#### Page 2: Combination Techniques & Practiced Examples\n- **Combination Method**:\n  - $21\\% \\text{ of } 6400$: $10\\% \\to 640.0 \\implies 20\\% \\to 1280$. Add $1\\% (64) \\implies 1280 + 64 = 1344$.\n  - $19\\% \\text{ of } 7200$: $20\\% - 1\\% = 1440 - 72 = 1368$.\n- **Practiced Examples from Notes**:\n  1. $24\\% \\text{ of } 8800 = 20\\% + 4\\% = 2112$ (or $25\\% - 1\\%$).\n  2. $91\\% \\text{ of } 3500 = 90\\% + 1\\% = 3150 + 35 = 3185$.\n  3. $28.2\\% \\text{ of } 1100 = 27.2\\% + 1\\% = 310.2$.\n  4. $61\\% \\text{ of } 12400 = 50\\% + 10\\% + 1\\% = 7564$.\n  5. $18\\% \\text{ of } 77.77 = 20\\% - 2\\% = 15.554 - 1.5554 = 13.9986$.\n\n#### Page 3: Problematic Understanding of Percentages\n- **Problem 1**: When a number is increased by $20\\%$ by itself, the result is 480. Find the number.\n  - Let number be $x\\% = 100\\%$.\n  - $x\\% + 20\\% = 120\\% \\to 480$ (Common multiplier: $120 \\times 4 = 480$).\n  - $100\\% \\to 100 \\times 4 = 400$. **Number = 400**.\n- **Problem 2**: If $40\\%$ of a number is 20 more than $30\\%$ of a number, find the number.\n  - Diff: $40\\% - 30\\% = 10\\% \\to 20$.\n  - Number $= 100\\% \\to 100 \\times 2 = 200$. **Number = 200**.\n- **Problem 3**: Candidate A won election by majority of 150 votes. Candidate A secured $60\\%$ of total votes.\n  - $A \\to 60\\%$, $B \\to 40\\%$. Majority $= 20\\% \\to 150$ votes.\n  - Total $= 100\\% \\to 750$ votes.\n\n#### Page 4 & 5: Equal Increase & Decrease Square Loss Rule\n- **Highly Important Concept**: If an entity is increased by $x\\%$ and then decreased by the same $x\\%$, we FINALLY end up with a **LOSS**.\n  - $(\\uparrow \\downarrow \\text{ or } \\downarrow \\uparrow \\implies \\text{Finally Loss})$\n  - $\\text{Loss} = \\text{Square of } 10^{\\text{th}} \\text{ multiple}$.\n  - $10\\% \\implies (1.0)^2 = 1\\%$ Loss.\n  - $20\\% \\implies (2.0)^2 = 4\\%$ Loss.\n  - $30\\% \\implies (3.0)^2 = 9\\%$ Loss.\n  - $5\\% \\implies (0.5)^2 = 0.25\\%$ Loss.\n  - $12\\% \\implies (1.2)^2 = 1.44\\%$ Loss.\n- **Sugar Price Worked Example**: Price of sugar increased by $30\\%$ then decreased by $30\\%$. Present price is Rs. 273.\n  - Original $= 100\\% \\implies +30\\% \\to 130\\%$.\n  - $-30\\% \\text{ of } 130 = 39 \\implies 130 - 39 = 91\\%$.\n  - $91\\% \\to 273$ ($91 \\times 3 = 273$).\n  - $100\\% (\\text{Original Price}) \\to 100 \\times 3 = \\text{Rs. } 300$.\n\n#### Page 6 & 7: Questioning Pattern Types & Area Expansion Rules\n- **3 Question Patterns**:\n  1. Initial Value + $\\%$ Given $\\implies$ Find Final Value (Calculation).\n  2. Initial Value + Final Value Given $\\implies$ Find $\\%$ (Fraction).\n  3. $\\%$ + Final Value Given $\\implies$ Find Initial Value (Equation).\n- **Square Area Increase Example**: Side of square increased by $20\\%$. Area increases by what $\\%$?\n  - Pattern $\\uparrow \\uparrow \\implies 20 + 20 + (2.0)^2 = 44\\%$ Increase!\n- **Square Area Reversal**: Area becomes 3380 sq. units after side increases by $30\\%$.\n  - Side $30\\% \\uparrow \\implies$ Area $30 + 30 + 3^2 = 69\\% \\uparrow \\implies 169\\% \\to 3380$.\n  - Original Area ($100\\%$) $= 2000$ sq. units.\n\n#### Page 8, 9 & 10: Salary, Election, & Comparison Formulas\n- **Remaining Expenditure Rule**: Expenditure can be from OVERALL salary OR REMAINING salary.\n  - Surya Salary Problem: Spends $60\\%$ on food (Rem $40\\%$). Spends $20\\%$ of remaining on petrol ($8\\%$, Rem $32\\%$). Spends $10\\%$ of remaining on entertainment ($3.2\\%$).\n  - Total Savings $= 100\\% - 60\\% - 8\\% - 3.2\\% = 28.8\\%$.\n  - $28.8\\% \\to \\text{Rs. } 288 \\implies 100\\% \\to \\text{Rs. } 1000$ Total Salary!\n- **Two Numbers Comparison Rules**:\n  - $A$ is what $\\%$ of $B \\implies \\left(\\frac{A}{B}\\right) \\times 100$.\n  - $A$ is how much $\\%$ MORE than $B \\implies \\frac{\\text{diff}}{\\text{diff} + B} \\times 100$.\n  - $A$ is how much $\\%$ LESS than $B \\implies \\frac{\\text{diff}}{\\text{diff} - A} \\times 100$.\n\n#### Page 11, 12 & 13: Expenditure Consumption & Venn Diagrams\n- **Consumption Reduction Formula**: Price of sugar increased by $40\\%$. To keep expenditure same:\n  - $\\text{Reduction}\\% = \\frac{40}{100 + 40} \\times 100 = \\frac{40}{140} \\times 100 = 28.57\\%$.\n- **Venn Diagram Problem**: In a town, $70\\%$ read Hindu, $40\\%$ read TOI, $30\\%$ read both.\n  - Hindu only $= 40\\%$, TOI only $= 10\\%$, Both $= 30\\%$.\n  - Total reading at least one $= 40 + 30 + 10 = 80\\%$.\n  - Neither $= 100\\% - 80\\% = 20\\%$.\n\n#### Page 14 & 15: Sugar Solution, Fuel Tank & Apple Price Reduction\n- **Sugar Solution**: 3 litres of $40\\%$ sugar solution ($1.2$L sugar). Add 1L pure water $\\implies 4$L total.\n  - New $\\%$ of sugar $= \\frac{1.2}{4} \\times 100 = 30\\%$.\n- **Fuel Tank Replacement Table**:\n  - Tank filled with Type A (100A, 0B). Half empty (50A). Fill B (50A, 50B). Half empty (25A, 25B). Fill B (25A, 75B). Half empty (12.5A, 37.5B). Fill B (37.5A, 62.5B).\n  - Present petrol state: Type A $= 37.5\\%$, Type B $= 62.5\\%$.\n- **Apple Price Reduction**: $20\\%$ price reduction enables buying 2 more apples for Rs. 100.\n  - $20\\% \\to 2 \\text{ apples} \\implies 100\\% \\to 10 \\text{ apples (Present)}, 80\\% \\to 8 \\text{ apples (Original)}$.\n  - Reduced Price $= \\frac{\\text{Rs. } 100}{10} = \\text{Rs. } 10 / \\text{apple}$.\n  - Original Price $= \\frac{\\text{Rs. } 100}{8} = \\text{Rs. } 12.5 / \\text{apple}$.\n",
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
        "name": "Profit and Loss (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 15 Handwritten PDF pages: Base CP 100%, Equal CP No Profit/No Loss, Equal SP Square Loss Rule, Reverse Term CP=SP, Equating Quantity Methods, Dishonest Dealer Tricks, Fraction Conversions, Egg Broken Problem, and Lemon Transaction Rules.",
        "icon": "\ud83d\udcc8",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Profit and Loss (15 Pages Transcribed)\n\n#### Page 1: Terminology & Core Principles\n- **Cost Price ($CP$)**: Always considered as $100\\%$ base!\n- **Selling Price ($SP$)**: $CP + P$ (if $SP > CP$, Profit) or $CP - L$ (if $CP > SP$, Loss).\n- **Profit ($P$)**: Difference between $CP$ and $SP$.\n- **Loss ($L$)**: Difference between $CP$ and $SP$.\n- **Profit $\\%$**: $P\\% = \\left(\\frac{P}{CP}\\right) \\times 100$.\n- **Loss $\\%$**: $L\\% = \\left(\\frac{L}{CP}\\right) \\times 100$.\n- **Key Note**: Everything is calculated ONLY on Cost Price, NOT on Selling Price!\n- **3 Question Types**: (1) Initial Value ($CP$), (2) Percentage Profit/Loss, (3) Final Value ($SP$).\n\n#### Page 2: Successive Discounts & Basic Worked Examples\n- **Example 1**: Purchased for Rs. 1500, sold for Rs. 1950.\n  - $\\text{Profit} = 1950 - 1500 = 450 \\implies P\\% = \\frac{450}{1500} \\times 100 = 30\\%$ Profit.\n- **Example 2**: $SP = \\text{Rs. } 3600$, Loss $= 10\\%$. Find $CP$.\n  - $CP = 100\\% \\implies SP = 90\\% \\to 3600 \\implies CP = 100\\% \\to \\mathbf{4000}$.\n- **Successive Discounts**: 3 successive discounts of $10\\%, 20\\%, 30\\%$ on Marked Price ($100\\%$):\n  - $1^{\\text{st}} \\to 10\\% \\implies 90\\%$.\n  - $2^{\\text{nd}} \\to 20\\% \\text{ of } 90 = 18\\% \\implies 72\\%$.\n  - $3^{\\text{rd}} \\to 30\\% \\text{ of } 72 = 21.6\\% \\implies 50.4\\%$.\n  - Total Discount $= 10\\% + 18\\% + 21.6\\% = \\mathbf{49.6\\%}$.\n\n#### Page 3: Equal Cost Price Rule (No Profit / No Loss)\n- **Important Note 1**: If a person purchases two items with **EQUAL COST PRICE** and sells one with $x\\%$ Profit and another with same $x\\%$ Loss:\n  - Result is ALWAYS **NO PROFIT / NO LOSS**!\n  - Example: Dravid bought 2 cars each at Rs. 4,59,000. Sold one at $13\\%$ profit & another at $13\\%$ loss $\\implies \\mathbf{\\text{No Profit / No Loss}}$.\n\n#### Page 4 & 5: Equal SP Square Loss Rule & Equating Terms\n- **Important Note 2**: If **SELLING PRICES of two items are equal** and one is sold at $x\\%$ profit and another at $x\\%$ loss:\n  - Result is ALWAYS a **LOSS** of $\\left(\\frac{x}{10}\\right)^2\\%$ or $(x.0)^2\\%$.\n  - Example: SP Rs. 5,43,400 each, $30\\%$ profit & $30\\%$ loss $\\implies (3.0)^2 = \\mathbf{9\\% \\text{ Loss}}$.\n- **Rule 3 (Equating CP of $x$ items = SP of $y$ items)**:\n  - Reverse the terms and equate $CP \\leftrightarrow SP$.\n  - Example: $CP$ of 80 articles $= SP$ of 60 articles $\\implies SP$ of $80 = CP$ of 60.\n  - $CP = 60, SP = 80 \\implies P\\% = \\frac{20}{60} \\times 100 = \\mathbf{33.33\\% \\text{ Profit}}$.\n- **Rule 4 (Quantity Rates)**:\n  - Example: Bought 16 for 24, sold 8 for 18.\n  - $CP \\text{ of } 16 = 24 \\implies SP \\text{ of } 16 = 36 \\implies P\\% = \\frac{12}{24} \\times 100 = \\mathbf{50\\%}$.\n\n#### Page 6 & 7: SP Target Scaling & Discount without Discount\n- **Question 1**: Sold for Rs. 306 with $30\\%$ loss. Find $SP$ to gain $40\\%$.\n  - $70\\% \\to 306 \\implies 140\\% (100+40) \\to 306 \\times 2 = \\mathbf{\\text{Rs. } 612}$.\n- **CP Average Note**: When SP is given for equal profit & loss: $CP = \\frac{SP_1 + SP_2}{2}$.\n- **Discount & Marked Price Rules**:\n  - Example 1: After $20\\%$ discount, profit is $12\\%$. If no discount is given, find $P\\%$.\n    - Discounted $SP = 80\\% \\to 112\\% \\implies 100\\% (\\text{Marked Price}) \\to 140\\% \\implies \\mathbf{P\\% = 40\\%}$.\n  - Example 2: After $20\\%$ discount, loss is $28\\%$. If $10\\%$ discount is given:\n    - $80\\% \\to 72\\% \\implies 90\\% \\to \\frac{72 \\times 90}{80} = 81\\% \\implies \\mathbf{19\\% \\text{ Loss}}$.\n\n#### Page 8: Dishonest Dealer / Cheating Rules\n- **Dishonest Dealer Formula**: $\\text{Profit } \\% = \\frac{\\text{Diff}}{\\text{False Weight}} \\times 100$.\n  - Example 1: Uses $1100g$ instead of $1.5\\text{ kg}$ ($1500g$).\n    - $P\\% = \\frac{1500 - 1100}{1100} \\times 100 = \\frac{400}{1100} \\times 100 = \\mathbf{36.36\\%}$.\n  - Example 2: Professes $CP$, but gains $25\\%$. Weight substituted for $1\\text{ kg}$?\n    - $\\text{Less } \\% = \\frac{25}{125} \\times 100 = 20\\% \\text{ less} \\implies 1000 - 200 = \\mathbf{800\\text{ grams}}$.\n\n#### Page 9: Simplified Fraction Conversion Method\n- **Fraction Speed Method**:\n  - Example 1: $P = 28.57\\% = \\frac{2}{7}$, $SP = 909$.\n    - $CP = 7, SP = 9 \\implies 9 \\to 909 \\implies 7 \\to \\mathbf{707}$.\n  - Example 2: $\\text{Loss} = 27.27\\% = \\frac{3}{11}$, $SP = 1680$.\n    - $SP = 8 \\to 1680 \\implies CP = 11 \\to \\mathbf{2310}$.\n  - Example 3: TV sold for Rs. 1800 at loss of $14.28\\% = \\frac{1}{7}$.\n    - $SP = 6 \\to 1800 \\implies CP = 7 \\to \\mathbf{2100}$.\n\n#### Page 10, 11 & 12: Price Shifts, Rice Mixture & Broken Eggs\n- **Price Shift Example**: Sold at $10\\%$ loss. If Rs. 60 more, gain would be $10\\%$.\n  - Diff $= 110\\% - 90\\% = 20\\% \\to 60 \\implies 100\\% = \\mathbf{\\text{Rs. } 300}$.\n- **Merchant Rice Mixture**: $20\\text{ kg}$ at Rs. 30/kg ($CP_1 = 600$) + $80\\text{ kg}$ at Rs. 25/kg ($CP_2 = 2000$). Total $CP = 2600$. Sells mixture at Rs. 27/kg ($SP = 2700$).\n  - Overall Profit $= 2700 - 2600 = \\mathbf{\\text{Rs. } 100}$.\n- **Broken Eggs Problem**: 80 dozen eggs at Rs. 6/dozen ($CP = 480$). 160 eggs broken ($800$ available). Target $P = 25\\% \\implies SP = 600$.\n  - Selling Price $= \\left(\\frac{600}{800}\\right) \\times 12 = \\mathbf{\\text{Rs. } 9 / \\text{dozen}}$.\n\n#### Page 13, 14 & 15: Mango Price Reduction, Options Trick & Lemon Transaction\n- **Mango Price Reduction**: $20\\% \\downarrow$ enables buying 4 more for Rs. 800.\n  - Original $= 16 \\implies \\text{Original Price} = 800/16 = \\mathbf{\\text{Rs. } 50}$.\n  - Reduced $= 20 \\implies \\text{Reduced Price} = 800/20 = \\mathbf{\\text{Rs. } 40}$.\n- **Options Consideration Trick**: Article sold for Rs. 144. $P\\%$ numerically equals $CP$.\n  - Option check $80$: $80 + 80\\% \\text{ of } 80 = 80 + 64 = 144 \\implies \\mathbf{CP = \\text{Rs. } 80}$.\n- **Lemon Transaction**: Sells 45 lemons for Rs. 40 (loses $20\\%$). For $20\\%$ profit:\n  - $45 \\to 80\\% \\to \\text{Rs. } 40 \\implies 45 \\to 120\\% \\to \\text{Rs. } 60$.\n  - For Rs. 24: $\\frac{45 \\times 24}{60} = \\mathbf{18\\text{ lemons}}$.\n",
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
        "name": "Simple Interest & Compound Interest (SI & CI)",
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
        "name": "Averages (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 11 Handwritten PDF pages: Assumption Concept, Class Join/Leave Tricks, Manager Salary Addition, Cricket Innings Highest/Lowest, Replacement Equality Rules, Mistaken Value Corrections, Missing & Middle Number Deviations, Weighted Average Ratios, and Consecutive Number Tricks.",
        "icon": "\u2696\ufe0f",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Averages (11 Pages Transcribed)\n\n#### Page 1: General Definition & Assumption Concept\n- **General Formulas**:\n  - $\\text{Average} = \\frac{\\text{Sum of obs.}}{\\text{No. of obs.}}$\n  - $\\text{No. of obs.} = \\frac{\\text{Sum of obs.}}{\\text{Average}}$\n  - $\\text{Sum of obs.} = \\text{No. of obs.} \\times \\text{Average}$\n- **Core Concept**:\n  - If every value is equal $\\implies \\text{Each Value} = \\text{Average}$.\n  - Value A = 200, Value B = 120 $\\implies$ Equal at 160 ($-40, +40$). Average $= 160$.\n  - **Key Insight**: Average is a concept of **Assumption, not reality**!\n- **Class Joining Worked Example**: 28 students with Avg wt 33 kg. 1 new student joins, avg increases by 2 kg. Find new student's weight ($91\\text{ kg}$).\n  - Routine: $\\text{Old Sum} = 28 \\times 33 = 924$, $\\text{New Sum} = 29 \\times 35 = 1015 \\implies \\text{New Student} = 1015 - 924 = \\mathbf{91\\text{ kg}}$.\n  - Shortcut (Take 35 & make 35): $35 + (28 \\times 2) = 35 + 56 = \\mathbf{91\\text{ kg}}$!\n\n#### Page 2 & 3: Multiple Joiners, Manager Salary, Cricket Innings & Replacement\n- **2 New Joiners**: 25 students (Avg 75 kg). 2 new students join, avg increases by 1 kg ($27 \\to 76$).\n  - Total wt of $A + B = 76 + 76 + 25 = \\mathbf{177\\text{ kg}}$.\n- **Manager Salary Inclusion**: 35 workers (Avg Rs. 1800). Manager included $\\implies 36 \\to \\text{Avg } 1925 (+125)$.\n  - Manager Salary $= 1925 + (125 \\times 35) = 1925 + 4375 = \\mathbf{\\text{Rs. } 6300}$.\n- **Cricket Innings Highest & Lowest**: 40 innings (Avg 50 runs). Highest exceeds Lowest by 172 runs. Excluded 2 innings $\\implies 38$ innings (Avg 48 runs).\n  - $H + L = 50 + 50 + (2 \\times 38) = 176$.\n  - $H - L = 172$.\n  - Highest Score $(H) = \\frac{176 + 172}{2} = \\mathbf{174}$.\n  - Lowest Score $(L) = \\frac{176 - 172}{2} = \\mathbf{2}$.\n- **Batsman 17th Innings**: Batsman scores 85 in $17^{\\text{th}}$ innings, increasing avg by 3 runs.\n  - Avg Before $17^{\\text{th}}$ innings (After $16^{\\text{th}}$) $= 85 - (3 \\times 17) = \\mathbf{34}$.\n  - Avg After $17^{\\text{th}}$ innings $= 34 + 3 = \\mathbf{37}$.\n- **Replacement Equality Concept**: Replacing one element causes average differences. Averages is all about **maintaining and distributing equality**!\n  - 15 men weight increases by 1 kg when 60 kg man is replaced by a new man.\n  - Extra 1 kg distributed to all 15 members $\\implies 60 + (1 \\times 15) = \\mathbf{75\\text{ kg}}$.\n\n#### Page 4 & 5: Mistaken Value Corrections & Set Difference Tricks\n- **Mistaken Reading Correction**: Avg height of 15 students is 159 cm. Reading 147 cm was wrongly read as 177 cm.\n  - Diff $= 177 - 147 = 30$. Distribute 30 equally to 15 students $\\implies \\frac{30}{15} = 2$.\n  - Correct Avg $= 159 - 2 = \\mathbf{157\\text{ cm}}$.\n  - General Formula: $\\text{Correct Avg} = 159 - \\left(\\frac{177 - 147}{15}\\right) = \\mathbf{157}$.\n- **Set Difference Problem**: 4 numbers. Avg of 1st 3 is 48. Avg of last 3 is 52. If Last No. is 58, find 1st No.\n  - Total 1st $3 = 144$, Total last $3 = 156 \\implies D - A = 156 - 144 = 12$.\n  - $58 - A = 12 \\implies \\mathbf{A = 46}$.\n- **A, B, C, D, E Weight Swap**: Avg wt of A, B, C is 80 kg. D joins $\\implies 4$ avg is 82 kg ($D = 88$). E (4 kg less than D $\\implies E = 84$) replaces A $\\implies$ B, C, D, E avg is 84 kg. Find A.\n  - Diff $B,C,D,E - A,B,C,D = 84 - 82 = 2 \\times 4 = 8 \\implies E$ is 8 more than $A \\implies A = 84 - 8 = \\mathbf{76\\text{ kg}}$.\n\n#### Page 6 & 7: Missing Numbers & Weighted Average Ratios\n- **Missing / Middle Number Deviation**:\n  - Avg of 7 numbers is 53. Avg of 1st 3 is 47 ($-6 \\times 3 = -18$). Avg of last 3 is 55 ($+2 \\times 3 = +6$). Net diff $= -12$.\n  - Missing Middle Number $= 53 - (-12) = \\mathbf{65}$.\n- **Overlapping Middle Number**: Avg of 9 numbers is 48. 1st 5 avg 45 ($-15$). Last 5 avg 52 ($+20$). Net $= +5$.\n  - Middle Number $= 48 + 5 = \\mathbf{53}$.\n- **Weighted Average Ratio Method**: Convert number of entities to simple ratios ($N_i = R_i$).\n  - Formula: $\\text{Weighted Avg} = \\frac{A_1 R_1 + A_2 R_2 + A_3 R_3}{R_1 + R_2 + R_3}$.\n  - Scenario: A (Avg 60, No 32), B (Avg 75, No 48), C (Avg 80, No 80).\n  - Ratio $32 : 48 : 80 = 2 : 3 : 5$.\n  - Weighted Avg $= \\frac{(60 \\times 2) + (75 \\times 3) + (80 \\times 5)}{2 + 3 + 5} = \\frac{120 + 225 + 400}{10} = \\mathbf{74.5}$.\n  - Virat Kohli Runs: Avg 30 in 25 matches, Avg 70 in next 75 matches. Ratio $25 : 75 = 1 : 3$.\n  - Overall Avg $= \\frac{(30 \\times 1) + (70 \\times 3)}{1 + 3} = \\frac{240}{4} = \\mathbf{60\\text{ Runs}}$.\n\n#### Page 8, 9, 10 & 11: Consecutive Numbers, Primes & Operation Persistence\n- **Consecutive Numbers & Common Difference Shortcuts**:\n  - $\\text{Average} = \\frac{\\text{First Obs} + \\text{Last Obs}}{2} = \\text{Exactly the Middle Number}$.\n  - Average of first $n$ **even** numbers $= \\mathbf{n + 1}$.\n  - Average of first $n$ **odd** numbers $= \\mathbf{n}$.\n- **Prime Numbers Rules**:\n  - Average of Prime Numbers between 23 and 53 (exclude boundaries 29, 31, 37, 41, 43, 47) $= \\mathbf{38}$.\n  - Average of Prime Numbers from 23 to 53 (include boundaries 23, 29, 31, 37, 41, 43, 47, 53) $= \\mathbf{38}$.\n- **Consecutive Number Examples from Notes**:\n  1. 7 consecutive natural numbers avg 43 $\\implies$ 43 is $4^{\\text{th}}$ value $\\implies$ Smallest $= 43 - 3 = \\mathbf{40}$.\n  2. 8 consecutive natural numbers avg 84.5 $\\implies$ Middle is 84.5 $\\implies$ Largest $= \\mathbf{88}$.\n  3. 5 consecutive EVEN numbers avg 48 $\\implies$ Smallest $= \\mathbf{44}$.\n  4. 6 consecutive ODD numbers avg 98 $\\implies$ Middle 98 $\\implies$ Largest $= \\mathbf{103}$.\n  5. Sum of 5 consecutive natural numbers is 145 $\\implies \\text{Avg} = 145/5 = 29 \\implies$ Smallest $= \\mathbf{27}$.\n  6. Sum of 7 consecutive EVEN numbers is 224 $\\implies \\text{Avg} = 224/7 = 32 \\implies$ Smallest $= \\mathbf{26}$.\n- **Mathematical Operation Persistence**:\n  - If every element in the observation is operated equally ($+,-,\\times,\\div$), the SAME operation applies directly to the Average!\n  - Example: Avg of 28 numbers is 25.\n    - If each number is multiplied by 3 $\\implies$ New Avg $= 25 \\times 3 = \\mathbf{75}$.\n    - If each number is increased by 6 $\\implies$ New Avg $= 25 + 6 = \\mathbf{31}$.\n",
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
        "name": "Alligations & Mixtures (PDF Placeholder)",
        "description": "Master the rule of alligation and mixture concentration problems.",
        "icon": "\ud83e\uddea",
        "xp_reward": 110,
        "formula_sheet": "### \ud83d\udcc4 Master Cheat Sheet: Alligations & Mixtures (PDF Placeholder)\n\n# Alligations and Mixtures\n\n- **Alligations and mixtures** is a rule that can be applied to Percentages, Profit and Loss, and Averages.\n- It is mostly used when the **Result** (or average/mixture value) is given.\n- In Alligation and mixtures, a total of three values (Result and two categories) will be given in the question.\n\n## The Alligation Rule (Cross-Difference Method)\nIf two categories $A$ and $B$ are mixed to get a Result $R$:\n```\n  A          B\n   \\        /\n    Result(R)\n   /        \\\n(B-R)  :  (R-A)\n```\n- Take the positive difference between the Result and each category.\n- The ratio of the quantities of $A$ and $B$ is $(B - R) : (R - A)$.\n- **Important Note:** All the values must be of the same style/format (i.e., either all percentages or all direct numerics like cost price).\n\n## Handling Successive Replacement\nWhen a quantity $x$ is removed from a total volume $V$ of pure liquid and replaced with water, and this is repeated $n$ times:\n- Use percentages or fractions to track the remaining amount.\n- Example: If 10% is removed, then 90% of the previous amount remains after each step.\n- You can step-by-step calculate the remaining amount: $m_{new} = m_{old} - (x/V) \\times m_{old}$.\n",
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
                "back": "Handwritten PDF Rule:\nAlligations and mixtures is a rule that can be applied to Percentages, Profit and Loss, and Averages.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 1"
            },
            {
                "title": "Rule 2: It is mostly used when the Result (",
                "front": "What is the rule or formula for: It is mostly used when the Result (or average/mixture value) is given.?",
                "back": "Handwritten PDF Rule:\nIt is mostly used when the Result (or average/mixture value) is given.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 2"
            },
            {
                "title": "Rule 3: In Alligation and mixtures, a total",
                "front": "What is the rule or formula for: In Alligation and mixtures, a total of three values (Result and two categories) will be given in the question.?",
                "back": "Handwritten PDF Rule:\nIn Alligation and mixtures, a total of three values (Result and two categories) will be given in the question.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 3"
            },
            {
                "title": "Rule 4: Take the positive difference betwee",
                "front": "What is the rule or formula for: Take the positive difference between the Result and each category.?",
                "back": "Handwritten PDF Rule:\nTake the positive difference between the Result and each category.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 4"
            },
            {
                "title": "Rule 5: The ratio of the quantities of $A$ ",
                "front": "What is the rule or formula for: The ratio of the quantities of $A$ and $B$ is $(B  R) : (R  A)$.?",
                "back": "Handwritten PDF Rule:\nThe ratio of the quantities of $A$ and $B$ is $(B  R) : (R  A)$.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 5"
            },
            {
                "title": "Rule 6: Important Note: All the values must",
                "front": "What is the rule or formula for: Important Note: All the values must be of the same style/format (i.e., either all percentages or all direct numerics like cost price).?",
                "back": "Handwritten PDF Rule:\nImportant Note: All the values must be of the same style/format (i.e., either all percentages or all direct numerics like cost price).\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 6"
            }
        ]
    },
    {
        "id": 7,
        "slug": "ages",
        "name": "Problems on Ages (PDF Placeholder)",
        "description": "Learn algebraic and ratio-based shortcuts for age gap problems.",
        "icon": "\u23f3",
        "xp_reward": 90,
        "formula_sheet": "### \ud83d\udcc4 Master Cheat Sheet: Problems on Ages (PDF Placeholder)\n\n# Ages\n\n## Core Concepts\n* In Ages, the age gap is always constant/same between the entities.\n* The equations of age (i.e. double, triple, 4 times, etc.) among the entities happens only a single time across life.\n\n## Problem Solving Approaches\n1. **Using Age Gaps:** Two person's age gap will be given. And how the ages relate with them (double, triple, 4 times, etc...). As we know, age gap is constant and only once in a lifetime a certain relation is possible. So, we equate the ages accordingly and calculate further.\n2. **Using Ratios:** The ages are given as ratio at present and again age will be given as ratio after some years. Find the present age. Equate the ratios w.r.t to each other (mostly according to the latest age ratio). By this, we get difference between them as years, with parts.",
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
                "back": "Handwritten PDF Rule:\nIn Ages, the age gap is always constant/same between the entities.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 1"
            },
            {
                "title": "Rule 2: The equations of age (i.e. double, ",
                "front": "What is the rule or formula for: The equations of age (i.e. double, triple, 4 times, etc.) among the entities happens only a single time across life.?",
                "back": "Handwritten PDF Rule:\nThe equations of age (i.e. double, triple, 4 times, etc.) among the entities happens only a single time across life.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 2"
            }
        ]
    },
    {
        "id": 7,
        "slug": "ratios-proportions",
        "name": "Ratios and Proportions (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 12 Handwritten PDF pages: Extremes & Means Product, Duplicate/Triplicate Types, Compound & Inverse Ratios, 4th/3rd/Mean Proportion Formulas, Equal Difference Subtraction Equating, Mixture Milk/Water Addition, Chain Rule Tables/Desks, Equation Inversion $xA=yB=zC$, Wages Ratio Multiplication, Coin Bag Values, and Percentage Modification Ratios.",
        "icon": "\u2696\ufe0f",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Ratios and Proportions (12 Pages Transcribed)\n\n#### Page 1 & 2: Core Definitions & Ratio Types\n- **Proportion Core Rule**:\n  - $a : b :: c : d \\implies \\frac{a}{b} = \\frac{c}{d}$.\n  - **Product of Extremes = Product of Means**: $a \\times d = b \\times c$.\n- **4 Types of Questionings**:\n  1. **Duplicate Ratio**: Square the numbers ($a^2 : b^2$).\n  2. **Sub-Duplicate Ratio**: Square root of numbers ($\\sqrt{a} : \\sqrt{b}$).\n  3. **Triplicate Ratio**: Cube the numbers ($a^3 : b^3$).\n  4. **Sub-Triplicate Ratio**: Cube root of numbers ($\\sqrt[3]{a} : \\sqrt[3]{b}$).\n- **Compounded Ratio**: Multiply fractional forms: $\\frac{a}{b} \\times \\frac{c}{d} = \\frac{ac}{bd}$.\n  - Example: Compound ratio of $2:5, 10:7, 14:9 = \\frac{2}{5} \\times \\frac{10}{7} \\times \\frac{14}{9} = \\frac{8}{9} = \\mathbf{8 : 9}$.\n- **Inverse Ratios**:\n  - $a : b \\implies b : a$.\n  - $a : b : c \\implies bc : ac : ab$ or $\\frac{1}{a} : \\frac{1}{b} : \\frac{1}{c}$.\n\n#### Page 3 & 4: Proportion Formulas & Income/Difference Problems\n- **Standard Proportion Formulas**:\n  - $4^{\\text{th}}$ Proportion: $D = \\mathbf{\\frac{BC}{A}}$. (Example: $20, 21, 40, ? \\implies D = \\frac{21 \\times 40}{20} = \\mathbf{42}$).\n  - $3^{\\text{rd}}$ Proportion: $C = \\mathbf{\\frac{B^2}{A}}$.\n  - Mean Proportion: $B = \\mathbf{\\sqrt{AC}}$. (Example: 8 and 18 $\\implies B = \\sqrt{8 \\times 18} = \\mathbf{12}$).\n- **Mobile & Tablet Example**: Mobile : Tablet CP $= 4 : 7$. Tablet is Rs. 15,000 more $\\implies 3 \\to 15000$. Mobile CP $= 7 \\to \\mathbf{\\text{Rs. } 35,000}$.\n- **Riya Income Example**: Sita : Riya : Kunal $= 84 : 76 : 89$. Riya Annual $= 4,56,000 (\\times 6000)$.\n  - Sita + Kunal $= 173 \\to 173 \\times 6000 = \\mathbf{\\text{Rs. } 10,38,000}$.\n\n#### Page 5 & 6: Equal Difference Subtraction & Income/Expense Equating\n- **Equal Subtraction Equating Rule**:\n  - Two numbers ratio $7 : 12$. 15 subtracted from both $\\implies 16 : 31$. Find largest number.\n  - Diff Before $= 5$, Diff After $= 15$. Multiply Before by $3 \\implies 21 : 36$.\n  - Diff in parts $= 21 - 16 = 5 \\to 15 (\\times 3)$. Largest number $= 36 \\times 3 = \\mathbf{108}$!\n- **Income & Expense Equating**: Incomes $4:5$, Expenses $5:7$, each saves Rs. 1500.\n  - Income $\\times 2 = 8 : 10$, Expenses $= 5 : 7 \\implies$ Savings $= 3 : 3 \\to 1500 (\\times 500)$.\n  - B's Income $= 10 \\times 500 = \\mathbf{\\text{Rs. } 5000}$.\n\n#### Page 7 & 8: Mixture Addition, Vessel Mixing & Ratio Combination\n- **Milk & Water Mixture**: 60L mixture $3:2$ (36L milk, 24L water). Make ratio $2:3$.\n  - Milk 36L $= 2$ parts $\\implies 1$ part $= 18\\text{L} \\implies$ Water needed $= 3 \\times 18 = 54\\text{L}$.\n  - Water to add $= 54 - 24 = \\mathbf{30\\text{ Litres}}$!\n- **3 Vessel Liquor/Water Mixing**: Equal capacity vessels $1:2, 2:1, 3:1$. Equalize to LCM 12:\n  - $(4:8) + (8:4) + (9:3) = 21 : 15 = \\mathbf{7 : 5}$.\n- **Combining Ratios**:\n  - $A:B = 2:3, B:C = 4:3 \\implies A:B:C = (2\\times 4) : (3\\times 4) : (3\\times 3) = \\mathbf{8 : 12 : 9}$.\n  - $A:B = 3:4, B:C = 8:10, C:D = 15:17 \\implies A:D = \\frac{3}{4} \\times \\frac{8}{10} \\times \\frac{15}{17} = \\mathbf{9 : 17}$.\n\n#### Page 9, 10, 11 & 12: Chain Rule, Equation Inversion, Coin Bags & Percentage Shifts\n- **Chain Rule Tables Cost**: $10\\text{T} = 27\\text{S}, 9\\text{S} = 15\\text{C}, 9\\text{C} = 3\\text{B}, 7\\text{B} = 14\\text{D}$. Desk $= \\text{Rs. } 500$.\n  - Back-substitute: $14\\text{D} = 7000 \\to 7\\text{B} = 7000 \\to 3\\text{B} = 3000 \\to 9\\text{C} = 3000 \\to 15\\text{C} = 5000 \\to 9\\text{S} = 5000 \\to 27\\text{S} = 15000 \\to 10\\text{T} = 15000 \\implies 1\\text{T} = \\mathbf{\\text{Rs. } 1500}$.\n- **Equation Inversion Rule**:\n  - If $xA = yB = zC \\implies A : B : C = yz : xz : xy$.\n  - Example: $3A = 4B = 5C \\implies A : B : C = 20 : 15 : 12$.\n  - If $\\frac{1}{2}A = \\frac{1}{3}B = \\frac{1}{6}C \\implies A : B : C = 2 : 3 : 6$. Total Rs. 1870 $\\implies 3^{\\text{rd}} \\text{ part} = 6 \\times 170 = \\mathbf{\\text{Rs. } 1020}$.\n- **Wages Multiplication**: Rs. 425 divided among 4 men, 5 women, 6 boys. Individual wages $9:8:4$.\n  - Group wages $= (4\\times 9) : (5\\times 8) : (6\\times 4) = 36 : 40 : 24 = 9 : 10 : 6$ (Total 25 parts).\n  - $25 \\to 425 (\\times 17) \\implies 5$ women $= 170 \\implies 1\\text{ woman wage} = \\frac{170}{5} = \\mathbf{\\text{Rs. } 34}$.\n- **Coin Bag Problem**: Rs. 1, 50p, 25p coins in ratio $5 : 6 : 7$. Total sum $=$ Rs. 78.\n  - Value ratio $= (5\\times 1) : (6\\times 0.5) : (7\\times 0.25) = 5 : 3 : 1.75 = 20 : 12 : 7$ (Total 39 parts).\n  - $39 \\to 78 (\\times 2) \\implies 50p$ value $= 24 \\implies$ Coins $= 24 \\times 2 = \\mathbf{48\\text{ coins}}$.\n- **Percentage Shift Ratio Modification**: Ratio $5 : 9$. 1st $-19\\%$, 2nd $+10\\%$.\n  - Value $100 : 180 \\implies -19 : +18 = 81 : 198 = \\mathbf{9 : 22}$.\n",
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
        "name": "Partnerships (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 8 Handwritten PDF pages: Profit Sharing Ratio Formula, Equal Time/Investment Rules, Time & Capital Ratios, Sleeping vs Working Partner Extra Fee, Capital Withdrawal Addition Rules, Charity Deduction Connected Problems, and Joining Month Back-Calculations.",
        "icon": "\ud83e\udd1d",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Partnerships (8 Pages Transcribed)\n\n#### Page 1: Core Formula & Profit Sharing Ratio\n- **Core Formula**:\n  $$\\text{Profit Sharing Ratio (PSR)} = \\text{Investment} \\times \\text{Time (months/years)}$$\n  - Calculated for **each investment individually**.\n  - PSR decides how profits are shared based on money invested and time duration.\n- **Derived Ratios**:\n  - $\\text{Investment Ratio} = \\frac{\\text{Profit Share Ratio}}{\\text{Time Ratio}}$\n  - $\\text{Time Ratio} = \\frac{\\text{Profit Share Ratio}}{\\text{Investment Ratio}}$\n- **Worked Example**: Investor A ($12000 \\times 12 = 144000$), Investor B ($18000 \\times 6 = 108000$).\n  - PSR $= 144 : 108 = 4 : 3$. Total profit $= 2,100,000$.\n  - A's Share $= \\frac{4}{7} \\times 21000000 = \\mathbf{12,000,000}$, B's Share $= \\mathbf{9,000,000}$.\n\n#### Page 2: Multiple Partners & Joining Time\n- **Ajay, Vijay & Jai Example**: Investments $8000, 4000, 8000$. Ajay left after 6m, Vijay & Jai stay 8m. Total profit $= 4005$.\n  - Investment ratio $= 2 : 1 : 2$. Time ratio $= 6 : 8 : 8 = 3 : 4 : 4$.\n  - PSR $= (2 \\times 3) : (1 \\times 4) : (2 \\times 4) = 6 : 4 : 8 = 3 : 2 : 4$ (Total 9 parts).\n  - Vijay's Share $(2) = \\frac{2}{9} \\times 4005 = \\mathbf{\\text{Rs. } 890}$.\n- **Purna & Vishal Example**: Purna ($98000 \\times 12$), Vishal ($63000 \\times 8$). Vishal share $= \\text{Rs. } 15000$.\n  - PSR $= (98 \\times 12) : (63 \\times 8) = 1176 : 504 = 7 : 3$.\n  - Vishal $(3) \\to 15000 \\implies$ Total Profit $(10) = \\mathbf{\\text{Rs. } 50,000}$.\n\n#### Page 3 & 4: In-Depth Equal Rules & Time/Investment Ratio Calculations\n- **Equal Time Rule**: If investment time of all partners is EQUAL $\\implies$ PSR is SAME as Investment Ratio!\n  - Example: Investments $60000 : 40000 : 100000 \\implies \\text{PSR} = \\mathbf{3 : 2 : 5}$.\n- **Equal Capital Rule**: If investments are EQUAL $\\implies$ PSR is SAME as Time Ratio!\n  - Example: Time $12 : 10 : 6 \\implies \\text{PSR} = \\mathbf{6 : 5 : 3}$.\n- **Time Ratio Calculation**: Capitals $5:2:3$, PSR $10:8:9 \\implies \\text{Time Ratio} = \\frac{10}{5} : \\frac{8}{2} : \\frac{9}{3} = \\mathbf{2 : 4 : 3}$.\n- **Investment Ratio Calculation**: Time $2:3:4$, PSR $5:4:3 \\implies \\text{Investment Ratio} = \\frac{5}{2} : \\frac{4}{3} : \\frac{3}{4} = \\mathbf{30 : 16 : 9}$.\n\n#### Page 5 & 6: Working Partner Extra Fee & Capital Withdrawal\n- **Working Partner Extra Fee**: Working partner gets extra returns for managing business before sharing remainder.\n  - Example: A ($5000$) and B ($8000$). A gets $22\\%$ total profit for managing. Rest shared in capital ratio ($5:8$). A's total share $= \\text{Rs. } 2028$.\n  - Capital ratio $A:B = 5:8$ (Total 13 parts). A gets $22\\% + \\frac{5}{13}(78\\%) = 22\\% + 30\\% = 52\\%$.\n  - $52\\% \\to 2028 \\implies \\text{Total Profit } 100\\% = \\mathbf{\\text{Rs. } 3900}$.\n- **Capital Withdrawal Rule**: Add the withdrawn amount and time with existing left over!\n  - Example: P ($1.5\\text{L} \\times 12 = 18\\text{L}$), Q ($1.2\\text{L} \\times 8 + 0.9\\text{L} \\times 4 = 13.2\\text{L}$). Q share $= 44000$.\n  - PSR $= 18 : 13.2 = 15 : 11$. Q $(11) \\to 44000 \\implies$ Total Profit $(26) = \\mathbf{\\text{Rs. } 1,04,000}$.\n\n#### Page 7 & 8: Charity Connected Problem & Joining Month Back-Calculation\n- **Charity Connected Problem**: Surya ($85000 \\times 12 = 10.2\\text{L}$), Chandu ($90000 \\times 4 + 146250 \\times 8 = 15.3\\text{L}$). PSR $= 2 : 3$.\n  - Total profit $= 98000$. Charity $= 20\\% (19600) \\implies$ Shared $= 78400$.\n  - Difference (Chandu - Surya $= 1 \\text{ part}) = \\frac{78400}{5} = \\mathbf{\\text{Rs. } 15,680}$.\n- **Joining Month Back-Calculation**: A ($70000 \\times 12$), B ($60000 \\times t$). PSR $= 2 : 1$.\n  - $\\frac{84}{6t} = \\frac{2}{1} \\implies 12t = 84 \\implies t = 7\\text{ months invested}$. B joined after $12 - 7 = \\mathbf{5\\text{ months}}$!\n",
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
        "name": "Time and Work (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 20 Handwritten PDF pages: MDH Universal Formula, Efficiency Reciprocal Rule, Middle Joining/Leaving Equations, Men/Women OR & AND Formulas, LCM Work Parts Method, Alternate Days Cycle Rules, Pairwise Double Work Trick, Efficiency Percentage Equations, Leaving at End Work Calculation, and Work & Wages Daily Ratio Rule.",
        "icon": "\u23f3",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Time and Work (20 Pages Transcribed)\n\n#### Page 1 & 2: Proportionality Rules & MDH Formula\n- **Proportionality Laws**:\n  - $\\text{Time} \\propto \\text{Work}$ (Directly proportional)\n  - $\\text{Men} \\propto \\text{Work}$ (Directly proportional)\n  - $\\text{Time} \\propto \\frac{1}{\\text{Men}}$ (Inversely proportional)\n- **The Universal MDH Formula**:\n  $$\\frac{M_1 \\times D_1 \\times H_1}{W_1} = \\frac{M_2 \\times D_2 \\times H_2}{W_2}$$\n  - $M, D, H$ are inversely proportional to each other, $W$ (work/wages) is directly proportional.\n- **One Day Work & Efficiency**:\n  - If a person finishes work in $n$ days, 1 day work is $\\frac{1}{n}$.\n  - $\\text{Efficiency} = \\frac{\\text{Total Work}}{\\text{Time Taken}} \\implies \\text{Time} \\propto \\frac{1}{\\text{Efficiency}}$.\n- **Worked Example**: 24 men finish in 36 days. How many days for 54 men?\n  - $M_1 D_1 = M_2 D_2 \\implies 24 \\times 36 = 54 \\times D_2 \\implies D_2 = \\mathbf{16\\text{ Days}}$.\n\n#### Page 3 & 4: Book Binders, Cow Fodder, Wages & Middle Joining/Leaving\n- **18 Binders Example**: 18 binders bind 900 books in 10 days. How many binders for 660 books in 12 days?\n  - $\\frac{18 \\times 10}{900} = \\frac{M_2 \\times 12}{660} \\implies M_2 = \\mathbf{11\\text{ Binders}}$.\n- **Cow Fodder Stock**: 20 cows stock lasts 36 days. How long for 15 cows?\n  - $20 \\times 36 = 15 \\times D_2 \\implies D_2 = \\mathbf{48\\text{ Days}}$.\n- **Wages Example**: 6 men working 8 hrs/day earn Rs. 840/week. 9 men working 6 hrs/day earn how much?\n  - $\\frac{6 \\times 8}{840} = \\frac{9 \\times 6}{W_2} \\implies W_2 = \\mathbf{\\text{Rs. } 945}$.\n- **Middle Joining & Leaving Rule**: Equate equations by adding \"before\" and \"after\" situations.\n  - 16 men do job in 30 days. After 10 days, 6 men left (10 men remain).\n  - $16 \\times 30 = (16 \\times 10) + (10 \\times D_2) \\implies 480 = 160 + 10 D_2 \\implies D_2 = \\mathbf{32\\text{ Days}}$.\n\n#### Page 5 & 6: Updated Men Days & Men/Women OR/AND Rules\n- **12 Men 3 Days Join Example**: 12 men in 8 days. After 3 days, 3 men join (15 men).\n  - $12 \\times 8 = (12 \\times 3) + (15 \\times D_2) \\implies 96 = 36 + 15 D_2 \\implies D_2 = \\mathbf{4\\text{ Days}}$. Total $= 3 + 4 = \\mathbf{7\\text{ Days}}$.\n- **Men/Women OR & AND Questions**:\n  - 10 men OR 12 women in 16 days. How many days for 15 men AND 6 women together?\n  - $10\\text{M} = 12\\text{W} \\implies 5\\text{M} = 6\\text{W}$.\n  - $15\\text{M} + 6\\text{W} = 15\\text{M} + 5\\text{M} = 20\\text{M}$.\n  - $10 \\times 16 = 20 \\times D_2 \\implies D_2 = \\mathbf{8\\text{ Days}}$.\n- **Shortcut Formula for OR & AND**:\n  $$\\text{Days} = \\frac{\\text{Given Days}}{\\frac{q_m}{I_m} + \\frac{q_w}{I_w}} = \\frac{16}{\\frac{15}{10} + \\frac{6}{12}} = \\mathbf{8\\text{ Days}}!$$\n\n#### Page 7 & 8: Pure AND Equations & Two Workers Product Rule\n- **Pure AND Equations**: 2M + 3W in 8 days; 3M + 2W in 7 days. How long for 5M + 4W?\n  - $(2M + 3W) \\times 8 = (3M + 2W) \\times 7 \\implies 16M + 24W = 21M + 14W \\implies \\mathbf{1M = 2W}$.\n  - $7W \\to 8\\text{ days} \\implies 5M + 4W = 14W \\to \\mathbf{4\\text{ Days}}$.\n- **Two Workers Product/Sum Rule**:\n  - Together time $= \\mathbf{\\frac{xy}{x + y}}$.\n  - One worker remaining time $= \\mathbf{\\frac{xy}{|x - y|}}$.\n\n#### Page 9, 10 & 11: LCM Work Parts Method & Multi-Stage Workers\n- **LCM Method Logic**: LCM of individual days gives Total Work Parts. Efficiency $= \\frac{\\text{Total Parts}}{\\text{Days}}$.\n- **Worked Example**: A (25d), B (30d), C (10d). Total LCM $= 150$ parts. ($A=6, B=5, C=15$).\n  - All start. After 3 days A left ($57$ parts done). After 2 more days C left ($26$ parts done). Remaining $= 67$ parts.\n  - B finishes remaining in $\\frac{67}{3} = \\mathbf{22 \\frac{1}{3}\\text{ Days}}$.\n\n#### Page 12, 13 & 14: Alternate Days Cycle Rules & Assisted Days\n- **Alternate Days Cycle**: Work done in 2 days cycle $= A + B$. Leftover work done by whoever started!\n  - Example: A (36d), B (40d). Total $= 120$ parts ($A=4, B=3$). Cycle 2 days $= 7$ parts.\n  - $17 \\times 7 = 119$ parts in 34 days. Leftover 1 part by A $\\implies \\mathbf{34 \\frac{1}{4}\\text{ Days}}$ (If A starts).\n  - If B starts $\\implies \\mathbf{34 \\frac{1}{3}\\text{ Days}}$.\n- **Assisted Alternate Days**: A (20d), B (30d), C (40d). Total $= 120$ parts ($A=6, B=4, C=3$).\n  - Day 1 (A+B) $= 10$, Day 2 (A+C) $= 9$. 2 days $= 19$ parts.\n  - 6 cycles ($114$ parts) $= 12$ days. Leftover 6 parts by A+B $\\implies \\mathbf{12 \\frac{3}{5}\\text{ Days}}$.\n\n#### Page 15 & 16: Pairwise Together Trick & Efficiency Percentages\n- **Pairwise Together Trick**: A+B (12d), B+C (15d), A+C (20d). Total $= 60$ parts.\n  - $2(A+B+C) = 5+4+3 = 12 \\implies A+B+C = 6$ parts/day.\n  - All together $= \\frac{60}{6} = \\mathbf{10\\text{ Days}}$.\n- **Fraction Work**: $\\frac{3}{7}$th work in 24 days $\\implies$ Total $= 56$ days, Remaining $= \\mathbf{32\\text{ Days}}$.\n- **Efficiency Percentage**: B is $50\\%$ more efficient than A (60d).\n  - $100 \\times 60 = 150 \\times D_2 \\implies D_2 = \\mathbf{40\\text{ Days}}$.\n\n#### Page 17, 18, 19 & 20: Efficiency Change, Leaving at END & Work & Wages\n- **Efficiency Change Problem**: A & B finish in 5 days. If A works $2\\times$ and B works $\\frac{1}{3}\\times$, finished in 3 days.\n  - $(A+B) \\times 5 = (2A + \\frac{1}{3}B) \\times 3 \\implies A = 4B \\implies \\mathbf{A \\text{ alone } = 6 \\frac{1}{4}\\text{ Days}}$.\n- **Leaving BEFORE Completion (at the END)**:\n  - Calculate backwards for persons working alone in last days, subtract from Total Parts, then divide remainder by joint efficiency.\n  - Example: A (20d), B (30d). Total $= 60$ parts. B left 3 days before completion.\n  - A alone last 3 days $= 3 \\times 3 = 9$ parts. Remainder $= 51 / 5 = 10 \\frac{1}{5}$ days. Total $= \\mathbf{13 \\frac{1}{5}\\text{ Days}}$.\n- **Work & Wages Rule**: Total wages are divided in the **Daily Work Unit Ratio**!\n",
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
        "name": "Speed, Distance and Time (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 18 Handwritten PDF pages: DST Triangle, km/h to m/s 5/18 conversion, Train Crossing 4 Cases, Relative Speeds, Train Overtaking Platform Lengths, Opposite/Same Direction Meeting Times, Overtaking Pursuit Overtake Times, Stoppage Time Formula, Walking vs Riding Logics, Speed Fraction Late Rules, Late/Early Distance Formulas, Square Root Destination Meeting Formula, Circular Track Crossings, and Hourly Speed Arithmetic Series.",
        "icon": "\ud83c\udfce\ufe0f",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Speed, Distance and Time (18 Pages Transcribed)\n\n#### Page 1: Definitions & Unit Conversions\n- **Basic Formula**: $\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}$ (DST Triangle).\n- **Units Conversion Rules**:\n  - $\\text{km/h} \\to \\text{m/s}$: Multiply by $\\mathbf{\\frac{5}{18}}$.\n  - $\\text{m/s} \\to \\text{km/h}$: Multiply by $\\mathbf{\\frac{18}{5}}$.\n\n#### Page 2, 3 & 4: Train Crossing 4 Cases & Platform Lengths\n- **Case 1 (Standing Man/Pole)**: $\\text{Distance} = \\text{Length of Train}$, $\\text{Speed} = \\text{Train Speed}$.\n- **Case 2 (Platform/Bridge)**: $\\text{Distance} = \\text{Train Length} + \\text{Platform Length}$.\n- **Case 3 (Running Person)**:\n  - Same Direction: $\\text{Relative Speed} = \\text{Train Speed} - \\text{Person Speed}$.\n  - Opposite Direction: $\\text{Relative Speed} = \\text{Train Speed} + \\text{Person Speed}$.\n- **Case 4 (Two Trains)**: Distance is **ALWAYS SUMMED UP ($L_1 + L_2$)**!\n  - Opposite Direction: $\\text{Time} = \\frac{L_1 + L_2}{S_1 + S_2}$.\n  - Same Direction: $\\text{Time} = \\frac{L_1 + L_2}{|S_1 - S_2|}$.\n- **Two Platform Example**: Crosses $96\\text{m}$ platform in $12\\text{s}$ and $141\\text{m}$ platform in $15\\text{s}$.\n  - In $3\\text{s}$, covers $45\\text{m} \\implies \\text{Speed} = 15\\text{ m/s}$. Train Length $= (15 \\times 12) - 96 = \\mathbf{84\\text{ meters}}$.\n\n#### Page 5, 6, 7 & 8: Meeting Places & Different Start Times\n- **Hyd to Blr Meeting**: $560\\text{ km}$ apart, start at 6 AM ($80\\text{ kmph}$ & $60\\text{ kmph}$).\n  - Relative Speed $= 140\\text{ kmph} \\implies \\text{Time} = \\frac{560}{140} = \\mathbf{4\\text{ hours}}$ (10 AM).\n- **Different Start Times**: A and B $440\\text{ km}$ apart. P at 4 AM ($30\\text{ kmph}$), Q at 7 AM ($40\\text{ kmph}$).\n  - P covers $30 \\times 3 = 90\\text{ km}$ by 7 AM. Remaining $= 350\\text{ km}$.\n  - Relative Speed $= 70\\text{ kmph} \\implies \\text{Time} = \\frac{350}{70} = 5\\text{ hrs} \\implies$ Meet at **12:00 PM** ($240\\text{km}$ from A, $200\\text{km}$ from B).\n\n#### Page 9 & 10: Overtaking Pursuit & Average Speed LCM\n- **Same Direction Pursuit**: Rajdhani 14:30 ($60\\text{ kmph}$), Duronto 16:30 ($80\\text{ kmph}$).\n  - Lead $= 120\\text{ km}$. Relative $= 20\\text{ kmph} \\implies \\text{Overtake} = \\frac{120}{20} = 6\\text{ hrs} \\implies \\mathbf{480\\text{ km from Delhi}}$.\n- **Average Speed Formulas**:\n  - Equal Distances: $\\text{Average Speed} = \\mathbf{\\frac{2xy}{x + y}}$.\n  - General: $\\text{Average Speed} = \\frac{\\text{Total Distance}}{\\text{Total Time}}$.\n\n#### Page 11 & 12: Stoppage Time Formula & Walking vs Riding\n- **Train Stoppage Formula**: Excluding $= 40\\text{ kmph}$, Including $= 25\\text{ kmph}$.\n  $$\\text{Stoppage Time (min/hr)} = \\frac{\\text{Excluding} - \\text{Including}}{\\text{Excluding}} \\times 60 = \\frac{40 - 25}{40} \\times 60 = \\mathbf{22.5\\text{ minutes/hour}}$$\n- **Walking vs Riding Logic**: Walking + Riding $= 5\\text{h } 45\\text{m}$. Riding both ways saves 2 hrs.\n  - Walking both ways loses 2 hrs $\\implies 5\\text{h } 45\\text{m} + 2\\text{h} = \\mathbf{7\\text{ hours } 45\\text{ minutes}}$!\n\n#### Page 13, 14 & 15: Speed Inversion, Late/Early Distance & Destination Square Root\n- **Speed Ratio Inversion**: Walking at $\\frac{5}{6}$th usual speed, 10 mins late.\n  - Speed $5:6 \\implies$ Time $6:5 \\implies$ Diff $1 \\to 10\\text{m} \\implies$ Usual time $= 5 \\times 10 = \\mathbf{50\\text{ minutes}}$.\n- **Late & Early Distance Formula**: $30\\text{ kmph}$ (10m late) vs $40\\text{ kmph}$ (5m early).\n  $$\\text{Distance} = \\frac{S_1 \\times S_2}{|S_1 - S_2|} \\times \\frac{\\text{Time Diff (mins)}}{60} = \\frac{30 \\times 40}{10} \\times \\frac{15}{60} = \\mathbf{30\\text{ km}}$$\n- **Destination Square Root Formula**: Two trains meet, then reach destinations in $T_1 = 9\\text{h}, T_2 = 16\\text{h}$. $S_1 = 80\\text{ kmph}$.\n  $$\\frac{S_1}{S_2} = \\sqrt{\\frac{T_2}{T_1}} \\implies \\frac{80}{S_2} = \\sqrt{\\frac{16}{9}} = \\frac{4}{3} \\implies S_2 = \\mathbf{60\\text{ kmph}}$$\n\n#### Page 16, 17 & 18: Circular Track Crossings & Hourly Speed Increment\n- **Circular Track Crossing**: A (1 round/hr), B (6 rounds/hr) from 7:30 AM.\n  - Relative $= 5\\text{ RPH} \\implies \\text{Time} = \\frac{1}{5}\\text{ hr} = 12\\text{ mins} \\implies$ Cross at **7:42 AM**.\n- **Hourly Speed Arithmetic Series**: Starts $35\\text{ kmph}$, $+2\\text{ kmph}$ every hour for 12 hrs.\n  - $\\text{Total Distance} = (35 \\times 12) + (12 \\times 11) = 420 + 132 = \\mathbf{552\\text{ km}}$.\n",
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
        "name": "Problems on Trains (PDF)",
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
                "title": "1. Problems on Trains (PDF) Core Principle",
                "front": "What is the main formula for Problems on Trains (PDF)?",
                "back": "Master core formulas and shortcut tricks for placement speed!",
                "badge": "\ud83d\udca1 Core Rule"
            }
        ]
    },
    {
        "id": 10,
        "slug": "boats-streams",
        "name": "Boats and Streams (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 3 Handwritten PDF pages: Downstream & Upstream Definitions, Boat & Stream Speed Averages, Round-Trip Distance Formula, and Simultaneous Equation Factor Substitutions.",
        "icon": "\ud83d\udea4",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Boats and Streams (3 Pages Transcribed)\n\n#### Page 1: Core Definitions & Speed Formulas\n- **Water Flow Effect**: Water flow affects rowing speed.\n  - **Downstream Speed ($D$)**: $\\text{Boat Speed} + \\text{Stream Speed} = x + y$.\n  - **Upstream Speed ($U$)**: $\\text{Boat Speed} - \\text{Stream Speed} = x - y$.\n- **Speed Formulas when $D$ and $U$ are given**:\n  $$\\text{Boat Speed in Still Water } (x) = \\frac{D + U}{2}$$\n  $$\\text{Stream / Current Speed } (y) = \\frac{D - U}{2}$$\n- **Worked Example 1**: Person rows at $8\\text{ kmph}$ in still water, takes 8 hours round trip. Stream speed $= 2\\text{ kmph}$. Find distance between A and B.\n  - Upstream $= 8 - 2 = 6\\text{ kmph}$, Downstream $= 8 + 2 = 10\\text{ kmph}$.\n\n#### Page 2 & 3: Round-Trip Distance Formula & Factor Substitution\n- **Round-Trip Distance Formula**:\n  $$\\text{Distance} = \\frac{\\text{Product of Speeds}}{\\text{Sum of Speeds}} \\times \\text{Total Time} = \\frac{6 \\times 10}{6 + 10} \\times 8 = \\mathbf{30\\text{ km}}$$\n- **Factor Substitution Method**: 40km U + 55km D in 13h; 30km U + 44km D in 10h.\n  - Factor trial: $D = 11\\text{ kmph} \\implies \\frac{55}{11} = 5\\text{h} \\implies U = \\frac{40}{13 - 5} = 5\\text{ kmph}$.\n  - Verify Eq 2: $\\frac{30}{5} + \\frac{44}{11} = 6 + 4 = 10\\text{h}$ (Verified!).\n  - Boat Speed $(x) = \\frac{11 + 5}{2} = \\mathbf{8\\text{ kmph}}$.\n  - Stream Speed $(y) = \\frac{11 - 5}{2} = \\mathbf{3\\text{ kmph}}$.\n",
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
        "name": "Pipes and Cisterns (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 5 Handwritten PDF pages: Extension of Time & Work, Filling (+ve) vs Emptying (-ve) Units, Closing Filling Pipes Rules, Highest Work Unit Buffer Rule in Alternate Minutes, and Target Closure Timing Calculations.",
        "icon": "\ud83d\udeb0",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Pipes and Cisterns (5 Pages Transcribed)\n\n#### Page 1: Time & Work Extension & Core Formulas\n- **Core Principle**: Pipes and Cisterns are an extension of Time and Work.\n  - BUT here, there is an element of **DESTROYING THE WORK** (i.e. sometimes pipes will be filling and simultaneously emptying!).\n- **Core Formulas**:\n  - (i) When both A and B are **Filling**:\n    $$\\text{Total Time} = \\mathbf{\\frac{xy}{x + y}}$$\n  - (ii) When one is **Filling** ($x$) and one is **Emptying** ($y$):\n    $$\\text{Total Time} = \\mathbf{\\frac{xy}{|x - y|}}$$\n\n#### Page 2 & 3: Negative Emptying Units & Pipe Closing Rules\n- **Negative Units Principle**: Entities responsible for **emptying are taken as NEGATIVE (-ve)**!\n  - Process uses LCM partitioning into total work units.\n- **Multi-Pipe Worked Example**: Pipe A (25m fill $+6$), Pipe B (30m fill $+5$), Pipe C (50m empty $-3$). Total $= 150$ units.\n  - All opened simultaneously. After 7 mins, A closed ($8 \\times 7 = 56$ units done).\n  - After 4 more mins, C closed ($(5 - 3) \\times 4 = 8$ units done).\n  - Total filled $= 64$ units. Remaining $= 86$ units.\n  - B fills remaining in $\\frac{86}{5} = \\mathbf{17 \\frac{1}{5}\\text{ mins}}$!\n- **Tank Never Filled Rules**:\n  - If all filling pipes are closed BEFORE the tank gets filled, the tank will **NEVER get filled**!\n  - In such cases, time taken to **EMPTY** the tank is calculated ONLY from the units filled up to that point.\n  - If emptying rate is greater than filling rate, the tank will also **NEVER get filled**!\n\n#### Page 4 & 5: Alternate Minutes Highest-Unit Buffer & Target Closure Time\n- **Alternate Minutes Cycle & Buffer Rule**:\n  - A (20m fill $+6$), B (30m fill $+4$), C (40m empty $-3$). Total $= 120$ units.\n  - Cycle $A \\to B \\to C$: 3 minutes $= 6 + 4 - 3 = 7$ units.\n  - **CRITICAL HANDWRITTEN RULE**: Unlike Time & Work, HERE we stop nearest to total capacity by maintaining a **minimum difference equal to the HIGHEST filling unit** (+6) to prevent overflow before emptying!\n  - 16 cycles ($7 \\times 16 = 112$ units) $= 48$ minutes.\n  - Next 1 min (A opened, $+6$) $= 118$ units in 49 mins.\n  - Next B opened (needs 2 out of 4) $= \\frac{2}{4} = \\frac{1}{2}$ min.\n  - Total time to fill $= \\mathbf{49 \\frac{1}{2}\\text{ minutes}}$!\n- **Target Closure Time Problem**: Pipe A (24m fill), Pipe B (32m fill). Tank must fill in 18 mins. When to close B?\n  - Total $= 96$ units. $A = 4$ units/min, $B = 3$ units/min.\n  - A works all 18 mins $\\implies 4 \\times 18 = 72$ units.\n  - Remaining for B $= 96 - 72 = 24$ units.\n  - Time for B $= \\frac{24}{3} = \\mathbf{8\\text{ minutes}}$. Close B after 8 minutes!\n",
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
        "name": "Permutations & Combinations (Master Handwritten PDF Edition)",
        "description": "100% Faithful Transcription of 13 Handwritten PDF pages: Arrangements vs Selection, nPr & nCr Identities, Identical Objects Division, Gap Method for Separation, Circular & Necklace Rules, Digit Formation with/without Zero, At Least Committee Rules, Polygon Diagonals n(n-3)/2, Handshakes vs Tickets Distinctions, and Tournament Match Equations.",
        "icon": "\ud83c\udfb2",
        "xp_reward": 500,
        "formula_sheet": "### \ud83d\udcc4 Master Handwritten Notes: Permutations & Combinations (13 Pages Transcribed)\n\n#### Page 1 & 2: Arrangements vs Selection & Key Identities\n- **Core Distinction**:\n  - **Permutation ($n P_r$)**: Arrangements (Position matters!). Multiply $r$ numbers from $n$ downwards.\n  - **Combination ($n C_r$)**: Selection (Just choosing!). Multiply $r$ numbers from $n$ downwards and divide by $r!$.\n- **Key Relation**:\n  $$n P_r = n C_r \\times r!$$\n- **Important Identities**:\n  - $n P_n = n!$, $n P_{n-1} = n!$, $n P_1 = n$, $n P_0 = 1$.\n  - $n C_r = n C_{n-r}$, $n C_n = n C_0 = 1$, $n C_1 = n$, $n C_{n-1} = n$.\n- **Identical Objects Rule**:\n  - Words with repeated letters (e.g. `BALLOON`: 7 letters, 2 Ls, 2 Os) $\\implies \\frac{7!}{2! 2!} = \\mathbf{1260}$.\n\n#### Page 3, 4 & 5: Vowels Together, GAP Method & Sitting Line\n- **Vowels Always Together (`TENDULKAR`)**:\n  - 9 letters, 3 vowels (`E, U, A`). Treat vowels as **single unit** $(EUA) \\implies (6 + 1) = 7$ units.\n  - Ways $= 7! \\times 3! = 5040 \\times 6 = \\mathbf{30,240}$.\n- **Vowels Never Together (GAP METHOD)**:\n  - Used when \"No two elements are together\".\n  - $\\text{Not Together} = \\text{Total} - \\text{Together}$.\n  - 3 boys and 2 girls (girls not together): Arrange boys ($3! = 6$), create 4 gaps `_ B _ B _ B _`, place girls ($4 C_2 \\times 2! = 12$).\n  - Total $= 6 \\times 6 = \\mathbf{36\\text{ ways}}$.\n  - `TENDULKAR` vowels never together: 6 consonants ($6! = 720$), 7 gaps for 3 vowels ($7 P_3 = 210$) $\\implies 720 \\times 210 = \\mathbf{151,200}$.\n\n#### Page 6 & 7: Circular Permutations & Number Formation Rules\n- **Circular Permutations**:\n  - Normal Circle $= (n - 1)!$.\n  - Necklace / Chain (clockwise = anticlockwise same) $= \\mathbf{\\frac{(n - 1)!}{2}}$.\n- **Number Formation Rules (3-Digit Numbers)**:\n  - Without Repetition, No Zero $\\{1,2,3,4,5\\} \\implies 5 P_3 = \\mathbf{60}$.\n  - Without Repetition, With Zero $\\{0,1,2,3,4\\} \\implies 1^{\\text{st}}$ digit 4 choices (no 0) $\\implies 4 \\times 4 \\times 3 = \\mathbf{48}$.\n  - With Repetition, No Zero $\\{1,2,3,4,5\\} \\implies 5^3 = \\mathbf{125}$.\n  - With Repetition, With Zero $\\{0,1,2,3,4\\} \\implies 4 \\times 5 \\times 5 = \\mathbf{100}$.\n- **4-Digit ATM PINs**: Total possible $= 10^4 = \\mathbf{10,000}$.\n\n#### Page 8, 9 & 10: Committee Selection & Polygon Diagonals\n- **At Least Committee Problem**: 5 men, 4 women. Committee of 5 members with **at least 2 women**:\n  - $(4 C_2 \\times 5 C_3) + (4 C_3 \\times 5 C_2) + (4 C_4 \\times 5 C_1) = 60 + 40 + 5 = \\mathbf{105\\text{ ways}}$.\n- **Octagon Triangles**: Vertices of Octagon ($n=8$) $\\implies 8 C_3 = \\mathbf{56\\text{ triangles}}$.\n- **Polygon Diagonals Formula**:\n  $$\\text{Number of Diagonals} = \\mathbf{\\frac{n(n - 3)}{2}}$$\n  - Hexagon ($n=6$) $\\implies \\frac{6(3)}{2} = \\mathbf{9\\text{ diagonals}}$.\n- **Inviting Friends**: Invite 1 or more of 6 friends $\\implies 2^n - 1 = 2^6 - 1 = \\mathbf{63\\text{ ways}}$.\n\n#### Page 11, 12 & 13: Handshakes vs Tickets & Tournament Matches\n- **Handshakes vs Tickets Distinction**:\n  - **Handshakes & Matches** (Order doesn't matter) $\\implies n C_2$. (Example: 20 people handshakes $= 20 C_2 = \\mathbf{190}$).\n  - **Gifts & Railway Tickets** (Order matters!) $\\implies n P_2$. (Example: 22 stations tickets $= 22 P_2 = 22 \\times 21 = \\mathbf{462}$).\n- **Cricket Tournament Matches**: 20 teams divided into 2 groups of 10.\n  - Group matches $= 10 C_2 + 10 C_2 = 45 + 45 = 90$.\n  - Knockouts $= 4 \\text{ (Quarters)} + 2 \\text{ (Semis)} + 1 \\text{ (Final)} = 7$. Total $= \\mathbf{97\\text{ matches}}$.\n- **Chess Tournament Participants**: $n C_2 = 325 \\implies \\frac{n(n - 1)}{2} = 325 \\implies n(n - 1) = 650 = 26 \\times 25 \\implies \\mathbf{n = 26\\text{ participants}}$.\n",
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
        "id": 16,
        "slug": "probability",
        "name": "Probability (PDF)",
        "description": "Master coin tosses, dice rolls, card decks, and conditional probability.",
        "icon": "\ud83c\udfb0",
        "xp_reward": 130,
        "formula_sheet": "### \ud83d\udcc4 Master Cheat Sheet: Probability (PDF)\n\n# Probability\n\n- Probability measures the chance of an event happening.\n- **Probability** = Favorable outcomes / Total outcomes\n- **Range of Probability**:\n  - `0` = Impossible Event\n  - `1` = Certain Event\n  - `0 <= P <= 1` => Possible Event\n- By Permutations and Combinations, Probability = our selections / Total selections\n\n## Rules\n- **Complement Rule**: `P(not E) = 1 - P(E)` (used for \"At least one\")\n- **Addition Rule (OR)**: If events are mutually exclusive, `P(A or B) = P(A) + P(B)`\n- **Multiplication Rule (AND)**: For independent events, `P(A and B) = P(A) * P(B)`\n- **Intersection (AND)**: A and B -> Both events happen together.\n- **Union (OR)**: A or B -> at least one of the events occurs.\n  - `P(A U B) = P(A) + P(B) - P(A \u2229 B)`\n  - `P(A \u2229 B) = P(A) * P(B)`\n\n## Coins\n- For `n` coins, Probability of exactly `r` heads: `nCr / 2^n`\n\n## Dice Probability\n- Total outcomes = `6^n`, where `n` = number of dice\n- Concept: If they ask even/odd outcomes, just use analogy with coins concept (i.e. No. of Dice -> coins, No. of odds -> No. of heads, No. of evens -> No. of tails).\n- Irrespective of the number of dice rolled, the odd product occurs \"only\" when all the dice return odd numbers.\n- **Even Product Probability** = `1 - (3/6)^n = 1 - (1/2)^n = (2^n - 1) / 2^n`\n- **6 sides consideration type models (Required output on some tables)**:\n  - **Sum of 2 dice**:\n    - Sum: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\n    - Prob (out of 36): 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1\n  - **Sum of 3 dice**:\n    - Sum: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18\n    - Prob (out of 216): 1, 3, 6, 10, 15, 21, 25, 27, 27, 25, 21, 15, 10, 6, 3, 1\n- Doublet and Triplet happens 6 times.\n\n## Cards Concept\n- Total 52 cards: 26 cards Red, 26 cards Black\n- Red -> Diamond (13), Heart (13)\n- Black -> Spade (13), Club (13)\n- Total 16 face cards:\n  - Kings -> 4 (1 Diamond, 1 Heart, 1 Club, 1 Spade)\n  - Queens -> 4 (1 Diamond, 1 Heart, 1 Club, 1 Spade)\n  - Jacks -> 4 (1 Diamond, 1 Heart, 1 Club, 1 Spade)\n  - Ace -> 4 (1 Diamond, 1 Heart, 1 Club, 1 Spade)\n- 36 Non face cards (2 to 10)",
        "questions": [
            {
                "difficulty": "intermediate",
                "text": "What is the Probability of having 53 Sundays in a non-leap year?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Answer is 1/7."
            },
            {
                "difficulty": "intermediate",
                "text": "2 Numbers are selected at random from a set of 1 to 100, what is the probability of getting a Prime number?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Select 2 numbers = 25C2. From 100 numbers = 100C2. Probability = 25C2 / 100C2 = (25 x 24 / 2) / (100 x 99 / 2) = 2/33."
            },
            {
                "difficulty": "intermediate",
                "text": "From 8 Red balls and 4 Green Balls, 3 Balls are picked randomly. What is the Probability that there is at least one Red Ball?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Usually: (8C1 * 4C2 + 8C2 * 4C1 + 8C3) / 12C3 = (48 + 112 + 56) / 220 = 54/55.\nOR use complement Rule: 1 - 4C3 / 12C3 = 1 - 4/220 = 1 - 1/55 = 54/55."
            },
            {
                "difficulty": "intermediate",
                "text": "6 coins are tossed. Find Probability of getting All Heads or All tails.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Total outcomes = 2^6. Probability = 1/2^6 + 1/2^6 = 1/32."
            },
            {
                "difficulty": "intermediate",
                "text": "5 coins are tossed. Find the Probability of getting exactly 3 Heads and 2 Tails.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Let n = number of coins. Then n! / (H! T!) / 2^n = 5! / (3! 2!) / 2^5 = 10 / 32 = 5/16. OR choose which 3 of the positions are Heads = 5C3 = 10. P = 5C3 / 2^5 = 10/32 = 5/16."
            },
            {
                "difficulty": "intermediate",
                "text": "8 coins are tossed. At least 6 Heads?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "6H 2T OR 7H 1T OR 8H. => (8C6 + 8C7 + 8C8) / 2^8 = (28 + 8 + 1) / 256 = 37/256."
            },
            {
                "difficulty": "intermediate",
                "text": "5 coins tossed. Atmost 2 Heads Probability?",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "2H 3T OR 1H 4T OR 5T. (5!/(2!3!) + 5!/(1!4!) + 5!/5!) / 2^5 = (10 + 5 + 1) / 32 = 16/32 = 1/2."
            },
            {
                "difficulty": "intermediate",
                "text": "A card is drawn from a pack of cards. What is the Probability that the card is 1. Black suit colour 2. A spade card 3. A red face card 4. A face card of club 5. Diamond or King",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "1. 26C1 / 52C1 = 26/52 = 1/2.\n2. 13C1 / 52C1 = 13/52 = 1/4.\n3. 8C1 / 52C1 = 8/52 = 2/13.\n4. 4C1 / 52C1 = 4/52 = 1/13.\n5. (13C1 + 4C1 - 1C1) / 52C1 = (13+4-1)/52 = 16/52 = 4/13."
            },
            {
                "difficulty": "intermediate",
                "text": "Two cards are drawn at Random what is the Probability that 1. Both are aces. 2. No face card 3. Atleast one King 4. No Diamond 5. one king and one Queen",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "1. 4C2 / 52C2 = 6/1326 = 1/221.\n2. 36C2 / 52C2 = 105/221.\n3. Atleast one = Total - None = 1 - 48C2 / 52C2 = 1 - 188/221 = 33/221.\n4. 39C2 / 52C2 = 19/34.\n5. (4C1 * 4C1) / 52C2 = 16/1326 = 8/663."
            },
            {
                "difficulty": "advanced",
                "text": "A Bag contains 6 Red Balls, 4 Blue Balls, 2 Green Balls and 3 Yellow Balls. If 4 Bales are Picked at Random, what is the Probability that one is green, two are blue and one is red.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "(2C1 * 4C2 * 6C1) / 15C4 = (2 * 6 * 6) / 1365 = 72/1365 = 24/455."
            },
            {
                "difficulty": "advanced",
                "text": "Two Persons wife and Husband appear in an interview for two vacancies. If the Probabilities of their selections are 1/4 and 1/6 respectively. then the Probability that 1. None of them selected 2. Exactly one of them selected 3. Atleast one of them selected 4. Both of them selected",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "1. None of them selected -> (3/4) * (5/6) = 15/24 = 5/8.\n2. Exactly one of them selected => (1/4 * 5/6) + (3/4 * 1/6) = 5/24 + 3/24 = 8/24 = 1/3.\n3. Atleast one of them selected => Total - None = 1 - 5/8 = 3/8.\n4. Both of them selected => 1/4 * 1/6 = 1/24."
            },
            {
                "difficulty": "advanced",
                "text": "A speaks truth in 60% cases and B speaks truth in 45% of the cases. In what % of cases are they likely to contradict each other, in narrating.",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "Contradict means \"not on the same statement\".\nA: True 60/100, False 40/100.\nB: True 45/100, False 55/100.\n=> (60/100 * 55/100) + (45/100 * 40/100) = 3300/10000 + 1800/10000 = 5100/10000 = 51%."
            },
            {
                "difficulty": "advanced",
                "text": "The Probability of Solving a Problem by 3 students A, B, C is 1/2, 1/3 and 1/4 respectively. The Probability that the Problem will be solved is",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "A solving 1/2, Not solving 1/2. B solving 1/3, Not solving 2/3. C solving 1/4, Not solving 3/4. Atleast one = Total - None. 1 - (1/2 * 2/3 * 3/4) = 1 - 1/4 = 3/4."
            },
            {
                "difficulty": "advanced",
                "text": "Tickets numbered 1 to 50 are mixed up and then a ticket is drawn at random. what is the Probability that the ticket drawn is a number which is multiple of a) 3 or 7 b) 3 and 7",
                "options": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_option_index": 0,
                "explanation": "a) 16 + 7 - 2 = 21. => 21/50.\nb) 2/50 = 1/25."
            }
        ],
        "flashcards": [
            {
                "title": "Rule 1: Probability measures the chance of ",
                "front": "What is the rule or formula for: Probability measures the chance of an event happening.?",
                "back": "Handwritten PDF Rule:\nProbability measures the chance of an event happening.\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 1"
            },
            {
                "title": "Rule 2: Probability = Favorable outcomes / ",
                "front": "What is the rule or formula for: Probability = Favorable outcomes / Total outcomes?",
                "back": "Handwritten PDF Rule:\nProbability = Favorable outcomes / Total outcomes\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 2"
            },
            {
                "title": "Rule 3: Range of Probability:",
                "front": "What is the rule or formula for: Range of Probability:?",
                "back": "Handwritten PDF Rule:\nRange of Probability:\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 3"
            },
            {
                "title": "Rule 4: By Permutations and Combinations, P",
                "front": "What is the rule or formula for: By Permutations and Combinations, Probability = our selections / Total selections?",
                "back": "Handwritten PDF Rule:\nBy Permutations and Combinations, Probability = our selections / Total selections\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 4"
            },
            {
                "title": "Rule 5: Complement Rule: `P(not E) = 1  P(E",
                "front": "What is the rule or formula for: Complement Rule: `P(not E) = 1  P(E)` (used for \"At least one\")?",
                "back": "Handwritten PDF Rule:\nComplement Rule: `P(not E) = 1  P(E)` (used for \"At least one\")\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 5"
            },
            {
                "title": "Rule 6: Addition Rule (OR): If events are m",
                "front": "What is the rule or formula for: Addition Rule (OR): If events are mutually exclusive, `P(A or B) = P(A) + P(B)`?",
                "back": "Handwritten PDF Rule:\nAddition Rule (OR): If events are mutually exclusive, `P(A or B) = P(A) + P(B)`\nMaster this concept for high-speed placement problem solving!",
                "badge": "\ud83d\udca1 Concept 6"
            }
        ]
    },
    {
        "id": 17,
        "slug": "mensuration",
        "name": "Mensuration 2D & 3D (PDF Master Edition)",
        "description": "Master 2D/3D formulas, Ratio Side-Area-Volume conversions, Cow Ungrazed Field, Wheel Revolutions, & Hollow Pipe metal rules.",
        "icon": "\ud83d\udcd0",
        "xp_reward": 150,
        "formula_sheet": "### \ud83d\udcc4 Master Cheat Sheet: Mensuration 2D & 3D (PDF Master Edition)\n\n# Mensuration Formula Sheet\n\n## 2D Mensuration (only has Perimeter, Area)\n\n1. **Square**\n   - Perimeter = 4a\n   - Area = a\u00b2\n   - Diagonal = a\u221a2\n   - All the sides are equal\n   - All the angles are 90\u00b0\n\n2. **Rectangle**\n   - Perimeter = 2(l+b)\n   - Area = l \u00d7 b\n   - Diagonal = \u221a(l\u00b2 + b\u00b2)\n   - Only opposite sides are equal\n   - All the angles are 90\u00b0\n\n3. **Rhombus**\n   - Perimeter = 4a\n   - Area = \u00bd \u00d7 d\u2081 \u00d7 d\u2082 (where d\u2081, d\u2082 are lengths of the diagonals)\n\n4. **Circle**\n   - Circumference = 2\u03c0r\n   - Area = \u03c0r\u00b2\n   - Diameter = 2r\n   - \u03c0 = 22/7 or 3.14\n\n5. **Equilateral Triangle**\n   - All the three sides are equal\n   - Perimeter = 3a\n   - Area = (\u221a3/4)a\u00b2\n   - Height = (\u221a3/2)a\n\n6. **Right-angled Triangle (Half of a Rectangle)**\n   - Area = \u00bd \u00d7 b \u00d7 h\n   - Perimeter = AB + BC + AC\n   - Pythagoras Theorem: Hypotenuse\u00b2 = Adjacent\u00b2 + Opposite\u00b2 \u21d2 AC = \u221a(AB\u00b2 + BC\u00b2)\n\n7. **Triangle with sides a, b, c**\n   - Perimeter = a + b + c\n   - Area = \u221a(s(s-a)(s-b)(s-c))\n   - where s = (a+b+c)/2\n\n8. **Trapezium**\n   - Area = \u00bd \u00d7 (Sum of two parallel sides) \u00d7 (Distance between them)\n\n## 3D Mensuration (has Volume, Area, Perimeter)\n\n1. **Cube**\n   - LSA (Lateral Surface Area) = 4a\u00b2\n   - TSA (Total Surface Area) = 6a\u00b2\n   - Volume = a\u00b3\n   - Diagonal = a\u221a3\n\n2. **Cuboid**\n   - LSA = 2(l+b)h\n   - TSA = 2(lb + bh + hl)\n   - Volume = l \u00d7 b \u00d7 h\n   - Diagonal = \u221a(l\u00b2 + b\u00b2 + h\u00b2)\n\n3. **Sphere**\n   - No LSA\n   - TSA = 4\u03c0r\u00b2\n   - Volume = 4/3 \u03c0r\u00b3\n\n4. **Hemisphere**\n   - CSA (Curved Surface Area) = 2\u03c0r\u00b2\n   - TSA = 3\u03c0r\u00b2\n   - Volume = 2/3 \u03c0r\u00b3\n\n5. **Cylinder**\n   - CSA = 2\u03c0rh\n   - TSA = 2\u03c0rh + 2\u03c0r\u00b2 = 2\u03c0r(r+h)\n   - Volume = \u03c0r\u00b2h\n\n6. **Cone**\n   - Slant Height (l) = \u221a(r\u00b2 + h\u00b2)\n   - Volume = 1/3 \u03c0r\u00b2h\n   - CSA = \u03c0rl\n   - TSA = \u03c0r\u00b2 + \u03c0rl = \u03c0r(r+l)\n\n## Miscellaneous Concepts and Shortcuts\n\n- **Ratios format in 2-Dimensions:**\n  1. If sides Ratio was given, then we get Areas Ratio by squaring the given Ratios individually.\n  2. If Areas Ratio was given, then we get sides Ratio by square rooting (\u221a) the given Ratios individually.\n\n- **Ratios format in 3-Dimensions:**\n  1. If sides Ratio was given, then we get Volumes Ratio by cubing the given Ratios individually.\n  2. If Volumes Ratio was given, then we get sides Ratio by cube rooting (\u221b) the given Ratios individually.\n  3. If in 3-D Areas Ratio was given, then we get Volumes Ratio by converting them into sides Ratio (by square rooting) and from then to cubing them to get Volumes Ratio.\n\n- **Percentage Based Miscellaneous:**\n  - Area \u2192 sq. units\n  - Perimeter \u2192 units\n  - Volume \u2192 cubic units\n  - For `units` \u2192 we perform only one increase/decrease operation\n  - For `sq. units` \u2192 we perform two increase/decrease operations\n  - For `cubic units` \u2192 we perform three increase/decrease operations\n",
        "questions": [
            {
                "difficulty": "intermediate",
                "text": "The ratio of respective sides of two rectangles (or two squares or two circles) is 19:17. Find the ratio of their respective areas?",
                "options": [
                    "361:289",
                    "19:17",
                    "289:361",
                    "17:19"
                ],
                "correct_option_index": 0,
                "explanation": "From side to area, we square the ratios: 19\u00b2 : 17\u00b2 = 361 : 289"
            },
            {
                "difficulty": "intermediate",
                "text": "The ratio of areas of two squares is 256:169. Find the ratio of their respective sides?",
                "options": [
                    "16:13",
                    "13:16",
                    "256:169",
                    "19:16"
                ],
                "correct_option_index": 0,
                "explanation": "From Area to side, we square root the ratios: \u221a256 : \u221a169 = 16:13"
            },
            {
                "difficulty": "intermediate",
                "text": "The Ratio of respective sides of two cuboids is 9:7. Find the ratio of their respective volumes.",
                "options": [
                    "729:343",
                    "81:49",
                    "9:7",
                    "343:729"
                ],
                "correct_option_index": 0,
                "explanation": "From side to volume, we cube the ratios: 9\u00b3 : 7\u00b3 = 729 : 343"
            },
            {
                "difficulty": "intermediate",
                "text": "The Ratio of volumes of two cubes is 1331:1728. Find the ratio of their respective sides.",
                "options": [
                    "11:12",
                    "12:11",
                    "13:12",
                    "11:13"
                ],
                "correct_option_index": 0,
                "explanation": "From volume to side, we cube root the ratios: \u221b1331 : \u221b1728 = 11:12"
            },
            {
                "difficulty": "advanced",
                "text": "The ratio of surface Areas of two spheres is 36:121. Find the ratio of their respective volumes?",
                "options": [
                    "216:1331",
                    "6:11",
                    "36:121",
                    "1331:216"
                ],
                "correct_option_index": 0,
                "explanation": "Convert Area to side, then side to volume. Area ratio 36:121 \u2192 Side ratio \u221a36:\u221a121 = 6:11 \u2192 Volume ratio 6\u00b3:11\u00b3 = 216:1331"
            },
            {
                "difficulty": "advanced",
                "text": "The ratio of volumes of two cubes is 125:729. Find the ratio of their respective Surface Areas?",
                "options": [
                    "25:81",
                    "5:9",
                    "125:729",
                    "81:25"
                ],
                "correct_option_index": 0,
                "explanation": "Convert Volume to side, then side to Area. Volume ratio 125:729 \u2192 Side ratio \u221b125:\u221b729 = 5:9 \u2192 Area ratio 5\u00b2:9\u00b2 = 25:81"
            },
            {
                "difficulty": "intermediate",
                "text": "The side of square (or radius of a circle) is decreased by 20%. Find the percentage change in its Area.",
                "options": [
                    "36% decrease",
                    "20% decrease",
                    "40% decrease",
                    "44% decrease"
                ],
                "correct_option_index": 0,
                "explanation": "Area is in sq. units, so we perform two successive decrease operations: -20 - 20 + (-20)(-20)/100 = -40 + 4 = -36%. This means a 36% decrease."
            },
            {
                "difficulty": "advanced",
                "text": "The length and breadth of a cuboid are increased by 10% and 20% respectively. Its height is decreased by 25%. Find % change in its volume?",
                "options": [
                    "1% decrease",
                    "1% increase",
                    "5% decrease",
                    "No change"
                ],
                "correct_option_index": 0,
                "explanation": "Three operations (Volume = L \u00d7 B \u00d7 H). First, L and B: 10 + 20 + (10\u00d720)/100 = 32% increase. Then with H (-25%): 32 - 25 + (32\u00d7(-25))/100 = 7 - 8 = -1%. 1% decrease."
            },
            {
                "difficulty": "intermediate",
                "text": "The area of circle is seven times that of circumference of a circle, what is the circumference (units) of a circle?",
                "options": [
                    "88 units",
                    "44 units",
                    "154 units",
                    "14 units"
                ],
                "correct_option_index": 0,
                "explanation": "Area = 7 \u00d7 Circumference \u21d2 \u03c0r\u00b2 = 7 \u00d7 2\u03c0r \u21d2 r = 14. Circumference = 2\u03c0r = 2 \u00d7 (22/7) \u00d7 14 = 88 units."
            },
            {
                "difficulty": "intermediate",
                "text": "A wire is bent in a form of a square encloses an area 484 m\u00b2. If the same wire is bent in the form of a circle, what will be the Area enclosed by the circle?",
                "options": [
                    "616 m\u00b2",
                    "484 m\u00b2",
                    "88 m\u00b2",
                    "154 m\u00b2"
                ],
                "correct_option_index": 0,
                "explanation": "Area of square = 484 \u21d2 side a = 22. Perimeter = 4a = 88, which is the length of the wire. For the circle, Circumference = 2\u03c0r = 88 \u21d2 2 \u00d7 (22/7) \u00d7 r = 88 \u21d2 r = 14. Area of circle = \u03c0r\u00b2 = (22/7) \u00d7 14 \u00d7 14 = 616 m\u00b2."
            },
            {
                "difficulty": "advanced",
                "text": "The side of cyclic Rhombus is 9 cm. find its Area.",
                "options": [
                    "81 cm\u00b2",
                    "18 cm\u00b2",
                    "36 cm\u00b2",
                    "45 cm\u00b2"
                ],
                "correct_option_index": 0,
                "explanation": "A cyclic Rhombus is a square because its angles are 90\u00b0 and diagonals are equal. Side = 9 cm. Area = 9 \u00d7 9 = 81 cm\u00b2."
            },
            {
                "difficulty": "intermediate",
                "text": "Find the area of the rectangle, with diagonal 20cm and length 16cm.",
                "options": [
                    "192 cm\u00b2",
                    "160 cm\u00b2",
                    "320 cm\u00b2",
                    "400 cm\u00b2"
                ],
                "correct_option_index": 0,
                "explanation": "Consider the right-angled triangle formed by length, breadth, and diagonal. By hypotenuse theorem, breadth = \u221a(20\u00b2 - 16\u00b2) = \u221a(400 - 256) = \u221a144 = 12. Area = L \u00d7 B = 16 \u00d7 12 = 192 cm\u00b2."
            },
            {
                "difficulty": "intermediate",
                "text": "The breadth of rectangular Plot is two-third of its length. If the area of a plot is 2400 m\u00b2, find its length.",
                "options": [
                    "60 m",
                    "40 m",
                    "80 m",
                    "120 m"
                ],
                "correct_option_index": 0,
                "explanation": "Breadth b = (2/3)l. Area = l \u00d7 b = 2400 \u21d2 l \u00d7 (2/3)l = 2400 \u21d2 (2/3)l\u00b2 = 2400 \u21d2 l\u00b2 = 3600 \u21d2 l = 60 m."
            },
            {
                "difficulty": "intermediate",
                "text": "Find the height of an isosceles triangle whose base is 8cm and equal sides are 5cm.",
                "options": [
                    "3 cm",
                    "4 cm",
                    "5 cm",
                    "6 cm"
                ],
                "correct_option_index": 0,
                "explanation": "Using Pythagoras theorem on half of the base: 5\u00b2 = 4\u00b2 + h\u00b2 \u21d2 h\u00b2 = 25 - 16 = 9 \u21d2 h = 3 cm."
            },
            {
                "difficulty": "intermediate",
                "text": "The Base and Height of a Parallelogram are 35 cm and 75 cm respectively. find its area?",
                "options": [
                    "2625 cm\u00b2",
                    "2525 cm\u00b2",
                    "2725 cm\u00b2",
                    "2825 cm\u00b2"
                ],
                "correct_option_index": 0,
                "explanation": "Area = Base \u00d7 Height = 35 \u00d7 75 = (55 - 20)(55 + 20) = 55\u00b2 - 20\u00b2 = 3025 - 400 = 2625 cm\u00b2."
            },
            {
                "difficulty": "intermediate",
                "text": "The length and breadth of a rectangle are in the ratio 5:3. Its Perimeter is 400 cm. find the area.",
                "options": [
                    "9375 cm\u00b2",
                    "8375 cm\u00b2",
                    "10375 cm\u00b2",
                    "1250 cm\u00b2"
                ],
                "correct_option_index": 0,
                "explanation": "Perimeter = 2(l+b) = 400 \u21d2 l+b = 200. With ratio 5:3, total 8 parts = 200. So 1 part = 25. Length = 5 \u00d7 25 = 125, Breadth = 3 \u00d7 25 = 75. Area = 125 \u00d7 75 = (100 + 25)(100 - 25) = 100\u00b2 - 25\u00b2 = 10000 - 625 = 9375 cm\u00b2."
            },
            {
                "difficulty": "advanced",
                "text": "The ratio of Length and breadth of a rectangle is 7:6. Its area is 378 sq.mts. find its diagonal.",
                "options": [
                    "\u221a765",
                    "\u221a441",
                    "\u221a324",
                    "21"
                ],
                "correct_option_index": 0,
                "explanation": "Let L = 7x, B = 6x. Area = L \u00d7 B = 378 \u21d2 42x\u00b2 = 378 \u21d2 x\u00b2 = 9 \u21d2 x = 3. So L = 21, B = 18. Diagonal = \u221a(21\u00b2 + 18\u00b2) = \u221a(441 + 324) = \u221a765."
            },
            {
                "difficulty": "intermediate",
                "text": "Find the total cost to pave a rectangular floor of measurements 32m x 14m, if cost per sq.mt is RS. 40?",
                "options": [
                    "\u20b9 17920",
                    "\u20b9 15920",
                    "\u20b9 18920",
                    "\u20b9 16920"
                ],
                "correct_option_index": 0,
                "explanation": "Total Area = L \u00d7 B = 32 \u00d7 14 = 448 sq.m. Total Cost = Area \u00d7 Cost per sq.m = 448 \u00d7 40 = \u20b9 17920."
            },
            {
                "difficulty": "intermediate",
                "text": "The length of a rectangular Plot is thrice its breadth. If the area of rectangular Plot is 7803 sq.mts. what is the breadth of the rectangular Plot.",
                "options": [
                    "51 cm",
                    "153 cm",
                    "61 cm",
                    "17 cm"
                ],
                "correct_option_index": 0,
                "explanation": "Area = 3x \u00d7 x = 7803 \u21d2 3x\u00b2 = 7803 \u21d2 x\u00b2 = 2601 \u21d2 x = \u221a2601 = 51 cm. The breadth is 51 cm."
            },
            {
                "difficulty": "intermediate",
                "text": "The diagonals of a Rhombus are 6cm and 8cm. find its Perimeter.",
                "options": [
                    "20 cm",
                    "40 cm",
                    "24 cm",
                    "14 cm"
                ],
                "correct_option_index": 0,
                "explanation": "Side of rhombus is the hypotenuse of the right triangle formed by half-diagonals (3cm and 4cm). Side = \u221a(3\u00b2 + 4\u00b2) = \u221a25 = 5. Perimeter = 4 \u00d7 5 = 20 cm."
            },
            {
                "difficulty": "intermediate",
                "text": "The diagonal of a square is 10\u221a2 cm. find its Perimeter.",
                "options": [
                    "40 cm",
                    "20 cm",
                    "80 cm",
                    "10 cm"
                ],
                "correct_option_index": 0,
                "explanation": "Area by diagonals = \u00bd d\u00b2 = \u00bd (10\u221a2)\u00b2 = \u00bd \u00d7 100 \u00d7 2 = 100. So a\u00b2 = 100 \u21d2 a = 10. Perimeter = 4 \u00d7 a = 4 \u00d7 10 = 40 cm."
            },
            {
                "difficulty": "intermediate",
                "text": "The diameter of a wheel is 42 cm. How many revolutions are required for a wheel to cover a distance of 9240 cm.",
                "options": [
                    "70 Revolutions",
                    "60 Revolutions",
                    "80 Revolutions",
                    "90 Revolutions"
                ],
                "correct_option_index": 0,
                "explanation": "Total Revolutions = Total Distance / Circumference = 9240 / (\u03c0d) = 9240 / (22/7 \u00d7 42) = 9240 / 132 = 70 Revolutions."
            },
            {
                "difficulty": "advanced",
                "text": "The circumference of a circle is same as Perimeter of a square whose side is 27.5 cm. find the area of a circle.",
                "options": [
                    "962.5 cm\u00b2",
                    "1925 cm\u00b2",
                    "3850 cm\u00b2",
                    "96.25 cm\u00b2"
                ],
                "correct_option_index": 0,
                "explanation": "Perimeter of square = 4a = 4 \u00d7 27.5 = 110. Circumference = 2\u03c0r = 110 \u21d2 2 \u00d7 (22/7) \u00d7 r = 110 \u21d2 r = 35/2 cm. Area = \u03c0r\u00b2 = (22/7) \u00d7 (35/2) \u00d7 (35/2) = (55 \u00d7 35) / 2 = 1925 / 2 = 962.5 cm\u00b2."
            },
            {
                "difficulty": "intermediate",
                "text": "An arc subtends an angle of 60\u00b0 at centre and radius of the circle is 14cm. find the Area of the sector and Length of the arc.",
                "options": [
                    "Area: 102.66 cm\u00b2, Length: 14.66 cm",
                    "Area: 308 cm\u00b2, Length: 44 cm",
                    "Area: 14.66 cm\u00b2, Length: 102.66 cm",
                    "Area: 616 cm\u00b2, Length: 88 cm"
                ],
                "correct_option_index": 0,
                "explanation": "Area of sector = (\u03c0r\u00b2\u03b8)/360 = (22/7 \u00d7 14 \u00d7 14 \u00d7 60)/360 = 308/3 = 102.66 cm\u00b2. Length of arc = (2\u03c0r\u03b8)/360 = (2 \u00d7 22/7 \u00d7 14 \u00d7 60)/360 = 44/3 = 14.66 cm."
            },
            {
                "difficulty": "advanced",
                "text": "A cow is tied on one of the corners of square grass field whose side is 30m. find the area of ungrazed field if the length of the rope is 14m.",
                "options": [
                    "746 sq.mt",
                    "900 sq.mt",
                    "154 sq.mt",
                    "1054 sq.mt"
                ],
                "correct_option_index": 0,
                "explanation": "Ungrazed area = Area of square - Area of sector (corner angle 90\u00b0). Area of square = 30\u00b2 = 900. Area of sector = (\u03c0r\u00b2\u03b8)/360 = (22/7 \u00d7 14 \u00d7 14 \u00d7 90)/360 = 154. Ungrazed area = 900 - 154 = 746 sq.mt."
            },
            {
                "difficulty": "intermediate",
                "text": "A lawn 30m long and 16m wide is surrounded by a path 2m wide. find the area of the path?",
                "options": [
                    "200 sq.mt",
                    "480 sq.mt",
                    "680 sq.mt",
                    "100 sq.mt"
                ],
                "correct_option_index": 0,
                "explanation": "Inner area = 30 \u00d7 16 = 480 sq.mt. Outer length = 30 + (2\u00d72) = 34m, outer breadth = 16 + (2\u00d72) = 20m. Outer area = 34 \u00d7 20 = 680 sq.mt. Area of path = 680 - 480 = 200 sq.mt."
            },
            {
                "difficulty": "intermediate",
                "text": "Three solid cubes whose sides are 6cm, 8cm and 10cm respectively are melted to form a single cube. find the side of new cube formed.",
                "options": [
                    "12 cm",
                    "14 cm",
                    "10 cm",
                    "24 cm"
                ],
                "correct_option_index": 0,
                "explanation": "Sum of volumes = 6\u00b3 + 8\u00b3 + 10\u00b3 = 216 + 512 + 1000 = 1728. New volume = a\u00b3 = 1728 \u21d2 a = \u221b1728 = 12 cm."
            },
            {
                "difficulty": "advanced",
                "text": "How much metal is required to make a 20m long pipe, if its inner and outer diameters are 12m and 16m respectively?",
                "options": [
                    "1760 sq.mt",
                    "880 sq.mt",
                    "3520 sq.mt",
                    "1200 sq.mt"
                ],
                "correct_option_index": 0,
                "explanation": "Outer radius R = 16/2 = 8m. Inner radius r = 12/2 = 6m. Metal volume = \u03c0h(R\u00b2 - r\u00b2) = (22/7) \u00d7 20 \u00d7 (8\u00b2 - 6\u00b2) = (22/7) \u00d7 20 \u00d7 (64 - 36) = 22/7 \u00d7 20 \u00d7 28 = 22 \u00d7 20 \u00d7 4 = 1760 cubic mt (written as sq.mt in notes)."
            },
            {
                "difficulty": "advanced",
                "text": "How many solid spherical balls of radius 1.5cm each are required to immerse into a cylindrical jar of radius 6cm to raise the level of water in the jar by 36cm?",
                "options": [
                    "288",
                    "144",
                    "72",
                    "312"
                ],
                "correct_option_index": 0,
                "explanation": "Volume of raised water in cylinder = No. of balls \u00d7 Volume of one sphere. \u03c0R\u00b2h = n \u00d7 (4/3)\u03c0r\u00b3 \u21d2 R\u00b2h = n \u00d7 (4/3)r\u00b3 \u21d2 6\u00b2 \u00d7 36 = n \u00d7 (4/3) \u00d7 1.5\u00b3. n = (36 \u00d7 36 \u00d7 3) / (4 \u00d7 1.5\u00b3) = 3888 / 13.5 = 288 balls."
            }
        ],
        "flashcards": [
            {
                "title": "1. Square & Rectangle Formulas",
                "front": "What are the Area, Perimeter, and Diagonal formulas for Square & Rectangle?",
                "back": "\u2022 **Square**: Area $= a^2 = \\frac{1}{2}d^2$ | Perim $= 4a$ | Diag $= a\\sqrt{2}$\n\u2022 **Rectangle**: Area $= l \\times b$ | Perim $= 2(l+b)$ | Diag $= \\sqrt{l^2+b^2}$",
                "badge": "\ud83d\udcd0 2D Geometry"
            },
            {
                "title": "2. Circle & Sector Formulas",
                "front": "What are Circumference, Area, and Sector Area formulas?",
                "back": "\u2022 **Circle**: Circum $= 2\\pi r$ | Area $= \\pi r^2$\n\u2022 **Sector**: Area $= \\frac{\\pi r^2 \\theta}{360^\\circ}$ | Arc Length $= \\frac{2\\pi r \\theta}{360^\\circ}$",
                "badge": "\u2b55 Circle Rules"
            },
            {
                "title": "3. Ratio Conversion Rules (Side vs Area vs Volume)",
                "front": "If side ratio is $a:b$, what are the Area ratio and Volume ratio?",
                "back": "\u2022 Side Ratio $= a:b$\n\u2022 Area Ratio $= a^2:b^2$\n\u2022 Volume Ratio $= a^3:b^3$\nExample: Area ratio $36:121 \\implies$ Side ratio $\\sqrt{36:121} = 6:11 \\implies$ Volume ratio $6^3:11^3 = 216:1331$!",
                "badge": "\u26a1 PDF Ratio Rule"
            },
            {
                "title": "4. Cow Ungrazed Field Shortcut",
                "front": "A cow is tied to a corner of a square field side $S$ with rope length $R$. What is the ungrazed area?",
                "back": "$\\text{Ungrazed Area} = \\text{Area of Square} - \\text{Area of Sector}(90^\\circ)$\n$= S^2 - \\frac{\\pi R^2 \\times 90^\\circ}{360^\\circ} = S^2 - \\frac{1}{4}\\pi R^2$\nExample: $S=30, R=14 \\implies 900 - 154 = 746 \\text{ sq.m}$!",
                "badge": "\ud83d\udc04 Cow Ungrazed Trick"
            },
            {
                "title": "5. Melting Solid Cubes",
                "front": "When 3 solid cubes of sides $a_1, a_2, a_3$ are melted into a single cube, what is new side $a$?",
                "back": "$a^3 = a_1^3 + a_2^3 + a_3^3 \\implies a = \\sqrt[3]{a_1^3 + a_2^3 + a_3^3}$\nExample: $6^3 + 8^3 + 10^3 = 216 + 512 + 1000 = 1728 \\implies a = 12 \\text{ cm}$!",
                "badge": "\ud83e\uddca Melting Cubes"
            }
        ]
    }
];

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { aptitudeTopics };
} else {
    window.aptitudeTopics = aptitudeTopics;
}
