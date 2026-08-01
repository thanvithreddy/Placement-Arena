from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten Speed/Distance/Trains and Boats/Streams PDF notes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with Speed/Distance/Trains and Boats/Streams PDF notes..."))

        # ----------------------------------------------------
        # 1. SPEED, DISTANCE & TIME / TRAINS - PDF MASTER NOTES
        # ----------------------------------------------------
        sdt_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Speed, Distance, Time & Trains

#### 1. Core Formulas & Unit Conversions
- $\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}$ | $\\text{Distance} = \\text{Speed} \\times \\text{Time}$ | $\\text{Time} = \\frac{\\text{Distance}}{\\text{Speed}}$
- **km/h to m/s**: Multiply by $\\frac{5}{18}$
- **m/s to km/h**: Multiply by $\\frac{18}{5}$

#### 2. The 4 Train Cases
1. **Crossing Standing Man / Pole**: Distance = Length of Train ($L$). Speed = Train Speed ($S$).
2. **Crossing Platform / Bridge**: Distance = Train Length ($L_1$) + Platform Length ($L_2$).
3. **Crossing Running Person**:
   - Same Direction: Relative Speed = $S_{\\text{train}} - S_{\\text{person}}$
   - Opposite Direction: Relative Speed = $S_{\\text{train}} + S_{\\text{person}}$
4. **Crossing Another Train**:
   - Distance is ALWAYS $L_1 + L_2$ regardless of direction.
   - Same Direction Time = $\\frac{L_1 + L_2}{|S_1 - S_2|}$ | Opposite Direction Time = $\\frac{L_1 + L_2}{S_1 + S_2}$

#### 3. Two Distant Places Meeting Concept
- Two vehicles start from A & B towards each other $\\implies$ Relative Speed $= S_1 + S_2$.
- **Different Starting Times Trick**: Calculate distance covered by earlier train BEFORE second train starts!
  - *PDF Example*: A & B 440km apart. Train P starts at 4 AM (30km/h). Train Q starts at 7 AM (40km/h).
  - From 4-7 AM (3 hrs), P covers $30 \\times 3 = 90\\text{km}$. Remaining $= 350\\text{km}$.
  - Relative Speed $= 30 + 40 = 70\\text{km/h}$. Time to meet $= \\frac{350}{70} = 5 \\text{ hrs after 7 AM} \\implies \\mathbf{12:00 \\text{ PM (Noon)}}$!

#### 4. Chasing Case (Same Direction)
- *PDF Example*: Rajdhani leaves at 14:30 (60km/h). Duronto leaves at 16:30 (80km/h).
  - Gap at 16:30 (2 hrs) $= 60 \\times 2 = 120\\text{km}$.
  - Relative Speed $= 80 - 60 = 20\\text{km/h}$. Time $= \\frac{120}{20} = 6 \\text{ hrs} \\implies \\mathbf{480\\text{km from Delhi}}$!

#### 5. Stoppage Time Formula per Hour
$$\\mathbf{\\text{Stoppage Time/hr} = \\left(\\frac{\\text{Speed excl. stoppages} - \\text{Speed incl. stoppages}}{\\text{Speed excl. stoppages}}\\right) \\times 60 \\text{ mins}}$$
- *PDF Example*: Incl = 25km/h, Excl = 40km/h $\\implies \\left(\\frac{40 - 25}{40}\\right) \\times 60 = \\mathbf{22.5 \\text{ mins/hr}}$!

#### 6. Late vs Early Distance Formula
$$\\mathbf{\\text{Distance} = \\frac{S_1 \\times S_2}{|S_1 - S_2|} \\times \\left(\\frac{\\Delta \\text{Time in mins}}{60}\\right)}$$
- *PDF Example*: 30km/h (10m late) vs 40km/h (5m early) $\\to \\Delta t = 15\\text{m} \\implies \\text{Distance} = \\frac{1200}{10} \\times \\frac{15}{60} = \\mathbf{30\\text{km}}$!

#### 7. Post-Meeting Time Formula
$$\\mathbf{\\frac{S_1}{S_2} = \\sqrt{\\frac{T_2}{T_1}}}$$
- *PDF Example*: After meeting, trains reach destinations in 9 hrs and 16 hrs. $S_1 = 80\\text{km/h} \\implies \\frac{80}{S_2} = \\sqrt{\\frac{16}{9}} = \\frac{4}{3} \\implies S_2 = \\mathbf{60\\text{km/h}}$!
"""

        sdt_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="speed-distance-time",
            defaults={
                "order": 13,
                "name": "Speed, Distance & Time / Trains (PDF Master Edition)",
                "description": "Master Train Cases, Platform Crossing, Chasing, Stoppage formula, Late/Early formula, & Post-Meeting Time root law.",
                "icon": "🚀",
                "formula_sheet": sdt_formula_sheet
            }
        )

        # ----------------------------------------------------
        # 2. BOATS AND STREAMS - PDF MASTER NOTES
        # ----------------------------------------------------
        boats_formula_sheet = """### 📄 User PDF Complete Master Cheat Sheet: Boats and Streams

#### 1. Core Speed Definitions & Formulas
- $B$ = Speed of boat in still water
- $W$ = Speed of stream / current / water flow
- **Downstream Speed ($D$)**: $D = B + W$ (moving WITH stream)
- **Upstream Speed ($U$)**: $U = B - W$ (moving AGAINST stream)
- **Boat Speed ($B$)**: $B = \\frac{D + U}{2}$
- **Stream Speed ($W$)**: $W = \\frac{D - U}{2}$

#### 2. Round-Trip Total Time Distance Formula
$$\\mathbf{\\text{Distance} = \\frac{D \\times U}{D + U} \\times \\text{Total Time} = \\frac{(B^2 - W^2)}{2B} \\times \\text{Total Time}}$$
- *PDF Example*: Boat speed = 8km/h, Stream = 2km/h ($D=10, U=6$). Takes 8 hours total round trip.
  - $\\text{Distance} = \\frac{10 \\times 6}{10 + 6} \\times 8 = \\frac{60}{16} \\times 8 = \\mathbf{30\\text{km}}$!

#### 3. Simultaneous Equations Factorization Method
- *PDF Example*: 40km upstream + 55km downstream in 13 hrs; 30km upstream + 44km downstream in 10 hrs.
  - Try common factors of 55 & 44 $\\implies D = 11\\text{km/h}$.
  - $55/11 = 5 \\implies 40/U = 8 \\implies U = 5\\text{km/h}$.
  - Boat Speed $B = \\frac{11 + 5}{2} = \\mathbf{8\\text{km/h}}$, Stream Speed $W = \\frac{11 - 5}{2} = \\mathbf{3\\text{km/h}}$!
"""

        boats_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="boats-and-streams",
            defaults={
                "order": 15,
                "name": "Boats and Streams (PDF Master Edition)",
                "description": "Master Downstream/Upstream laws, Round-Trip Distance formula, & Simultaneous Equations factorization trick.",
                "icon": "⛵",
                "formula_sheet": boats_formula_sheet
            }
        )

        # Seed PDF Worked Questions
        AptitudeQuestion.objects.get_or_create(
            topic=sdt_topic,
            text="A train travelling at constant speed crosses a 96m long platform in 12 seconds and another 141m long platform in 15 seconds. Find the length of the train.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "72m", "option_b": "84m", "option_c": "90m", "option_d": "96m",
                "correct_option": "B",
                "explanation": "PDF Extra Distance Method: Extra distance = 141 - 96 = 45m in extra time = 15 - 12 = 3s.\nTrain Speed = 45 / 3 = 15 m/s.\nDistance in 12s = 15 * 12 = 180m.\nTrain Length = 180 - 96 = 84m!"
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=sdt_topic,
            text="Two trains start simultaneously from Hyderabad to Chennai and Chennai to Hyderabad. After meeting, they reach their destinations in 9 hours and 16 hours respectively. If the first train speed is 80km/h, find the speed of the second train.",
            defaults={
                "difficulty": "advanced",
                "option_a": "50 km/h", "option_b": "60 km/h", "option_c": "70 km/h", "option_d": "64 km/h",
                "correct_option": "B",
                "explanation": "Post-Meeting Formula: S1 / S2 = sqrt(T2 / T1) -> 80 / S2 = sqrt(16 / 9) = 4 / 3.\nS2 = 80 * (3 / 4) = 60 km/h!"
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=boats_topic,
            text="A man can row 40km upstream and 55km downstream in 13 hours. Also, he can row 30km upstream and 44km downstream in 10 hours. Find the speed of the man in still water.",
            defaults={
                "difficulty": "advanced",
                "option_a": "6 km/h", "option_b": "8 km/h", "option_c": "10 km/h", "option_d": "7 km/h",
                "correct_option": "B",
                "explanation": "PDF Factorization Method: Common factors of 55 and 44 is D = 11 km/h.\n55/11 = 5 hrs -> 40/U = 8 hrs -> U = 5 km/h.\nBoat Speed B = (D + U) / 2 = (11 + 5) / 2 = 8 km/h!"
            }
        )

        self.stdout.write(self.style.SUCCESS("Speed/Distance/Trains and Boats/Streams PDF notes & worked problems successfully seeded!"))
