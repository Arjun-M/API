from flask import Flask, send_file, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return "<b> Hello World </b>"
