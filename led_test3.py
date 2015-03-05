import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "Setup LED pins as outputs"

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)

for x in range(0,7):
	GPIO.output(17, True)
	time.sleep(0.2)

	GPIO.output(17, False)
	time.sleep(0.2)


GPIO.cleanup()
