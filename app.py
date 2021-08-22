from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') #add your file here

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') #add your file here
  
@app.route('/invite')
def invite():
  return redirect("https://discord.com/oauth2/authorize?client_id=877994181623160882&permissions=2416125952&scope=bot", code=302)

if __name__ == '__main__':
    app.run(debug=True)