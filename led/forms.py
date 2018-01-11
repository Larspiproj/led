from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired

class GpioForm(FlaskForm):
    pin = IntegerField('Pin', validators=[DataRequired()])
    mode = RadioField('Mode', choices = [('Input','Input'),('Output','Output')],
                                                   validators=[DataRequired()])
    pud = RadioField('Pud', choices = [('pud_off', 'pud_off'),
                       ('pud_down', 'pud_down'), ('pud_up', 'pud_up')],
                                           validators=[DataRequired()])
    state = RadioField('State', choices = [('0','Low'),('1','High')],
                                         validators=[DataRequired()])
    submit = SubmitField("Apply")
