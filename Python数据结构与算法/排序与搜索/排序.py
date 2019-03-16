# 用顺序表实现的，链表也可以，但是链表要注意指针的连接，顺序表直接复制内存地址
# # 冒泡排序
# def bubble_sort(alist):
#     n = len(alist)
#     for j in range(n - 1):
#         count = 0
#         for i in range(0, n - j - 1):
#             if alist[i] > alist[i + 1]:
#                 alist[i], alist[i + 1] = alist[i + 1], alist[i]
#                 count += 1
#         # 这个列表如果你一步都没有移动，肯定是排好序的
#         # 此处优化能将算法最优复杂度降到O(n)，但是最坏复杂度还是O(n^2)
#         if 0 == count:
#             return
#
# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     bubble_sort(li)
#     print(li)

# # 选择排序
# def select_sort(alist):
#     n = len(alist)
#     for j in range(0, n - 1):
#         index_min = j
#         for i in range(j + 1, n):
#             if alist[i] < alist[index_min]:
#                 index_min = i
#         # 上面只换了下标，下面这行代码换了下标所指的值
#         alist[index_min], alist[j] = alist[j], alist[index_min]
#
# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     select_sort(li)
#     print(li)

# # 插入排序
# # 第一个循环，是外部选择排序数的循环，第二个循环是内部进行排序的循环，这个过程和选择排序刚好相反
# def insert_sort(alist):
#     n = len(alist)
#     for j in range(1, n - 1):
#         i = j
#         # 优化算法，此时如果输入有效数列，则内部排序循环只执行一次，就break了，降低了时间复杂度
#         while i > 0:
#             if alist[i] < alist[i - 1]:
#                 alist[i], alist[i - 1] = alist[i - 1], alist[i]
#                 i -= 1
#             else:
#                 break
#
# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     insert_sort(li)
#     print(li)

# 希尔排序
# def shell_sort(alist):
#     n = len(alist)
#     gap = n // 2
#
#     while gap > 0:
#         # 插入算法，与普通的插入算法的区别就是gap步长
#         for j in range(gap, n):
#             i = j
#             while i > 0:
#                 if alist[i] < alist[i - gap]:
#                     alist[i - gap], alist[i] = alist[i], alist[i - gap]
#                     i -= gap
#                 else:
#                     break
#
#         # 缩短gap步长
#         gap //= 2
#
# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     shell_sort(li)
#     print(li)

# 快速排序
# 有自身递归
def quick_sort(alist, first, last):
    middle_value = alist[first]
    low = first
    high = last

    if first >= last:
        return
    while low < high:
        # low 右移
        while low < high and alist[low] < middle_value:
            low += 1
        alist[high] = alist[low]

        #  high 左移
        # = 是为了处理相同字母的情况，放在上面不行，只能放在这里
        while low < high and alist[high] >= middle_value:
            high -= 1
        alist[low] = alist[high]

    # 第一轮走完之后，选定的值已经归位了，然后再接着往后面走
    alist[low] = middle_value

    # 这个地方为什么这么写而不用切片？
    # 你要注意此时传进来的值依然是一个完整的列表，所以要有起始和终止值，但仍然归于alist，你用切片意味着传进来一个新的列表，这就无法和上述的
    # 快排统一起来
    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low - 1)
    # 对low右边的列表排序
    quick_sort(alist, low + 1, last)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)

# # 归并排序
# def merge_sort(alist):
#     n = len(alist)
#     if n <= 1:
#         # 这个地方一定要有返回值，因为alist是被分解成的单一的元素
#         return alist
#     mid = n // 2
#
#     # left 采用递归排序后形成的新序列
#     left_li = merge_sort(alist[:mid])
#
#     # right 采用递归排序后形成的新序列
#     right_li = merge_sort(alist[mid:])
#
#     # print(left_li,right_li)
#
#     # 将两个子序列合并成一个序列
#     # 左右指针
#     left_pointer, right_pointer = 0, 0
#     result = []
#
#     while left_pointer < len(left_li) and right_pointer < len(right_li):
#         if left_li[left_pointer] <= right_li[right_pointer]:
#             result.append(left_li[left_pointer])
#             left_pointer += 1
#         else:
#             result.append(right_li[right_pointer])
#             right_pointer += 1
#
#     # 此时还有最后一个元素没有加入到列表中，切片是没有越界的，它返回一个空列表
#     result += left_li[left_pointer:]
#     result += right_li[right_pointer:]
#     return result
#
# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     print(li)
#     sort_li = merge_sort(li)
#     print(sort_li)

'''
54, 26, 93, 17, 77, 31, 44, 55, 20
left_li = merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20][:4])                     # 此时并没有进入right_li
                     [54, 26, 93, 17]                                              [77, 31, 44, 55, 20]
left_li = merge_sort([54, 26, 93, 17][:2])                                         # 此时也没有进入right_li
                     [54, 26]                                                      [93,17]
left_li = merge_sort([54, 26][:1])                                                 # 进入right_li = merge_sort([54, 26][1:])
                     [54]                                                          [26]
                                              排序  result = [26,54]
                                                    return result
                                                                                   # 进入上一个函数的right_li = merge_sort([54, 26, 93, 17][2:])
                                                                                   [93, 17]
left_li = merge_sort([93,17][:1])                                                  right_li = merge_sort([93, 17][1:])
                     [93]                                                          [17]
                                              排序  result = [93,17]
                                                    return result

                                              排序  result = [17, 26, 54, 93]
                                                    return result
                                                                                   # 进入上一个函数.......
'''
