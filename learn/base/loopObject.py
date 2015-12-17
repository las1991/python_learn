# encoding=utf-8
'''

'''
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000
if __name__ == '__main__':
    for i in gen():
        print i

    L = []
    for x in range(10):
        L.append(x**2)

    L = [x**2 for x in range(10)]


    xl = [1,3,5]
    yl = [9,12,13]
    L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
    print L