# encoding=utf-8
'''
range()

enumerate()

zip()

'''
import sys

if __name__ == '__main__':
    str='http://www.cnblogs.com/vamei/archive/2012/07/09/2582435.html'
    for i in range(0,len(str),1):
        sys.stdout.write(str[i])

    print
    for (index,char) in enumerate(str):
        print index,char,
    sys.stdout.flush()

    print
    ta = [1,2,3]
    tb = [9,8,7]
    tc = ['a','b','c']
    for (a,b,c) in zip(ta,tb,tc):
        print(a,b,c)

    ta = [1,2,3]
    tb = [9,8,7]

    # cluster
    zipped = zip(ta,tb)
    print(zipped)

    # decompose
    na, nb = zip(*zipped)
    print(na, nb)
