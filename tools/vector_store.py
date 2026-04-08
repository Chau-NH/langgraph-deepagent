from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()

    docs = [
        Document(page_content=chunk["text"], metadata={"page": chunk["page"]})
        for chunk in chunks
    ]

    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store
