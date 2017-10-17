# # 闭包
# def test(number):
#     print("------1-------")
#
#     def test_in(number2):
#         print("------2------")
#         print(number + number2)
#
#     print('-------3-------')
#     # 注意这里的返回值是test_in,是一个代指变量，不是一个函数，但是其返回值是一个指向函数的变量，当然可以对其进行赋值
#     return test_in
#
# ret = test(100)
# ret(200)

# # 闭包应用 一个有关简单线性函数的调用
# # 这种写法经典在于外部函数体test中的a、b两个值是一直保存的，你只要给内部函数赋值即可。
# def test(a, b):
#     def test_in(x):
#         print(a * x + b)
#     return test_in
#
# line=test(10,1)
# line(0)

# # 装饰器原理
# # 首先调用w1，传入f1，返回了inner变量，这个变量用f1去接，那么f1就指向了inner这个函数，调用了这个函数的时候，里面又调用了
# # f1，也就是说在首先调用了inner函数完成验证之后，再次调用了功能函数f1
# def w1(func):
#     def inner():
#         print('验证权限----')
#         func()
#     return inner
#
# def f1():
#     print('----1-----')
#
# def f2():
#     print('----2----')
#
# f1 = w1(f1)
# f1()

# # 这个版本最大的变化就是使用了装饰器，用w1函数给f1和f2装饰了一下
# def w1(func):
#     def inner():
#         print('验证权限----')
#         func()
#     return inner
#
# @w1
# def f1():
#     print('----1-----')
#
# @w1
# def f2():
#     print('----2----')
#
# f1()
# f2()

# # 装饰器运行顺序问题
# # 以下代码是标准装饰器运行代码，从装饰器角度来讲，首先装饰makeItalic这一层，然后装饰makeBold这一层，运行是从1到3的，可是就装饰而言，
# # 调用makeBold时，下面要接一个函数，所以首先封装makeItalic这一层，给其传入test()做fn，再向上时给makeBold传入下一层已封装好的函数
# # 做fn，所以打出来的结果是<b><i>hello world</i></b>
# def makeBold(fn):
#     def wrapped():
#         print('----1----')
#         return '<b>' + fn() + '</b>'
#     return wrapped
#
# def makeItalic(fn):
#     def wrapped():
#         print('----2----')
#         return '<i>' + fn() + '</i>'
#     return wrapped
#
# @makeBold
# @makeItalic
# def test():
#     print('----3----')
#     return 'hello world'
#
# ret = test()
# print(ret)

# # 通用的装饰器模型
# # 下面算是一个通用的装饰器模型，无论是有返回值还是无返回值的，还是是否传参的，都可以
# def func(functionName):
#     def func_in(*args, **kwargs):
#         print('----显示日志----')
#         ret = functionName(*args, **kwargs)
#         return ret
#     return func_in
#
# @func
# def test():
#     print('--test--')
#     return 'haha'
#
# def test2():
#     print('--test2--')
#
# def test3(a):
#     print('--test3--a=%d' % a)
#
# ret = test()
# print('test return value is %s' % ret)
#
# ret = test2()
# print('test return value is %s' % ret)
#
# ret = test3(3)
# # print('test3 return value is %d' % ret)

# Python动态添加属性和方法
import types
class Person(object):
    def __init__(self, newName, age):
        self.name = newName
        self.age = age

    def eat(self):
        print("---吃---%s" % self.name)

def run(self):
    print("---跑---%s" % self.name)

p = Person('laowang', 18)
p.eat()
p.run = types.MethodType(run, p)
p.run()
