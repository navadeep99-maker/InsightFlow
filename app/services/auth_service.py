from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials
from typing import Dict

# In-memory user database with passwords and metadata (role and c_level flag)
users_db: Dict[str, Dict[str, str]] = {
    "Tony": {"password": "password123", "role": "engineering", "c_level": "no"},
    "Bruce": {"password": "securepass", "role": "finance", "c_level": "no"},
    "Sam": {"password": "financepass", "role": "ceo", "c_level": "yes"},
    "Peter": {"password": "pete123", "role": "engineering", "c_level": "no"},
    "Sid": {"password": "sidpass123", "role": "marketing", "c_level": "no"},
    "Natasha": {"password": "hrpass123", "role": "hr", "c_level": "no"}
}

# Authenticates user credentials and returns role-based identity metadata
def authenticate_user(credentials: HTTPBasicCredentials):
    username = credentials.username
    password = credentials.password
    user = users_db.get(username)

    # Reject invalid credentials
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Return authenticated user data
    return {
        "username": username,
        "role": user["role"],
        "c_level": user["c_level"]
    }