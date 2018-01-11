import pigpio

pi = pigpio.pi()

def mode(pin, mode):
    if mode == "output":
        pi.set_mode(pin, pigpio.OUTPUT)
    if mode == "input":
        pi.set_mode(pin, pigpio.INPUT)
def pud(pin, pud):
    if pud == "pud_up":
        pi.set_pull_up_down(pin, pigpio.PUD_UP)
    if pud == "pud_down":
        pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
    if pud == "pud_off":
        pi.set_pull_up_down(pin, pigpio.PUD_OFF)

def write(pin, state):
    pi.write(int(pin), int(state))

def pwm_dutycycle(pin, dutycycle):
    pi.set_PWM_dutycycle(pin, dutycycle)

def pwm_frequency(pin, frequency):
    pi.set_PWM_frequency(pin,frequency)
