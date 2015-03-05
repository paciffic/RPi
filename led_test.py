import RPi.GPIO as GPIO
import time

port_num = 25

GPIO.setmode(GPIO.BCM)
print "Pin Test as outputs"

GPIO.setup(port_num, GPIO.OUT)
GPIO.output(port_num, False)

for x in range(0, 7):
	GPIO.output(port_num, True)
	time.sleep(0.2)

	GPIO.output(port_num, False)
	time.sleep(0.2)

GPIO.cleanup()
