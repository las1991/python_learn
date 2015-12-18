#encoding=utf-8
'''
try:
    ...
except exception1:
    ...
except exception2:
    ...
except:
    ...
else:
    ...
finally:
    ...

流程如下:
try->异常->except->finally

try->无异常->else->finally
'''
if __name__ == '__main__':
    re = iter(range(5))

    try:
        for i in range(100):
            print re.next()
    except StopIteration:
        print 'here is end ',i

    try:
        print 'Lalala'
        raise StopIteration
        print 'Hahaha'
    except StopIteration:
        print 'StopIteration'
    else:
        print 'else'
    finally:
        print 'finally'