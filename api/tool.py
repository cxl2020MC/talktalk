import datetime, pytz
def 格式化当前时间():
    # a = datetime.datetime.today()
    # o = datetime.timedelta(hours=8)
    # return (a+o).strftime("%Y/%m/%d %H:%M")
    tz = pytz.timezone('Asia/Shanghai')
    utc_time = datetime.datetime.utcnow()
    格式化时间 = tz.fromutc(utc_time).strftime("%Y/%m/%d %H:%M")
    return 格式化时间

if __name__ == '__main__':
    print(格式化当前时间())