from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, SubmitField, \
TextField
from wtforms.validators import DataRequired, NumberRange

class InputForm(FlaskForm):
    pin = TextField('Pin', validators=[DataRequired()])
    pud = RadioField('Pud', choices = [('pud_off', 'pud_off'),
                       ('pud_down', 'pud_down'), ('pud_up', 'pud_up')],
                                           validators=[DataRequired()])
    submit = SubmitField("Apply")

class OutputForm(FlaskForm):
    pin = TextField('Pin', validators=[DataRequired()])
    state = RadioField('State', choices = [('0','Low'),('1','High')],
                                         validators=[DataRequired()])
    submit = SubmitField("Apply")
class GpioForm(FlaskForm):
    #pin = IntegerField('Pin', validators=[DataRequired()])
    pin = TextField('Pin', validators=[DataRequired()])
    mode = RadioField('Mode', choices = [('Input','Input'),('Output','Output')],
                                                   validators=[DataRequired()])
    pud = RadioField('Pud', choices = [('pud_off', 'pud_off'),
                       ('pud_down', 'pud_down'), ('pud_up', 'pud_up')],
                                           validators=[DataRequired()])
    state = RadioField('State', choices = [('0','Low'),('1','High')],
                                         validators=[DataRequired()])
    submit = SubmitField("Apply")

class PwmForm(FlaskForm):
    pin = TextField('Pin', validators=[DataRequired()])
    dutycycle = IntegerField('PWM_dutycycle', validators=[NumberRange
                                            (min=0,max=255)])
    frequency = IntegerField('PWM_frequency', validators=[DataRequired()])
    submit = SubmitField("Apply")
class ReadForm(FlaskForm):
    pin = TextField('Pin', validators=[DataRequired()])
    submit = SubmitField("Apply")
