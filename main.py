from flask import Flask, send_file , jsonify, request
from PIL import Image, ImageDraw, ImageFont
from deta import Drive
from src import mainSERVER , FONTS , BACKGROUNDS

app = Flask(__name__)
disk = Drive("Disk")

@app.route('/', methods=['GET'])
def home():
  return "<b> Hello World </b>"


@app.route('/logo/<text>', methods=['GET'])
def image(text):
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
  return send_file ( img )        
  

  
  
  
#files.get(name)
#files.list()
#files.put(file.filename, file.file)
