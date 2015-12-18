#encoding=utf-8
'''

'''
import time

import datetime

if __name__ == '__main__':
    print(time.time())   # wall clock time, unit: second
    print(time.clock())  # processor clock time, unit: second

    print time.gmtime()      # 返回struct_time格式的UTC时间
    print time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
    print time.mktime(time.gmtime())    # 将struct_time格式转换成wall clock time

    print('start')
    time.sleep(0.1)     # sleep for 10 seconds
    print('wake up')

    t=datetime.datetime(2012,9,3,21,30)
    print t

    format= "output-%Y-%m-%d-%H%M%S.txt"
    str= "output-1997-12-23-030000.txt"

    t=datetime.datetime.strptime(str,format)
    print t

    print datetime.datetime.now()
