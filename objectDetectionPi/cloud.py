############################################################################
# Script Name: cloud.py
# Description: ThingsBoard - Dual-way Communication
# Parameters: Buzzer, Temp & Hum. Sensor
# Copyright: Following code is written for educational purposes by Cardiff University.
# Latest Version: 15/04/2022 (by Hakan KAYAN)
############################################################################

import os
import time
import paho.mqtt.client as mqtt
import json
import grovepi

# THINGSBOARD_HOST = 'demo.thingsboard.io'
THINGSBOARD_HOST = 'thingsboard.cs.cf.ac.uk'
ACCESS_TOKEN = 'KV8ua9VXNu9cOQ8Op4DS' # <== Insert your own access token here.

# Check if we can successfully push a data to thingsboard
def on_publish(client,userdata,result):
    print("Success")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print ('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload))
    # Decode JSON request
    data = json.loads(msg.payload)
    #print(data)
    # Check request method
    if data['method'] == 'setValue':
        print(data['params']) 
        buzzer_state['State'] = data['params']
        grovepi.digitalWrite(buzzer, data['params'])
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc, *extra_params):
    print('Connected with result code ' + str(rc))

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT11.
INTERVAL=3
sensor_entry_data = {'car_count': 1}
sensor_exit_data = {'car_count': -1}

next_reading = time.time() 

# We assume that Buzzer is OFF
buzzer_state = {'State': False}

# Generate your client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
# Set access token
client.username_pw_set(ACCESS_TOKEN)
# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)
# Register connect callback
client.on_connect = on_connect
# Register publish callback
client.on_publish = on_publish
# Registed publish message callback
client.on_message = on_message

# subscribe to RPC commands from the server - This will let you to control your buzzer.
client.subscribe('v1/devices/me/rpc/request/+')

client.loop_start()
# Connect DHT to digital port D4
sensor = 4  # The Sensor goes on digital port 4.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.
# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8
grovepi.pinMode(buzzer,"OUTPUT")

def post_data(image_data , isEntry):
    print('POSTING DATA TO CLOUD',image_data)
    if(len(image_data.detections) <= 0):
     return
    print(type(image_data.detections[0].categories))
    json_data = ""
    if(isEntry):
        json_data = json.dumps(sensor_entry_data)
    else:
        json_data = json.dumps(sensor_exit_data)
     
    try:    
        for image in image_data.detections:
            for category in image.categories:
                print('CLOUD CODE::DETECTED OBJECT CATEGORY ::',category)
                if category.category_name.lower() == 'car':
                    print('CLOUD CODE::REQUIRED OBJECT DETECTED ::',category)
                    print('CLOUD CODE::REQUIRED OBJECT DETECTED ::',client)
                    client.publish('v1/devices/me/telemetry', json_data, 1)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
        print ("Terminated.")
        os._exit(0)                