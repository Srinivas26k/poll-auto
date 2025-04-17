# poll_loop.py

import time
from transcribe_live import transcribe
from llama_infer import generate_poll
from post_poll import create_zoom_poll

# Replace these with your own values
meeting_id = '97630877109'  # e.g. '97630877109'
access_token = 'eyJzdiI6IjAwMDAwMiIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6ImMxZTQ1M2M4LWE3MzktNGU4MC1hNzc5LWQ0NTdlZmE1NDVlZSJ9.eyJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJjRU9vYWNPblMyMldzbU42YjNwa09BIiwidmVyIjoxMCwiYXVpZCI6IjQ2MWU4ZjQwNDNmNTIxNDQ2OGZlOGQ3ZGIxMWQ0MDZlZGJjMWMzZDMxODkxOWFlNWZhNmFkZDQxY2NjNGFjMDciLCJuYmYiOjE3NDQ4MDY5NTAsImNvZGUiOiJIZENmQlVwV0k3YngyWWRnTHB2VFVhZFF0Nm15Ym5tYXciLCJpc3MiOiJ6bTpjaWQ6b2ZKMTkwczRSOVM2MF9CU3Z5aDB3ZyIsImdubyI6MCwiZXhwIjoxNzQ0ODEwNTUwLCJ0eXBlIjowLCJpYXQiOjE3NDQ4MDY5NTAsImFpZCI6InZzd3VqUm1OU2V5eTQyNDBGSFJCRVEifQ.rAsclCF5RCQ4oAiBcD6DBVUX1AasEwWswoPUgY6bxmETN8gvI_1CGKP3FHKwFPgGqgHOWIDAEbTzXWPQ7ncQgQ'

def main():
    print("🚀 Poll Automation Test Started")

    # Get user settings
    duration = int(input("⏱️ How many seconds should transcription run? (e.g., 60): "))
    delay = int(input("⏳ After how many seconds should the next poll be posted? (e.g., 120): "))

    while True:
        print(f"\n🎤 Transcribing for {duration} seconds...")
        transcript = transcribe(duration)
        print("📝 Transcript collected.")

        print("🤖 Generating poll question and options...")
        question, options = generate_poll(transcript)

        print("🗳️ Posting poll to Zoom...")
        success = create_zoom_poll(access_token, meeting_id, question, options)

        if success:
            print("✅ Poll posted successfully!")
        else:
            print("❌ Poll failed.")

        print(f"⏳ Waiting {delay} seconds before next cycle...")
        time.sleep(delay)

if __name__ == "__main__":
    main()
