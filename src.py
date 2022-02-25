from PIL import Image, ImageDraw, ImageFont
import json , requests

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
      
