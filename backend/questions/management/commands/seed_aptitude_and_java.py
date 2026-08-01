from django.core.management.base import BaseCommand
from questions.models import AptitudeTopic, AptitudeQuestion, JavaTopic

class Command(BaseCommand):
    help = 'Seeds all 15 Aptitude Topics and 23 Gamified Java Quest Topics'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database seeding..."))

        # ----------------------------------------------------
        # 1. SEED 15 QUANTITATIVE APTITUDE TOPICS
        # ----------------------------------------------------
        aptitude_data = [
            {
                "order": 1, "name": "Percentages", "slug": "percentages", "icon": "📊",
                "desc": "Master fraction to percentage conversions, percentage increase/decrease, and population change formulas.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Base Percentage**: $$\\text{Percentage} = \\left(\\frac{\\text{Value}}{\\text{Total}}\\right) \\times 100$$\n- **Percentage Increase/Decrease**: $$\\% \\text{ Change} = \\frac{\\text{New} - \\text{Old}}{\\text{Old}} \\times 100$$\n- **Fraction Equivalents**: $\\frac{1}{6} = 16.66\\%$, $\\frac{1}{7} = 14.28\\%$, $\\frac{1}{8} = 12.5\\%$, $\\frac{1}{11} = 9.09\\%$.\n- **Successive Change**: $$A + B + \\frac{AB}{100}$$"
            },
            {
                "order": 2, "name": "Profit and Loss", "slug": "profit-and-loss", "icon": "📈",
                "desc": "Calculate Cost Price, Selling Price, Markups, Discounts, and False Weights.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Profit %**: $$\\left(\\frac{SP - CP}{CP}\\right) \\times 100$$\n- **Loss %**: $$\\left(\\frac{CP - SP}{CP}\\right) \\times 100$$\n- **Discount %**: $$\\left(\\frac{\\text{Marked Price} - \\text{Selling Price}}{\\text{Marked Price}}\\right) \\times 100$$\n- **False Weight Trick**: $$\\text{Profit } \\% = \\left(\\frac{\\text{Error}}{\\text{True Value} - \\text{Error}}\\right) \\times 100$$"
            },
            {
                "order": 3, "name": "Simple & Compound Interest", "slug": "simple-compound-interest", "icon": "💰",
                "desc": "Understand SI vs CI growth, compounding frequencies, and 2-year/3-year CI-SI differences.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Simple Interest**: $$SI = \\frac{P \\times R \\times T}{100}$$\n- **Compound Amount**: $$A = P\\left(1 + \\frac{R}{100}\\right)^n$$\n- **Difference between CI and SI for 2 Years**: $$D_2 = P\\left(\\frac{R}{100}\\right)^2$$\n- **Difference for 3 Years**: $$D_3 = P\\left(\\frac{R}{100}\\right)^2 \\left(3 + \\frac{R}{100}\\right)$$"
            },
            {
                "order": 4, "name": "Averages", "slug": "averages", "icon": "⚖️",
                "desc": "Find weighted averages, replacement problems, and consecutive number properties.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Average**: $$\\text{Average} = \\frac{\\text{Sum of Observations}}{\\text{Total Number of Observations}}$$\n- **Weighted Average**: $$\\text{Avg}_{w} = \\frac{n_1 a_1 + n_2 a_2}{n_1 + n_2}$$\n- **Average Speed (Equal Distances)**: $$\\frac{2xy}{x+y}$$"
            },
            {
                "order": 5, "name": "Alligations & Mixtures", "slug": "alligations-mixtures", "icon": "🧪",
                "desc": "Solve mixing ratio problems, mean price rules, and repeated dilution formulas.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Rule of Alligation**: $$\\frac{\\text{Cheaper Quantity}}{\\text{Dearer Quantity}} = \\frac{d - m}{m - c}$$\n- **Repeated Dilution**: $$\\text{Remaining Liquid} = X \\left(1 - \\frac{Y}{X}\\right)^n$$"
            },
            {
                "order": 6, "name": "Problems on Ages", "slug": "problems-on-ages", "icon": "⏳",
                "desc": "Ratio-based age problems, past/present/future age algebraic equations.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Constant Difference**: The age difference between two individuals remains constant at all points in time.\n- If present age ratio is $a:b$ and after $N$ years ratio is $c:d$, use cross-multiplication for quick values."
            },
            {
                "order": 7, "name": "Ratios & Proportions", "slug": "ratios-proportions", "icon": "📐",
                "desc": "Direct/inverse proportions, duplicate ratios, and mean proportionals.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Compounded Ratio** of $(a:b)$ and $(c:d)$ is $(ac : bd)$.\n- **Mean Proportional** between $a$ and $b$ is $\\sqrt{ab}$.\n- **Third Proportional** to $a$ and $b$ is $\\frac{b^2}{a}$."
            },
            {
                "order": 8, "name": "Partnerships", "slug": "partnerships", "icon": "🤝",
                "desc": "Active vs sleeping partners, capital investment duration and profit sharing ratios.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Profit Ratio**: $$P_A : P_B = (C_A \\times T_A) : (C_B \\times T_B)$$\n- Investment $\\times$ Time = Profit Share."
            },
            {
                "order": 9, "name": "Time and Work", "slug": "time-and-work", "icon": "⏱️",
                "desc": "Work efficiency ratios, combined work rates, and alternate day work scenarios.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Work Rate**: If A completes a job in $X$ days, A's 1-day work = $\\frac{1}{X}$.\n- **Combined Rate**: $$\\text{Days taken together} = \\frac{XY}{X+Y}$$\n- **Efficiency**: $\\text{Work} = \\text{Efficiency} \\times \\text{Time}$."
            },
            {
                "order": 10, "name": "Speed, Distance & Time", "slug": "speed-distance-time", "icon": "🚀",
                "desc": "Relative speed, train crossing stationary & moving objects, and stream currents.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Unit Conversion**: $1 \\text{ km/h} = \\frac{5}{18} \\text{ m/s}$, $1 \\text{ m/s} = \\frac{18}{5} \\text{ km/h}$.\n- **Relative Speed (Opposite Direction)**: $S_1 + S_2$.\n- **Relative Speed (Same Direction)**: $|S_1 - S_2|$."
            },
            {
                "order": 11, "name": "Pipes and Cisterns", "slug": "pipes-and-cisterns", "icon": "🚰",
                "desc": "Inlet & outlet pipe fill rates, leak calculations, and alternating pipe opening.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Net Fill Rate**: $\\frac{1}{\\text{Inlet}} - \\frac{1}{\\text{Outlet}}$.\n- If inlet fills in $A$ hours and outlet empties in $B$ hours, net time = $\\frac{AB}{B-A}$ (when $B > A$)."
            },
            {
                "order": 12, "name": "Permutations & Combinations", "slug": "permutations-combinations", "icon": "🔢",
                "desc": "Arrangements vs selections, circular permutations, and restricted grouping rules.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Permutation (Order Matters)**: $$^nP_r = \\frac{n!}{(n-r)!}$$\n- **Combination (Order Doesn't Matter)**: $$^nC_r = \\frac{n!}{r!(n-r)!}$$\n- **Circular Permutation**: $(n-1)!$."
            },
            {
                "order": 13, "name": "Probability", "slug": "probability", "icon": "🎲",
                "desc": "Sample space calculations, independent events, Bayes' theorem, and card/dice probabilities.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Probability**: $$P(E) = \\frac{\\text{Favorable Outcomes}}{\\text{Total Sample Space}}$$\n- **Complement**: $P(E') = 1 - P(E)$.\n- **At Least One**: $P(\\text{At least 1}) = 1 - P(\\text{None})$."
            },
            {
                "order": 14, "name": "Mensuration (2D & 3D)", "slug": "mensuration", "icon": "📐",
                "desc": "Areas, perimeters, surface areas, and volumes of circles, cylinders, cones, and spheres.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Circle Area**: $\\pi r^2$, **Circumference**: $2\\pi r$.\n- **Cylinder Volume**: $\\pi r^2 h$, **Curved Surface Area**: $2\\pi r h$.\n- **Cone Volume**: $\\frac{1}{3}\\pi r^2 h$, **Sphere Volume**: $\\frac{4}{3}\\pi r^3$."
            },
            {
                "order": 15, "name": "LCM & HCF", "slug": "lcm-and-hcf", "icon": "🧮",
                "desc": "Prime factorization, Euclidean division algorithm, fraction LCM/HCF rules.",
                "formula": "### 💡 Key Formulas & Shortcuts\n- **Product Rule**: $$a \\times b = \\text{LCM}(a,b) \\times \\text{HCF}(a,b)$$\n- **Fractions LCM**: $$\\text{LCM} = \\frac{\\text{LCM of Numerators}}{\\text{HCF of Denominators}}$$\n- **Fractions HCF**: $$\\text{HCF} = \\frac{\\text{HCF of Numerators}}{\\text{LCM of Denominators}}$$"
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
            # Add sample practice question if empty
            if not topic.questions.exists():
                AptitudeQuestion.objects.create(
                    topic=topic,
                    difficulty="intermediate",
                    text=f"A sample placement question on {topic.name}: If a number is increased by 20% and then decreased by 20%, what is the net percentage change?",
                    option_a="No Change",
                    option_b="4% Increase",
                    option_c="4% Decrease",
                    option_d="2% Decrease",
                    correct_option="C",
                    explanation="Net Change Formula: A + B + (A*B)/100 = 20 - 20 + (20 * -20)/100 = -4%. Therefore, a 4% net decrease occurs."
                )

        self.stdout.write(self.style.SUCCESS("Aptitude topics seeded successfully!"))

        # ----------------------------------------------------
        # 2. SEED 23 GAMIFIED JAVA MASTERY QUEST TOPICS
        # ----------------------------------------------------
        java_quest_topics = [
            {
                "order": 1, "slug": "variables-and-data-types", "title": "Variables & Data Types",
                "summary": "Java is a strongly-typed language. Learn primitive types (byte, short, int, long, float, double, boolean, char) and variable scoping.",
                "rules": [
                    "Primitives hold raw binary values directly on the Stack memory.",
                    "Default value for uninitialized instance variables: int is 0, boolean is false, object reference is null.",
                    "Local variables MUST be explicitly initialized before use or a compilation error occurs!"
                ],
                "code": "public class VariablesDemo {\n    public static void main(String[] args) {\n        int age = 22;\n        double salary = 85000.50;\n        char grade = 'A';\n        boolean isPlaced = true;\n        \n        System.out.println(\"Student: Age=\" + age + \", Grade=\" + grade + \", Placed=\" + isPlaced);\n    }\n}",
                "memory": {"stack": ["int age = 22", "double salary = 85000.50", "char grade = 'A'"], "heap": ["No objects allocated on Heap (all primitives)"]},
                "errors": ["java: variable age might not have been initialized", "java: incompatible types: possible lossy conversion from double to int"],
                "xp": 100,
                "quiz": [{"q": "Which data type is stored directly on the Stack?", "opts": ["String", "int", "Scanner", "int[]"], "ans": 1, "exp": "int is a primitive data type and stores its raw value directly on the stack."}]
            },
            {
                "order": 2, "slug": "arithmetic-and-logical-operators", "title": "Arithmetic & Logical Operators",
                "summary": "Master binary arithmetic (+, -, *, /, %), increment/decrement (++a vs a++), and short-circuit logical operators (&&, ||).",
                "rules": [
                    "Integer division truncates decimals: 5 / 2 evaluates to 2 (not 2.5). Use 5.0 / 2 for double result.",
                    "Short-circuit evaluation: In (A && B), if A is false, B is NOT evaluated.",
                    "Pre-increment (++a) increments first then returns; Post-increment (a++) returns first then increments."
                ],
                "code": "public class OperatorsDemo {\n    public static void main(String[] args) {\n        int a = 10, b = 3;\n        System.out.println(\"Division: \" + (a / b)); // Output: 3\n        System.out.println(\"Modulus: \" + (a % b));  // Output: 1\n        \n        int x = 5;\n        System.out.println(x++); // Output: 5\n        System.out.println(++x); // Output: 7\n    }\n}",
                "memory": {"stack": ["a = 10", "b = 3", "x = 7"], "heap": []},
                "errors": ["java: arithmetic exception: / by zero"],
                "xp": 100,
                "quiz": [{"q": "What is the output of 10 % 3 in Java?", "opts": ["3", "3.33", "1", "0"], "ans": 2, "exp": "10 divided by 3 has a remainder of 1."}]
            },
            {
                "order": 3, "slug": "basic-memory-management", "title": "Basic Memory Management (Stack vs Heap)",
                "summary": "Understand JVM Execution Engine, Stack Frame allocation for methods & primitives, Heap space for Objects, and Garbage Collection.",
                "rules": [
                    "Stack Stores: Local variables, primitive data, and reference variables (pointers).",
                    "Heap Stores: All Objects created via 'new' keyword.",
                    "Garbage Collector automatically reclaims Heap memory when an object has 0 active references."
                ],
                "code": "public class MemoryDemo {\n    public static void main(String[] args) {\n        int x = 10; // Stored in main() Stack Frame\n        String name = new String(\"Placement Arena\"); // Reference on Stack -> Object on Heap\n    }\n}",
                "memory": {"stack": ["main() Frame", "int x = 10", "String name -> ref@0x4f"], "heap": ["String Object @0x4f (\"Placement Arena\")"]},
                "errors": ["java.lang.OutOfMemoryError: Java heap space", "java.lang.StackOverflowError"],
                "xp": 120,
                "quiz": [{"q": "Where are Objects stored in Java memory?", "opts": ["Stack Memory", "Heap Memory", "Metaspace", "Register"], "ans": 1, "exp": "All Java objects created via 'new' are stored in Heap memory."}]
            },
            {
                "order": 4, "slug": "arrays", "title": "Arrays in Java",
                "summary": "Contiguous memory allocation for homogeneous elements. Master 1D arrays, 2D matrices, array length property, and bounds checking.",
                "rules": [
                    "Arrays are OBJECTS in Java and stored on the Heap.",
                    "Attempting to access arr[arr.length] throws ArrayIndexOutOfBoundsException at runtime.",
                    "Array size is FIXED at creation time and cannot be resized dynamically."
                ],
                "code": "public class ArrayDemo {\n    public static void main(String[] args) {\n        int[] numbers = {10, 20, 30, 40, 50};\n        System.out.println(\"Length: \" + numbers.length);\n        for (int i = 0; i < numbers.length; i++) {\n            System.out.println(\"Element \" + i + \": \" + numbers[i]);\n        }\n    }\n}",
                "memory": {"stack": ["int[] numbers -> ref@0x9a"], "heap": ["int array object @0x9a: [10, 20, 30, 40, 50]"]},
                "errors": ["java.lang.ArrayIndexOutOfBoundsException"],
                "xp": 100,
                "quiz": [{"q": "What is the index of the last element in an array 'arr'?", "opts": ["arr.length", "arr.length - 1", "arr.size", "arr.length()"], "ans": 1, "exp": "Java arrays are 0-indexed, so the last element is at index arr.length - 1."}]
            },
            {
                "order": 5, "slug": "strings", "title": "Strings & String Constant Pool",
                "summary": "Strings in Java are IMMUTABLE objects. Master String Pool optimization, equals() vs == operator, StringBuilder & StringBuffer.",
                "rules": [
                    "String literals are stored in the String Constant Pool (SCP) inside Heap.",
                    "== checks reference equality (memory address); .equals() checks actual character content equality.",
                    "Use StringBuilder for fast, mutable string concatenation in single-threaded environments."
                ],
                "code": "public class StringDemo {\n    public static void main(String[] args) {\n        String s1 = \"Java\";\n        String s2 = \"Java\";\n        String s3 = new String(\"Java\");\n        \n        System.out.println(s1 == s2);      // true (same SCP memory)\n        System.out.println(s1 == s3);      // false (different Heap memory)\n        System.out.println(s1.equals(s3)); // true (same content)\n    }\n}",
                "memory": {"stack": ["s1 -> SCP@0x01", "s2 -> SCP@0x01", "s3 -> Heap@0x09"], "heap": ["String Pool @0x01: \"Java\"", "Heap Object @0x09: \"Java\""]},
                "errors": ["java.lang.NullPointerException when calling methods on a null string"],
                "xp": 120,
                "quiz": [{"q": "Why is String immutable in Java?", "opts": ["Security & Thread Safety", "Caching in SCP", "Hashcode Caching", "All of the above"], "ans": 3, "exp": "Immutability allows string pool caching, thread safety, and secure key usage in HashMaps."}]
            },
            {
                "order": 6, "slug": "static-keyword", "title": "Static Keyword & Metaspace",
                "summary": "Static members belong to the CLASS rather than instance objects. Master static variables, static methods, static blocks, and Metaspace memory.",
                "rules": [
                    "Static variables are shared across all instances of a class.",
                    "Static methods CANNOT directly access non-static instance variables or 'this' keyword.",
                    "Static blocks execute ONCE when the class is first loaded into Metaspace."
                ],
                "code": "public class StaticDemo {\n    static String college = \"KIT\"; // Shared memory\n    String studentName;\n    \n    static void displayCollege() {\n        System.out.println(\"College: \" + college);\n    }\n    \n    public static void main(String[] args) {\n        StaticDemo.displayCollege();\n    }\n}",
                "memory": {"metaspace": ["Class Metadata for StaticDemo", "static String college = \"KIT\""], "stack": ["main() Frame"], "heap": []},
                "errors": ["java: non-static variable studentName cannot be referenced from a static context"],
                "xp": 110,
                "quiz": [{"q": "When does a static block execute in Java?", "opts": ["When an object is created", "When the class is loaded into memory", "When main() finishes", "During garbage collection"], "ans": 1, "exp": "Static blocks execute once when the JVM loads the class."}]
            },
            {
                "order": 7, "slug": "encapsulation", "title": "Encapsulation & Data Hiding",
                "summary": "Wrapping data (variables) and code (methods) together as a single unit while hiding internal state using private fields and public getters/setters.",
                "rules": [
                    "Declare class variables as 'private'.",
                    "Provide public getter and setter methods to control read/write validation.",
                    "Prevents external code from corrupting internal object state."
                ],
                "code": "public class BankAccount {\n    private double balance;\n    \n    public double getBalance() {\n        return this.balance;\n    }\n    \n    public void deposit(double amount) {\n        if (amount > 0) {\n            this.balance += amount;\n        }\n    }\n}",
                "memory": {"stack": ["accountRef -> Heap@0x77"], "heap": ["BankAccount Object @0x77: { private balance: 5000.0 }"]},
                "errors": ["java: balance has private access in BankAccount"],
                "xp": 110,
                "quiz": [{"q": "What is the primary goal of Encapsulation?", "opts": ["Data Hiding & Security", "Faster Execution", "Multiple Inheritance", "Garbage Collection"], "ans": 0, "exp": "Encapsulation protects object state by hiding private fields behind public accessor methods."}]
            },
            {
                "order": 8, "slug": "constructors", "title": "Constructors & Constructor Chaining",
                "summary": "Special method invoked when an object is instantiated. Learn Default, Parameterized, Copy Constructors, and 'this()' chaining.",
                "rules": [
                    "Constructor name MUST match the class name exactly and has NO return type.",
                    "If you do NOT write any constructor, Java automatically provides a default no-arg constructor.",
                    "Constructor chaining via this(...) must be the VERY FIRST statement inside the constructor!"
                ],
                "code": "public class Student {\n    String name;\n    int id;\n    \n    public Student() {\n        this(\"Unknown\", 0); // Constructor chaining\n    }\n    \n    public Student(String name, int id) {\n        this.name = name;\n        this.id = id;\n    }\n}",
                "memory": {"stack": ["s1 -> Heap@0x12"], "heap": ["Student Object @0x12: { name: \"Unknown\", id: 0 }"]},
                "errors": ["java: call to this() must be first statement in constructor"],
                "xp": 120,
                "quiz": [{"q": "What is the return type of a Java constructor?", "opts": ["void", "int", "Object", "No return type"], "ans": 3, "exp": "Constructors do not have any return type, not even void."}]
            },
            {
                "order": 9, "slug": "anonymous-objects", "title": "Anonymous Objects",
                "summary": "Objects created without assigning a reference variable name (e.g. 'new Calculation().fact(5);').",
                "rules": [
                    "Used for one-time method invocations where stored reference is unnecessary.",
                    "Eligible for Garbage Collection immediately after the statement executes.",
                    "Saves Stack memory since no reference variable is allocated."
                ],
                "code": "public class AnonymousDemo {\n    void showMessage() {\n        System.out.println(\"Executing via Anonymous Object!\");\n    }\n    \n    public static void main(String[] args) {\n        new AnonymousDemo().showMessage(); // One-time execution\n    }\n}",
                "memory": {"stack": ["main() Frame (No local reference saved)"], "heap": ["Anonymous Object allocated -> Method called -> Eligible for GC immediately"]},
                "errors": ["N/A - Syntax is concise"],
                "xp": 100,
                "quiz": [{"q": "When is an anonymous object eligible for Garbage Collection?", "opts": ["Immediately after its method execution finishes", "Never", "When main() exits", "When the class is unloaded"], "ans": 0, "exp": "Since no reference holds an anonymous object, it becomes eligible for GC immediately."}]
            },
            {
                "order": 10, "slug": "inheritance", "title": "Inheritance & IS-A Relationship",
                "summary": "Mechanism where a subclass inherits fields and methods from a superclass using 'extends'. Supports Single, Multilevel, and Hierarchical inheritance.",
                "rules": [
                    "Java does NOT support Multiple Inheritance with classes to avoid the Diamond Problem.",
                    "Subclass inherits all public and protected members of superclass.",
                    "Private fields are NOT directly accessible by subclass (must use getters)."
                ],
                "code": "class Animal {\n    void eat() { System.out.println(\"Eating...\"); }\n}\n\nclass Dog extends Animal {\n    void bark() { System.out.println(\"Barking...\"); }\n}\n\npublic class TestInheritance {\n    public static void main(String[] args) {\n        Dog d = new Dog();\n        d.eat();  // Inherited method\n        d.bark(); // Subclass method\n    }\n}",
                "memory": {"stack": ["d -> Heap@0x55"], "heap": ["Dog Object @0x55 (contains Animal + Dog methods)"]},
                "errors": ["java: cyclic inheritance involving ClassA"],
                "xp": 120,
                "quiz": [{"q": "Why does Java disallow Multiple Inheritance with classes?", "opts": ["Diamond Problem / Ambiguity", "Memory Leak", "Garbage Collector Limitation", "Performance Overhead"], "ans": 0, "exp": "Multiple inheritance causes compiler ambiguity if two parent classes have methods with identical signatures."}]
            },
            {
                "order": 11, "slug": "this-and-super-keywords", "title": "This and Super Keywords / Methods",
                "summary": "Master 'this' (refers to current object) and 'super' (refers to parent object), along with constructor calls 'this()' and 'super()'.",
                "rules": [
                    "this refers to the current class instance.",
                    "super refers to the immediate parent class instance.",
                    "super() is invoked automatically as the first line of any subclass constructor if not explicitly written."
                ],
                "code": "class Parent {\n    Parent() { System.out.println(\"Parent Constructor\"); }\n}\n\nclass Child extends Parent {\n    Child() {\n        super(); // Invokes Parent constructor\n        System.out.println(\"Child Constructor\");\n    }\n}",
                "memory": {"stack": ["childRef -> Heap@0x33"], "heap": ["Child Object @0x33 (Parent portion initialized first)"]},
                "errors": ["java: call to super() must be first statement in constructor"],
                "xp": 120,
                "quiz": [{"q": "Which statement is added automatically as the first line of a constructor if missing?", "opts": ["this();", "super();", "return;", "System.exit(0);"], "ans": 1, "exp": "The compiler automatically inserts super() to initialize the parent class."}]
            },
            {
                "order": 12, "slug": "access-modifiers", "title": "Access Modifiers & Visibility Matrix",
                "summary": "Control access to classes, constructors, methods, and fields: private, default (package-private), protected, and public.",
                "rules": [
                    "private: Accessible ONLY within the same class.",
                    "default: Accessible ONLY within the same package.",
                    "protected: Accessible within the same package AND by subclasses in different packages.",
                    "public: Accessible everywhere across the application."
                ],
                "code": "public class AccessDemo {\n    private int secret = 100;\n    int defaultVar = 200;\n    protected int protectedVar = 300;\n    public int publicVar = 400;\n}",
                "memory": {"metaspace": ["Access Modifier Visibility Matrix"], "stack": [], "heap": []},
                "errors": ["java: secret has private access in AccessDemo"],
                "xp": 110,
                "quiz": [{"q": "Which modifier allows access to subclasses in different packages?", "opts": ["private", "default", "protected", "public"], "ans": 2, "exp": "protected grants access within the same package and to child classes outside the package."}]
            },
            {
                "order": 13, "slug": "packages", "title": "Packages & Import Statements",
                "summary": "Organize classes into namespaces to prevent naming collisions and manage access permissions using package declarations and imports.",
                "rules": [
                    "Package declaration MUST be the very first non-comment line in a Java source file.",
                    "java.lang package is imported automatically by default (String, System, Math).",
                    "Importing subpackages requires explicit import statements (e.g. java.util.* does NOT import java.util.concurrent.*)."
                ],
                "code": "package com.placementarena.utils;\n\nimport java.util.ArrayList;\nimport java.util.List;\n\npublic class PackageDemo {\n    public static void main(String[] args) {\n        List<String> items = new ArrayList<>();\n    }\n}",
                "memory": {"metaspace": ["Package namespace mapping"], "stack": [], "heap": []},
                "errors": ["java: package com.placementarena.utils does not exist"],
                "xp": 100,
                "quiz": [{"q": "Which package is imported automatically in every Java program?", "opts": ["java.util", "java.io", "java.lang", "java.net"], "ans": 2, "exp": "java.lang is automatically imported into all Java translation units."}]
            },
            {
                "order": 14, "slug": "dynamic-method-dispatch", "title": "Dynamic Method Dispatch (Run-time Polymorphism)",
                "summary": "Mechanism where a call to an overridden method is resolved at RUNTIME rather than compile time using parent reference pointing to child object.",
                "rules": [
                    "Parent reference can hold Child object: SuperClass obj = new SubClass();",
                    "Which METHOD executes depends on the actual OBJECT type at runtime, not the reference type!",
                    "Which VARIABLE is accessed depends on the REFERENCE type (variables are NOT polymorphic)."
                ],
                "code": "class Bike {\n    void run() { System.out.println(\"Bike running...\"); }\n}\nclass Splendor extends Bike {\n    @Override\n    void run() { System.out.println(\"Splendor running safely at 60km/h\"); }\n}\n\npublic class TestDispatch {\n    public static void main(String[] args) {\n        Bike b = new Splendor(); // Upcasting\n        b.run(); // Executes Splendor's run() at runtime!\n    }\n}",
                "memory": {"stack": ["Bike b -> Heap@0x99"], "heap": ["Splendor Object @0x99 (V-Table points to Splendor.run())"]},
                "errors": ["java: cannot find symbol method childSpecificMethod()"],
                "xp": 130,
                "quiz": [{"q": "In 'Parent p = new Child(); p.show();', which show() executes if overridden?", "opts": ["Parent's show()", "Child's show()", "Compiler Error", "Runtime Exception"], "ans": 1, "exp": "Dynamic Method Dispatch executes the overridden method of the actual object (Child)."}]
            },
            {
                "order": 15, "slug": "final-keyword", "title": "Final Keyword (Variables, Methods, Classes)",
                "summary": "Restricted keyword used to apply immutability and prevent modification.",
                "rules": [
                    "final variable: Value cannot be reassigned once initialized (Constant).",
                    "final method: Cannot be OVERRIDDEN by any subclass.",
                    "final class: Cannot be INHERITED / EXTENDED by any class (e.g. String class is final)."
                ],
                "code": "final class ImmutableConfig {\n    final int MAX_ATTEMPTS = 3;\n    \n    final void display() {\n        System.out.println(\"Max attempts: \" + MAX_ATTEMPTS);\n    }\n}",
                "memory": {"metaspace": ["ImmutableConfig marked final"], "stack": [], "heap": []},
                "errors": ["java: cannot assign a value to final variable MAX_ATTEMPTS", "java: cannot inherit from final ImmutableConfig"],
                "xp": 110,
                "quiz": [{"q": "What happens if you try to inherit from a 'final' class?", "opts": ["Compilation Error", "Warning", "Runtime Exception", "Allowed"], "ans": 0, "exp": "Final classes cannot be extended, causing a compilation error."}]
            },
            {
                "order": 16, "slug": "upcasting-and-downcasting", "title": "Upcasting, Downcasting & Instanceof Operator",
                "summary": "Type casting object references up and down the inheritance hierarchy safely using the 'instanceof' operator.",
                "rules": [
                    "Upcasting (Sub to Super): Safe and done implicitly (Parent p = new Child()).",
                    "Downcasting (Super to Sub): Unsafe! Requires explicit cast (Child c = (Child) p).",
                    "Always check with 'instanceof' before downcasting to avoid ClassCastException!"
                ],
                "code": "class Parent {}\nclass Child extends Parent {\n    void special() { System.out.println(\"Special Child Method\"); }\n}\n\npublic class CastDemo {\n    public static void main(String[] args) {\n        Parent p = new Child(); // Upcasting\n        if (p instanceof Child) {\n            Child c = (Child) p; // Downcasting\n            c.special();\n        }\n    }\n}",
                "memory": {"stack": ["p -> Heap@0x44", "c -> Heap@0x44"], "heap": ["Child Object @0x44"]},
                "errors": ["java.lang.ClassCastException: Parent cannot be cast to Child"],
                "xp": 130,
                "quiz": [{"q": "Which operator is used to check an object's type before downcasting?", "opts": ["typeof", "instanceof", "isinstance", "castof"], "ans": 1, "exp": "instanceof safely checks if an object is an instance of a specific class or interface."}]
            },
            {
                "order": 17, "slug": "wrapper-classes", "title": "Wrapper Classes, Autoboxing & Unboxing",
                "summary": "Converting primitive types into Object wrappers (int -> Integer, double -> Double) to use in Collections Framework.",
                "rules": [
                    "Autoboxing: Automatic conversion of primitive to wrapper (Integer obj = 10;).",
                    "Unboxing: Automatic conversion of wrapper to primitive (int x = obj;).",
                    "Integer Caching: Values between -128 and 127 are cached in Integer Cache Pool."
                ],
                "code": "public class WrapperDemo {\n    public static void main(String[] args) {\n        int p = 50;\n        Integer obj = p; // Autoboxing\n        int back = obj;  // Unboxing\n        \n        System.out.println(\"Parsed: \" + Integer.parseInt(\"123\"));\n    }\n}",
                "memory": {"stack": ["int p = 50", "Integer obj -> Heap@0x88", "int back = 50"], "heap": ["Integer Object @0x88 (value: 50)"]},
                "errors": ["java.lang.NullPointerException when unboxing a null Wrapper object!"],
                "xp": 110,
                "quiz": [{"q": "What is the term for automatic conversion of primitive to Wrapper object?", "opts": ["Autoboxing", "Unboxing", "Upcasting", "Parsing"], "ans": 0, "exp": "Autoboxing is Java's automatic conversion of primitive types to their corresponding wrapper classes."}]
            },
            {
                "order": 18, "slug": "abstract-keyword", "title": "Abstract Keyword & Abstract Classes",
                "summary": "Achieving partial abstraction (0 to 100%) using abstract classes and abstract methods.",
                "rules": [
                    "An abstract class CANNOT be instantiated directly using 'new'.",
                    "Abstract methods have NO body (e.g. abstract void draw();) and MUST be implemented by concrete subclasses.",
                    "If a class contains even one abstract method, the class MUST be declared abstract."
                ],
                "code": "abstract class Shape {\n    abstract void draw(); // Abstract method\n    void info() { System.out.println(\"Shape Object\"); }\n}\n\nclass Circle extends Shape {\n    @Override\n    void draw() { System.out.println(\"Drawing Circle\"); }\n}",
                "memory": {"stack": ["Shape s -> Heap@0x22 (Circle instance)"], "heap": ["Circle Object @0x22"]},
                "errors": ["java: Shape is abstract; cannot be instantiated"],
                "xp": 120,
                "quiz": [{"q": "Can an abstract class have a constructor in Java?", "opts": ["Yes", "No", "Only static constructors", "Only private constructors"], "ans": 0, "exp": "Yes! Abstract class constructors are invoked when a concrete subclass object is instantiated."}]
            },
            {
                "order": 19, "slug": "inner-classes", "title": "Inner Classes & Nested Classes",
                "summary": "Classes defined inside another class: Member Inner Class, Static Nested Class, Local Inner Class, and Anonymous Inner Class.",
                "rules": [
                    "Member Inner Class requires an instance of Outer class: Outer.Inner in = outerObj.new Inner();",
                    "Static Nested Class does NOT require an outer instance: Outer.StaticNested sn = new Outer.StaticNested();",
                    "Anonymous Inner Class is declared and instantiated in a single expression without a name."
                ],
                "code": "class Outer {\n    private String msg = \"Hello Inner!\";\n    \n    class Inner {\n        void print() { System.out.println(msg); }\n    }\n}\n\npublic class InnerTest {\n    public static void main(String[] args) {\n        Outer outer = new Outer();\n        Outer.Inner inner = outer.new Inner();\n        inner.print();\n    }\n}",
                "memory": {"stack": ["outer -> Heap@0x11", "inner -> Heap@0x12"], "heap": ["Outer Object @0x11", "Inner Object @0x12 (holds outer reference)"]},
                "errors": ["java: non-static variable this cannot be referenced from a static context"],
                "xp": 130,
                "quiz": [{"q": "Which inner class can be instantiated without creating an outer class instance?", "opts": ["Member Inner Class", "Static Nested Class", "Local Inner Class", "Anonymous Inner Class"], "ans": 1, "exp": "Static nested classes do not require an outer class instance to be instantiated."}]
            },
            {
                "order": 20, "slug": "interfaces", "title": "Interfaces & Multiple Inheritance",
                "summary": "Achieving 100% Abstraction and Multiple Inheritance in Java using 'interface' and 'implements'. Includes Java 8+ default and static methods.",
                "rules": [
                    "All fields in an interface are implicitly 'public static final'.",
                    "All abstract methods are implicitly 'public abstract'.",
                    "Java 8 introduced 'default' methods (with bodies) and 'static' utility methods inside interfaces."
                ],
                "code": "interface Printable {\n    void print();\n    default void log() {\n        System.out.println(\"Default logging method\");\n    }\n}\n\nclass Document implements Printable {\n    public void print() {\n        System.out.println(\"Printing Document...\");\n    }\n}",
                "memory": {"stack": ["p -> Heap@0x66"], "heap": ["Document Object @0x66"]},
                "errors": ["java: print() in Document cannot implement print() in Printable; attempting to assign weaker access privileges (must be public)"],
                "xp": 130,
                "quiz": [{"q": "What is the implicit modifier for fields declared in an Interface?", "opts": ["private final", "public static final", "protected static", "transient"], "ans": 1, "exp": "All interface fields are implicitly public, static, and final."}]
            },
            {
                "order": 21, "slug": "enums", "title": "Enums in Java",
                "summary": "Special data type that enables a variable to be a set of predefined constants.",
                "rules": [
                    "Enum constants are implicitly 'public static final' instances of the Enum class.",
                    "Enums can contain fields, constructors, and methods.",
                    "Enum constructors are PRIVATE by default and cannot be called with 'new'."
                ],
                "code": "enum Day {\n    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY;\n}\n\npublic class EnumDemo {\n    public static void main(String[] args) {\n        Day today = Day.FRIDAY;\n        System.out.println(\"Today is: \" + today + \" (Ordinal: \" + today.ordinal() + \")\");\n    }\n}",
                "memory": {"metaspace": ["Enum Day class metadata & static constant instances"], "stack": ["Day today -> Enum Instance"], "heap": []},
                "errors": ["java: enum types may not be instantiated with new"],
                "xp": 110,
                "quiz": [{"q": "Which method returns an array of all constants in an Enum?", "opts": ["values()", "getConstants()", "toArray()", "all()"], "ans": 0, "exp": "The values() method returns an array containing all enum constants in order."}]
            },
            {
                "order": 22, "slug": "lambda-expressions", "title": "Lambda Expressions & Functional Interfaces",
                "summary": "Writing concise functional programming code using Arrow (->) syntax and @FunctionalInterface.",
                "rules": [
                    "A Functional Interface contains EXACTLY ONE abstract method.",
                    "Lambda Syntax: (params) -> { body }",
                    "Eliminates boilerplate anonymous inner class code."
                ],
                "code": "@FunctionalInterface\ninterface MathOperation {\n    int operate(int a, int b);\n}\n\npublic class LambdaDemo {\n    public static void main(String[] args) {\n        MathOperation add = (a, b) -> a + b;\n        MathOperation multiply = (a, b) -> a * b;\n        \n        System.out.println(\"Sum: \" + add.operate(10, 20));\n        System.out.println(\"Product: \" + multiply.operate(10, 20));\n    }\n}",
                "memory": {"stack": ["add -> Lambda Instance", "multiply -> Lambda Instance"], "heap": ["Invokedynamic callsite objects"]},
                "errors": ["java: unexpected @FunctionalInterface annotation (found multiple abstract methods)"],
                "xp": 140,
                "quiz": [{"q": "How many abstract methods can a @FunctionalInterface contain?", "opts": ["Exactly One", "Zero", "Unlimited", "At least two"], "ans": 0, "exp": "A functional interface must contain exactly one abstract method."}]
            },
            {
                "order": 23, "slug": "exceptions", "title": "Exception Handling & Custom Exceptions",
                "summary": "Handling runtime errors using try, catch, finally, throw, and throws keywords.",
                "rules": [
                    "Checked Exceptions (IOException, SQLException) MUST be handled or declared with 'throws'.",
                    "Unchecked Exceptions (NullPointerException, ArithmeticException) extend RuntimeException.",
                    "finally block ALWAYS executes regardless of whether an exception occurs or is caught."
                ],
                "code": "public class ExceptionDemo {\n    public static void main(String[] args) {\n        try {\n            int result = 10 / 0;\n        } catch (ArithmeticException e) {\n            System.err.println(\"Caught Division by Zero: \" + e.getMessage());\n        } finally {\n            System.out.println(\"Cleanup executed successfully.\");\n        }\n    }\n}",
                "memory": {"stack": ["main() Frame", "Exception Object created on Heap -> Caught in catch block"], "heap": ["ArithmeticException Object @0x99"]},
                "errors": ["java: unreported exception java.io.IOException; must be caught or declared to be thrown"],
                "xp": 140,
                "quiz": [{"q": "Which block ALWAYS executes whether an exception is thrown or caught?", "opts": ["try", "catch", "finally", "throws"], "ans": 2, "exp": "The finally block always executes after try-catch for clean resource closing."}]
            }
        ]

        for item in java_quest_topics:
            JavaTopic.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "order": item["order"],
                    "title": item["title"],
                    "concept_summary": item["summary"],
                    "syntax_rules": item["rules"],
                    "code_example": item["code"],
                    "memory_diagram_json": item["memory"],
                    "common_errors": item["errors"],
                    "xp_reward": item["xp"],
                    "quiz_json": item["quiz"]
                }
            )

        self.stdout.write(self.style.SUCCESS("All 23 Java Quest topics seeded successfully!"))
