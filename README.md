# RAG-Based QA Bot with Interactive Interface 🚀

### Developer: Pratyush Puri Goswami
### Email: ppurigoswami2002@gmail.com

## 🌟 Introduction

Welcome to the RAG-Based QA Bot project! In this project, I developed a Retrieval-Augmented Generation (RAG) model capable of answering questions based on the contents of documents or datasets. This bot can be used to extract precise information from your PDFs with the power of OpenAI’s GPT-4o model for generating contextually relevant answers!

This project consists of two major parts:

***RAG Model for QA Bot (Part 1)***
***Interactive QA Bot Interface (Part 2)***

## 🧠 Part 1: RAG Model for QA Bot

**⚙️ Overview**

The goal was to create a Retrieval-Augmented Generation (RAG) model that could answer queries based on a provided document. This involves utilizing document embeddings in a vector database, allowing the bot to fetch the most relevant information and then generate well-structured answers.

**🛠️ Key Components**

Vector Database: I used Chroma to store and retrieve document embeddings. It’s fast, efficient, and scalable, making it perfect for real-time queries.

Generative Model: The OpenAI GPT-4o model powers the bot’s ability to produce contextually rich, coherent answers.

**🧩 My Approach**

***🏗️ 1. Environment Setup***

Installed packages such as langchain, pdfplumber, chroma, and more for efficient document processing and querying.

Configured environment variables to securely manage API keys for Langchain and OpenAI.

***📄 2. Document Loading and Processing***

Extracted text from PDFs using pdfplumber and created Document objects for further processing.

Split large documents into manageable text chunks using the RecursiveCharacterTextSplitter for optimal performance.

***🗂️ 3. Vector Store Creation***

Added document chunks to the Chroma Vector Store. This enabled quick retrieval of relevant information based on user queries.

***🤖 4. Generative Model Setup***

Integrated GPT-4o for generating responses based on the retrieved chunks, ensuring answers are detailed, well-structured, and informative.

***🔄 5. Retrieval and Generation***

Processed user queries by retrieving relevant information from Chroma and using GPT-4o to generate coherent answers.

If no relevant content was found, the bot falls back to generating a default response indicating no relevant information.

## Part 2: Interactive QA Bot Interface

**🌟 Overview**

In this part, I created a user-friendly interface using Streamlit, where users can upload PDF documents and ask questions based on the content. The interface integrates with the RAG model, providing real-time answers with relevant document sources.

**🛠️ My Approach**

***💻 Frontend Development***

Built a simple web interface using Streamlit that allows users to upload PDFs and ask questions in real-time.

***📥 Document Handling***

Handled PDF uploads and used pdfplumber to extract the text for further processing and splitting.

***🧠 Query Handling***

Integrated the Chroma Vector Store and GPT-4o for querying. The answers are displayed with relevant document sections to enhance user trust and understanding.

***🔄 Clear & Refresh Functionality***

Implemented a database clearing function that resets the Chroma vector store for each document upload, ensuring new PDFs are always processed freshly.

### 📦 Installation & Usage Guide

#### 1️⃣ Running the RAG Model with Colab Notebook (Part 1)

**Open the Colab Notebook:** Start by opening the RAG model's Colab notebook in your browser.

**Set Up the Environment:** Connect to the Colab environment and set up the notebook by running the initial cells.

**Upload Your PDF 📄:** Upload your local PDF to the Colab environment that you'd like to query.

**Generate an OpenAI API Key 🔑:** Get your API key from the OpenAI platform to access GPT-4o’s capabilities.

**Ask Your Questions ❓:** Now, simply input your question in the notebook’s query section!

**Get Your Answers 🎉:** The RAG chatbot will generate responses based on the uploaded PDF and return them to you.


#### 2️⃣ Running the Fully Functional RAG Chatbot with UI (Part 2)

**Set Up a Virtual Environment:**

**Create and activate a virtual environment for the project:**

      python3 -m venv myenv  

      source myenv/bin/activate  

**Install Dependencies from requirements.txt 📜:**

**Install the necessary packages by running:**

      pip install -r requirements.txt  

**Use an IDE (PyCharm recommended) 🖥️:** Open the project in an IDE, such as PyCharm or VSCode, for seamless development.

**Run the App 🚀:** 

Start the Streamlit app using the following command in your terminal:

      streamlit run app.py  

**Upload a PDF 📂:** Use the interface to upload a PDF document that you want to interact with.

**Chat with the RAG Bot 💬:** Type your queries and receive answers based on the uploaded document.


### 🚀 Conclusion
This project showcases the power of RAG models combined with a user-friendly interface to create an efficient and responsive document-based chatbot. With tools like Chroma for fast retrieval, GPT-4o for generation, and Streamlit for interactivity, this solution brings document querying to a new level.

Feel free to reach out via email for any questions or feedback. Happy querying! 🎉
