# encoding=utf-8
'''
将东西根据属性归类 ( 将object归为class )

方法是一种属性，表示动作

用继承来说明父类-子类关系。子类自动具有父类的所有属性。

self代表了根据类定义而创建的对象。



建立对一个对象： 对象名 = 类名()

引用对象的属性： object.attribute


通过self调用类属性

__init__(): 在建立对象时自动执行

类属性和对象的性质的区别

'''


class Bird(object):
    def __init__(self):
        self.way_of_reproduction = 'egg'
        self.have_feather = True

    def move(self, dx, dy):
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position


# 鸡
class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True


# 黄鹂
class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False


if __name__ == '__main__':
    summer = Bird()
    print summer.way_of_reproduction, ",", 'after move:', summer.move(5, 8)

    oriole = Oriole()
    print oriole.way_of_move, ',', oriole.possible_in_KFC