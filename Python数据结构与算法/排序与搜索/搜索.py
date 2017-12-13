# 二分法
import time
# 递归版本
def binary_search(alist, item):
    n = len(alist)

    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False

# 非递归版本
def binary_search_2(alist, item):
    n = len(alist)
    first = 0
    last = n - 1

    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == '__main__':
    # li必须是有序表，否则查不出来的
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    start_time = time.time()
    print(binary_search(li, 54))
    print(binary_search(li, 100))
    print('fun1_time: %s' % (time.time() - start_time))
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 100))
    print('fun2_time: %s' % (time.time() - start_time))
