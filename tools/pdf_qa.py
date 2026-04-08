from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_pdf(vector_store, question, history=None):
    docs = vector_store.similarity_search(question, k=3)

    # Build context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Collect pages
    pages = sorted(set([doc.metadata.get("page") for doc in docs]))

    # History
    history_text = "\n".join(
        [h.content for h in history[-4:]]
    ) if history else ""

    prompt = f"""
    Conversation History:
    {history_text}

    Answer the question based on ONLY the following context.
    Keep the answer concise.

    Context:
    {context}

    Question:
    {question}
    """
    
    response = llm.invoke(prompt)
    answer = response.content.strip()

    pages_text = ", ".join([f"Page {p}" for p in pages])

    return f"""
    {answer}

    Sources: {pages_text}
    """
