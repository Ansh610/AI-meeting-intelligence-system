import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_summary(text):

    prompt = f"""
    You are an AI meeting assistant.

    Create a concise professional summary of the meeting transcript.

    Rules:
    - Use bullet points
    - Mention important decisions
    - Mention responsibilities
    - Mention deadlines

    Meeting Transcript:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
