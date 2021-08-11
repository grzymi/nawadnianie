from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import NameForm, SelectMethod, TimeForZones
from dane import suma

import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'to_trzeba_zmienic_przed_finalna_wersja'

'''
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
    form = SelectMethod()
    if form.validate_on_submit():
        if form.automatic.data:
            return redirect(url_for('automatic'))
        elif form.manual.data:
            return redirect(url_for('manual'))
    return render_template('index.html', current_time = datetime.utcnow(), form=form)

@app.route('/automatic', methods=['GET', 'POST'])
def automatic():
    #plot = 0
    #altana = 0
    #corner = 0
    #front = 0
    form = TimeForZones()
    if form.validate_on_submit():
        session['godzina'] = form.godzina.data
        session['plot'] = form.plot.data
        session['altana'] = form.altana.data
        session['corner'] = form.corner.data
        session['front'] = form.front.data
        return redirect(url_for('automatic')), suma(form.godzina.data, form.plot.data, form.altana.data, form.corner.data, form.front.data)
    return render_template('automatic.html', current_time = datetime.utcnow(), form=form,
                           plot=session.get('plot'), altana=session.get('altana'), corner=session.get('corner'),
                           front=session.get('front'), godzina=session.get('godzina'))
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