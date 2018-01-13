import pigpio
import time
from flask import Flask, render_template, flash, redirect, url_for, request
from forms import InputForm, OutputForm, GpioForm, PwmForm, ReadForm
#from pwmforms import PwmForm
import functions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development key'

pi = pigpio.pi()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if request.method == 'POST' and form.validate_on_submit():
        #pin = int(request.form['pin'])
        pinstr = request.form['pin']
        pinsplit = pinstr.split(',')
        pud = request.form['pud']
        functions.input(pinsplit, pud)
        flash("Settings for input updated!")
        flash("Hi from /input")
        return render_template('settings.html', title='settings',
             pin=pinstr, mode="input", pud=pud, state=0, dutycycle="n/a",
             pwm_on_percent="n/a", frequency="n/a", real_frequency="n/a") 
    return render_template('input.html', title='input', form=form)

@app.route('/output', methods=['GET', 'POST'])
def output():
    form = OutputForm()
    if request.method == 'POST' and form.validate_on_submit():
        pinstr = request.form['pin']
        pinsplit = pinstr.split(',')
        state = request.form['state']
        functions.output(pinsplit, state)
        flash("Settings for input/output updated!")
        flash("Hi from /output")
        return render_template('settings.html', title='settings',
             pin=pinstr, mode="output", pud="n/a", state=state, dutycycle="n/a",
             pwm_on_percent="n/a", frequency="n/a", real_frequency="n/a") 
    return render_template('output.html', title='output', form=form)

@app.route('/pwm', methods=['GET', 'POST'])
def pwm():
    form = PwmForm()
    if request.method == 'POST' and form.validate_on_submit():
        pinstr = request.form['pin']
        pinsplit = pinstr.split(',')
        dutycycle = int(request.form['dutycycle'])
        frequency = int(request.form['frequency'])
        functions.pwm_dutycycle(pinsplit, dutycycle)
        functions.pwm_frequency(pinsplit, frequency)
        pwm_on_percent = '{:.0%}'.format(dutycycle / 255)
        for pin in pinsplit:
            real_frequency = pi.get_PWM_frequency(int(pin))
        flash("Settings for PWM updated")
        flash("Hi from /pwm")
        return render_template('settings.html', title='settings', pin=pinstr,
                   mode="n/a", pud="n/a", state="n/a", dutycycle=dutycycle,
                   pwm_on_percent=pwm_on_percent,
          frequency=frequency, real_frequency=real_frequency)
    return render_template('pwm.html', title='pwm', form=form)


@app.route('/read', methods=['GET', 'POST'])
def read():
    form = ReadForm()
    if request.method == 'POST' and form.validate_on_submit():
        pinstr = request.form['pin']
        pinsplit = pinstr.split(',')
        for pin in pinsplit:
            state = pi.read(int(pin))
            mode = pi.get_mode(int(pin))
            #real_frequency = pi.get_PWM_frequency(int(pin))
            #dutycycle = pi.get_PWM_dutycycle(int(pin))
        flash("State for Pin")
        return render_template('settings.html', title='settings',
             pin=pinstr, mode=mode, pud="n/a", state=state, dutycycle="dutycycle",
             pwm_on_percent="n/a", frequency="n/a", real_frequency="real_frequency")
    return render_template('read.html', title='read', form=form)
######################### not used ###########################

@app.route('/inputs', methods=['GET', 'POST'])
def inputs():
    form = GpioForm()
    if request.method == 'POST' and form.validate_on_submit():
        #settings = request.form 
        #pin = int(request.form['pin'])
        pinstr = request.form['pin']
        pinsplit = pinstr.split(',')
        mode = request.form['mode']
        pud = request.form['pud']
        state = request.form['state']
        functions.strtest(strpin)
        functions.mode(pinsplit, mode)
        functions.pud(pinsplit, pud)
        functions.write(pinsplit, state)
        flash("Settings for input/output updated!")
        flash("Hi from /inputs")
        return render_template('settings.html', title='settings',
             pin=pinstr, mode=mode, pud=pud, state=state, dutycycle="n/a",
             pwm_on_percent="n/a", frequency="n/a", real_frequency="n/a") 
    return render_template('inputs.html', title='inputs', form=form)
######################### not used #############################
