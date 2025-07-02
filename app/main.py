from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.schema.model import ChatRequest, AuthResponse
from app.services.auth_service import authenticate_user
from app.services.chat_service import get_answer

# Initialize the FastAPI application and security mechanism
app = FastAPI(title="InsightFlow API")
security = HTTPBasic()

# Endpoint to authenticate users via HTTP Basic credentials
@app.get("/access", response_model=AuthResponse)
def access(credentials: HTTPBasicCredentials = Depends(security)):
    return authenticate_user(credentials)

# Endpoint to handle chat requests and return AI-generated responses
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = get_answer(request.query, request.role, request.c_level)
        return {"final_answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))