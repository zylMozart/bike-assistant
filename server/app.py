import json
import sys
from gps import *
import RPi.GPIO as GPIO
import time
import smbus
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import *
import threading
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2
from imusensor.MPU9250 import MPU9250

gpsd=None
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

gpsp = GpsPoller() # create the thread
gpsp.start() # start it up

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域

@app.route('/')
def index():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/location')
def location():
    print ('latitude' , gpsd.fix.latitude)
    print ('longitude' , gpsd.fix.longitude)
    print ('altitude (m)' , gpsd.fix.altitude)
    return jsonify({"code":0,"msg":"OK" ,"data":{
        "latitude":gpsd.fix.latitude, "longitude":gpsd.fix.longitude,"altitude":gpsd.fix.altitude,"status":gpsd.fix.status,"speed":gpsd.fix.speed
    } })

@app.route('/posture')
def posture():
    imu.readSensor()
    imu.computeOrientation()
    print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll, imu.pitch, imu.yaw))
    return jsonify({"code":0,"msg":"OK","data":{"roll":imu.roll, "pitch":imu.pitch,"yaw":imu.yaw}})

@app.route('/temperature')
def temperature():
    imu.readSensor()
    return jsonify({"code":0,"msg":"OK","data":imu.Temp})

@app.route('/sound/play')
def play_sound():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/sound/stop')
def stop_sound():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/light/down')
def get_light():
    GPIO.output(11, GPIO.LOW)
    return jsonify({"code":0,"msg":"OK" })

@app.route('/light/up')
def set_light():
    GPIO.output(11, GPIO.HIGH)
    return jsonify({"code":0,"msg":"OK" })

@app.route('/light2/down')
def get_light2():
    GPIO.output(11, GPIO.LOW)
    return jsonify({"code":0,"msg":"OK" })

@app.route('/light2/up')
def set_light2():
    GPIO.output(11, GPIO.HIGH)
    return jsonify({"code":0,"msg":"OK" })

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock

	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

if __name__ == '__main__':
    app.run(port=8003)