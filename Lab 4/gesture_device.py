# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#import board
#from adafruit_apds9960.apds9960 import APDS9960

#i2c = board.I2C()

#apds = APDS9960(i2c)
#apds.enable_proximity = True
#apds.enable_gesture = True

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

#while True:
    #gesture = apds.gesture()

    #if gesture == 0x01:
        #print("straight")
    #elif gesture == 0x02:
        #print("back")
    #elif gesture == 0x03:
        #print("left")
    #elif gesture == 0x04:
        #print("right")




#imports
#displays
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import busio
#oled
import adafruit_ssd1306
#gesture
from adafruit_apds9960.apds9960 import APDS9960
#button
import qwiic_button
import os

cwd =os.getcwd()

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font_mid = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

#set up button
greenButton = qwiic_button.QwiicButton()
greenButton.begin()

#configure gesture sensor
i2c_gesture = board.I2C()
apds = APDS9960(i2c_gesture)
apds.enable_proximity = True
apds.enable_gesture = True


while True:
    
    #Draw a black filled box to clear the image.
    #draw.rectangle((0,0, width, height), outline = 0, fill =0)

    #TODO: Lab part D work should be filled in here
    #set up landing page messages to guide user
    y = top
    #header = "Gesture -> Directions"
    #space = "             "
    #clock = strftime("%m/%d/%Y %H:%M:%S")
    first = "Press green button"
    second = "to start recording"
    draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
    draw.text((x, y), first, font=font, fill="#0093AF")
    y += font.getsize(first)[1]
    draw.text((x, y), second, font=font, fill="#0093AF")    
    #y += font.getsize(header)[1]
    #draw.text((x, y), space, font=font, fill="#0093AF")    

    disp.image(image, rotation)
    time.sleep(1)
    
    if greenButton.is_button_pressed()==True:
        start = "Start Recording"
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        draw.text((x,y),start,font=font_mid,fill = "#0093AF")

    else:
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        
        
    gesture = apds.gesture()
    directions = []
    if gesture == 0x01:
        #print("straight")
        directions.append("straight")

    elif gesture == 0x02:
                #print("back")
        directions.append("back")
                
    elif gesture == 0x03:
                #print("left")
        directions.append("left")

    elif gesture == 0x04:
                #print("right")
        directions.append("straight")
                
            
    #if greenButton.is_button_pressed()==False:
    draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
    draw.text((x,y),str(directions),font=font_mid,fill = "#0093AF")

    disp.image(image,rotation)
    time.sleep(5)
    



# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
#i2c_oled = busio.I2C(board.SCL, board.SDA)
#oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c_oled)

# start with a blank screen
#oled.fill(0)

# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
#oled.show()

#oled.pixel(0,0,1)
#oled.pixel(64,16,1)
#oled.pixel(127,31,1)
#oled.show()