# coding=utf-8
import turtle


# def drawSnake(rad, angle, len, neckrad):
#     for i in range(len):
#         turtle.circle(rad, angle)
#         turtle.circle(-rad, angle)
#     turtle.circle(rad, angle / 2)
#     turtle.fd(rad)
#     turtle.circle(neckrad + 1, 180)
#     turtle.fd(rad * 2 / 3)
#
#
# def main():
#     turtle.setup(1300, 800, 0, 0)
#     pythonsize = 30
#     turtle.pensize(pythonsize)
#     turtle.pencolor('blue')
#     turtle.seth(-40)
#     drawSnake(40, 80, 5, pythonsize / 2)

## 蟒蛇每个部分颜色不一样

def num(len_list, len1, list):
    list_new = list
    if len_list > len1:
        return list
    else:
        len_temp = len1 - len_list
        if len_temp < len_list:
            pass
        else:
            len_times = len_temp // len_list
            list_new = list * (len_times + 1)
            len_temp = len_temp - len_times * len_list

        # for放在最外面不行，第一次控制的len_temp没有更新回来，i还是按照没有更新len_temp之前的数进行循环，会越界！！！
        for i in range(len_temp):
            list_new.append(list[i])
            print(list[i])

        print(list_new)
        return list_new


def drawSnake(rad, angle, len1, neckrad):
    list = ['blue', 'green', 'yellow', 'red']
    len_list = len(list)
    list = num(len_list, len1, list)
    for i in range(len1):
        turtle.pencolor(list[i])
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)

    # 最后一个圈
    turtle.pencolor('green')
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawSnake(40, 80, 15, pythonsize / 2)
    # turtle.getscreen().getcanvas().postscript(file='python.jpg')


if __name__ == '__main__':
    main()
