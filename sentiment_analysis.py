from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):

    result = sentiment_model(text[:512])

    label = result[0]["label"]
    score = round(result[0]["score"] * 100, 2)

    return f"{label} ({score}%)"
