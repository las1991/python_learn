#encoding=utf-8
'''

'''
import os
import shutil

if __name__ == '__main__':
    path='d:/python_fileManagerTest'
    if not os.path.exists(path):
        print 'mkdir :',path
        os.mkdir(path)
    print os.path.exists(path)
    os.rename(path,path+'1')
    print os.path.exists(path),os.path.exists(path+'1')
    os.rename(path+'1',path)
    f=open(path+'/test.txt','w')
    f.close()
    print os.listdir(path)
    print os.stat(path)
    print os.getcwd()
    shutil.rmtree(path)
    print os.path.exists(path)