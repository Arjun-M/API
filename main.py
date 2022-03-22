from fastapi import Request, FastAPI
from PIL import Image, ImageDraw, ImageFont
from pyTelegramClient import TelegramClient,  createConnection 
from src import FONTS , BACKGROUNDS ,randomString
import os , random , string , json

app = FastAPI()
client = TelegramClient( token= "5161532146:AAHwSF3PruBpjMpuGkRNBQAmDhX7cIuv_2M" )
Bot = createConnection( client = client )

@client.messageHandler( commands= ["/start" , "/help"] )
def start( request ):
    markup = json.dumps( {"inline_keyboard": [[{ "text":"👨‍✈️ Developer" , "url":"t.me/itz_ArjunM" }]] } ) 
    Bot.sendMessage( request["user"]["id"], "Hello! i can create awsome logo's for you\n\nJust sent the text for the logo ." , parse_mode = "Markdown" , allow_sending_without_reply=True , reply_to_message_id = request["message_id"] , reply_markup=markup )   
    return 

@client.messageHandler( regexp = "(.*?)" )
def echo( request ):
    user = request["user"]["id"]
    Bot.sendMessage( user , "Creating your logo... wait !" , allow_sending_without_reply=True , reply_to_message_id = request["message_id"])
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
    img.save(f"/temp/{user}.jpeg")
    with open(f"/temp/{user}.jpeg", 'rb') as f:
        Bot.sendPhoto (user , photo= f , caption="* *", parse_mode="Markdown",  reply_markup= markup)
    return

@app.post("/hook")
async def get_body(request: Request):
    body = await request.body()
    client.processUpdate( body )
    return "OK"

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
