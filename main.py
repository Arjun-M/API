from flask import Flask, request ,jsonify , redirect  ,send_file
from PIL import Image, ImageDraw, ImageFont
from src import mainSERVER , FONTS , BACKGROUNDS 
import os , random , string

app = Flask(__name__)
logos = [] 

  
"""
@app.route('/logo', methods=['GET'])
def logo():
  try:
    text = request.args.get('text')
    if text == None :
      return jsonify ({"ok":False , "error": "text is required to be encoded in url" })      
    file = api.randomString(10)
    img = Image.open(random.choice(BACKGROUNDS))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    semx = random.choice(FONTS)
    font = ImageFont.truetype(semx, 150)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=15, stroke_fill="black")
    img.save(f"./assets/{file}.jpeg")
    logos.append ({"string": file , "url": f"https://{host}/image/{file}" })
    return jsonify ({"ok":True , "result":{ "string": file , "url": f"https://{host}/image/{file}" } }) 
    #return send_file( "./assets/10101.jpeg" , mimetype='image/jpeg')  
  except Exception as e:
    return jsonify ({"ok":False , "error": str(e) })
"""
