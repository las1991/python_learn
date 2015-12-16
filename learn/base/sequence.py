# coding=utf-8

'''
tuple元素不可变，list元素可变

序列的引用 s[2], s[1:8:2]

字符串是一种tuple
'''

if __name__ == '__main__':
    tuple =(2, 1.3, 'love', 5.6, 9, 12, False)
    for i in xrange(tuple.__len__()):
        print tuple[i]

    print tuple,type(tuple)

    list=[2, 1.3, 'love', 5.6, 9, 12, False]
    print list,type(list)

    #字符串是一种特殊的元素，因此可以执行元组的相关操作。
    str="http://www.cnblogs.com/vame"


    #范围引用： 基本样式[下限:上限:步长]
    print str[:5]             # 从开始到下标4 （下标5的元素 不包括在内）
    print str[2:]             # 从下标2到最后
    print str[0:5:2]          # 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）
    print str[2:0:-1]         # 从下标2到下标1

    print str[-1]             # 序列最后一个元素
    print str[-3]             # 序列倒数第三个元素

    # for i in range(0,str.__len__()):
    #     print str[i]