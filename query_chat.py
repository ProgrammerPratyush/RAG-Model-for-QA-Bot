import os
import shutil
import uuid
import time
import pdfplumber
from langchain.llms import OpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores.chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema.document import Document

# Load environment variables
load_dotenv()

# Constants
CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
You are a helpful assistant. Answer the question with detailed explanations, including headings, sub-headings, and clear paragraphs for better readability.

Context:
{context}

---

Answer the following question: {question}
"""

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response match the expected response? 
"""

# Initialize Chroma DB only once to avoid reloading each time
chroma_db = None

def get_embedding_function():
    """Returns the embedding function using OpenAI Embeddings."""
    return OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

@st.cache_data
def load_documents(pdf_file_path):
    """Load PDF document from the provided path and cache the result."""
    documents = []
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                documents.append(Document(page_content=text, metadata={"source": pdf_file_path}))
    return documents

def split_documents(documents: list[Document]):
    """Split text into smaller chunks for processing."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Increased chunk size for longer context
        chunk_overlap=50,  # Reduced overlap for faster processing
    )
    return text_splitter.split_documents(documents)

@st.cache_data
def add_to_chroma(_chunks: list[Document]):
    """Add document embeddings into Chroma."""
    global chroma_db  # Use global to avoid reinitializing Chroma DB

    if chroma_db is None:
        embedding_function = get_embedding_function()
        chroma_db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Add new chunks to the Chroma database
    chroma_db.add_documents(_chunks)
    chroma_db.persist()


def query_rag(query_text: str):
    """Query the Chroma database and get a response from the OpenAI model."""
    global chroma_db, document_name

    if chroma_db is None:
        embedding_function = get_embedding_function()
        chroma_db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search for relevant chunks in the Chroma database
    results = chroma_db.similarity_search_with_score(query_text, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Use OpenAI model with a pre-defined temperature
    openai_model = OpenAI(temperature=0.5, max_tokens=2048)
    response_text = openai_model(prompt)

    # Use the document name for sources
    sources = [document_name] * len(results)
    formatted_response = f"Response:\n{response_text}\n\nSources: {', '.join(sources)}"
    return formatted_response

def clear_database():
    """Clear the Chroma database."""
    global chroma_db
    if os.path.exists(CHROMA_PATH):
        try:
            if chroma_db:
                chroma_db._client.close()  # Close the Chroma client safely
            shutil.rmtree(CHROMA_PATH)
            chroma_db = None  # Reset the global variable after clearing
            print("Successfully removed the Chroma directory.")
        except Exception as e:
            print(f"Error removing Chroma directory: {e}")

# Global variable to store document name
global document_name
document_name = None

def main():
    """Run the Streamlit app."""
    global document_name
    st.title("RAG Document Chatbot 📄")

    # PDF Upload section
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        # Save the uploaded PDF
        document_name = uploaded_file.name
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("PDF uploaded successfully!")

        # Process the PDF
        st.write("Processing the uploaded document...")
        documents = load_documents("uploaded_file.pdf")
        chunks = split_documents(documents)

        # Clear the Chroma database before adding new documents
        clear_database()

        # Add the chunks to the Chroma database
        add_to_chroma(chunks)
        st.success("Document successfully added to the database!")

    # Query section
    query_text = st.text_input("Ask a question about the document:")
    if st.button("Submit Query"):
        if query_text:
            response = query_rag(query_text)
            st.write(f"Response: {response}")
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
