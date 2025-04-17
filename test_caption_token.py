import requests

access_token = "eyJzdiI6IjAwMDAwMiIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6IjU2MDVmNzYxLWNlMjctNGY5My04MzIyLTY5ZTdlN2E0MzA5YSJ9.eyJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJjRU9vYWNPblMyMldzbU42YjNwa09BIiwidmVyIjoxMCwiYXVpZCI6IjQ2MWU4ZjQwNDNmNTIxNDQ2OGZlOGQ3ZGIxMWQ0MDZlZGJjMWMzZDMxODkxOWFlNWZhNmFkZDQxY2NjNGFjMDciLCJuYmYiOjE3NDQ4MTAzNjUsImNvZGUiOiJ4VHIyaTNGanNLZkdhSlhidlNFUXhxYTVvNy1ObWdjd0EiLCJpc3MiOiJ6bTpjaWQ6b2ZKMTkwczRSOVM2MF9CU3Z5aDB3ZyIsImdubyI6MCwiZXhwIjoxNzQ0ODEzOTY1LCJ0eXBlIjowLCJpYXQiOjE3NDQ4MTAzNjUsImFpZCI6InZzd3VqUm1OU2V5eTQyNDBGSFJCRVEifQ.va4PFkQTvfCthp01xaa1TGyXB6TZ_Jnt7bvZWDj0DItX_J9lKEH2d7SLRw6yYiFaNT81BIEfaur-LR8nNcvVRA"
meeting_id = "96014521103"

url = f"https://api.zoom.us/v2/meetings/{meeting_id}/token?type=closed_caption"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ Caption Token:", response.json()["token"])
else:
    print("❌ Failed:", response.status_code, response.text)
