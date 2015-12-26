#encoding=utf-8
'''

'''
import glob
import os

if __name__ == '__main__':
    path = 'E:/workspace_inteliJ/python_learn/learn/base/test.txt'
    path ='F:/workspace/python_learn/learn/base/test.txt'
    print(os.path.basename(path))    # 查询路径中包含的文件名
    print(os.path.dirname(path))     # 查询路径中包含的目录
    info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
    print info
    path2 = os.path.join('E:', 'workspace_inteliJ', 'python_learn', 'learn', 'base')  # 使用目录名和文件名构成一个路径字符串
    p_list=[path,path2]
    print os.path.commonprefix(p_list)

    print os.path.normpath(path)

    print os.path.exists(path)

    print os.path.getsize(path)

    print(os.path.getatime(path))  # 查询文件上一次读取的时间

    print(os.path.getmtime(path))  # 查询文件上一次修改的时间

    print(os.path.isfile(path))    # 路径是否指向常规文件

    print os.path.isdir(path)      # 路径是否指向目录文件

    print glob.glob('F:/workspace/python_learn/learn/base/*')