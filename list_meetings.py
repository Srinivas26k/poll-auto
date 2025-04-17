# list_meetings.py

import requests

# Paste your access token here
access_token = 'eyJzdiI6IjAwMDAwMiIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6Ijg4OWJlNWY2LWFlZmYtNGZiMS1iMWM2LWY0OTkzZTZkMjZmNiJ9.eyJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJjRU9vYWNPblMyMldzbU42YjNwa09BIiwidmVyIjoxMCwiYXVpZCI6IjQ2MWU4ZjQwNDNmNTIxNDQ2OGZlOGQ3ZGIxMWQ0MDZlZGJjMWMzZDMxODkxOWFlNWZhNmFkZDQxY2NjNGFjMDciLCJuYmYiOjE3NDQ4MDMyODEsImNvZGUiOiJIcUFBdEVDUnFIZ0x0Vm5YX0ZJUUhpQWpnYkl1R2NuVEEiLCJpc3MiOiJ6bTpjaWQ6b2ZKMTkwczRSOVM2MF9CU3Z5aDB3ZyIsImdubyI6MCwiZXhwIjoxNzQ0ODA2ODgxLCJ0eXBlIjowLCJpYXQiOjE3NDQ4MDMyODEsImFpZCI6InZzd3VqUm1OU2V5eTQyNDBGSFJCRVEifQ.w8fl4NdUw0r0SPAFXe5PqvzTYbbTNnIXioutsqOGX46kTtwO27Ojj9S_G0ztJR_2v2mm2IQZQQv71gAAsuuCiQ'

def list_zoom_meetings():
    url = "https://api.zoom.us/v2/users/me/meetings"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "type": "upcoming",  # You can also try "scheduled"
        "page_size": 10
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        meetings = response.json().get("meetings", [])
        if not meetings:
            print("❌ No upcoming meetings found for this Zoom user.")
        else:
            print("✅ Found the following meetings:")
            for m in meetings:
                print(f"- Topic: {m['topic']} | ID: {m['id']}")
    else:
        print("❌ Failed to fetch meetings:")
        print(response.status_code, response.text)

list_zoom_meetings()
