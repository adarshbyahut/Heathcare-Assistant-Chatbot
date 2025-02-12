import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot= pipeline("text-generation",model="distilgpt2")

def healthcare_chatbot(user_input):
    if "sympton" in user_input:
        return "Please consult Doctor for Accurate advicce"
    elif "appointment" in user_input:
       return "would you like to schedule appointment with the doctor?"
    elif "medication" in user_input:
      return "it's important to take precisribe medicines regularly"
    else:
        response=chatbot(user_input,max_length=500,num_return_sequences=1)
    return response[0]['generated_text']
    
def main():
    st.title("Healthcare Assistant Chatbot")
    user_input=st.text_input("How can I assist you today")
    if st.button("submit"):
        if user_input:
            st.write("user:",user_input)
            with st.spinner("processing your querry, please wait...."):
              response=healthcare_chatbot(user_input)
            st.write("HealthCare Assistant: Please consult Doctor for Accurate advicce",response)
        else:
            st.write("Please enter a message to get a response.")
main()