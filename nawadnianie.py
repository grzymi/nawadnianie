from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/status')
def status():
    relay1 = requests.post(url = 'http://192.168.0.169/cm?cmnd=Power1%20Status')
    if '"ON"' in relay1.text:
        relay1 = requests.post(url = 'http://192.168.0.169/cm?cmnd=Power1%20Off')
        state = f'Switch OFF'
    elif '"OFF"' in relay1.text:
        relay1 = requests.post(url = 'http://192.168.0.169/cm?cmnd=Power1%20On')
        state = f'Switch ON'
    return render_template('status.html', state=state)
    