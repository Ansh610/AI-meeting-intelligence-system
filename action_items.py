import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def extract_actions(text):

    prompt = f"""
    Extract action items from the meeting transcript.

    Rules:
    - Mention responsible person
    - Mention task
    - Mention deadline if available
    - Use bullet points

    Transcript:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
