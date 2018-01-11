import pigpio
import time
from flask import Flask, render_template, flash, redirect, url_for, request
from forms import GpioForm
from pwmforms import PwmForm
import functions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development key'

pi = pigpio.pi()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/inputs', methods=['GET', 'POST'])
def inputs():
    form = GpioForm()
    if request.method == 'POST' and form.validate_on_submit():
        #settings = request.form 
        pin = int(request.form['pin'])
        mode = request.form['mode']
        pud = request.form['pud']
        state = int(request.form['state'])
        functions.mode(pin, mode)
        functions.pud(pin, pud)
        functions.write(pin, state)
        flash("Settings for input/output updated!")
        flash("Hi from /inputs")
        return render_template('settings.html', title='settings',
                     pin=pin, mode=mode, pud=pud, state=state, dutycycle="n/a",
                     pwm_on_percent="n/a", frequency="n/a", real_frequency="n/a") 
    return render_template('inputs.html', title='inputs', form=form)

@app.route('/pwm', methods=['GET', 'POST'])
def pwm():
    form = PwmForm()
    if request.method == 'POST' and form.validate_on_submit():
        pin = int(request.form['pin'])
        dutycycle = int(request.form['dutycycle'])
        frequency = int(request.form['frequency'])
        functions.pwm_dutycycle(pin, dutycycle)
        functions.pwm_frequency(pin, frequency)
        real_frequency = pi.get_PWM_frequency(pin)
        pwm_on_percent = int(100 * dutycycle / 255)
        flash("Settings for PWM updated")
        flash("Hi from /pwm")
        return render_template('settings.html', title='settings', pin=pin,
                   mode="n/a", pud="n/a", state="n/a", dutycycle=dutycycle,
                   pwm_on_percent=pwm_on_percent,
          frequency=frequency, real_frequency=real_frequency)
    return render_template('pwminputs.html', title='pwminputs', form=form)

@app.route('/css')
def css():
    return render_template('css.html')
