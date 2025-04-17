import requests
import time

# 🔁 PASTE your actual Caption API token URL below 👇
CAPTION_API_URL = "https://wmcc.zoom.us/closedcaption?id=96014521103&ns=dGVzdCB6b29t&expire=108000&sparams=id%2Cns%2Cexpire&signature=k58xy3gQ1cs4uZ5Erfg1TpY5B6XzrAVblof2d3GhUZs.AG.PKX_SY7EpqvyUBCJV5MAHUhXC_BMQev3F0wv3wiGgDWnezaJQ7TB8fF4FT-qdcBw3CW-CgWndygCDJ7gCnY-qQKAqrwzzo7Oj8aGDiLbUnELZ_5jkMUlVJhZ-VB0V85bkr-t_JvwVBKEHdyypxyEGLMyqFCK04UFMnXYozCdmMzpLF2uZkc3P3b6Jy3TS7NCOHe3.S6TuVVCcSUBwOmRuEDbz_A.1URpqeekTx8-OTfI"

# 📝 Example caption text
caption_text = "This is a test caption sent via the API."

# Send caption via POST
response = requests.post(
    CAPTION_API_URL,
    data=caption_text.encode('utf-8'),
    headers={
        "Content-Type": "text/plain; charset=utf-8"
    }
)

if response.status_code == 200:
    print("✅ Caption successfully sent to Zoom!")
else:
    print(f"❌ Failed to send caption: {response.status_code}")
    print(response.text)
