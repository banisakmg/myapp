import streamlit as st

st.title("AI Tutor for Kids")

subject = st.selectbox(
    "Choose a subject:",
    ["Math", "Science", "History", "English"]
)

question = st.text_input("Ask your question:")

if question:
    st.success(f"You asked about {subject}: {question}")
  
