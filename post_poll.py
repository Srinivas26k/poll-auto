# post_poll.py

import requests

def create_zoom_poll(access_token, meeting_id, question, options):
    url = f"https://api.zoom.us/v2/meetings/{meeting_id}/polls"

    poll_data = {
        "title": "Automated Poll",
        "anonymous": False,
        "poll_type": 1,
        "questions": [
            {
                "name": question,
                "type": "single",
                "answers": options,
                "answer_required": True
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=poll_data, headers=headers)
    
    if response.status_code == 201:
        return True
    else:
        print(f"❌ Failed to create poll:\n{response.status_code} {response.text}")
        return False
