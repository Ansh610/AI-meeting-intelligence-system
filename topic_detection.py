from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])
def extract_topics(text):

    prompt = f"""
    Identify the main topics discussed in the meeting.

    Rules:
    - Return short bullet points
    - Focus on key project discussions

    Transcript:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content