import RPi.GPIO as gpio
from time import sleep





gpio.setmode(gpio.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perev(a):
    return[int (elem) for elem in bin(a) [2:].zfill(8)]

def adc():
    a = 0
    for i in range (7, -1, -1):
        a += 2**i
        gpio.output(dac, perev(a))
        sleep(0.005)
        if gpio.input(comp) == 0:
            a -= 2**i
    return a

def volume(k, n):
    x = round(k / n*8)
    ans = [0 for i in range(8)]
    for i in range (x):
        ans[i] = 1
    return ans



try:
    while True:
        k = adc()
        gpio.output(leds, volume(k, 65))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
