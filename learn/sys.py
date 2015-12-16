# coding=utf-8
import sys

if __name__ == '__main__':
    print "sys.argv 命令行参数List，第一个元素是程序本身路径"
    for i in sys.argv:
        print i
    print '-----------------------------'

    print "sys.modules 返回系统导入的模块字段，key是模块名，value是模块"
    modules=sys.modules
    print modules
    print '-----------------------------'

