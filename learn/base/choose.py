# encoding=utf-8
'''
if语句之后的冒号

以四个空格的缩进来表示隶属关系, Python中不能随意缩进

if  <条件1>:

    statement

elif <条件2>:

    statement

elif <条件3>：

    statement

else:

    statement
'''
if __name__ == '__main__':
    i  = 5
    if i > 1:
        print 'i bigger than 1'
        print 'good'
        if i > 2:
            print 'i bigger than 2'
            print 'even better'
    else:
        print 'i smaller than 1'