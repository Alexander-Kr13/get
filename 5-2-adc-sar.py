import RPi.GPIO as gpio
from time import sleep





gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perev(a):
    return[int (elem) for elem in bin(a) [2:].zfill(8)]

def adc():
    a = 0
    for i in range (7, -1, -1):
        a += 2**i
        gpio.output(dac, perev(a))
        sleep(0.001)
        if gpio.input(comp) == 0:
            a -= 2**i
    return a



try:
    while True:
        b = adc()
        if b != 0:
            print(b, '{:.2f}v'.format(3.3*b/256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
