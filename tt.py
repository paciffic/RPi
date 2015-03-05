import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
print "read light sense value as inputs"

GPIO.setup(23, GPIO.IN)

for i in range(100):
	print(GPIO.input(23))
	time.sleep(0.5)

GPIO.cleanup()
