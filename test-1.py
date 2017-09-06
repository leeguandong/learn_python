# # coding=utf-8
# print("你好")

# name = 'dongge'
# print(name)
# # python定义变量时自己知道是什么类别,不需要定义
# print(type(name))

# # \n换行  \t是tab
# print('名称：\ndongge')
# print('名称：\t东哥')

# print("aaaaa", end='=')
# print("bbbbb")

# # input
# userName = input('请输入用户名')
# print("您刚刚输入的名字是%s" % userName)
# userName是一个字符串，不是整形。

# name = input("姓名")
# qq = input("QQ")
# phoneNum = input("手机号")
# address = input("公司地址")

# print("姓名" + name + "\nQQ" + qq + "\n手机号" + phoneNum + "\n公司地址" + address)

# 编写程序，从键盘获取用户名和密码，然后判断，如果正确就输出一下信息
# userName = input("请输入用户名：")
# passWord = input("请输入密码：")
#
# if userName=="dong" and passWord=="123":
#     print("登陆成功！！！")

# 白富美例子  too simple

# 剪刀石头布
# 2.让电脑产生一个数字
# import random
#
# while True:
#     computer = random.randint(0, 2)
#     # print("computer----%d" % computer)
#
#     # 1.提示用户并获取一个数字
#     player = int(input("请选择 0剪刀 1石头 2布  "))
#
#     # 3.判断输赢，并显示相应结果
#     if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#         print("赢了")
#     elif player == computer:
#         print("平局")
#     else:
#         print("输了")

# while True:
#     print("6666")

# i=1
# while i<1000:
#     print("重复执行1000次")
#     i+=1

# 1-100之间的偶数
# i = 2
# while i <= 100:
#     print(i)
#     i = i + 2

# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

# 1-100的累积和
# i = 1
# resultnum = 0
# while i <= 100:
#     if i % 2 == 0:
#         resultnum += i
#     i = i + 1
# print(resultnum)

# *
# **
# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1

# i = 1
# while i <= 5:
#     j = 0
#     while j < i:
#         print("* ", end="")
#         j = j + 1
#     print("")  # print默认换行
#     i = i + 1


# 99乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         k = i * j
#         print("%d*%d=%-2d " % (j, i, k),end="") # %2d是预留两个空可以对齐，%-2的还是占两位，向左对齐。
#         j = j + 1
#     print("")
#     i = i + 1

# i=0
# while i<0:
#     i=i+1
#     print()

# name = "qweryhh"
# for temp in name:  # 每次循环从name中取一个，temp是一个临时变量
#     print(temp)
#
# i = 0
# while i < 5:
#     print(name[i])  # 从字符串中取数据，下标
#     i = i + 1

# 面试题  给定一个字符串astr，返回使用空格或者\t分割后的倒数第二个子串
# astr = "python and leeguandong  666"
# astr.split()
#
# # 列表
# infos = [100, "xiaohong", 3.14]
# for temp in infos:
#     print(temp)
#
# i = 0
# while i < len(infos):
#     print(infos[i])
#     i = i + 1

# # 有一个花名册，判断我输入的名字在不在里面
# names = ["思聪", "老王", "李冠东", "马云", '比尔盖茨']
#
# name = input("请输入你的名字")
#
# for temp in names:
#     if temp == name:
#         print("你的名字是%s" % temp)
#     else:
#         print("没有找到")
#         names.append(name)
#     break
# print(names)

import random

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机分配
# 你这个问题在放到办公室的列表没搞清楚，还有不知道怎么放进去
# teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
# room = [[], [], []]
#
# i = 0
# while i < 8:
#     num = random.randint(0, 7)
#     print(num)
#     room.insert(1, teachers[num])
#     i = i + 1
# print(room)

# # 1.定义一个列表，嵌套的列表
# rooms = [[], [], []]
#
# # 2.有一个列表，保存了8名老师的名字
# teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
#
# # 3.随机把8名老师的名字添加到第一个列表中
# for name in teachers:
#     randomNum = random.randint(0, 2)
#     rooms[randomNum].append(name)
# # print(rooms)
#
# for room in rooms:
#     print("办公室%d的人有：" % int(rooms.index(room) + 1))
#     for name in room:
#         print(name, end=" ")
#     print("")

# 小项目   学生信息管理系统
# 需要完成基本功能：1.添加名片 2.删除名片 3.修改名片 4.查询名片 5.退出系统
# 程序运行后，除非选择退出系统，否则重复执行功能
stuInfos = []
while True:
    # 1.打印功能提示
    print("=" * 30)
    print("  学生管理系统V1.0")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("0. 退出系统")
    print("=" * 30)

    # 2.获取功能的选择
    key = input("请输入功能对应的数字：")

    # 3.根据用户的选择，进行相应的操作
    if key == "1":
        newName = input("请输入学生的名字：")
        newSex = input("请输入学生的性别：")
        newPhone = input("请输入学生的手机号：")

        newInfos = {}
        newInfos["name"] = newName
        newInfos["sex"] = newSex
        newInfos["phone"] = newPhone

        stuInfos.append(newInfos)

    elif key == "3":
        studId = int(input("请输入要修改学生的序号："))
        newName = input("请输入学生的名字：")
        newSex = input("请输入学生的性别：")
        newPhone = input("请输入学生的手机号：")

        stuInfos[studId - 1]['name'] = newName
        stuInfos[studId - 1]['sex'] = newSex
        stuInfos[studId - 1]['phone'] = newPhone

    elif key == "5":
        # print(stuInfos)
        print("=" * 30)
        print("学生信息如下：")
        print("=" * 30)

        print("序号       姓名      性别      手机号码")
        i = 1
        for tempInfo in stuInfos:
            print("%d         %s       %s        %s" % (i, tempInfo['name'], tempInfo['sex'], tempInfo["phone"
            ]))
            i = i + 1
