from django.core.management.base import BaseCommand
from textbook.models import TextbookChunk
from textbook.rag_engine import get_text_embedding

class Command(BaseCommand):
    help = 'Seeds raw textbook notes and concept chunks into the database for True AI RAG'

    def handle(self, *args, **options):
        self.stdout.write("Seeding raw RAG textbook concept chunks...")

        dataset = [
            {
                "subject": "verbal",
                "topic_slug": "tenses-verb-forms",
                "chapter_title": "12 Tenses & 5 Verb Forms",
                "content": "Simple Present Tense uses V1 or V1+s/es for habits and universal facts. Present Continuous uses am/is/are + V4 (-ing). Present Perfect uses have/has + V3 for completed actions with present connection. Stative verbs like know, believe, understand, love, sound never take continuous -ing forms. Simple Past uses V2 form exclusively."
            },
            {
                "subject": "verbal",
                "topic_slug": "nouns-deep-detail",
                "chapter_title": "Uncountable Nouns & Compound Plurals",
                "content": "Master list of uncountable nouns: Information, Advice, Furniture, Equipment, Luggage, Scenery, Poetry, Machinery, News, Physics, Mathematics, Athletics, Bread, Traffic. Uncountable nouns are NEVER pluralized with -s and take singular verbs. Compound nouns pluralize the root noun: Mothers-in-law, Commanders-in-chief, Passers-by."
            },
            {
                "subject": "verbal",
                "topic_slug": "pronouns-agreement",
                "chapter_title": "Who vs Whom & 231 Pronoun Order",
                "content": "Who vs Whom Magic Trick: Replace with HE -> WHO (subject), replace with HIM -> WHOM (object). After prepositions like between/among/to, always use object pronouns: Between you and me (NOT between you and I). 231 Rule for positive contexts: You, he and I. 123 Rule for mistakes/confessions: I, you and he."
            },
            {
                "subject": "verbal",
                "topic_slug": "subject-verb-agreement",
                "chapter_title": "20 Golden SVA Rules",
                "content": "Each of / One of / Every one of + Plural Noun ALWAYS takes a SINGULAR verb (e.g., Each of the students is present). A number of takes a PLURAL verb, whereas The number of takes a SINGULAR verb. Either...or / Neither...nor agrees with NEAREST subject. Along with / As well as agrees with FIRST subject."
            },
            {
                "subject": "verbal",
                "topic_slug": "articles-sound-rules",
                "chapter_title": "Sound-based A vs An Rules",
                "content": "Articles depend on SOUND, NOT SPELLING. Use 'a' before consonant sounds: a university (Yu sound), a European country, a one-eyed man. Use 'an' before vowel sounds: an hour (silent H), an honest man, an MBA graduate (Em sound), an MLA. Parallel comparatives take 'The' on both sides: The higher you go, THE cooler it is."
            },
            {
                "subject": "aptitude",
                "topic_slug": "percentages-growth",
                "chapter_title": "Vedic Multiplication & SI vs CI Growth",
                "content": "Simple Interest grows linearly: SI = P*R*T/100. Compound Interest grows exponentially: A = P*(1 + R/100)^T. Difference between CI and SI for 2 years: Diff = P*(R/100)^2. For 3 years: Diff = P*(R/100)^2 * (300 + R)/100. Dishonest dealer formula: Gain % = (Error / (True Value - Error)) * 100."
            },
            {
                "subject": "java",
                "topic_slug": "java-oop-mastery",
                "chapter_title": "Inheritance, Polymorphism & Abstraction",
                "content": "Java OOP 4 Pillars: Encapsulation (private fields + getters/setters), Abstraction (hiding implementation details using abstract classes and interfaces), Inheritance (extends keyword for code reuse), Polymorphism (Method Overloading compile-time vs Method Overriding runtime @Override). Interfaces allow multiple inheritance of type in Java."
            }
        ]

        created_count = 0
        for data in dataset:
            obj, created = TextbookChunk.objects.get_or_create(
                subject=data["subject"],
                topic_slug=data["topic_slug"],
                chapter_title=data["chapter_title"],
                content=data["content"],
                defaults={"vector_json": get_text_embedding(data["content"])}
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {created_count} raw RAG textbook chunks into DB!"))
