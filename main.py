from flask import Flask, send_file , jsonify, request
from deta import Drive
from src import mainSERVER

app = Flask(__name__)
disk = Drive("Disk")

@app.route('/', methods=['GET'])
def home():
  return "<b> Hello World </b>"


@app.route('/logo/<text>', methods=['GET'])
def image(text):
  try:
    logo = mainSERVER(True)
    img = logo.createLogo(text)
    return send_file(img )
  except Exception as e:
    return str(e)
  

  
  
  
#files.get(name)
#files.list()
#files.put(file.filename, file.file)
