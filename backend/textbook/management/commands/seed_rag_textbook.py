from django.core.management.base import BaseCommand
from textbook.models import Document, DocumentChunk
from textbook.rag_engine import get_text_embedding

class Command(BaseCommand):
    help = 'Seeds raw subject document notes and concept chunks into the database for Multi-Document RAG'

    def handle(self, *args, **options):
        self.stdout.write("Seeding Multi-Document RAG concept store...")

        documents_data = [
            {
                "title": "Verbal Ability Master Notes Vol 1",
                "file_name": "Verbal_Master_Notes_139P.pdf",
                "subject": "verbal",
                "topic_slug": "tenses-verb-forms",
                "chunks": [
                    "Simple Present Tense uses V1 or V1+s/es for habits and universal facts. Present Continuous uses am/is/are + V4 (-ing). Present Perfect uses have/has + V3 for completed actions with present connection. Stative verbs like know, believe, understand, love, sound never take continuous -ing forms. Simple Past uses V2 form exclusively.",
                    "Master list of uncountable nouns: Information, Advice, Furniture, Equipment, Luggage, Scenery, Poetry, Machinery, News, Physics, Mathematics, Athletics, Bread, Traffic. Uncountable nouns are NEVER pluralized with -s and take singular verbs. Compound nouns pluralize the root noun: Mothers-in-law, Commanders-in-chief, Passers-by.",
                    "Who vs Whom Magic Trick: Replace with HE -> WHO (subject), replace with HIM -> WHOM (object). After prepositions like between/among/to, always use object pronouns: Between you and me (NOT between you and I). 231 Rule for positive contexts: You, he and I. 123 Rule for mistakes/confessions: I, you and he.",
                    "Each of / One of / Every one of + Plural Noun ALWAYS takes a SINGULAR verb (e.g., Each of the students is present). A number of takes a PLURAL verb, whereas The number of takes a SINGULAR verb. Either...or / Neither...nor agrees with NEAREST subject. Along with / As well as agrees with FIRST subject.",
                    "Articles depend on SOUND, NOT SPELLING. Use 'a' before consonant sounds: a university (Yu sound), a European country, a one-eyed man. Use 'an' before vowel sounds: an hour (silent H), an honest man, an MBA graduate (Em sound), an MLA. Parallel comparatives take 'The' on both sides: The higher you go, THE cooler it is."
                ]
            },
            {
                "title": "Aptitude Formulas & Shortcuts Handbook",
                "file_name": "Aptitude_Shortcuts_Handwritten.pdf",
                "subject": "aptitude",
                "topic_slug": "percentages-growth",
                "chunks": [
                    "Simple Interest grows linearly: SI = P*R*T/100. Compound Interest grows exponentially: A = P*(1 + R/100)^T. Difference between CI and SI for 2 years: Diff = P*(R/100)^2. For 3 years: Diff = P*(R/100)^2 * (300 + R)/100. Dishonest dealer formula: Gain % = (Error / (True Value - Error)) * 100."
                ]
            },
            {
                "title": "Java OOP & Design Patterns Core Guide",
                "file_name": "Java_OOP_Mastery.pdf",
                "subject": "java",
                "topic_slug": "java-oop-mastery",
                "chunks": [
                    "Java OOP 4 Pillars: Encapsulation (private fields + getters/setters), Abstraction (hiding implementation details using abstract classes and interfaces), Inheritance (extends keyword for code reuse), Polymorphism (Method Overloading compile-time vs Method Overriding runtime @Override). Interfaces allow multiple inheritance of type in Java."
                ]
            }
        ]

        total_chunks = 0
        for doc_info in documents_data:
            doc_obj, _ = Document.objects.get_or_create(
                title=doc_info["title"],
                file_name=doc_info["file_name"],
                subject=doc_info["subject"],
                topic_slug=doc_info["topic_slug"]
            )

            for idx, content in enumerate(doc_info["chunks"]):
                chunk_obj, created = DocumentChunk.objects.get_or_create(
                    document=doc_obj,
                    subject=doc_info["subject"],
                    topic_slug=doc_info["topic_slug"],
                    chapter_title=doc_info["title"],
                    chunk_index=idx,
                    content=content,
                    defaults={"vector_json": get_text_embedding(content)}
                )
                if created:
                    total_chunks += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {total_chunks} multi-document RAG concept chunks!"))
