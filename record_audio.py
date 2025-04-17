import pyaudio
import wave

# Audio parameters
RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paInt16
DURATION = 5 * 60      # 5 minutes
CHUNK = 1024

p = pyaudio.PyAudio()

# Find Stereo Mix device
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if "Stereo Mix" in dev["name"]:
        dev_index = i
        break
else:
    raise RuntimeError("Stereo Mix device not found")

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=dev_index)

frames = []
print("🔴 Recording 5 minutes of system audio...")
for _ in range(int(RATE / CHUNK * DURATION)):
    data = stream.read(CHUNK)
    frames.append(data)

print("⏹️ Recording complete, saving to 5min.wav")
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open("5min.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()
