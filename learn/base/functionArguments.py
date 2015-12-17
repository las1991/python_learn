# encoding=utf-8
'''
先位置，再关键字，再包裹位置，再包裹关键字
'''

#参数默认值
def add(a,b,c=10):
    return a+b+c

#包裹位置传递
def func(*name):
    print type(name)
    print name
#包裹关键字传递
def func1(**dict):
    print type(dict)
    print dict
#解包裹(unpacking)
def func2(a,b,c):
    print a,b,c

if __name__ == '__main__':
    func(1,2,3)
    func([1,2,3])
    func({1:1,2:2,3:3})
    print add(1,2)
    print add(1,2,3)

    func1(a=1,b=9)
    args = (1,2,3)
    func2(*args)
    dict = {'a':1,'b':2,'c':3}
    func2(**dict)