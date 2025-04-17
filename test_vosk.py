# test_vosk.py
import sys
import os
from vosk import Model, KaldiRecognizer
import wave
import json

# 1. Verify model directory
if not os.path.exists("model"):
    print("❌ Model directory 'model/' not found.")
    sys.exit(1)

# 2. Load Vosk model
print("🔍 Loading Vosk model from 'model/'...")
model = Model("model")

# 3. Open test WAV file
wav_path = "test.wav"
if not os.path.exists(wav_path):
    print(f"❌ Test audio '{wav_path}' not found.")
    sys.exit(1)

wf = wave.open(wav_path, "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
    print("❌ Audio must be WAV mono 16-bit 16 kHz. Please convert your file accordingly.")
    sys.exit(1)

# 4. Initialize recognizer
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# 5. Process audio in chunks
results = []
print("🎙  Transcribing 'test.wav'...")
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        results.append(json.loads(rec.Result()))
    else:
        # capture partial results as well
        results.append(json.loads(rec.PartialResult()))

# 6. Final result
results.append(json.loads(rec.FinalResult()))
wf.close()

# 7. Extract and print text
transcript = " ".join(item.get("text", "") for item in results)
print("📝 Transcript Output:\n", transcript)
