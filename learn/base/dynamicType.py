#encoding=utf-8
'''

'''
def f0(x):
    x=100
    print x

def f1(x):
    x[0] = 100
    print x

if __name__ == '__main__':

    a=1
    f0(a)
    print a

    a = [1,2,3]
    f1(a)
    print a