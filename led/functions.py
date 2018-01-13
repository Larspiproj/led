import pigpio

pi = pigpio.pi()

def input(pinsplit, pud):
    for pin in pinsplit:
        pi.write(int(pin), 0)
    for pin in pinsplit:
        pi.set_mode(int(pin), pigpio.INPUT)
    if pud == "pud_up":
        for pin in pinsplit:
            pi.set_pull_up_down(int(pin), pigpio.PUD_UP)
    if pud == "pud_down":
        for pin in pinsplit:
            pi.set_pull_up_down(int(pin), pigpio.PUD_DOWN)
    if pud == "pud_off":
        for pin in pinsplit:
            pi.set_pull_up_down(int(pin), pigpio.PUD_OFF)

def output(pinsplit, state):
    for pin in pinsplit:
        pi.write(int(pin), int(state))

def pwm_dutycycle(pinsplit, dutycycle):
    for pin in pinsplit:
        pi.set_PWM_dutycycle(int(pin), dutycycle)

def pwm_frequency(pinsplit, frequency):
    for pin in pinsplit:
        pi.set_PWM_frequency(int(pin),frequency)

####################### not used #############################

def mode(pinsplit, mode):
    if mode == "output":
        for pin in pinsplit:
            pi.set_mode(int(pin), pigpio.OUTPUT)
    if mode == "input":
        for pin in pinsplit:
            pi.set_mode(int(pin), pigpio.INPUT)
def pud(pinsplit, pud):
    if pud == "pud_up":
        for pin in pinsplit:
            pi.set_pull_up_down(int(pin), pigpio.PUD_UP)
    if pud == "pud_down":
        for pin in pinsplit:
            pi.set_pull_up_down(int(pin), pigpio.PUD_DOWN)
    if pud == "pud_off":
        for pin in pinsplit:
            pi.set_pull_up_down(int(pin), pigpio.PUD_OFF)

def write(pinsplit, state):
    for pin in pinsplit:
        pi.write(int(pin), int(state))

######################## not used ###########################
