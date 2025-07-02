import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_anthropic import ChatAnthropic

# Load environment variables and initialize the language model
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", api_key=ANTHROPIC_API_KEY)

# Load markdown documents from role-specific subfolders, tagging each with metadata
def load_documents_by_role(root_folder: str):
    all_docs = []
    for role in os.listdir(root_folder):
        role_folder = os.path.join(root_folder, role)
        if not os.path.isdir(role_folder):
            continue
        for file in os.listdir(role_folder):
            if file.endswith(".md"):
                path = os.path.join(role_folder, file)
                loader = TextLoader(path, encoding="utf-8")
                docs = loader.load()
                for doc in docs:
                    doc.metadata["role"] = role
                    doc.metadata["c_level"] = "yes"
                all_docs.extend(docs)
    return all_docs

# Load and print metadata for verification
documents = load_documents_by_role(r"C:\Users\chunc\Music\projectfin\bot\resources\roles")


# Split documents into overlapping chunks for embedding
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
)
chunked_docs = splitter.split_documents(documents)

# Initialize or load FAISS vector index with HuggingFace sentence embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
index_path = "faiss_index"

if os.path.exists(index_path):
    vectorstore = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)
else:
    vectorstore = FAISS.from_documents(chunked_docs, embedding_model)
    vectorstore.save_local(index_path)