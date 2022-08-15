from api import 读取说说
from api import 发送说说
from api import 编辑说说
from api import 登录

def mian(info, ip):
    if info.get('type') == 'load':
        return 读取说说.main(info)
    elif info.get('type') == 'login':
        return 登录.main(info)
    elif info.get('type') == 'send':
        return 发送说说.main(info, ip)
    elif info.get('type') == 'edit':
        return 编辑说说.main(info)