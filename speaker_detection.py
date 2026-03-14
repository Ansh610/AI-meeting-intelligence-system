import whisper

model = whisper.load_model("small")

def detect_speakers(audio_path):

    result = model.transcribe(audio_path)

    segments = result["segments"]

    speakers = []

    speaker_id = 1

    for seg in segments:

        start = round(seg["start"],2)
        end = round(seg["end"],2)
        text = seg["text"]

        speakers.append(
            f"Speaker {speaker_id}: {start}s - {end}s → {text}"
        )

        speaker_id += 1

    return speakers
