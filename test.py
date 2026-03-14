from transcription import transcribe_audio
from summarizer import generate_summary
from action_items import extract_actions
from topic_detection import extract_topics

text = transcribe_audio("audio/meeting.wav")

print("\nTRANSCRIPT:\n")
print(text)

summary = generate_summary(text)

print("\nSUMMARY:\n")
print(summary)

actions = extract_actions(text)

print("\nACTION ITEMS:\n")
print(actions)

topics = extract_topics(text)

print("\nTOPICS DISCUSSED:\n")
print(topics)