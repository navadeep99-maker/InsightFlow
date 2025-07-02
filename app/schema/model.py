from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str
    role: str
    c_level: str

class AuthResponse(BaseModel):
    username: str
    role: str
    c_level: str