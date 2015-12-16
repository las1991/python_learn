# encoding=utf-8
'''
def function_name(a,b,c):
    statement
    return something  # return不是必须的

函数的目的： 提高程序的重复可用性。

return     None

通过位置，传递参数。

基本数据类型的参数：值传递

表作为参数：指针传递

'''
def square_sum(a,b):
    return a**2-b**2;

if __name__ == '__main__':
    print square_sum(3,4)
    print square_sum(b=4,a=3)