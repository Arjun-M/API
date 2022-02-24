from flask import Flask, send_file, jsonify, request
from deta import Drive

app = Flask(__name__)
image_db = Drive("files")

@app.route('/', methods=['GET'])
def home():
  return "<b> Hello World </b>"


#files.get(name)
#files.list()
#files.put(file.filename, file.file)
