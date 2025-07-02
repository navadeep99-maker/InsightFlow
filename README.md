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



🚀 How It Works:

Login System: Authenticated via FastAPI’s HTTPBasic. Each user has a role and C-level access.

Role-based Document Retrieval: .md files stored by role → vectorized → indexed.

Dynamic Prompting: Prompt template adjusts to user's role and clearance.

LLM-Powered Answers: Using Claude or any other LLM with LangChain RetrievalQA.

Chat UI: Streamlit-powered interface for seamless interaction.


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


🧍 Test User Credentials
Here’s a sample of available user types, each mapped to a unique domain and access level. You can use these to demo how InsightFlow dynamically adjusts search scope and prompt construction:
- 👷 Tony
- Role: engineering
- C-level: ❌
- Username: Tony  Password: password123
- Tests access to engineering knowledge and developer docs
- 💼 Bruce
- Role: finance
- C-level: ❌
- Username: Bruce  Password: securepass
- Used to validate financial document queries from a non-C-level finance role
- 🧠 Sam
- Role: ceo
- C-level: ✅
- Username: Sam  Password: financepass
- Tests executive access to sensitive content across roles

  - 📣 Sid
- Role: marketing
- C-level: ❌
- Username: Sid  Password: sidpass123
- Focus on testing campaign strategy and marketing material retrieval
- 🧾 Natasha
- Role: hr
- C-level: ❌
- Username: Natasha  Password: hrpass123
- Tests HR-related queries like onboarding, benefits, and policies
special testing questions file provided with 50 questions accross all all files
All usernames and passwords are casesensitive
  

✨ What’s Coming Next
- OAuth2 or JWT Authentication
- Admin Portal to Manage/Upload Content




✨ further improvement ideas

OAuth2 or JWT authentication

Admin portal to upload/manage role content

Analytics dashboard for usage and insights

🤝 Author
Developed by Navadeep — exploring scalable, secure, and intelligent systems with a flair for clean UI.

 Resources provided by codebasics.
