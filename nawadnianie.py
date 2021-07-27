from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)


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
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500