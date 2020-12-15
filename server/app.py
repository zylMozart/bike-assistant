import json
import sys
import time
import smbus
from flask import Flask
from flask import jsonify
from flask import request
from imusensor.MPU9250 import MPU9250
address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()


while True:

        time.sleep(0.1)
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/location')
def location():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/posture')
def posture():
    imu.readSensor()
    imu.computeOrientation()
    print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll, imu.pitch, imu.yaw))
    return jsonify({"code":0,"msg":"OK","data":{
        "roll":imu.roll, "pitch":imu.pitch,"yaw":imu.yaw
    } })

@app.route('/temperature')
def temperature():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/sound/play')
def play_sound():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/sound/stop')
def stop_sound():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/light/get')
def get_light():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/light/set')
def set_light():
    return jsonify({"code":0,"msg":"OK" })

if __name__ == '__main__':
    app.run()