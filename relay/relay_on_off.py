import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

RELAY_GPIO = 17  # pin 11

GPIO.setup(RELAY_GPIO, GPIO.OUT)

while True:
    print("on")
    GPIO.output(RELAY_GPIO, GPIO.LOW)
    time.sleep(2)
    print("off")
    GPIO.output(RELAY_GPIO, GPIO.HIGH)
    time.sleep(2)
