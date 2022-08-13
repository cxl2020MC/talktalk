from flask import Flask,  request, jsonify
from api import main


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
# app.debug = True

@app.route('/', methods=['GET'])
def index():
    return jsonify({"code": 200, "msg":"说说后端运行正常", "data":None})

@app.route('/api/v1/talktalk/', methods=['POST', 'GET'])
def api():
    info = request.json
    print("请求数据: {}".format(info))
    ip = request.remote_addr
    print('远程ip地址: {}'.format(ip))
    data = main.mian(info, ip)
    print('返回数据: {}'.format(data))
    if data == None: 
        return jsonify({"code": 200, "msg": "OK", "data": None})
    return jsonify({"code": 200, "msg": "OK", "data": data})

@app.errorhandler(400)
def server_error(e):
    return jsonify({"code": 400, "msg": "{}: {}".format(e.__class__.__name__, e), "data": None})


@app.errorhandler(404)
def server_error(e):
    return jsonify({"code": 404, "msg": "{}: {}".format('404错误', '在请求的服务器上找不到请求的URL'), "data": None})

@app.errorhandler(500)
def server_error(e):
    return jsonify({"code": 500, "msg": "{}: {}".format(e.__class__.__name__, e), "data": None})

if __name__ == '__main__':
    app.run()
