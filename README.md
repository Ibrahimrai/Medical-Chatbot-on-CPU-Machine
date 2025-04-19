🧠 Medical Chatbot on CPU using LLaMA 2 – 100% Open Source

This project is a fully offline **Medical Chatbot** built with **LLaMA 2**, running entirely on **CPU** using open-source tools. It reads medical PDF documents and answers user questions using a local language model – **no cloud**, **no API keys**, and **no GPU** required.



🚀 Features

- 💬 Ask natural language questions about your own medical PDFs
- 🧠 Powered by **LLaMA 2 7B GGML** (`.bin` format)
- 📄 Embeds content from medical books using `sentence-transformers`
- 🔍 Fast vector search with **FAISS (CPU)**
- ⚡ Interactive chat UI with **Chainlit**
- ✅ Shows the **actual chunks of data used** to answer your question (retrieval transparency)



🧪 Tech Stack

| Tool                                                        | Purpose                               |
|-----------------------------------------------------------------------------------------------------|
| [LangChain](https://www.langchain.com/)                     | LLM orchestration & document handling |
| [HuggingFace Sentence Transformers](https://www.sbert.net/) | Embedding medical text |
| [FAISS (CPU)](https://github.com/facebookresearch/faiss)    | Fast local vector search |
| [LLaMA 2 (GGML)](https://huggingface.co/TheBloke)           | Local language model |
| [Chainlit](https://www.chainlit.io/)                        | Real-time chat interface |


📁 Pipeline
Medical PDF → LangChain → SentenceTransformer + FAISS → LLaMA 2 (GGML) → Chainlit UI
