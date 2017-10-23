# import gc
# class ClassA():
#     def __init__(self):
#         print('object born,id:%s'%str(hex(id(self))))
#
# def f2():
#     # 循环调用
#     while True:
#         c1=ClassA()
#         c2=ClassA()
#         c1.t=c2
#         c2.t=c1
#         del c1
#         del c2
#
# # 把垃圾回收机制关了
# gc.disable()
# f2()

# class Itcast(object):
#     def __init__(self, subject1):
#         self.subject1 = subject1
#         self.subject2 = 'cpp'
#
#     # 属性访问时拦截器，可以打log日志
#     def __getattribute__(self, obj):
#         # 当你访问subject1这个属性时，可以记录你的访问信息
#         if obj == 'subject1':
#             print('log subject1')
#             return 'redirect python'
#         else:
#             # 如果没有访问，就直接调用父类的方法，原来怎么用，现在还是怎么用
#             temp=object.__getattribute__(self, obj)
#             print(temp)
#             # 这里有返回值，调用show()函数就不会崩
#             return temp
#
#     def show(self):
#         print('this is Itcast')
#
# s = Itcast('python')
# # 只要你一调用对象的属性，就会触发__getattribute__方法
# print(s.subject1)
# print(s.subject2)
#
# # 1.先获取show()属性对应的结果，应该是一个方法
# # 2.方法()
# # 函数这个方法指向show这个变量所创建的一片内存
# s.show()

# # 内建属性调用的内部循环调用
# class Preson(object):
#      def __getattribute__(self, obj):
#          print('---test---')
#          if obj.startwith('a'):
#              return 'haha'
#          else:
#              # 这一步会直接让程序挂掉，因为在程序内部调用self.test，其实就是调用t.test，会继续在__getattribute__里面找是否有这个属性，
#              # 从而产生递归调用，最终内存耗尽，程序崩溃，不要自己程序内部再次调用self.方法，容易是程序出现问题
#              return self.test
#
#      def test(self):
#          print('heihei')
#
# t=Preson()
# t.a
# t.b

# wrapper()方法
import functools

def note(func):
    'note function'
    @functools.wraps(func)
    def wrapper():
        'wrapper function'
        print('note something')
        return func()
    return wrapper

@note
def test():
    'test function'
    print('i am test')

print(help(test))
