import datetime, pytz, requests, os
from flask import session

def 格式化当前时间():
    # a = datetime.datetime.today()
    # o = datetime.timedelta(hours=8)
    # return (a+o).strftime("%Y/%m/%d %H:%M")
    tz = pytz.timezone('Asia/Shanghai')
    utc_time = datetime.datetime.utcnow()
    格式化时间 = tz.fromutc(utc_time).strftime("%Y/%m/%d %H:%M")
    return 格式化时间

def 获取ip地址信息(ip):
    url = "https://api.live.bilibili.com/client/v1/Ip/getInfoNew?ip=" + str(ip)
    try:
        data = requests.get(url).json()
        print('ip信息: {}'.format(data))
    except Exception as e:
        print('ip信息读取失败， 报错信息：{}: {}'.format(e.__class__.__name__, e))
        return
    if data['code'] == 0:
        data = data['data']
        国家 = data['country']
        省 = data['province']
        城市 = data['city']
        运营商 = data['isp']
        return {'country': 国家, 'province': 省, 'city': 城市, 'isp': 运营商}

def 校验是否登录():
    if not session.get('login'):
        print('用户未登录，返回错误信息')
        raise Exception('未登录')
    else:
        密码 = os.getenv('LOGIN_PWD')
        if 密码 == session.get('login'):
            print('用户已登录，返回True')
            return True
        else:
            print('登录密码错误，返回错误信息')
            raise Exception('登录密码错误')
        
if __name__ == '__main__':
    print(获取ip地址信息('42.192.189.61'))
    print(格式化当前时间())