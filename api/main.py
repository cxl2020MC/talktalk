from api import 读取说说
from api import 发送说说

def mian(info, ip):
    if info['type'] == 'load':
        return 读取说说.main(info)
    elif info['type'] == 'send':
        return 发送说说.main(info, ip)
    