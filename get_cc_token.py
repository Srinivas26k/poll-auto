import requests

def get_closed_caption_token(meeting_id, access_token):
    url = f"https://api.zoom.us/v2/meetings/{meeting_id}/token?type=closed_caption"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        token = response.json().get("token")
        return token
    else:
        print(f"❌ Failed to get token: {response.status_code} {response.text}")
        return None
