# encoding=utf-8
'''

'''
import cPickle as pickle


class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'


if __name__ == '__main__':
    summer = Bird()  # construct an object
    picklestring = pickle.dumps(summer)  # serialize object
    print picklestring
    fn = 'a.pkl'
    with open(fn, 'w') as f:  # open file with write-mode
        picklestring = pickle.dump(summer, f)  # serialize and save object
    with open(fn, 'r') as f:
        summer_read = pickle.load(f)   # read file and build object
    print summer_read.way_of_reproduction

