from langchain.chains import RetrievalQAWithSourcesChain
from app.utils.vector_utils import vectorstore, llm
from langchain.prompts import PromptTemplate
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
import os   

def get_answer(query: str, role: str, c_level: str):
    # Step 1: Construct custom prompt
    custom_prompt = PromptTemplate(
        input_variables=["role", "c_level", "summaries", "question"],
        template="""
You are a precise and helpful assistant supporting a user with role: {role}.  
Their clearance level: {c_level}. Respond strictly based on their access privileges.  

Response Guidelines:
- Be natural and confident. Do not introduce yourself, mention you're an AI, or go off-topic.
- Keep responses focused only on the user's question and the document context.
- No extra suggestions, alternatives, or hypotheticals unless explicitly asked.
- If the user lacks access to specific content, reply with:  
  **"I can’t share the full details due to access limits."**
- If there’s no relevant information, say:  
  **"I couldn’t find anything specific related to that."**
- Match tone to the user’s communication style and role—factual, direct, and human.

Context from documents:  
{summaries}

User question:  
{question}
"""
    )
    # Step 2: Filtered retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={
           "filter": {
            "$or": [
                {"role": role},
                {"c_level": c_level},
                {"role": "general"}
            ]
        },
            "search_type": "mmr",
            "k": 10
        }
    )

    # Step 3: Custom QA chain with injected prompt
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": custom_prompt}
    )

    # Step 4: Chain execution with custom variables
    result = qa_chain.invoke({
        "role": role,
        "c_level": c_level,
        "question": query
    })

    # Step 5: Answer + source extraction
    answer = result.get("answer", "I'm not sure how to answer that right now.")
    source_docs = result.get("source_documents", [])

    unique_sources = sorted(set(
        os.path.basename(doc.metadata.get("source", "Unknown Source"))
        for doc in source_docs
    ))

    if unique_sources:
        sources_formatted = "\n\nSources:\n" + "\n".join(f"- {src}" for src in unique_sources)
        return answer + sources_formatted
    else:
        return answer


