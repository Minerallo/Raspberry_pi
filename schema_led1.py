import RPi.GPIO as GPIO
import time

nout = 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(nout, GPIO.OUT)

GPIO.output(nout, GPIO.HIGH)
time.sleep(1)
GPIO.output(nout, GPIO.LOW)
GPIO.cleanup



