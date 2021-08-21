from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') #add your file here

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') #add your file here

if __name__ == '__main__':
    app.run(debug=True)