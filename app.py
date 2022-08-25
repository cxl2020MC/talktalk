from flask import Flask,  request, jsonify
from flask_cors import CORS
from api import main
import traceback

app = Flask(__name__)
cors = CORS(app, origins = "*", supports_credentials=True)
app.config["JSON_AS_ASCII"] = False
app.config['SECRET_KEY']='talktalk-vercel-py_powered_by_cxl2020mc'
app.debug = True


@app.route('/', methods=['GET'])
def index():
    try:
        import db
        print("检查数据库连接成功，数据库列表: {}".format(db.client.list_database_names()))
    except Exception as e:
        错误信息 = traceback.format_exc()
        print(错误信息)
        return jsonify({"code": 500,
                        "msg":"数据库连接失败，错误信息(详细信息请查看日志): {}: {}".format(e.__class__.__name__, e), 
                        "data":None})
    return jsonify({"code": 200, "msg":"说说后端运行正常", "data":None})

@app.route('/api/v1/talktalk/', methods=['POST', 'GET'])
def api():
    try:
        info = request.json
        print("请求数据: {}".format(info))
        ip = request.remote_addr
        print('远程ip地址: {}'.format(ip))
        data = main.mian(info, ip)
        print('返回数据: {}'.format(data))
        if data == None: 
            return jsonify({"code": 200, "msg": "OK", "data": None})
        return jsonify({"code": 200, "msg": "OK", "data": data})
    except Exception as e:
        错误信息 = traceback.format_exc()
        print(错误信息)
        return jsonify({"code": 500, "msg": "{}: {}".format(e.__class__.__name__, e), "data": None})

@app.errorhandler(400)
def server_error(e):
    return jsonify({"code": 400, "msg": "{}: {}".format(e.__class__.__name__, e), "data": None})


@app.errorhandler(404)
def server_error(e):
    return jsonify({"code": 404, "msg": "{}: {}".format('404错误', '在请求的服务器上找不到请求的URL'), "data": None})


if __name__ == '__main__':
    app.run()
