from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO


pins = [ 11 ]                   # pin 11 is GPIO17
on = []

GPIO.setmode(GPIO.BOARD)        # GPIO MODE

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin , 1)
    on.append(0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', on=on)

@app.route('/status/<relay>')
def get_status(relay):
    return("on" if on[int(relay)] == 1 else "off")

@app.route('/on/<relay>', methods=['POST'])
def switch_on(relay):
    print("relay", relay, "on")
    on[int(relay)] = 1
    GPIO.output(pins[int(relay)], 0)     #low
    return(make_response(redirect(url_for('index'))))

@app.route('/off/<relay>', methods=['POST'])
def switch_off(relay):
    print("relay", relay, "off")
    on[int(relay)] = 0
    GPIO.output(pins[int(relay)] , 1)    #high
    return(make_response(redirect(url_for('index'))))

app.run(debug=True, host='0.0.0.0', port=8000)
