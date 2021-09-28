import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from adafruit_rgb_display.rgb import color565

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

#button settings
buttonA = digitalio.DigitalInOut(board.D23)
buttonA.switch_to_input()
buttonB = digitalio.DigitalInOut(board.D24)
buttonB.switch_to_input()

while True:
    #Draw a black filled box to clear the image.
    #draw.rectangle((0,0, width, height), outline = 0, fill =0)

    #TODO: Lab part D work should be filled in here
    #set up landing page messages to guide user
    y = top
    header = "Puzzle Clock"
    space = "             "
    buttons = "Buttons"
    top_button = "Top: month word scramble"
    bottom_button = "Bottom: hour word search"
    both = "Both: other puzzles"
    draw.rectangle((0, 0, width, height), outline=0, fill="#FAE785")
    draw.text((x, y), header, font=font_large, fill="#0093AF")
    y += font.getsize(header)[1]
    draw.text((x, y), space, font=font_large, fill="#D70040")    
    y += font.getsize(space)[1]
    draw.text((x, y), buttons, font=font, fill="#000000")    
    y += font.getsize(buttons)[1]
    draw.text((x, y), top_button, font=font, fill="#D70040")
    y += font.getsize(top_button)[1]
    draw.text((x, y), bottom_button, font=font, fill="#FF55A3")
    y += font.getsize(bottom_button)[1]
    draw.text((x, y), both, font=font, fill="#8A2BE2")
    
    #set info for top button - month word scramble
    month = int(strftime("%m"))
    if month == 1:
        scramble = 'UJRNAAY'
    elif month == 2:
        scramble = 'RBYRUAEF'
    elif month == 3:
        scramble = 'CAHMR'
    elif month == 4:
        scramble = 'RIAPL'
    elif month == 5:
        scramble = 'YAM'
    elif month == 6:
        scramble = 'NEJU'
    elif month == 7:
        scramble = 'UYLJ'
    elif month == 8:
        scramble = 'UUTAGS'
    elif month == 9:
        scramble = 'EEEMSTRBP'
    elif month == 10:
        scramble = 'BOEOCTR'
    elif month == 11:
        scramble = 'REVOMEBN'
    elif month == 12:
        scramble = 'BEEDRCME'

    #set info for bottom button - time of day word search
    hour = int(strftime("%H"))
    if hour >=0 and hour < 12: # morning
        img = "morning_crop14.png"
    elif hour >= 12 and hour < 17: # afternoon
        img = "afternoon_wordsearch.png"
    elif hour >= 17: #evening
        img = "evening_wordsearch.png"



    #set info for both buttons about recommended actions
    day = int(strftime("%d"))
    if day % 2 ==0:
        rec = "try a sudoku"
    else:
        rec = "try a crossword puzzle"
    #sudoku_img = 


    clock_time = strftime("%m/%d/%Y %H:%M:%S")
    y = top

    if buttonB.value and not buttonA.value:  # just top button - tell about time of year - word scramble
        draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
        draw.text((x, y), scramble, font=font_large, fill="#E3DAC9")
        disp.image(image, rotation)
        time.sleep(2)
    
    if buttonA.value and not buttonB.value:  # just bottom button
        image = Image.open(img)
        #scale image to smaller screen
        image_ratio = image.width / image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
            scaled_width = image.width * height // image.height
            scaled_height = height
        else:
            scaled_width = width
            scaled_height = image.height * width // image.width
        image = image.resize((scaled_width, scaled_height), Image.BICUBIC)
        #crop and center image
        x = scaled_width // 2 - width // 2
        y = scaled_height // 2 - height // 2
        image = image.crop((x, y, x+width, y + height))
        # Display image.
        disp.image(image, rotation)
        time.sleep(2)
        #draw black box to clear image
        height = disp.width  
        width = disp.height
        image = Image.new("RGB", (width, height))
        rotation = 90
        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        disp.image(image, rotation)

    if not buttonA.value and not buttonB.value:  # both buttons
        draw.rectangle((0, 0, width, height), outline=0, fill="#D891EF")
        draw.text((x, y), rec, font=font, fill="#E3DAC9")    
        disp.image(image, rotation)
        time.sleep(2)


    disp.image(image, rotation)
    time.sleep(0.5)
