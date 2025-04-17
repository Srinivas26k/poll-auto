import whisper

model = whisper.load_model("small")  # small for speed; base/medium for accuracy
print("🧠 Transcribing 5min.wav with Whisper...")
result = model.transcribe("5min.wav")
transcript = result["text"].strip()
print("📝 Transcript:\n", transcript)

# Save to file for later use
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(transcript)