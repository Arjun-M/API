from flask import Flask, send_file , jsonify, request
from deta import Drive

app = Flask(__name__)
disk = Drive("Disk")

@app.route('/', methods=['GET'])
def home():
  return "<b> Hello World </b>"


@app.route('/image', methods=['GET'])
def image():
  try:
    return send_file("./assets/IMG_20220224_200511_453.jpg")
  except Exception as e:
    return str(e)

  
@app.route('/image2', methods=['GET'])
def image():
  try:
    f = open( "./assets/IMG_20220224_200511_453.jpg" , 'r')
    return send_file(f)
  except Exception as e:
    return str(e)
  
  
#files.get(name)
#files.list()
#files.put(file.filename, file.file)
