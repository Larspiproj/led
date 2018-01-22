import pigpio
import time
from flask import Flask, render_template, flash, redirect, url_for, request
from forms import InputForm, OutputForm, GpioForm, PwmForm, ReadForm
#from pwmforms import PwmForm
import functions
#from collections import OrderedDict

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
        # Convert pins to integers using list comprehensions
        pinsplit = [int(x) for x in pinsplit]
        statelist = []
        modelist =[]
        #statedict = {}
        #modedict = {}
        # Read pins and store state and mode in lists
        for pin in pinsplit:
            state = pi.read(int(pin))
            mode = pi.get_mode(int(pin))
            statelist.append(int(state))
            modelist.append(int(mode))
        # Make dictionaries with pins as keys and state/mode as values.
        #statedict = dict(zip(pinsplit, statelist))
        statedictunsort = dict(zip(pinsplit, statelist))
        modedictunsort = dict(zip(pinsplit, modelist))
        # Code for converting pins to integer not needed(se above).
        #int_statedictunsort = {int(pinsplit) : statelist for pinsplit,
        #        statelist in statedictunsort.items()}
        #int_modedictunsort = {int(pinsplit) : modelist for pinsplit,
        #        modelist in modedictunsort.items()}
        # Sort dictionaries by keys. Result returned as lists with
        # tuples like (4, 0).
        statedict = sorted(statedictunsort.items())
        modedict = sorted(modedictunsort.items())
        #for i in range(len(pinsplit)):
        #    statedict.update({pinsplit[i]: statelist[i]})
        #    modedict.update({pinsplit[i]: modelist[i]})
            #real_frequency = pi.get_PWM_frequency(int(pin))
            #dutycycle = pi.get_PWM_dutycycle(int(pin))
        flash("State for Pin")
        return render_template('configurations.html', title='configurations',
                                      statedict=statedict, modedict=modedict)

    return render_template('read.html', title='read', form=form)

######################### not used ###########################

@app.route('/read/configuration', methods=['GET', 'POST'])
def configuration():
    form = ReadForm()
    if request.method == 'POST' and form.validate_on_submit():
        pinstr = request.form['pin']
        pinsplit = pinstr.split(',')
        statelist = []
        modelist =[]
        for pin in pinsplit:
            state = pi.read(int(pin))
            mode = pi.get_mode(int(pin))
            statelist.append(state)
            modelist.append(mode)
        statedict = dict(zip(pinsplit, statelist))
        modedict = dict(zip(pinsplit, modelist))
        flash("State for Pin")
        return render_template('configurations.html', title='configurations',
                                      statedict=statedict, modedict=modedict)
    return render_template('read.html', title='read', form=form)


@app.route('/readtest', methods=['GET','POST'])
def readtest():
    form = ReadForm()
    if request.method == 'POST' and form.validate_on_submit():
        pinstr = request.form['pin']
        pinsplit = pinstr.split(',')
        return render_template('readtest.html', title='readtest', pinstr=pinstr, pinsplit=pinsplit)
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
