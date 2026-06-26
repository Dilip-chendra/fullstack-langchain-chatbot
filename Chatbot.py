import streamlit as st
import requests

st.set_page_config(page_title="Personal AI Assistant", page_icon="🤖", layout="centered")

st.title("🤖 :rainbow[Personal Chat Bot]")
st.markdown("Your advanced AI workspace for managing day-to-day reasoning tasks.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
if user_prompt := st.chat_input("Enter your message here..."):
    with st.chat_message("user"):
        st.write(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            try:
                url1 = "https://fullstack-langchain-chatbot.onrender.com/ChatBot" 
                params1 = {"message": user_prompt}
                response = requests.get(url=url1, params=params1)
                
                if response.status_code == 200:
                    data = response.json()
                    ai_response = data["result"] 

                    st.write(ai_response)
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": ai_response
                    })
                    st.balloons() 
                else:
                    st.error(f"Backend Server Error (Status {response.status_code})")
            except Exception as e:
                st.error(f"Failed to connect to FastAPI Backend: {e}")
