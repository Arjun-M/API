from flask import Flask, request ,jsonify , redirect  ,send_file
from PIL import Image, ImageDraw, ImageFont
from src import mainSERVER , FONTS , BACKGROUNDS 
import os , random , string

app = Flask(__name__)
api = mainSERVER (logs = False) # don't  log .
host = os.getenv('HOST', "logo-000-api.herokuapp.com" )
logos = [] 


@app.route("/" , methods=['GET'])
def helloname():
  return f"Hello 👋"  


@app.route("/logo/list" , methods=['GET'])
def debug_logo_list():
  return jsonify ({"ok": True , "result": {"list": logos}})

# API debug "/logo/clean" has bugs .
"""
@app.route("/logo/clean" , methods=['GET'])
def debug_logo_clean():
  cleaned = 0
  error = 0
  for x in logos :
    try:
      cleaned += 1
      os.remove("./assets/"+x["string"]+".jpeg")
    except:
      error += 1
  logos = []
  return jsonify ({ "ok" : True , "result":{ "cleaned": cleaned , "error": error} })
"""


@app.route('/image/<file>', methods=['GET'])
def send_logo(file):
  try:
    return send_file( f"./assets/{file}.jpeg" , mimetype='image/jpeg')  
  except Exception as e:
    print("Send Logo Error : "+ str(e) )
    return send_file( random.choice(BACKGROUNDS) , mimetype= 'image/jpeg' )
  

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
    
