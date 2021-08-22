from requests_oauthlib import OAuth2Session
import getpass
from flask import Flask, request, redirect, session, render_template
import os

# Settings for your app
base_discord_api_url = 'https://discordapp.com/api'
client_id = r'877994181623160882' # Get from https://discordapp.com/developers/applications
client_secret =  os.getenv('name')
redirect_uri='http://192.168.1.168:8000/profile'
scope = ['identify', 'email']
token_url = 'https://discordapp.com/api/oauth2/token'
authorize_url = 'https://discordapp.com/api/oauth2/authorize'

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def home():
    return render_template('index.html') #add your file here

@app.route("/login")
def login():
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    login_url, state = oauth.authorization_url(authorize_url)
    session['state'] = state
    print("Login url: %s" % login_url)
    return redirect(login_url)
    return 

@app.route("/oauth_callback")
def oauth_callback():
    """
    The callback we specified in our app.
    Processes the code given to us by Discord and sends it back
    to Discord requesting a temporary access token so we can 
    make requests on behalf (as if we were) the user.
    e.g. https://discordapp.com/api/users/@me
    The token is stored in a session variable, so it can
    be reused across separate web requests.
    """
    discord = OAuth2Session(client_id, redirect_uri=redirect_uri, state=session['state'], scope=scope)
    token = discord.fetch_token(
        token_url,
        client_secret=client_secret,
        authorization_response=request.url,
    )
    session['discord_token'] = token
    return 'Thanks for granting us authorization. We are logging you in! You can now visit <a href="/profile">/profile</a>'

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') #add your file here
  
@app.route('/invite')
def invite():
  return redirect("https://discord.com/oauth2/authorize?client_id=877994181623160882&permissions=2416125952&scope=bot", code=302)

if __name__ == '__main__':
    app.run(debug=True)