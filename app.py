from flask import Flask,  request, jsonify
# from db import db
from api import main
# import requests

app = Flask(__name__)
# app.debug = True

@app.route('/', methods=['GET'])
def index():
    return jsonify({"code": 200, "msg":"说说后端运行正常", "data":None})

@app.route('/api/v1/talktalk', methods=['POST', 'GET'])
def api():
    info = request.json
    print(type(info))
    print(info)
    data = main.mian(info)
    if data == None: 
        return jsonify({"code": 200, "msg": "OK", "data": None})
    return jsonify({"code": 200, "msg": "OK", "data": data})

@app.errorhandler(400)
def server_error(e):
    return jsonify({"code": 400, "msg": "{}:{}".format(e.__class__.__name__, e), "data": None})

@app.errorhandler(500)
def server_error(e):
    return jsonify({"code": 500, "msg": "{}:{}".format(e.__class__.__name__, e), "data": None})

if __name__ == '__main__':
    app.run()
