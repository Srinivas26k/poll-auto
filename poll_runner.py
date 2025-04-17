import requests
import time
import json
import websocket
import threading
from openai import OpenAI

# Your Zoom Meeting ID
MEETING_ID = "96014521103"

# Paste the caption WebSocket URL you got from Zoom (from Copy API Token)
CAPTION_WEBSOCKET_URL = "https://wmcc.zoom.us/closedcaption?id=96014521103&ns=dGVzdCB6b29t&expire=108000&sparams=id%2Cns%2Cexpire&signature=k58xy3gQ1cs4uZ5Erfg1TpY5B6XzrAVblof2d3GhUZs.AG.PKX_SY7EpqvyUBCJV5MAHUhXC_BMQev3F0wv3wiGgDWnezaJQ7TB8fF4FT-qdcBw3CW-CgWndygCDJ7gCnY-qQKAqrwzzo7Oj8aGDiLbUnELZ_5jkMUlVJhZ-VB0V85bkr-t_JvwVBKEHdyypxyEGLMyqFCK04UFMnXYozCdmMzpLF2uZkc3P3b6Jy3TS7NCOHe3.S6TuVVCcSUBwOmRuEDbz_A.1URpqeekTx8-OTfI"

# Your Zoom OAuth Access Token (for posting the poll)
ZOOM_ACCESS_TOKEN = "eyJzdiI6IjAwMDAwMiIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6IjU2MDVmNzYxLWNlMjctNGY5My04MzIyLTY5ZTdlN2E0MzA5YSJ9.eyJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJjRU9vYWNPblMyMldzbU42YjNwa09BIiwidmVyIjoxMCwiYXVpZCI6IjQ2MWU4ZjQwNDNmNTIxNDQ2OGZlOGQ3ZGIxMWQ0MDZlZGJjMWMzZDMxODkxOWFlNWZhNmFkZDQxY2NjNGFjMDciLCJuYmYiOjE3NDQ4MTAzNjUsImNvZGUiOiJ4VHIyaTNGanNLZkdhSlhidlNFUXhxYTVvNy1ObWdjd0EiLCJpc3MiOiJ6bTpjaWQ6b2ZKMTkwczRSOVM2MF9CU3Z5aDB3ZyIsImdubyI6MCwiZXhwIjoxNzQ0ODEzOTY1LCJ0eXBlIjowLCJpYXQiOjE3NDQ4MTAzNjUsImFpZCI6InZzd3VqUm1OU2V5eTQyNDBGSFJCRVEifQ.va4PFkQTvfCthp01xaa1TGyXB6TZ_Jnt7bvZWDj0DItX_J9lKEH2d7SLRw6yYiFaNT81BIEfaur-LR8nNcvVRA"

# Poll config
POLL_TITLE = "Automated Poll"
QUESTION = "What did we just discuss?"
MEETING_ID_FOR_POLL = MEETING_ID  # keep it same for simplicity

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # required but unused
)

captions = []

def on_message(ws, message):
    text = message.strip()
    if text:
        print("🗣️", text)
        captions.append(text)

def on_error(ws, error):
    print("❌ WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    print("🛑 Caption stream closed")

def start_caption_stream(duration=30):
    print("🎙️ Connecting to Zoom Caption Stream...")
    ws = websocket.WebSocketApp(CAPTION_WEBSOCKET_URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    thread = threading.Thread(target=ws.run_forever)
    thread.daemon = True
    thread.start()

    time.sleep(duration)
    ws.close()

def generate_poll_question(text):
    print("🤖 Asking LLaMA to generate poll from transcription...")
    prompt = f"Generate a poll question with 4 options from this discussion:\n{text}\nRespond in JSON like this: {{'question': '...', 'options': ['A', 'B', 'C', 'D']}}"

    response = client.chat.completions.create(
        model="llama3.2:latest",
        messages=[
            {"role": "system", "content": "You are a poll assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    raw = response.choices[0].message.content.strip()
    print("📥 LLaMA Output:\n", raw)

    try:
        data = json.loads(raw.replace("'", '"'))
        return data['question'], data['options']
    except Exception as e:
        print("⚠️ Failed to parse LLaMA output. Using fallback.")
        return QUESTION, ["Option A", "Option B", "Option C", "Option D"]

def post_poll(question, options):
    print("📤 Posting poll to Zoom...")
    poll_data = {
        "title": POLL_TITLE,
        "questions": [
            {
                "name": question,
                "type": "single",
                "answer_required": True,
                "answers": options
            }
        ]
    }

    response = requests.post(
        f"https://api.zoom.us/v2/meetings/{MEETING_ID_FOR_POLL}/polls",
        headers={"Authorization": f"Bearer {ZOOM_ACCESS_TOKEN}",
                 "Content-Type": "application/json"},
        json=poll_data
    )

    if response.status_code == 201:
        print("✅ Poll created successfully!")
        print(json.dumps(response.json(), indent=2))
    else:
        print("❌ Failed to create poll:")
        print(response.status_code, response.text)

def run():
    print("🚀 Auto Poll From Captions Started")
    try:
        duration = int(input("🕒 How long (seconds) should caption stream run? (default: 30) ") or 30)
    except ValueError:
        duration = 30

    start_caption_stream(duration)

    full_transcript = " ".join(captions)
    print("\n📝 Final Transcript:\n", full_transcript)

    q, opts = generate_poll_question(full_transcript)
    post_poll(q, opts)

if __name__ == "__main__":
    run()