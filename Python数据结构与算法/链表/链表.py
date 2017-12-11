# # 单向链表
# class Node(object):
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#
# class SingleLink(object):
#     def __init__(self, node=None):
#         self.__node = node
#
#     def is_empty(self):
#         # 链表是否为空
#         return self.__node == None
#
#     def length(self):
#         # 链表长度
#         # cur游标，用来移动遍历节点
#         cur = self.__node
#         count = 0
#         while cur != None:
#             count += 1
#             cur = cur.next
#         return count
#
#     def travel(self):
#         # 遍历整个链表
#         cur = self.__node
#         while cur != None:
#             # cur从一开始就是赋予的头结点，而节点本身是有数据区和指针区的
#             print(cur.elem)
#             cur = cur.next
#
#     def add(self, item):
#         # 链表头部添加元素
#         node = Node(item)
#         node.next = self.__node
#         self.__node = node
#
#     def append(self, item):
#         # 链表尾部添加元素
#         node = Node(item)
#         cur = self.__node
#         if self.is_empty():
#             self.__node = node
#         else:
#             while cur.next != None:
#                 cur = cur.next
#             cur.next = node
#
#     def insert(self, pos, item):
#         # 指定位置添加元素
#         if pos <= 0:
#             self.add(item)
#         elif pos > (self.length() - 1):
#             self.append(item)
#         else:
#             pre = self.__node
#             count = 0
#             while count < (pos - 1):
#                 count += 1
#                 pre = pre.next
#             # 当循环退出时，pre指向pos-1
#             node = Node(item)
#             node.next = pre.next
#             pre.next = node
#
#     def remove(self, item):
#         # 删除节点
#         pass
#
#     def search(self, item):
#         # 查找节点是否存在
#         cur = self.__node
#         while cur != None:
#             if item == cur.elem:
#                 return True
#             else:
#                 cur = cur.next
#         return False
#
# # node = Node(100)
# # single_obj = SingleLink()
# # single_obj.travel()
#
# if __name__ == '__main__':
#     ll = SingleLink()
#     print(ll.is_empty())
#     print(ll.length())
#
#     ll.append(1)
#     print(ll.is_empty())
#     print(ll.length())
#
#     ll.append(2)
#     ll.add(8)
#     ll.append(3)
#     ll.travel()
#
#     ll.insert(-1, 9)
#     ll.insert(3, 100)

class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
                # print('死循环？？？？？？？？？？？？？？')  不加break这里形成了一个死循环，不知道为什么？
                # 因为cur = cur.next这一步没执行，始终还是在判断游标与原来元素一致的这种条件
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
