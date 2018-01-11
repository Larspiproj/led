from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class PwmForm(FlaskForm):
    pin = IntegerField('Pin', validators=[DataRequired()])
    dutycycle = IntegerField('PWM_dutycycle', validators=[NumberRange
                                            (min=0,max=255)])
    frequency = IntegerField('PWM_frequency', validators=[DataRequired()])
    submit = SubmitField("Apply")
