from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, NumberRange

class NameForm(FlaskForm):
    name = StringField('Jak masz na imie?', validators = [DataRequired()])
    submit = SubmitField('Wyślij')

class SelectMethod(FlaskForm):
    automatic = SubmitField('Sterowanie automatyczne')
    manual    = SubmitField('Sterowanie ręczne')


class TimeForZones(FlaskForm):
    '''
    1 - wzdluz plotu
    2 - altana
    3 - naroznik ogrodu
    4 - front
    '''
    godzina= DateTimeField('Godzina włączenia', format='%H:%M', validators = [DataRequired()])
    plot   = IntegerField('Wzdłuż płotu', validators = [DataRequired(), NumberRange(min=0, max=15)])
    altana = IntegerField('Koło altany', validators = [DataRequired(), NumberRange(min=0, max=15)])
    corner = IntegerField('Narożnik ogrodu', validators = [DataRequired(), NumberRange(min=0, max=15)])
    front  = IntegerField('Przed domem', validators = [DataRequired(), NumberRange(min=0, max=15)])
    submit = SubmitField('Zatwierdź')