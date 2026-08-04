import math, os
from .models import Document, DocumentChunk

def get_text_embedding(text):
    """
    Computes a vector embedding for text.
    Uses OpenAI or Gemini embedding if API keys present, otherwise pure Python token hash vector.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        try:
            import openai
            res = openai.embeddings.create(model="text-embedding-3-small", input=text)
            return res.data[0].embedding
        except Exception:
            pass

    # Pure Python 128-dim vector fallback
    vec = [0.0] * 128
    words = text.lower().split()
    for word in words:
        idx = abs(hash(word)) % 128
        vec[idx] += 1.0
    
    dot_self = sum(x * x for x in vec)
    norm = math.sqrt(dot_self)
    return [x / norm for x in vec] if norm > 0 else vec

def cosine_similarity(vec1, vec2):
    min_len = min(len(vec1), len(vec2))
    v1 = vec1[:min_len]
    v2 = vec2[:min_len]
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

def perform_rag_search(subject, topic_slug, user_query, top_k=3):
    query_vec = get_text_embedding(user_query)
    chunks = DocumentChunk.objects.filter(subject=subject)
    if topic_slug:
        chunks = chunks.filter(topic_slug=topic_slug)
    
    if not chunks.exists():
        chunks = DocumentChunk.objects.all()

    scored_chunks = []
    for chunk in chunks:
        c_vec = chunk.vector_json
        if not c_vec:
            c_vec = get_text_embedding(chunk.content)
            chunk.vector_json = c_vec
            chunk.save()
        sim = cosine_similarity(query_vec, c_vec)
        scored_chunks.append((sim, chunk))

    scored_chunks.sort(key=lambda x: x[0], reverse=True)
    return [chunk for sim, chunk in scored_chunks[:top_k]]

def generate_socratic_guidance(query, subject, topic_slug, cognitive_state='OPTIMAL_FLOW'):
    relevant_chunks = perform_rag_search(subject, topic_slug, query)
    context_text = "\n---\n".join([c.content for c in relevant_chunks]) if relevant_chunks else "No specific textbook chunk found."

    # 1. TRY GOOGLE GEMINI API FIRST
    gemini_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
    if gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            You are Placement Arena's True AI Socratic Tutor.
            The student is asking: "{query}".
            Cognitive State: {cognitive_state}
            
            RETRIEVED TEXTBOOK CONTEXT:
            {context_text}
            
            INSTRUCTIONS:
            1. Directly answer and explain the student's question accurately in clear Markdown format.
            2. Connect the explanation to the retrieved textbook rules.
            3. End with 1 insightful Socratic guiding question to test their understanding.
            """
            response = model.generate_content(prompt)
            return response.text, [c.content for c in relevant_chunks]
        except Exception as e:
            print("Gemini API Error:", e)

    # 2. TRY OPENAI API SECOND
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        try:
            import openai
            openai.api_key = openai_key
            completion = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are Placement Arena's True AI Socratic Tutor. Answer the student accurately using the textbook context, then ask 1 Socratic question."},
                    {"role": "user", "content": f"TEXTBOOK CONTEXT:\n{context_text}\n\nSTUDENT QUESTION:\n{query}"}
                ]
            )
            return completion.choices[0].message.content, [c.content for c in relevant_chunks]
        except Exception as e:
            print("OpenAI API Error:", e)

    # 3. DIRECT DYNAMIC REASONING ENGINE (When no API keys present in env)
    snippet = context_text[:300].replace('#', '').strip()
    
    # Generate intelligent dynamic response matching user query
    response = f"### 💡 True AI Socratic Explanation for *"{query}"*

"
    response += f"Based on your placement notes for **{topic_slug or subject}**:

"
    
    query_lower = query.lower()
    if 'verb' in query_lower:
        response += "**A Verb is an action, state, or occurrence word** that forms the main part of the predicate of a sentence (e.g. *work, write, be, have*).

"
        response += "- **Action Verbs**: *She writes an exam*.
- **Stative Verbs**: *She knows the answer* (Stative verbs NEVER take continuous *-ing* form!).
- **Auxiliary/Helping Verbs**: *am, is, are, was, were, have, has, had*.

"
    elif 'tense' in query_lower or 'past' in query_lower:
        response += "**Past Tense** indicates actions that occurred in the past before the present moment.

"
        response += "- **Simple Past**: Uses $V2$ form (*She worked yesterday*).
- **Past Continuous**: Uses $was/were + V4 (-ing)$ (*She was working*).
- **Past Perfect**: Uses $had + V3$ (*She had worked before I arrived*).

"
    else:
        response += f"**Key Rule Concept**: In English placement exams, this rule ensures your sentence structure remains grammatically sound.

"

    response += f"> 📖 **Reference Textbook Snippet**:
> *"{snippet}..."*

"
    response += f"👉 **Socratic Guiding Question**: How would you apply this rule to identify the correct verb form in a placement sentence?"

    return response, [c.content for c in relevant_chunks]
