# Importing required packages
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# loading enviroment variables from .env enviroment
load_dotenv()

# streamlit page configuration
st.set_page_config(
    page_title = "Chatty",
    page_icon = "💬",
    layout = "centered" #setting page layout to center
)
 
# getting api key from our enviroment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# diaplaying chat bot title:
st.title("💬All in One Chatbot-Chatty")
# loading google's Gemini Pro model with api key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")



# creating a function that translate roles between model and streamlit for better user experience by Streamlit
def translate_role_for_streamlit(user_role):
    if user_role=="model":
        return "assistant"
    else:
       return user_role


# Intializing streamlit chat session:
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])




# displaying chat history on chatbot page
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
       st.markdown(message.parts[0].text)


# Input field for user
user_prompt = st.chat_input("Ask something...")


# After getting user prompt generating response
if user_prompt:
    # if user_prompt==convo:
    st.chat_message("user").markdown(user_prompt)

    
         
    gemini_response = st.session_state.chat_session.send_message((user_prompt))
    # gemini_response = convo.send_message(user_prompt)
    
    with st.chat_message("assistant"):
       st.markdown(gemini_response.text)

