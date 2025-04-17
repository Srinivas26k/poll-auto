import websocket
import threading
import time

transcript_buffer = []

def on_message(ws, message):
    print("🗣️", message)
    transcript_buffer.append(message)

def start_caption_stream(meeting_id, token, duration=60):
    ws_url = f"wss://wmcc.zoom.us/closedcaption?id={meeting_id}&ns=1&token={token}&lang=en-US"

    ws = websocket.WebSocketApp(ws_url, on_message=on_message)
    thread = threading.Thread(target=ws.run_forever)
    thread.start()

    print(f"🔴 Streaming captions for {duration} seconds...")
    time.sleep(duration)

    ws.close()
    thread.join()

    return " ".join(transcript_buffer)
