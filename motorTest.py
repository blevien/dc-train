import RPi.GPIO as GPIO
import time

# Modified From https://embeddedcircuits.com/raspberry-pi/tutorial/how-to-generate-pwm-signal-from-raspberry-pi

speed = 100
speedPin = 25
m1p1 = 24
m1p2 = 23

# Use Board Numbering, not Chip Pin order Numbering
GPIO.setmode(GPIO.BCM)

# Configure Speed Pin for PWM at 1,000 khz
GPIO.setup(speedPin, GPIO.OUT)
GPIO.output(speedPin, GPIO.LOW)
pwm = GPIO.PWM(speedPin, 1000)

# Configure Direction Pins
GPIO.setup(m1p1, GPIO.OUT)
GPIO.setup(m1p2, GPIO.OUT)

# Start the PWM at 0
pwm.start(0)

# Go Backwards
GPIO.output(m1p1, GPIO.HIGH)
GPIO.output(m1p2, GPIO.LOW)

# Run motor for 3 seconds
pwm.ChangeDutyCycle(speed)
time.sleep(3)

# Go Forwards
GPIO.output(m1p1, GPIO.LOW)
GPIO.output(m1p2, GPIO.HIGH)
time.sleep(3)

# Stop and Shut Everything Down
pwm.stop()
GPIO.output(speedPin, GPIO.LOW)
GPIO.output(m1p1, GPIO.LOW)
GPIO.output(m1p2, GPIO.LOW)
GPIO.cleanup()