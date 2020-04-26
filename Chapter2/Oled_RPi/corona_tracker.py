import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import requests
import json


url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
state_del=[]

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "83f25eb412msh3dad515eed599ecp1e68f7jsn243ed7d1a1c6"
    }


RST = None




disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 1
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

while True:

    
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    a=data['total_values']['confirmed']
    y=data['total_values']['active']
    z=data['total_values']['recovered']
    w=data['total_values']['deaths']
    t=data['total_values']['lastupdatedtime']

    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    draw.text((x+10, top),       "Live Corona Tracker",  font=font, fill=255)
    draw.text((x+0,  top+9),       "-----------------------------",  font=font, fill=255)
    draw.text((x+20, top+15),       "Confirm: "+str(a),  font=font, fill=255)
    draw.text((x+20, top+23),     "Active: "+str(y), font=font, fill=255)
    draw.text((x+20, top+31),    "Recovered: "+str(z),  font=font, fill=255)
    draw.text((x+20, top+39),    "Death: "+str(w),  font=font, fill=255)
    draw.text((x+10, top+49),    t,  font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(1.5)






