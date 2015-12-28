#encoding=utf-8
'''

'''
import subprocess

import signal

if __name__ == '__main__':
    rc = subprocess.call(["ping", "-c", "1", "www.baidu.com"])
    print "rc:",rc

    out = subprocess.call("dir", shell=True)
    print "out:",out

    child=subprocess.Popen(["ping", "-c", "10", "www.baidu.com"])
    child.wait()
    print child.poll()           # 检查子进程状态
    #child.send_signal(signal.SIGINT)    # 向子进程发送信号
    print child.pid
    print "parent process"