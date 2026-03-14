import whisper

def clean_transcript(text):

    corrections = {
        "Lakshid": "Lakshit",
        "Ash": "Ansh"
    }

    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)

    return text


def transcribe_audio(audio_path):

    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    text = result["text"]

    text = clean_transcript(text)

    return text