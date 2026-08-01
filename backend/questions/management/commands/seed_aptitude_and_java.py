from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds Aptitude Topics with user handwritten Mensuration (2D & 3D) PDF notes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding with Mensuration 2D & 3D PDF notes..."))

        # ----------------------------------------------------
        # MENSURATION (2D & 3D) - PDF MASTER NOTES
        # ----------------------------------------------------
        mensuration_formula_sheet = r"""### 📄 User PDF Complete Master Cheat Sheet: Mensuration (2D & 3D)

#### 1. 2D Shapes (Perimeter & Area)
- **Square**: Perimeter = 4a | Area = a^2 = (1/2) * d^2 | Diagonal = a * sqrt(2)
- **Rectangle**: Perimeter = 2(l+b) | Area = l * b | Diagonal = sqrt(l^2 + b^2)
- **Rhombus**: Perimeter = 4a | Area = (1/2) * d1 * d2
- **Circle**: Circumference = 2 * pi * r | Area = pi * r^2 (r = D/2)
- **Equilateral Triangle**: Perimeter = 3a | Area = (sqrt(3)/4) * a^2 | Height = (sqrt(3)/2) * a
- **Right-Angled Triangle**: Area = (1/2) * b * h | Hypotenuse = sqrt(Adj^2 + Opp^2)
- **General Triangle (Heron's Formula)**: S = (a+b+c)/2 ==> Area = sqrt(S(S-a)(S-b)(S-c))
- **Trapezium**: Area = (1/2) * (Sum of Parallel Sides) * Distance Between Them = Avg * D
- **Sector of Circle**: Area = (pi * r^2 * theta) / 360 | Arc Length = (2 * pi * r * theta) / 360

#### 2. 3D Shapes (LSA, TSA & Volume)
- **Cube**: LSA = 4a^2 | TSA = 6a^2 | Volume = a^3 | Diagonal = a * sqrt(3)
- **Cuboid**: LSA = 2(l+b)h | TSA = 2(lb+bh+hl) | Volume = l * b * h | Diagonal = sqrt(l^2+b^2+h^2)
- **Sphere**: No LSA | TSA = 4 * pi * r^2 | Volume = (4/3) * pi * r^3
- **Hemisphere**: CSA = 2 * pi * r^2 | TSA = 3 * pi * r^2 | Volume = (2/3) * pi * r^3
- **Cylinder**: CSA = 2 * pi * r * h | TSA = 2 * pi * r(r+h) | Volume = pi * r^2 * h
- **Cone**: Slant Height l = sqrt(r^2+h^2) | CSA = pi * r * l | TSA = pi * r(r+l) | Volume = (1/3) * pi * r^2 * h

#### 3. Ratio Conversion Rules (Side vs Area vs Volume)
- **2D Shapes**: Side Ratio = a:b ==> Area Ratio = a^2:b^2 | Area Ratio = A:B ==> Side Ratio = sqrt(A):sqrt(B)
- **3D Shapes**: Side Ratio = a:b ==> Volume Ratio = a^3:b^3 | Volume Ratio = V1:V2 ==> Side Ratio = cube_root(V1):cube_root(V2)
- **Area to Volume Conversion**: Area Ratio -> Side Ratio (sqrt) -> Volume Ratio (cube)
  - *PDF Ex*: Surface area ratio 36:121 ==> Side ratio sqrt(36:121) = 6:11 ==> Volume ratio 6^3:11^3 = 216:1331!

#### 4. Percentage Change Operations
- **1D Units (Perimeter/Radius/Side)**: Perform 1 increase/decrease operation.
- **2D Units (Area, sq units)**: Perform 2 successive operations (x + y + xy/100).
  - *PDF Ex*: Side of square decreased by 20% ==> -20 - 20 + 400/100 = -36% (36% decrease)!
- **3D Units (Volume, cubic units)**: Perform 3 successive operations.

#### 5. Advanced Geometry & Special Tricks
- **Revolutions of Wheel**: Total Revolutions = Total Distance / (pi * D)
  - *PDF Ex*: Diameter = 42cm, Distance = 9240cm ==> 9240 / ((22/7) * 42) = 70 Revolutions!
- **Cow Tied in Square Field (Ungrazed Area)**:
  - Ungrazed Area = Area of Square - Area of Sector (90 deg)
  - *PDF Ex*: Field side = 30m, rope = 14m ==> 30^2 - ((22/7) * 14 * 14 * (90/360)) = 900 - 154 = 746 sq.m!
- **Roads Crossing in Middle**: Total Road Area = (l * w) + (b * w) - w^2
- **Hollow Pipe Metal Volume**: Metal Volume = pi * h * (R^2 - r^2)
- **Melting Solids into Single Cube**: a^3 = a1^3 + a2^3 + a3^3
  - *PDF Ex*: Cubes of sides 6cm, 8cm, 10cm melted ==> 6^3 + 8^3 + 10^3 = 216 + 512 + 1000 = 1728 ==> New Side = cube_root(1728) = 12cm!
- **Immersing Spheres to Raise Water Level**: pi * R^2 * h = N * (4/3) * pi * r^3
"""

        mensuration_topic, _ = AptitudeTopic.objects.update_or_create(
            slug="mensuration",
            defaults={
                "order": 16,
                "name": "Mensuration 2D & 3D (PDF Master Edition)",
                "description": "Master 2D/3D formulas, Ratio Side-Area-Volume conversions, Cow Ungrazed Field, Wheel Revolutions, & Hollow Pipe metal rules.",
                "icon": "📐",
                "formula_sheet": mensuration_formula_sheet
            }
        )

        # Seed PDF Worked Questions
        AptitudeQuestion.objects.get_or_create(
            topic=mensuration_topic,
            text="The ratio of surface areas of two spheres is 36:121. Find the ratio of their respective volumes.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "216 : 1331", "option_b": "36 : 121", "option_c": "6 : 11", "option_d": "108 : 665.5",
                "correct_option": "A",
                "explanation": "PDF Area to Volume Conversion Shortcut: Area Ratio 36:121 -> Side Ratio sqrt(36:121) = 6:11 -> Volume Ratio = 6^3 : 11^3 = 216 : 1331!"
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=mensuration_topic,
            text="A cow is tied on one of the corners of a square grass field whose side is 30m. Find the area of the ungrazed field if the length of the rope is 14m.",
            defaults={
                "difficulty": "advanced",
                "option_a": "746 sq.m", "option_b": "616 sq.m", "option_c": "754 sq.m", "option_d": "700 sq.m",
                "correct_option": "A",
                "explanation": "PDF Ungrazed Field Formula: Area = Area of Square - Area of Sector(90 deg) = 30^2 - (22/7 * 14 * 14 * 90/360) = 900 - 154 = 746 sq.m!"
            }
        )

        AptitudeQuestion.objects.get_or_create(
            topic=mensuration_topic,
            text="Three solid cubes whose sides are 6cm, 8cm and 10cm respectively are melted to form a single cube. Find the side of the new cube formed.",
            defaults={
                "difficulty": "intermediate",
                "option_a": "11 cm", "option_b": "12 cm", "option_c": "14 cm", "option_d": "15 cm",
                "correct_option": "B",
                "explanation": "PDF Melting Cubes Formula: V_total = 6^3 + 8^3 + 10^3 = 216 + 512 + 1000 = 1728 cm^3.\nNew Side = cube_root(1728) = 12 cm!"
            }
        )

        self.stdout.write(self.style.SUCCESS("Mensuration 2D & 3D PDF notes & worked problems successfully seeded!"))
