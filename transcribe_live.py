# transcribe_live.py

import queue
import sounddevice as sd
import vosk
import json
import time

model = vosk.Model("model")
q = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"⚠️ Audio status: {status}")
    q.put(bytes(indata))

def transcribe(duration_seconds=600):  # 👈 default = 10 minutes
    print("🎙️ Listening...")

    device_index = 3  # Replace with correct mic input if needed

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=audio_callback,
        device=device_index
    ):
        rec = vosk.KaldiRecognizer(model, 16000)
        transcript = ""
        start_time = time.time()

        try:
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    text = result.get('text', '')
                    transcript += text + ' '
                    print("🗣️", text)

                if time.time() - start_time > duration_seconds:
                    break

        except KeyboardInterrupt:
            print("🛑 Stopped by user.")

        return transcript.strip()
