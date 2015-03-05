import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "Setup LED pins as outputs"

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)

for x in range(0,7):
	GPIO.output(23, True)
	GPIO.output(24, False)
	time.sleep(0.2)

	GPIO.output(23, False)
	GPIO.output(24, True)
	time.sleep(0.2)


GPIO.cleanup()
