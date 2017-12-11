class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

class DoubleCycleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
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
        print('')

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        # p要指向node，self.__head向后的指针要指向node，最后node的指针要指向原来self.__head指针指向的地方
        node.next = self.__head
        self.__head = node
        node.next.prev = node

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
            node.prev = cur

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
            while count < pos:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre
            node.prev = pre.prev
            pre.prev = node
            node.prev.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                return
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 最后一个元素单独判断，在循环里面指定不到最后一个元素的值
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    ll = DoubleCycleLinkList()
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
