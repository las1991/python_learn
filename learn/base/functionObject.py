# encoding=utf-8
'''

'''
def test(f, a, b):
    print 'test'
    print f(a, b)

def filter_func(a):
    if a > 100:
        return True
    else:
        return False

if __name__ == '__main__':
    func = lambda x,y: x + y
    print func(3,4)

    test(func, 3, 5)

    test((lambda x,y: x**2 + y), 6, 9)

    re = map((lambda x: x+3),[1,3,5,6])
    print re


    print  filter(filter_func,[10,56,101,500])

    print reduce((lambda x,y: x+y),[1,2,5,7,9])  #(((1+2)+5)+7)+9