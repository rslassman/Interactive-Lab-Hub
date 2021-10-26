# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_apds9960.apds9960 import APDS9960
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from adafruit_rgb_display.rgb import color565
import qwiic_button


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
y = top

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

#configure gesture sensor
i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

#configure button
greenButton = qwiic_button.QwiicButton()
greenButton.begin()
# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

directions = []
while True:
    
    if greenButton.is_button_pressed()==True:
        start = "Start Recording"
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        draw.text((x,y),start,font=font_mid,fill = "#0093AF")
        disp.image(image, rotation)
        time.sleep(2)

    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
        directions.append("straight")
    elif gesture == 0x02:
        print("down")
        directions.append("back")
    elif gesture == 0x03:
        print("left")
        directions.append("left")
    elif gesture == 0x04:
        print("right")
        directions.append("right")
    if len(directions) >= 5:
        print (directions)
        
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        draw.text((x, y), str(directions[0]), font=font, fill="#D70040")    
        y += font.getsize(str(directions))[1]
        draw.text((x, y), str(directions[1]), font=font, fill="#D70040")    
        y += font.getsize(str(directions))[1]
        draw.text((x, y), str(directions[2]), font=font, fill="#D70040")    
        y += font.getsize(str(directions))[1]
        draw.text((x, y), str(directions[3]), font=font, fill="#D70040")
        y += font.getsize(str(directions))[1]
        draw.text((x, y), str(directions[4]), font=font, fill="#D70040")
        #y += font.getsize(bottom_button)[1]
        #draw.text((x, y), both, font=font, fill="#8A2BE2")

        
        
        
        disp.image(image, rotation)
        time.sleep(2)

        break
    
