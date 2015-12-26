#encoding:utf-8
'''
f    = open(name, "r")

line = f.readline()

f.write('abc')

f.close()

'''
if __name__ == '__main__':
    f = open('C:\\Users\\las\Desktop\\jd-gui.cfg', "r")
    content = f.read(1)  # 读取N bytes的数据
    print content
    content = f.readline()  # 读取一行
    print content
    content = f.readlines()  # 读取所有行，储存在列表中，每个元素是一行。
    print content
    f.close()

    dic ={'tom':(12,86),'Lee':(15, 99),'Lucy':(11, 58),'Joseph':(19, 56)}
    f=open("test.txt","w")
    content=""
    for d in dic:
        str=''
        for i in dic[d]:
            str=str+','+i.__str__()
        content+=d+str+"\n"
        f.write(d+str+"\n")
    #f.writelines(content)

    f.close()

    file=open("test.txt","r")

    for line in file:
        print line
