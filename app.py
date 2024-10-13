import streamlit as st
import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyAnnno_unCyRyQ64fLIN02Yh0Zkc_q48ok") 

# Function to interact with Gemini API (as shown in the previous response)
def smart_search(query):
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )

    response = chat_session.send_message(query+ "  use USAspending.gov as data source")
    return response

# Streamlit UI elements
st.title("Federal smart spending explorer")

search_query = st.text_input("Enter Searching Agency")
if st.button("Analyze"):
  if search_query:
    with st.spinner("Analyzing..."):
      response = smart_search(search_query)
      st.write(response.text)
  else:
    st.warning("Please enter a search query.")