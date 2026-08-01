from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten Time & Work and Pipes & Cisterns PDF notes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with Time & Work and Pipes & Cisterns PDF notes..."))

        # ----------------------------------------------------
        # 1. TIME AND WORK - PDF MASTER NOTES
        # ----------------------------------------------------
        tnw_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Time and Work

#### 1. Fundamental Proportionality Laws
- **Time $\\propto$ Work** (Directly proportional)
- **Men $\\propto$ Work** (Directly proportional)
- **Time $\\propto \\frac{1}{\\text{Men}}$** (Inversely proportional)

#### 2. Universal MDH Formula
$$\\frac{M_1 \\times D_1 \\times H_1}{W_1} = \\frac{M_2 \\times D_2 \\times H_2}{W_2}$$
- $M_1 D_1 = M_2 D_2$ (when hours and work are constant)
- $M_1 D_1 H_1 = M_2 D_2 H_2$ (when work is constant)
- $\\text{Work} = \\text{Time} \\times \\text{Efficiency}$ | $\\text{Efficiency} = \\frac{\\text{Total Work}}{\\text{Time Taken}}$

#### 3. Middle Joining & Middle Leaving (Equation Method)
- Add before and after situations to find remaining days!
- *Example*: 16 men do job in 30 days. After 10 days, 6 men left. How many days for remaining work?
  - Total work $= 16 \\times 30 = 480$.
  - Work done in 10 days $= 16 \\times 10 = 160 \\implies \\text{Remaining} = 320$.
  - Remaining 10 men $\\implies D_2 = \\frac{320}{10} = \\mathbf{32 \\text{ days}}$!

#### 4. "OR" and "AND" Type Questions Shortcut
- **Direct Shortcut for "AND" from "OR"**:
  $$\\text{Days} = \\frac{\\text{Given Days}}{\\frac{M_2}{M_1} + \\frac{W_2}{W_1}}$$
  - *Example*: 10 men OR 12 women do work in 16 days. How many days for 15 men AND 6 women?
  - $\\text{Days} = \\frac{16}{\\frac{15}{10} + \\frac{6}{12}} = \\frac{16}{1.5 + 0.5} = \\frac{16}{2} = \\mathbf{8 \\text{ days}}$!

#### 5. Pure "AND" Type Equating Method
- 2M + 3W do in 8 days; 3M + 2W do in 7 days.
  - $(2M + 3W) \\times 8 = (3M + 2W) \\times 7 \\implies 16M + 24W = 21M + 14W \\implies 1M = 2W$.
  - Total work $= 7W \\times 8 = 56 \\text{ units}$.
  - $5M + 4W = 14W \\implies \\text{Days} = \\frac{56}{14} = \\mathbf{4 \\text{ days}}$!

#### 6. Leaving BEFORE Completion (Backwards Leaving Trick)
- If a worker leaves $X$ days BEFORE completion, **ADD their potential work** to total work!
  - *Example*: A in 20d, B in 30d (Total 60 units: A=3, B=2). B left 3 days BEFORE completion.
  - Add B's 3-day work ($3 \\times 2 = 6$) to total $\\to 60 + 6 = 66$ units.
  - Total time $= \\frac{66}{3+2} = \\frac{66}{5} = \\mathbf{13\\frac{1}{5} \\text{ days}}$!

#### 7. Alternate Days Working Concept
- Calculate work done in a 2-day cycle $(A+B)$. Multiply cycle until near total work, then complete leftover units with the worker who started!
"""

        tnw_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="time-and-work",
            defaults={
                "order": 12,
                "name": "Time and Work (PDF Master Edition)",
                "description": "Master Proportionality laws, Universal MDH Formula, Middle Joining/Leaving, OR to AND shortcut, & Backwards Leaving trick.",
                "icon": "⏱️",
                "formula_sheet": tnw_formula_sheet
            }
        )

        # ----------------------------------------------------
        # 2. PIPES AND CISTERNS - PDF MASTER NOTES
        # ----------------------------------------------------
        pnc_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Pipes and Cisterns

#### 1. Core Principles & Negative Work
- Extension of Time & Work, but includes **Destroying/Emptying elements** (negative work).
- **Filling Pipe (Inlet)**: Positive work ($+X$).
- **Emptying Pipe (Outlet)**: Negative work ($-Y$).
- **Two Filling Pipes**: Total time $= \\frac{xy}{x+y}$
- **One Filling & One Emptying**: Total time $= \\frac{xy}{|x-y|}$

#### 2. LCM Partitioning Method
- Pipe A (fill 25m), B (fill 30m), C (empty 50m). Total Capacity $= \\text{LCM}(25,30,50) = 150 \\text{ units}$.
  - $A = +6, B = +5, C = -3$ units/min.
  - All opened for 7 mins $(+8 \\times 7 = 56)$. A closed. Next 4 mins $(+2 \\times 4 = 8)$. C closed.
  - Remaining units $= 150 - 64 = 86$ units filled by B ($+5$) $\\implies \\frac{86}{5} = \\mathbf{17\\frac{1}{5} \\text{ mins}}$!

#### 3. Tank Will NEVER Be Filled Rule
- If all filling pipes are closed before tank is full, or if emptying rate exceeds filling rate $\\implies$ **Tank will NEVER be filled**!

#### 4. Alternate Minutes Filling & Emptying (Safety Margin Trick)
- Pipe A (+6), B (+4), C (-3). Total $= 120$ units. Cycle (3 mins) $= +7$ units.
- **CRITICAL TRICK**: Keep a safety margin equal to peak filling capacity ($6+4 = 10$ units) before multiplying cycles!
  - Target $= 120 - 10 = 110$ units.
  - $7 \\times 16 = 112$ units in $16 \\times 3 = 48$ mins.
  - Min 49 (A opens): $+6 \\to 118$ units.
  - Min 50 (B opens): Needs 2 units out of 4 $\\implies 1/2$ min.
  - Total time $= \\mathbf{49\\frac{1}{2} \\text{ minutes}}$!

#### 5. Mid-Way Pipe Closing Trick
- Pipes A & B fill in 24m and 32m (Total 96 units: A=+4, B=+3). Both opened. When to close B so tank is full in 18 mins?
  - A works all 18 mins $\\to 4 \\times 18 = 72$ units.
  - Remaining $= 96 - 72 = 24$ units filled by B ($+3$).
  - Time for B $= \\frac{24}{3} = \\mathbf{8 \\text{ minutes}}$! Close B after 8 mins.
"""

        pnc_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="pipes-and-cisterns",
            defaults={
                "order": 14,
                "name": "Pipes and Cisterns (PDF Master Edition)",
                "description": "Master Filling/Emptying signs, LCM Capacity Partitioning, Safety Margin Alternate Cycle trick, & Mid-Way Closing formula.",
                "icon": "🚰",
                "formula_sheet": pnc_formula_sheet
            }
        )

        # Seed PDF Worked Questions
        AptitudeQuestion.objects.get_or_create(
            topic=tnw_topic,
            text="If 10 men or 12 women can do a piece of work in 16 days, in how many days can 15 men and 6 women together do the same work?",
            defaults={
                "difficulty": "intermediate",
                "option_a": "6 days", "option_b": "8 days", "option_c": "10 days", "option_d": "12 days",
                "correct_option": "B",
                "explanation": "PDF Shortcut Method: Days = Given Days / (M2/M1 + W2/W1) = 16 / (15/10 + 6/12) = 16 / (1.5 + 0.5) = 16 / 2 = 8 days!"
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=tnw_topic,
            text="A can do a piece of work in 20 days and B in 30 days. They start together, but B leaves 3 days before the completion of the work. In how many days is the total work completed?",
            defaults={
                "difficulty": "advanced",
                "option_a": "12 days", "option_b": "13 1/5 days", "option_c": "15 days", "option_d": "14 days",
                "correct_option": "B",
                "explanation": "Backwards Leaving Trick: Total Work = LCM(20,30) = 60 units (A=3, B=2).\nAdd B's 3-day work (3 * 2 = 6 units) -> Total = 60 + 6 = 66 units.\nTotal Days = 66 / (3 + 2) = 66 / 5 = 13 1/5 days."
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=pnc_topic,
            text="Two pipes A and B can fill a tank in 24 minutes and 32 minutes respectively. If both pipes are opened together, after how much time should B be closed so that the tank is full in 18 minutes?",
            defaults={
                "difficulty": "advanced",
                "option_a": "6 minutes", "option_b": "8 minutes", "option_c": "10 minutes", "option_d": "12 minutes",
                "correct_option": "B",
                "explanation": "Mid-Way Closing Trick: Total Capacity = LCM(24,32) = 96 units (A=+4, B=+3).\nA works for all 18 mins -> A's work = 4 * 18 = 72 units.\nRemaining work for B = 96 - 72 = 24 units.\nTime for B = 24 / 3 = 8 minutes!"
            }
        )

        self.stdout.write(self.style.SUCCESS("Time & Work and Pipes & Cisterns PDF notes & worked problems successfully seeded!"))
