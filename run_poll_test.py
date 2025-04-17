# run_poll_test.py

from post_poll import create_zoom_poll

# 🔑 Your fresh access token (valid for ~1 hour)
access_token = 'eyJzdiI6IjAwMDAwMiIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6ImFhOTlmZGVlLTI1MmUtNDdiNC1hYzQ0LWVhNWNiMGM5Zjc1ZCJ9.eyJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJjRU9vYWNPblMyMldzbU42YjNwa09BIiwidmVyIjoxMCwiYXVpZCI6IjQ2MWU4ZjQwNDNmNTIxNDQ2OGZlOGQ3ZGIxMWQ0MDZlZGJjMWMzZDMxODkxOWFlNWZhNmFkZDQxY2NjNGFjMDciLCJuYmYiOjE3NDQ4MDg3OTAsImNvZGUiOiI5cVBsUGhVUFVZdTVrNklJMW1ZUTZlS1Itd2JwYzlEc2ciLCJpc3MiOiJ6bTpjaWQ6b2ZKMTkwczRSOVM2MF9CU3Z5aDB3ZyIsImdubyI6MCwiZXhwIjoxNzQ0ODEyMzkwLCJ0eXBlIjowLCJpYXQiOjE3NDQ4MDg3OTAsImFpZCI6InZzd3VqUm1OU2V5eTQyNDBGSFJCRVEifQ.hIFZBKanv0vfKfhVw2TLa6qQpEv_Hkj4H8jh09SZkQGaNM3rqsSM0mxS6fBG7wcG2F5oFcEKO_uC4rYyZYtH6w'

# 🧾 Zoom meeting ID (from your link)
meeting_id = '97630877109'

# 🗳️ Poll content to post
question = "where are you?"
options = [
    "iit-h",
    "iit-r",
    "iit-kgp",
    "iit-del"
]

# 🚀 Send the poll
create_zoom_poll(access_token, meeting_id, question, options)
