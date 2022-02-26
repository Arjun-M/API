from flask import Flask, request ,jsonify , redirect  ,send_file
from PIL import Image, ImageDraw, ImageFont
from src import mainSERVER , FONTS , BACKGROUNDS
import os , random

app = Flask(__name__)


@app.route("/" , methods=['GET'])
def helloname():
  return f"Hello 👋"  


@app.route('/logo/<text>', methods=['GET'])
def logo(text):
  img = Image.open(random.choice(BACKGROUNDS))
  draw = ImageDraw.Draw(img)
  image_widthz, image_heightz = img.size
  pointsize = 500
  fillcolor = "gold"
  shadowcolor = "blue"
  semx = random.choice(FONTS)
  font = ImageFont.truetype(semx, 300)
  w, h = draw.textsize(text, font=font)
  h += int(h*0.21)
  image_width, image_height = img.size
  draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
  x = (image_widthz-w)/2
  y= ((image_heightz-h)/2+6)
  draw.text((x, y), text, font=font, fill="white", stroke_width=15, stroke_fill="black")
  img.save("./assets/10101.jpeg")
  return send_file( "./assets/10101.jpeg" , media_type="image/jpeg")        
  
  
#files.get(name)
#files.list()
#files.put(file.filename, file.file)
