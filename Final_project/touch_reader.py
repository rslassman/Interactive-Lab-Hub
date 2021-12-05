import paho.mqtt.client as mqtt
import uuid

import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[2]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(500, 2500)

def move_servo(direction):
    if direction == "Right":
        servo.angle = 0
        print(direction)
        
    elif direction == "Left":
        servo.angle = 180
        print(direction)
        
    elif direction == "Straight":
        servo.angle = 90
        print(direction)
    
    return servo.angle

#set up MQTT
topic = 'IDD/rsl252/servo'

# some other examples
# topic = 'IDD/a/fun/topic'

#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)
    # you can subsribe to as many topics as you'd like
    # client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(client, userdata, msg):
    if msg.topic == topic:
        direction = msg.payload.decode('UTF-8')
        move_servo(direction)



# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')
# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message
#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_start()

# MAIN LOOP
while True:
    servo.angle
    time.sleep(2)