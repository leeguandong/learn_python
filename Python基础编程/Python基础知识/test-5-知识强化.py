# # 这是一个替换的方法，从字符串中替换掉一个或者多个字符
# # 方法一：
# pstr = 'hello world'
#
# def myReplace(pstr, oldStr, newStr):
#     result = pstr.split(oldStr)
#     return newStr.join(result)
#
# a = myReplace(pstr, 'world', 'Tom')
# print(a)
#
# # 方法二：
# # 提供的是一种思路，对于类似问题如何解决，首先先找到你要替换的字符的位置，然后把你要替换的为东西加进去，接着把后面的字串在接上，其次保存到同名的
# # 变量中，方便循环调用
# pstr = "hello world"
#
# def myReplace(pstr, oldStr, newStr):
#     while True:
#         if position==-1:
#             break
#         position = pstr.find(oldStr)
#         pstr = pstr[:position] + newStr + pstr[position + len(oldStr):]
#     return pstr
#
# a = myReplace(pstr, "world", "tom")
# print(a)

# # 第八题
# def extendlist(a, b=[], c={}):
#     b.append(a)
#     c[a] = a
#     return b, c
#
# list1 = extendlist(10)
# list2 = extendlist(123, ['a', 'b', 'c'])
# list3 = extendlist('a')
#
# print(list1)
# print(list2)
# print(list3)
#
# # 这一题的结果如下，是不是很吃惊，b=[]作为一个可变的缺省参数，b列表只初始化一次，当你输入10的时候，
# # 返回的b是一个指向b内存的地址，而再次输入'a'的时候，b列表此时已经存了10了，所以返回来是两个值，此题是面试题，极好。
# # [10, 'a']
# # ['a', 'b', 'c', 123]
# # [10, 'a']

# 第五题
import random
def test(n):
    newList=[]
    while True:
        if len(newList)==10:
            break

        num=random.randint(1,n)
        if num not in newList:
            newList.append(num)

    return newList

result=test(10)
print(result)
