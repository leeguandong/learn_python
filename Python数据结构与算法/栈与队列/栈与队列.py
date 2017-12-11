# # 实现栈既可以用顺序表，也可以用链表，用什么数据结构，时间复杂度是不同的
# # 用顺序表list来实现栈操作，底层都是封装好得函数
# class Stack(object):
#     def __init__(self):
#         self.__list = []
#
#     def push(self, item):
#         self.__list.append(item)
#
#     def pop(self):
#         return self.__list.pop()
#
#     def peek(self):
#         if self.__list:
#             return self.__list[-1]
#         else:
#             return None
#
#     def is_empty(self):
#         return self.__list == []
#
#     def size(self):
#         return len(self.__list)
#
# if __name__ == '__main__':
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.pop()
#     s.pop()
#     s.pop()

# 队列
class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

# 双端队列
class Deque(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)
