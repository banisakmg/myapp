import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Tutor for Kids")
st.title("🎓 AI Tutor for Kids")

subject = st.selectbox("Choose a subject:", ["Math", "Science", "History", "English", "Computer Science"])
grade = st.selectbox("Choose grade level:", ["Elementary", "Middle School", "High School", "College"])
question = st.text_area("Ask your question:")

if st.button("Ask Tutor"):
    if question.strip() == "":
        st.warning("Please type a question first.")
    else:
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"""
You are a friendly AI tutor for kids.

Subject: {subject}
Grade level: {grade}

Rules:
- Explain clearly and simply.
- Be encouraging.
- Do not just give the answer if it is homework.
- Show steps when useful.
- End with one small practice question.

Student question:
{question}
"""
            )

            st.subheader("Tutor Answer")
            st.write(response.output_text)
