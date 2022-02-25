from flask import Flask, send_from_directory , jsonify, request
from deta import Drive

app = Flask(__name__)
image_db = Drive("files")

@app.route('/', methods=['GET'])
def home():
  return "<b> Hello World </b>"


@app.route('/image', methods=['GET'])
def image():
  return send_from_directory("assets/IMG_20220224_200511_453.jpg")

#files.get(name)
#files.list()
#files.put(file.filename, file.file)
