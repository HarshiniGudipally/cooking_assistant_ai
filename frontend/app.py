import streamlit as st
import requests
import uuid
import re

BACKEND_URL = "http://localhost:8000"

st.title("Cooking Assistant AI")

# Initialize session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's your cooking question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = requests.post(f"{BACKEND_URL}/chat", json={"session_id": st.session_state.session_id, "content": prompt})
        full_response = response.json()["response"]
        
        # Process the response to convert [LINK:URL] to clickable links
        processed_response = re.sub(r'\[LINK:(.*?)\]', r'<a href="\1" target="_blank">Click here for more information</a>', full_response)
        
        message_placeholder.markdown(processed_response, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


# Option to view full conversation history
if st.button("View Full Conversation History"):
    response = requests.get(f"{BACKEND_URL}/history/{st.session_state.session_id}")
    if response.status_code == 200:
        history = response.json()
        for message in history:
            st.write(f"{message['role'].capitalize()}: {message['content']}")
            st.write(f"Timestamp: {message['timestamp']}")
            st.write("---")
