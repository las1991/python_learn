# encoding=utf-8
'''

'''
if __name__ == '__main__':
    dic = {'tom':11, 'sam':57,'lily':100}
    for i in dic:
        print dic[i]

    print dic.keys()           # 返回dic所有的键

    print dic.values()         # 返回dic所有的值

    print dic.items(),type(dic.items()),type(dic.items()[0])          # 返回dic所有的元素（键值对）

    print(len(dic))            # 查询词典中的元素总数

    #dic.clear()                # 清空dic，dict变为{}
    #del dic['tom']             # 删除 dic 的‘tom’元素