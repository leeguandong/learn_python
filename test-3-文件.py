# # 小练习：文件的备份
# name = input("请输入要复制的文件名")
#
# # 1. 打开要复制的文件
# f_read = open(name, 'r')
#
# # 2. 创建一个新的文件，用来存储源文件的数据内容
# findposition = name.rfind(".")
# newName = name[:findposition] + "[复制]" + name[findposition:]
# f_write = open(newName, 'w')
#
# # 3. 复制
# # 第一种方式
# # content = f_read.read()
# # f_write.write(content)
# # 第二种方式
# # for lineContent in f_read.readlines():
# #     f_write.write(lineContent)
# # 第三种方式
# while True:
#     lineContent = f_read.readline()
#     if len(lineContent) > 0:
#         f_write.write(lineContent)
#     else:
#         break
#
# # 4. 关闭
# f_read.close()
# f_write.close()

# 批量修改文件名   1.0
# import os
# # 1.获取制定路径下的所有文件名
# allFileName = os.listdir("./test")
# print(allFileName)
# # 2.循环的方式一次重命名
# for name in allFileName:
#     os.rename("./test/" + name, "./test/" + "[东京热出品]" + name)

# # 批量修改文件名   2.0
# import os
# needRenameFile = input("请输入要批量重命名的文件夹")
# # 1.获取制定路径下的所有文件名
# allFileName = os.listdir("./" + needRenameFile)
# print(allFileName)
# # 2.循环的方式一次重命名
# for name in allFileName:
#     os.rename("./" + needRenameFile + "/" + name, "./" + needRenameFile + "/" + "[东京热出品]" + name)

# 学生管理系统的文件版

stuInfos = []


def printmenu():
    print("=" * 30)
    print("  学生管理系统V1.0")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 保存数据 ")
    print("0. 退出系统")
    print("=" * 30)


def getinfo():
    # 尽量不使用全局变量
    # global newPhone
    # global newSex
    # global newName

    newName = input("请输入学生的名字：")
    newSex = input("请输入学生的性别：")
    newPhone = input("请输入学生的手机号：")

    # 使用列表把数据整合到一起，当然元组、字典也可以，因为返回多个值，又不能多次使用return，只能整成一个列表返回。如果
    # 只写return newName，newSex，newPhone返回的是元组
    return [newName, newSex, newPhone]


def addstuinfo():
    result = getinfo()

    newInfos = {}
    newInfos["name"] = result[0]
    newInfos["sex"] = result[1]
    newInfos["phone"] = result[2]

    stuInfos.append(newInfos)


def modifyStuinfo():
    studId = int(input("请输入要修改学生的序号："))
    result = getinfo()

    stuInfos[studId - 1]['name'] = result[0]
    stuInfos[studId - 1]['sex'] = result[1]
    stuInfos[studId - 1]['phone'] = result[2]


def save2file():
    f = open("backup.data", "w")
    f.write(str(stuInfos))
    f.close()


def recoverData():
    global stuInfos
    f = open("backup.data", )
    content = f.read()
    stuInfos = eval(content)
    print(stuInfos)
    f.close()


def main():
    # 恢复之前的数据
    recoverData()
    print(stuInfos)

    while True:
        # 1.打印功能提示
        printmenu()

        # 2.获取功能的选择
        key = input("请输入功能对应的数字：")

        # 3.根据用户的选择，进行相应的操作
        if key == "1":
            addstuinfo()

        elif key == "3":
            modifyStuinfo()

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

        elif key == "6":
            save2file()


main()
