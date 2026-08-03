import math, os
from .models import TextbookChunk

def get_text_embedding(text):
    """
    Computes a vector embedding for text.
    If OPENAI_API_KEY is present, calls OpenAI embeddings API.
    Otherwise uses a 128-dim normalized token hash vector in pure Python.
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
    chunks = TextbookChunk.objects.filter(subject=subject)
    if topic_slug:
        chunks = chunks.filter(topic_slug=topic_slug)
    
    if not chunks.exists():
        chunks = TextbookChunk.objects.all()

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

    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        try:
            import openai
            sys_msg = "You are Placement Arena's True AI NeuroTutor. Use ONLY the provided document context to guide the student step-by-step using Socratic questioning without giving away direct answers."
            if cognitive_state == 'COGNITIVE_OVERLOAD':
                sys_msg += " The student is experiencing cognitive overload. Simplify the concept using a real-world physical analogy and ask 1 simple question."
            elif cognitive_state == 'UNDER_STIMULATED':
                sys_msg += " The student is under-stimulated/bored. Present a challenging real-world placement edge-case."
            
            completion = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": sys_msg},
                    {"role": "user", "content": f"RAW TEXTBOOK KNOWLEDGE:\n{context_text}\n\nSTUDENT QUESTION:\n{query}"}
                ]
            )
            return completion.choices[0].message.content, [c.content for c in relevant_chunks]
        except Exception:
            pass

    # Clean Fallback
    snippet = context_text[:300]
    response = f"💡 **Socratic Guidance**: Based on your textbook notes for *{topic_slug or subject}*:\n\n"
    if cognitive_state == 'COGNITIVE_OVERLOAD':
        response += "⚠️ **Cognitive Assistance Triggered**: Let's break this down into a simpler picture.\n\n"
    elif cognitive_state == 'UNDER_STIMULATED':
        response += "🚀 **Placement Edge-Case Challenge**: Excellent speed! Consider this advanced placement variation.\n\n"

    response += f"📖 **Relevant Textbook Snippet**:\n\"{snippet}...\"\n\n"
    response += f"👉 **Guiding Question**: How would applying this core rule help solve your query *\"{query}\"*? What is the first step?"

    return response, [c.content for c in relevant_chunks]
