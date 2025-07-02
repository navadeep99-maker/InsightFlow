import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

# Page configuration
st.set_page_config(page_title="InsightFlow", page_icon="🌊", layout="wide")

# Hide Streamlit header elements
st.markdown("""
    <style>
    [data-testid="stHeaderActionElements"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------
# Session state initialization
# ------------------------
defaults = {
    "authenticated": False,
    "username": "",
    "role": "",
    "c_level": "no",
    "messages": [],
    "chat_started": False,
    "pending_first_message": None
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ------------------------
# Function to handle user messages and get assistant response
# ------------------------
def handle_message(user_msg: str):
    
    st.session_state.messages.append({"role": "user", "content": user_msg})
    with st.chat_message("user"):
        st.markdown(user_msg)

    with st.spinner("Thinking..."):
        try:
            payload = {
                "role": st.session_state.role,
                "c_level": st.session_state.c_level,
                "query": user_msg
            }
            response = requests.post("http://127.0.0.1:8000/chat", json=payload)
            if response.status_code == 200:
                reply = response.json().get("final_answer", "No answer found.")
            else:
                reply = f"Error {response.status_code}: {response.text}"
        except Exception as e:
            reply = f"Request failed: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

# ------------------------
# Header layout with New Chat and Logout buttons
# ------------------------
col1, col2 = st.columns([9, 1])

with col1:
    # Show app title if not authenticated
    if not st.session_state.authenticated:
       st.markdown(f"""
        <div style="text-align: left;">
            <h1 style="font-size: 60px; margin: 0;
                    background: linear-gradient(to right, #6a11cb, #2575fc);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-weight: 0;">
              🌊InsightFlow
            </h1>
            
        </div>
        """, unsafe_allow_html=True)

    # Show New Chat button only if authenticated AND chat has started
    if st.session_state.authenticated and st.session_state.chat_started:
        if st.button("🗨️"):
            # Reset chat-related state, but keep user session info
            st.session_state.messages = []
            st.session_state.chat_started = False
            st.session_state.pending_first_message = None
            st.rerun()

with col2:
    # Show Logout button if authenticated
    if st.session_state.authenticated:
        if st.button("Logout"):
            for key in defaults:
                st.session_state[key] = defaults[key]
            st.rerun()
with col1:
    # Show smaller app title if authenticated
    if st.session_state.authenticated:
       st.markdown(f"""
        <div style="text-align: left;">
            <h1 style="font-size: 30px; margin: 0;
                    background: linear-gradient(to right, #6a11cb, #2575fc);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-weight: 20;
                   margin-bottom:20px;">
                🌊InsightFlow
            </h1>
            
        </div>
        """, unsafe_allow_html=True)

# ------------------------
# Login logic and authentication
# ------------------------
if not st.session_state.authenticated:
    st.subheader("Login to continue")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            response = requests.get(
                "http://127.0.0.1:8000/access",
                auth=HTTPBasicAuth(username, password)
            )
            if response.status_code == 200:
                data = response.json()
                st.session_state.update({
                    "username": username,
                    "role": data["role"],
                    "c_level": data["c_level"],
                    "authenticated": True,
                    "messages": [],
                    "chat_started": False,
                    "pending_first_message": None
                })
                st.success(f"Welcome {username}! Role: {data['role']} | C-Level: {data['c_level']}")
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")
        except Exception as e:
            st.error(f"Request failed: {str(e)}")

# ------------------------
# Chat logic and message handling
# ------------------------
else:
    # Show greeting if chat not started
    if not st.session_state.chat_started:
        st.markdown(f"""
        <div style="text-align: left;">
            <h1 style="font-size: 60px; margin: 0;
                    background: linear-gradient(to right, #6a11cb, #2575fc);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-weight: 0;">
                Hello, {st.session_state.username}
            </h1>
            <p style="font-size: 54px; color: #aaa; margin-top: 0px; font-weight: 200;">
                How can I help you today?
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input box
    query = st.chat_input("Type your message...")

    # Start chat on first message and rerun
    if query and not st.session_state.chat_started:
        st.session_state.pending_first_message = query
        st.session_state.chat_started = True
        st.rerun()

    # Handle pending first message
    elif st.session_state.chat_started and st.session_state.pending_first_message:
        handle_message(st.session_state.pending_first_message)
        st.session_state.pending_first_message = None

    # Handle normal message
    elif query and st.session_state.chat_started:
        handle_message(query)
