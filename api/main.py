from api import 读取说说

def mian(info):
    if info['type'] == 'load':
        return 读取说说.main(info)
    elif info['type'] == 'send':
        return '发送说说'
    