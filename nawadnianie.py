from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'to_trzeba_zmienic_przed_finalna_wersja'

class NameForm(FlaskForm):
    name = StringField('Jak masz na imie?', validators = [DataRequired()])
    submit = SubmitField('Wyślij')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time = datetime.utcnow(), form=form, name=session.get('name'))


'''
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time = datetime.utcnow(), form=form, name=name)
'''


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time = datetime.utcnow())

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