# class Cat:
#     # 属性
#
#     # 当创建完一个对象之后会自动调用的方法，有点像java中的构造函数，在创建对象的时候可以输入属性，方便后面调用
#     def __init__(self, newColor, newWeight, newWeiba):
#         self.color = newColor
#         self.weight = newWeight
#         self.weiba = newWeiba
#         print("--haha--")
#
#     # 方法
#     def eat(self):
#         print("--吃-- ")
#
#     def drink(self):
#         print("--喝--")
#
#     def printInfo(self):
#         # 在函数里面没有weiba这个变量，所以不加self是错误的，想通过对象里面的方法访问属性，则需要加self
#         print(self.weiba)
#
#
# # 调用类中方法
# xiaohuamao = Cat("白色", 5, "有没有")  # 创建了一个对象
# xiaohuamao.eat()  # 调用了类里面的方法
# xiaohuamao.printInfo()
#
# # 给xiaohuama对象添加属性
# xiaohuamao.color = "绿色"
# xiaohuamao.weight = 5  # kg
# xiaohuamao.weiba = '有'
#
# # 获取xiaohuamao对象的属性
# a = xiaohuamao.color
# print(a)-
#
# # 如果没有属性，但偏要访问这属性，则会产生异常信息
# # 这行代码要放在产生属性之后，python属于动态语言，没有动态添加属性即访问时会报错的，所以怎么避免这个问题呢？在_init_中初始化属性
# xiaohuamao.printInfo()


# # 小例子   烤地瓜
# # cookedlevel：0-3生的 3-5半生不熟 5-8烤好了 8以上 考烤成木炭了
# # cookedString：这是字符串，描述地瓜的生熟程度
# # condiments：这是地瓜的配料列表，比如番茄酱、芥末酱等等
# # 面向对象中，在一个类中数据可以在不同函数中调用
# class SweetPotato:
#     # 完成初始化工作
#     def __init__(self):
#         self.cookedString = "生的"
#         self.cookedlevel = 0
#         self.condiments = []
#
#     # 打印对象的一些属性信息
#     def __str__(self):
#         msg = "地瓜的成熟程度：" + self.cookedString
#         msg += " 等级为：" + str(self.cookedlevel)
#         if len(self.condiments) > 0:
#             msg += " 作料为："
#
#             for temp in self.condiments:
#                 msg += temp + "，"
#
#             # 第一种方式去掉最后一个逗号
#             msg = msg[:-1]
#
#             # 第二种方式去掉最好一个逗号
#             # msg=msg.strip(",")
#         else:
#             msg += " 当前没有任何作料"
#         return msg
#
#     def cook(self, times):
#         self.cookedlevel += times
#         if self.cookedlevel > 8:
#             self.cookedString = "焦了"
#         elif self.cookedlevel > 5:
#             self.cookedString = "烤熟了"
#         elif self.cookedlevel > 3:
#             self.cookedString = "半生不熟"
#         else:
#             self.cookedString = "生的"
#
#     # 添加作料
#     def addcondiments(self, zuoniao):
#         self.condiments.append(zuoniao)
#
# digua = SweetPotato()
# print(digua)
#
# digua.cook(10)
# print(digua)
#
# digua.addcondiments("芥末酱")
# print(digua)
#
# digua.addcondiments("老干妈")
# print(digua)

# # 小例子 存放家具
# # 涉及到两个对象，两个对象之间要发生关系
# # 在家对象中创建一个存家具的函数，把床对象存到家中的列表里面，取到家对象，再从家对象中取出其名称
# # 开关功能，在home里面写了开关功能，调用了床对象里面的turnoff函数，home里面是关，则窗对象那边全是off
# class Home:
#     def __init__(self, area):
#         self.area = area
#         self.light = "on"
#         self.containsItem = []
#
#     def __str__(self):
#         msg = "家当前可面积为:" + str(self.area)
#         if len(self.containsItem) > 0:
#             msg += "\n"
#             msg += "家里的物品有："
#
#             for temp in self.containsItem:
#                 msg += temp.getName() + ","
#                 # msg += ",".join(self.containsIttem)
#                 msg = msg[:-1]
#         else:
#             msg += " 没有任何东西"
#
#         if self.light == "on":
#             msg += " 当前灯是亮着的，所有的物品都是可见的"
#         else:
#             msg += " 当前灯是关着的"
#
#         return msg
#
#     def addItem(self, item):
#         # 两次调用浪费时间，不如直接定义一个变量，获取别的类需要等装一个方法，获取自己类的对象的属性不需要在写一个方法
#         needArea = item.getArea()
#         if self.area > needArea:
#             self.containsItem.append(item)
#             self.area -= needArea
#
#     def turnoff(self):
#         self.light = "off"
#         # 修改所有物品的可见度，这里只要一调可见度，所有添加进来的物品全都看不见了
#         for temp in self.containsItem:
#             temp.turnoff()
#
#
# class Bed:
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#         self.light = "on"
#
#     def __str__(self):
#         msg = self.name + " 床的面积为：" + str(self.area) + " 当前的可见度：" + self.light
#         return msg
#
#     def getName(self):
#         return self.name
#
#     def getArea(self):
#         return self.area
#
#     def turnoff(self):
#         self.light = "off"
#
#
# # 创建一个家对象
# home = Home(128)
# print(home)
#
# # 创建一个床对象
# bed = Bed("皖宝床垫", 4)
# print(bed)
#
# # 添加对象的时候要判断条件，只有满足了条件，才往里面添加家具
# home.addItem(bed)
# print(home)
#
# print("========分割========")
# home.turnoff()
# print(bed)

# # 小例子  老王开枪
# # 这个例子很好，老王和敌人属于人类，有枪、子弹、弹夹类，一共四类，，人拿枪，开枪，设，弹夹上子弹，子弹有伤害力，人掉血
# class Ren:
#     def __init__(self, name):
#         self.name = name
#         self.xue = 100
#         self.qiang = None
#
#     def __str__(self):
#         return self.name + "血量剩余为" + str(self.xue)
#
#     # 此时调用了传递过来的对象的方法
#     def anzidan(self, Danjia, zidan):
#         Danjia.Baocunzidan(zidan)
#
#     def andanjia(self, qiang, danjia):
#         qiang.lianjiedanjia(danjia)
#
#     def naqiang(self, qiang):
#         self.qiang = qiang
#
#     def kaiqiang(self, diren):
#         self.qiang.she(diren)
#
#     def diaoxue(self, shanghaili):
#         self.xue -= shanghaili
#
# class Danjia:
#     def __init__(self, rongliang):
#         self.rongliang = rongliang
#         self.rongnaiList = []
#
#     def __str__(self):
#         return "此时弹夹中的子弹数为：" + str(len(self.rongnaiList)) + "/" + str(self.rongliang)
#
#     def Baocunzidan(self, zidan):
#         if len(self.rongnaiList) < 20:
#             self.rongnaiList.append(zidan)
#
#     def chuzidan(self):
#         if len(self.rongnaiList) > 0:
#             # 首先取得最后一个对象，然后把最后一个对象给消除掉
#             zidan = self.rongnaiList[-1]
#             self.rongnaiList.pop()
#             return zidan
#         else:
#             return None
#
# class Zidan:
#     def __init__(self, shanghaili):
#         self.shanghaili = shanghaili
#
#     def shanghai(self, diren):
#         diren.diaoxue(self.shanghaili)
#
# class Qiang:
#     def __init__(self):
#         self.danjia = None
#
#     def __str__(self):
#         if self.danjia:
#             return "枪此时有弹夹"
#         else:
#             return "枪此时没有弹夹"
#
#     def lianjiedanjia(self, danjia):
#         # 一开始设了None，所以此时要让他变成True，才能往里面添加弹夹
#         if not self.danjia:
#             self.danjia = danjia
#
#     def she(self, diren):
#         zidan = self.danjia.chuzidan()
#         if zidan:
#             zidan.shanghai(diren)
#         else:
#             print("没有子弹了，放了空枪")
#
# class Sandan(Qiang):
#     # def she(self, diren):
#     #     i = 0
#     #     while i < 3:
#     #         zidan = self.danjia.chuzidan()
#     #         if zidan:
#     #             zidan.shanghai(diren)
#     #         else:
#     #             print("没有子弹了，放了空枪")
#     #         i += 1
#     def she(self, diren):
#         i = 0
#         while i < 3:
#             # 重写父类的方法还想要调用父类的方法，这手super和java中的super也很类似啊，都是在重写时出现的
#             super().she(diren)
#             i += 1
#
# class AK47(Qiang):
#     pass
#
# class M98K(Qiang):
#     pass
#
# laowang = Ren("老王")
#
# danjia = Danjia(20)
# print(danjia)
#
# i = 0
# while i < 5:
#     zidan = Zidan(5)
#     laowang.anzidan(danjia, zidan)
#     i = i + 1
#
# print(danjia)
#
# qiang = Sandan()
# print(qiang)
# laowang.andanjia(qiang, danjia)
# print(qiang)
#
# diren = Ren("敌人")
# print(diren)
# print(danjia)
# laowang.naqiang(qiang)
# laowang.kaiqiang(diren)
# print(diren)
# print(danjia)

# 实例属性和类属性
# class Test(object):
#     num = 0
#
#     def __init__(self):
#         self.age = 1
#
#     # 修饰器
#     @classmethod
#     def setNum(cls,newNum):
#         cls.num=newNum
#
#     # 静态方法
#     @staticmethod
#     def printTest():
#         print("我是测试用的，没其他什么用的")
#
# a=Test()
# print(Test.num)
#
# # a.setNum(300)
# Test.setNum(300)
#
# print(Test.num)
# Test.printTest()
#
# # 不允许使用类名访问实例属性和实例方法，一定会报异常
# # print(Test.num)
# # print(Test.test())

# 设计一个卖车的4s店
# 要把销售和生产分开，使用简单工厂模式即可,如果生产环节变化了，我们希望销售环节不变，两者之间的耦合度是越小越好的，是一个解耦的过程，相当于
# 在原来生产和销售之间多加了一个类，这个类负责生产各种类型的车
# 对于一个类而言，类的方法越单一越好，越简单越好
# class suolata():
#     pass
#
# class yilante():
#     pass
#
# class CarFactory(object):
#     def createCar(self, typeName):
#         self.typeName = typeName
#         if typeName == "索拉塔":
#             self.car = suolata()
#         elif typeName == "伊兰特":
#             self.car = yilante()
#
#         return self.car
#
# class carstore():
#     def __init__(self):
#         self.carFactory=CarFactory()
#
#     def order(self,typeName):
#         car=self.carFactory.createCar(typeName)

# # 开蛋糕店
# # 使用简单工厂模式
# class AppleCake():
#     def __init__(self, weidao="苹果味道"):
#         self.weidao = weidao
#
# class OrangeCake():
#     def __init__(self, weidao="橘子味道"):
#         self.weidao = weidao
#
# class CakeFactoty():
#     def createcake(self, weidao):
#         if weidao == "橘子":
#             cake = OrangeCake()
#         elif weidao == "苹果":
#             cake = AppleCake()
#         return cake
#
# class Cakestore():
#     def __init__(self):
#         self.cakefactory = CakeFactoty()
#
#     def taste(self, weidao):
#         cake = self.cakefactory.createcake(weidao)
#         print("品尝味道:%s" % cake.weidao)
#
# a=Cakestore()
# a.taste("橘子")

# # 单例模式
# __new__()函数方法
# class Test():
#     # 完成初始化功能，往往是完成属性的初始化
#     def __init__(self,num=200):
#         self.num=num
#
#     # __new__（）完成对象的创建，在__init__()函数之前，__init__()可以自己定义，但是目前水平有限，所以一般继承父类的__new__()方法，完成子类的
#     # 创建，必须要有返回值，在此处返回值便是Test类的对象，也是self所指的值
#     def __new__(cls):
#         print(cls)
#         print("-----new-----")
#         return super().__new__(cls)
#
# a=Test()
# print(a.num)

# # 单例模式例子
# class SingleTon(object):
#     # 类属性
#     __instance = None
#     __first_init = False
#
#     def __new__(cls, age, name):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls);
#         return cls.__instance
#
#     def __init__(self, age, name):
#         if not self.__first_init:
#             self.age = age
#             self.name = name
#             SingleTon.__first_init = True
#
# a = SingleTon(18, "kun")
# b = SingleTon(8, "kunnnn")
# print(a)
# print(b)

# # try catch的应用场景
# import time
# try:
#     f=open('test.txt')
#     while True:
#         content=f.readline()
#         if len(content)==0:
#             break
#         time.sleep(2)
#         print(content)
# finally:
#     # 不管怎么样，你都要把打开的文件关闭掉
#     f.close()
#     print('关闭文件')

# 自定义异常类
class Test(Exception):
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast

try:
    s=input("请输入一个值")
    if len(s)<3:
        raise Test(len(s),3)
except Test as result:
    print("输入数据太短，太%s"%result.length)
















