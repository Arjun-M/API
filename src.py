from PIL import Image, ImageDraw, ImageFont
import json , requests , random, re

BACKGROUNDS = [
       "./assets/background/A.jpg", "./assets/background/L.jpg", "./assets/background/m.jpg", "./assets/background/n.jpg",
       "./assets/background/o.jpg", "./assets/background/R.jpg", "./assets/background/s.jpg", "./assets/background/t.jpg",
       "./assets/background/U.jpg", "./assets/background/as.jpg","./assets/background/ad.jpg", "./assets/background/af.jpg", 
       "./assets/background/ag.jpg", "./assets/background/ah.jpg", "./assets/background/aj.jpg", "./assets/background/ak.jpg",
       "./assets/background/al.jpg", "./assets/background/az.jpg", "./assets/background/ax.jpg"
      ]

FONTS =[
      "./assets/fonts/Illegal Curves Bold.otf", "./assets/fonts/Martyric_PersonalUse.ttf", "./assets/fonts/Neon machine.otf", "./assets/fonts/Neon machine.ttf",
      "./assets/fonts/Revolvingdor.otf", "./assets/fonts/Ace Records.ttf", "./assets/fonts/Dry Brush.ttf", "./assets/fonts/Emberclaws.ttf",
      "./assets/fonts/Fast Hand(1).otf",  "./assets/fonts/Martyric_PersonalUse.ttf", "./assets/fonts/Revolvingdor.otf", "./assets/fonts/thunderstrike.ttf",
      "./assets/fonts/thunderstrike3d.ttf", "./assets/fonts/thunderstrikecond.ttf", "./assets/fonts/thunderstrikeexpand.ttf", "./assets/fonts/thunderstrikegrad.ttf",
      "./assets/fonts/thunderstrikehalf.ttf", "./assets/fonts/thunderstrikeitalic.ttf", "./assets/fonts/thunderstrikelaser.ttf", "./assets/fonts/Vampire Wars Italic.otf",
      "./assets/fonts/Vampire Wars.otf", "./assets/fonts/Vampire Wars.ttf", "./assets/fonts/Zenzai Itacha.ttf", "./assets/fonts/Zenzai Itache.ttf",
      "./assets/fonts/Zenzai Itachi.ttf"
     ]

class mainSERVER:
    def __init__(self, log = False):
        self.log = log
        
    def createLogo(self , text ):
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
        return img
