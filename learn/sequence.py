# coding=utf-8
if __name__ == '__main__':
    tuple =(2, 1.3, 'love', 5.6, 9, 12, False)
    for i in xrange(tuple.__len__()):
        print tuple[i]

    print tuple,type(tuple)

    list=[2, 1.3, 'love', 5.6, 9, 12, False]
    print list,type(list)

    str="http://www.cnblogs.com/vame"

    print str[:5]             # 从开始到下标4 （下标5的元素 不包括在内）
    print str[2:]             # 从下标2到最后

    # for i in range(0,str.__len__()):
    #     print str[i]