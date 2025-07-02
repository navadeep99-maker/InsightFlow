🌊 InsightFlow – Role-Based AI Assistant:

InsightFlow is an intelligent conversational assistant that delivers role-specific responses based on hierarchical access. It blends FastAPI for backend logic, LangChain + FAISS (or pluggable vector stores) for semantic search, and Streamlit for a seamless chat UI experience.

💻 Tech Stack:

💻 Tech Stack
- Python – The core engine driving backend logic and orchestration.
- FastAPI – Powers the authentication layer and serves chat endpoints.
- LangChain – Enables role-aware prompting through RetrievalQA and custom chains.
- LLMs (Claude, GPT-4, etc.) – Generates natural language responses with citation-ready accuracy.
- Vector Stores (FAISS / Qdrant / Chroma / Pinecone) – Embed and retrieve relevant document chunks via semantic similarity.
- Streamlit – Delivers a chat-first UI with login, chat memory, and interactive frontend behaviors.
- Markdown (.md) – Used to organize role-based knowledge files, making documentation easy to manage and update.

💡 Some resource structure and design inspiration derived from Codebasics open-source projects.

🏗️ Project Structure:


BOT/
├── app/
│   ├── main.py                # FastAPI application with chat endpoints
│   ├── auth_service.py        # Authentication using HTTPBasic with role/c_level
│   ├── chat_service.py        # Query resolution logic (get_answer)
├── schema/
│   ├── models.py              # Pydantic models for request/response bodies
├── services/
│   ├── document_loader.py     # Load .md files tagged with role/c_level
│   ├── retrieval_chain.py     # Prompt template + LangChain QA chain
├── utils/
│   ├── vector_utils.py        # FAISS index creation and retrieval
├── resources/
│   └── roles/                 # Role-based markdown content
├── faiss_index/               # Serialized FAISS vectorstore
├── ui/
│   └── app.py                 # Streamlit frontend with login, chat, logout
├── .env                       # Environment variables (e.g. API keys)
├── .gitignore
├── README.md                  # Project documentation
├── requirements.txt
├── pyproject.toml


🚀 How It Works:

Login System: Authenticated via FastAPI’s HTTPBasic. Each user has a role and C-level access.

Role-based Document Retrieval: .md files stored by role → vectorized → indexed.

Dynamic Prompting: Prompt template adjusts to user's role and clearance.

LLM-Powered Answers: Using Claude or any other LLM with LangChain RetrievalQA.

Chat UI: Streamlit-powered interface for seamless interaction.



🧪 Local Development Setup:

# Clone the repo
git clone https://github.com/your-repo/insightflow.git
cd insightflow
# Install dependencies
install on based dependencies by using requirements.txt
# Set up environment variables
# (Create a .env file and add your claude API key)
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env

# Run backend
uvicorn app.main:app --reload
# Run frontend
streamlit run ui/app.py


🔑 Key Features
🔐 Role-Based Access Control
Users are authenticated through FastAPI and assigned a role (like engineer, ceo, or hr). InsightFlow dynamically filters what knowledge a user can access and tailors responses accordingly. C-level roles receive higher-tier insights, while general access is scoped appropriately—this helps ensure both relevance and security.
📄 Editable Markdown Knowledge Base
Content is stored as .md files, categorized by role. This makes the system incredibly flexible—non-tech contributors can update knowledge sources, and the assistant automatically adapts. Markdown is clean, maintainable, and integrates seamlessly into the indexing pipeline.
🧠 LangChain-Driven Prompt Engineering
At the heart of InsightFlow is a dynamic prompting system. Based on the user’s role and query, LangChain constructs custom prompts that guide the LLM to retrieve relevant content. The system balances contextual depth and brevity for optimal usability.
🔎 Semantic Search with MMR Filtering
Using FAISS (or a pluggable vector store), the system indexes role-based docs and performs fast, intelligent lookups. Max Marginal Relevance ensures diversity and avoids echo-chamber responses by selecting the most relevant and varied document chunks.
💬 Streamlit Chat UI with Memory & Auth
The front-end—built entirely in Streamlit—features login/logout logic, chat history memory, and a clean UI that's easily styled with custom CSS/HTML. It’s snappy, secure, and designed for long-form conversations that adapt as you go.
⚡ Pluggable Design
From vector stores to UI theming, everything is modular. Want to swap out FAISS for Qdrant or deploy to another UI framework? Minimal refactoring is needed. It's developer-friendly, extensible, and ready for upgrades.




✨ further improvement ideas

OAuth2 or JWT authentication

Admin portal to upload/manage role content

Analytics dashboard for usage and insights

🤝 Author
Developed by Navadeep — exploring scalable, secure, and intelligent systems with a flair for clean UI.

 Resources provided by codebasics.