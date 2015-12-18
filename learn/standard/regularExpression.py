#encoding=utf-8
'''

'''
import re

if __name__ == '__main__':
    print re.search('[0-9]','abcd4ef').group(0)
    print re.match('[0-9]','abcd4ef')

    m = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
    print m.group("year")


    str = re.sub('[0-9]', '#','abcd4ef')
    print str

    print re.split('[0-9]','abcd4ef')

    print re.findall('[0-9]','1a2b3c4d5e6f')