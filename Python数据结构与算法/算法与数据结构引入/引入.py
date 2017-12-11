# 面试题
# 如果a+b+c = 1000，且2^2+b^2=c^2(a、b、c为自然数)，如何求生所有的a、b、c可能的组合？
# 思路 枚举法
# import time
#
# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print('a,b,c:%d,%d,%d' % (a, b, c))
# end_time = time.time()
# print('finisned')

# T = 1000*1000*1000*2
# T = N*N*N*2
# T和解决问题的规模有关系
# T(n) = n^3 * 2

# # 上述代码改进
# import time
#
# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000 - a - b
#         if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#             print('a,b,c:%d,%d,%d' % (a, b, c))
# end_time = time.time()
# print('finisned：time %d' % (end_time - start_time))

# 测试代码
# append和expand的区别在于，后者可以添加列表，而前者只能添加元素
from timeit import Timer

def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        li = li + [i]

# 列表生成器
def t3():
    li = [i for i in range(10000)]

def t4():
    li = list(range(10000))

def t5():
    li = []
    for i in range(10000):
        li.extend([i])

timer1 = Timer('t1()', 'from __main__ import t1')
print('append:', timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("+:", timer2.timeit(1000))

timer3 = Timer("t3()", "from __main__ import t3")
print("[i for i in range]:", timer3.timeit(1000))

timer4 = Timer("t4()", "from __main__ import t4")
print("list(range()):", timer4.timeit(1000))

timer5 = Timer("t5()", "from __main__ import t5")
print("extend:", timer5.timeit(1000))

# append: 0.8710457548613924
# +: 144.70819558154002
# [i for i in range]: 0.37937327789683195
# list(range()): 0.20041992158567723
# extend: 1.468430231983973