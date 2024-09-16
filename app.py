from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

speed = 0
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


@app.route("/")
def hello_world():
    global speed

    return render_template("base.html", speed=speed)


@app.route("/update", methods=["POST"])
def update():

    global speed
    json_data = request.json

    try:
        speed = json_data["speed"]

    except:
        pass

    setSpeed(speed)

    return str(speed)


def setSpeed(target):

    target = float(target)

    if target > 0:
        print(target, "speed forwards!")
        # Go Forwards
        GPIO.output(m1p1, GPIO.LOW)
        GPIO.output(m1p2, GPIO.HIGH)
        pwm.ChangeDutyCycle(target)
    elif target < 0:
        print(target, "speed backwards!")
        # Go Forwards
        GPIO.output(m1p1, GPIO.HIGH)
        GPIO.output(m1p2, GPIO.LOW)
        pwm.ChangeDutyCycle(abs(target))
    else:
        # Stop
        print("Stopped.")
        GPIO.output(m1p1, GPIO.LOW)
        GPIO.output(m1p2, GPIO.LOW)
        pwm.ChangeDutyCycle(target)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
