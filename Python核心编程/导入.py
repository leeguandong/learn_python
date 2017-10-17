# 版本一
# class Test(object):
#     def __init__(self):
#         self.__num = 100
#
#     def setNum(self, newNum):
#         self.__num = newNum
#
#     def getNum(self):
#         # self.__num = 50
#         return self.__num
#
#     num = property(getNum, setNum)
#
# t = Test()
#
# print('*'*20)
# t.num = 200
# print(t.num)
#
# # 注意点
# # t.num到底是调用getNum()还是setNum(),要根据实际情况的场景来判断
# # 1.如果是给t.num赋值 那么一定调用setNum()
# # 2.如果是获取t.num的值，那么就一定调用getNum()
# # property的作用：相当于把方法进行了封装，开发者在对属性设置数据更方便，用属性掩盖了函数

# # 版本二
# class Test(object):
#     def __init__(self):
#         self.__num = 100
#
#     # 这个property是装饰器，这种写法第一取代了getter函数，第二省了对property函数的申明
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, newNum):
#         self.__num = newNum
#
# t = Test()
# t.num = 250
# print(t.num)

