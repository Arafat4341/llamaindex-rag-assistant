# 🚀 LlamaIndex RAG Assistant

A **Retrieval-Augmented Generation (RAG)** powered AI assistant built using **LlamaIndex** and **Granite LLM (via IBM Watsonx)**.  
This project enables real-time, context-aware querying and summarization of documents like PDFs, making complex information retrieval efficient, accurate, and secure.

---

## 📚 Objective

In today's information-rich environment, navigating vast amounts of documents—scientific papers, reports, manuals—can be overwhelming.  
This project demonstrates how to build an AI assistant capable of:

- **Ingesting private documents (PDF, HTML, TXT, etc.)**
- **Indexing and embedding them locally**
- **Retrieving the most relevant content at query time**
- **Generating accurate, context-aware answers using a Large Language Model (LLM)**

---

## 🧠 RAG Architecture Overview

**RAG (Retrieval-Augmented Generation)** enhances an LLM's knowledge by retrieving relevant, external information at query time and inserting it into the prompt.  
Here’s how the flow works in this project:

1. **Indexing Pipeline:**
   - **Load:** Documents are loaded from diverse formats (PDF in this case).
   - **Split:** Large documents are split into smaller chunks.
   - **Embed:** Chunks are converted into vector embeddings using **Watsonx Embeddings**.
   - **Store:** Embeddings are stored in a local vector index (**VectorStoreIndex**).

2. **Retrieval + Generation Pipeline:**
   - **Retrieve:** Relevant chunks are retrieved based on the user's query.
   - **Generate:** **Llama LLM (via IBM Watsonx)** generates a precise, context-aware response.

---

## 🛠️ Technologies Used

| Component                  | Technology                                    |
|---------------------------|-----------------------------------------------|
| Document Loading           | `SimpleDirectoryReader` (LlamaIndex)          |
| Splitting                  | `SentenceSplitter` (LlamaIndex)               |
| Embeddings                 | `WatsonxEmbeddings` (IBM)                     |
| Vector Indexing            | `VectorStoreIndex` (LlamaIndex)               |
| Retrieval                  | LlamaIndex retriever                          |
| Generation (LLM)           | `WatsonxLLM` (Granite LLM via IBM Watsonx)    |
| Config Management          | `dotenv`                                      |
| Language                   | Python                                        |

---

## 📂 Project Structure

```
llamaindex-rag-assistant/
├── data/                         # Input documents (PDF, HTML, TXT)
│   └── lora_paper.pdf
├── config/
│   └── .env                      # API keys, IBM Watsonx configs
├── modules/
│   ├── loader.py                 # Handles document loading
│   ├── splitter.py               # Handles document splitting
│   ├── embedder.py               # Embedding model setup
│   ├── indexer.py                # Index building
│   ├── llm.py                    # LLM model setup
│   └── query_engine.py           # Query engine creation
├── main.py                       # Orchestrates all steps
├── requirements.txt              # Dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/Arafat4341/llamaindex-rag-assistant
cd llamaindex-rag-assistant
```

---

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### 3. **Configure Environment Variables**

Create a `.env` file in `config/`:

```
IBM_URL=your_ibm_url
IBM_API_KEY=your_ibm_api_key
IBM_PROJECT_ID=your_ibm_project_id
```

---

### 4. **Add Documents**

Place your documents (PDF, TXT, HTML, etc.) in the `data/` folder.

Example:
```
data/lora_paper.pdf
```

---

### 5. **Run the Application**

```bash
python main.py
```

---

## 💬 Example Usage

**Sample Queries:**
- *"What is the lora paper about?"*
- *"List all the evaluation datasets used in the lora paper."*

The assistant will retrieve the most relevant document sections and generate accurate responses in real time.

---

## 🔑 Key Learning Highlights

- Mastered **RAG architecture** to combine retrieval + generation seamlessly.
- Understood how **LlamaIndex simplifies multi-source document ingestion & indexing**.
- Integrated IBM's **Granite LLM via Watsonx** for advanced query generation.
- Gained experience with embedding models, vector storage, and LLM orchestration.

---

## 🏆 Future Extensions

- Add support for **multiple document formats (HTML, TXT, CSV)**.
- Integrate with other vector DBs (FAISS, Pinecone).
- Implement a **web UI interface (Streamlit/Flask)**.
- Experiment with **different LLMs (local models, OpenAI, Hugging Face)**.

---

## 📜 License

MIT License – Feel free to fork, modify, and build upon this project!

---

## 👋 Let's Connect!

Feel free to reach out or fork the project if you're working on similar document-based AI assistants!