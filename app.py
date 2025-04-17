# app.py

from flask import Flask, redirect, request, render_template
import requests
import base64
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authorize')
def authorize():
    auth_url = (
        f"https://zoom.us/oauth/authorize"
        f"?response_type=code"
        f"&client_id={config.CLIENT_ID}"
        f"&redirect_uri={config.REDIRECT_URI}"
    )
    return redirect(auth_url)

@app.route('/oauth/callback')
def oauth_callback():
    code = request.args.get('code')
    if not code:
        return 'Authorization code not found.', 400

    token_url = 'https://zoom.us/oauth/token'
    auth_str = f"{config.CLIENT_ID}:{config.CLIENT_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        'Authorization': f'Basic {b64_auth_str}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': config.REDIRECT_URI
    }

    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get('access_token')
        return f"Access Token: {access_token}"
    else:
        return f"Failed to obtain access token: {response.text}", response.status_code

if __name__ == '__main__':
    app.run(port=8000)
