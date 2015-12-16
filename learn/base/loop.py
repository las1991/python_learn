# encoding=utf-8
'''
range()

for 元素 in 序列:

while 条件:

continue

break
'''
if __name__ == '__main__':
    for i in range(0,100):
        if i==50:
            print i
        elif i==99 :
            print "now break"
            break
        else:
            continue

    i=0
    while i<100:
        i=i+1
        if i==51:
            print i
        elif i==99 :
            print "now break"
            break
        else:
            continue