import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "read light sense value as inputs"

GPIO.setup(18, GPIO.IN)

print(GPIO.input(18))

GPIO.cleanup()
