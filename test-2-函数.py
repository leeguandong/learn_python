# # 从键盘中取两个数，输入到函数中
# def sum(num1, num2):
#     print(num1 + num2)
#
# a = int(input("请输入一个数："))
# b = int(input('请输入一个数：'))
# sum(a, b)

# # 学生管理系统的函数版
# stuInfos = []
#
# def printmenu():
#     print("=" * 30)
#     print("  学生管理系统V1.0")
#     print("1. 添加学生信息")
#     print("2. 删除学生信息")
#     print("3. 修改学生信息")
#     print("4. 查询学生信息")
#     print("5. 显示所有学生信息")
#     print("0. 退出系统")
#     print("=" * 30)
#
# def getinfo():
#     # 尽量不使用全局变量
#     # global newPhone
#     # global newSex
#     # global newName
#
#     newName = input("请输入学生的名字：")
#     newSex = input("请输入学生的性别：")
#     newPhone = input("请输入学生的手机号：")
#
#     # 使用列表把数据整合到一起，当然元组、字典也可以，因为返回多个值，又不能多次使用return，只能整成一个列表返回。如果
#     # 只写return newName，newSex，newPhone返回的是元组
#     return [newName, newSex, newPhone]
#
# def addstuinfo():
#     result = getinfo()
#
#     newInfos = {}
#     newInfos["name"] = result[0]
#     newInfos["sex"] = result[1]
#     newInfos["phone"] = result[2]
#
#     stuInfos.append(newInfos)
#
# def modifyStuinfo():
#     studId = int(input("请输入要修改学生的序号："))
#     result = getinfo()
#
#     stuInfos[studId - 1]['name'] = result[0]
#     stuInfos[studId - 1]['sex'] = result[1]
#     stuInfos[studId - 1]['phone'] = result[2]
#
# def main():
#     while True:
#         # 1.打印功能提示
#         printmenu()
#
#         # 2.获取功能的选择
#         key = input("请输入功能对应的数字：")
#
#         # 3.根据用户的选择，进行相应的操作
#         if key == "1":
#             addstuinfo()
#
#         elif key == "3":
#             modifyStuinfo()
#
#         elif key == "5":
#             # print(stuInfos)
#             print("=" * 30)
#             print("学生信息如下：")
#             print("=" * 30)
#
#             print("序号       姓名      性别      手机号码")
#             i = 1
#             for tempInfo in stuInfos:
#                 print("%d         %s       %s        %s" % (i, tempInfo['name'], tempInfo['sex'], tempInfo["phone"
#                 ]))
#                 i = i + 1
#
# main()

# 练习：1.写一个函数打印一条横线   2.打印自定义行数的横线
# 这个练习的意义在于要熟练掌握对于函数的调用，别人写好的东西直接拿过来用就行了，不需要重复去写
# def printLine():
#     print("-" * 30)
#
# def printLineNum(n):
#     i = 0
#     while i < n:
#         printLine()
#         i = i + 1
#
# num = int(input("请输入要打印的个数："))
# printLineNum(num)

# 这个例子和之前的那个还是一个道理，就是尽量利用之前写好的，不要乱改之前写好的代码
# # 定义一个函数，完成3个数的求和和平均值
# def sum(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# def average(a, b, c):
#     result = sum(a, b, c)
#     average = result / 3
#     return average
#
#
# result=average(11, 22, 33)
# print(result)
# # num = sum(11, 22, 33)
# # print(num)

# 缺省参数
# def test(a,b):
#     print(a)
#     print(b)
#
# test(b=11,a=22)

# # 不定长参数
# def test(a, b, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# # test(11,22,33,11,55,99,m=55,n=99)
#
# A = [11, 22, 33]
# B = {"AA": 100, "bb": 22}
#
# # 当列表/元组在当做实参传递的时候，如果前面有一个*，表示对其进行解包，输入的时候意思是：[11,22,33]--->11,22,33
# # 当字典当做一个是残进行传递的时候，如果前面有一个**，表示对其解包，输入的时候 意思是：{"aa":100,"bb":200}--->aa=100,bb=200
#
# test(11, 22, *A, **B)

# # 在这个函数中，形参的A、B都是引用，都指向内存中的100或者200的位置，在函数test中，由于数字是不可变类型，所以对a实际上市重新赋值
# # 他的id是变了的
# def test(a,b):
#     print(id(a))
#     a=a+1
#     print(id(a))
#
# A=100
# B=200
#
# print(id(A))
# test(A,B)

# # 下面这个函数三个id都没变，到那时print（A）变成了[11,33,11,33]
# # a=a+a和a+=a是不一样的，a+=a是直接对a进行修改，所以最后打印出来的是[11,33],而且最后的id是变化的
# def test(a, b):
#     print(id(a))
#     a += a
#     # a=a+a
#     print(id(a))
#
# A = [11, 22]
# print(id(A))
# test(A, 33)
# print(A)

# # 阶乘1到100
# i = 1
# n = 1
# while i <= 100:
#     n = n * i
#     i = i + 1
# print(n)
# # 通过递归来实现阶乘，存的数据在内存中以栈的形式存储下来
# def test(num):
#     if num > 1:
#         return num * test(num - 1)
#     else:
#         return 1
# # return用的好，return可以直接就break了
#
# result = test(100)
# print(result)

# # 匿名函数
# def test(a):
#     return a + 1
#
# aa = lambda a: a + 1
#
# print(test(8))
# print(aa(8))
# 匿名函数当做参数使用
def test(a, b, xxx):
    return xxx(a, b)

result = test(11, 22, lambda x, y: x - y)
print(result)

# b = [{"xuhao": 1, "age": 22}, {"xuhao": 5, 'age': 45}, {"xuhao": 12, "age": 67}]
# b.sort(key=lambda x: x["age"])
