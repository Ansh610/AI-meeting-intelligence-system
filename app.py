import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from textwrap import fill

from transcription import transcribe_audio
from summarizer import generate_summary
from action_items import extract_actions
from topic_detection import extract_topics
from speaker_detection import detect_speakers
from keyword_extraction import extract_keywords
from sentiment_analysis import analyze_sentiment


st.set_page_config(
    page_title="AI Meeting Intelligence",
    layout="wide",
    page_icon="🤖"
)

# CUSTOM CSS

st.markdown("""
<style>

.main-title{
font-size:60px;
font-weight:800;
background: linear-gradient(90deg,#00c6ff,#0072ff,#00ffcc);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
text-align:center;
margin-bottom:10px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#bbbbbb;
margin-bottom:40px;
}

.metric-card{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
padding:20px;
border-radius:12px;
text-align:center;
color:white;
font-size:20px;
}

.keyword{
background:#0072ff;
padding:8px 15px;
border-radius:20px;
color:white;
display:inline-block;
margin:5px;
}

</style>
""", unsafe_allow_html=True)


# HEADER

st.markdown(
'<div class="main-title">🤖 AI Meeting Intelligence System</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Upload meeting audio and generate AI insights automatically</div>',
unsafe_allow_html=True
)

st.divider()

# FILE UPLOAD

audio_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["mp3","wav","m4a"]
)

# MAIN PROCESS

if audio_file:

    with open("temp_audio.wav","wb") as f:
        f.write(audio_file.read())

    st.success("Audio uploaded successfully!")

    with st.spinner("Analyzing meeting audio..."):

        transcript = transcribe_audio("temp_audio.wav")
        summary = generate_summary(transcript)
        actions = extract_actions(transcript)
        topics = extract_topics(transcript)
        speakers = detect_speakers("temp_audio.wav")
        keywords = extract_keywords(transcript)
        sentiment = analyze_sentiment(transcript)

    st.divider()

# ANALYTICS DASHBOARD

    st.subheader("📊 Meeting Analytics")

    col1,col2,col3,col4 = st.columns(4)

    col1.markdown(
        f'<div class="metric-card">🗣 Speakers<br><h2>{len(speakers)}</h2></div>',
        unsafe_allow_html=True
    )

    col2.markdown(
        f'<div class="metric-card">📌 Topics<br><h2>{len(topics.splitlines())}</h2></div>',
        unsafe_allow_html=True
    )

    col3.markdown(
        f'<div class="metric-card">✅ Tasks<br><h2>{len(actions.splitlines())}</h2></div>',
        unsafe_allow_html=True
    )

    col4.markdown(
        f'<div class="metric-card">🔑 Keywords<br><h2>{len(keywords)}</h2></div>',
        unsafe_allow_html=True
    )

    st.divider()

# TRANSCRIPT

    with st.expander("📜 Meeting Transcript", expanded=True):

        st.write(transcript)

        st.download_button(
            "Download Transcript",
            transcript,
            file_name="meeting_transcript.txt"
        )

# SPEAKER SEGMENTS

    with st.expander("🗣 Speaker Segments"):

        for s in speakers:
            st.write(s)

# SUMMARY

    st.subheader("📝 Meeting Summary")

    st.write(summary)

# ACTION ITEMS

    st.subheader("✅ Action Items")

    st.write(actions)

# TOPICS

    st.subheader("📌 Topics Discussed")

    st.write(topics)

# KEYWORDS

    st.subheader("🔑 Key Meeting Keywords")

    for k in keywords:
        st.markdown(f'<span class="keyword">{k}</span>', unsafe_allow_html=True)

    st.divider()

# SENTIMENT

    st.subheader("🙂 Meeting Sentiment")

    if "POSITIVE" in sentiment:
        st.success(sentiment)
    elif "NEGATIVE" in sentiment:
        st.error(sentiment)
    else:
        st.warning(sentiment)

    st.divider()

# CHARTS

    st.subheader("📈 Meeting Insights")

    col1, col2 = st.columns(2)

# Speaker Distribution Chart

    with col1:

        speaker_counts = Counter([s.split(":")[0] for s in speakers])

        fig, ax = plt.subplots(figsize=(6,5))

        fig.patch.set_facecolor("#0E1117")
        ax.set_facecolor("#0E1117")

        ax.pie(
            speaker_counts.values(),
            labels=speaker_counts.keys(),
            autopct="%1.0f%%",
            textprops={'color':'white'},
            colors=["#00c6ff","#0072ff","#00ffcc","#6a5acd"]
        )

        ax.set_title("Speaker Distribution", color="white")

        plt.tight_layout()

        st.pyplot(fig)

# Topic Frequency Chart

    with col2:

        topic_list = [t.strip("- ") for t in topics.split("\n") if t]

        topic_counts = Counter(topic_list)

        labels = [fill(label, 25) for label in topic_counts.keys()]

        fig, ax = plt.subplots(figsize=(7,5))

        fig.patch.set_facecolor("#0E1117")
        ax.set_facecolor("#0E1117")

        ax.barh(labels, topic_counts.values(), color="#00c6ff")

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        ax.set_title("Topic Frequency", color="white")

        plt.tight_layout()

        st.pyplot(fig)

# ELSE BLOCK

else:

    st.info("Upload a meeting audio file to start analysis.")
