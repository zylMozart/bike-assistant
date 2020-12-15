from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/location')
def location():
    return jsonify({"code":0,"msg":"OK" })

@app.route('/posture')
def posture():
    return jsonify({"code":0,"msg":"OK" })

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