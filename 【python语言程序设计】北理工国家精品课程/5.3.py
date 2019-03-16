# coding=utf-8
# 广度优先算法
from turtle import Turtle


# p = Turtle()
# p.speed(3)
# p.pensize(5)
# p.color('black', 'yellow')
# p.begin_fill()
# for i in range(5):
#     p.forward(200)
#     p.right(144)
# p.end_fill()

def tree(plist, l, a, f):
    """
    plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level.
    """

    if l > 5:  #
        lst = []
        for p in plist:
            p.forward(
                l)  # 沿着当前的方向画画Move the turtle forward by the specified distance, in the direction the turtle is headed.
            q = p.clone()  # Create and return a clone of the turtle with same position, heading and turtle properties.
            p.left(a)  # Turn turtle left by angle units
            q.right(
                a)  # turn turtle right by angle units, nits are by default degrees, but can be set via the degrees() and radians() functions.
            lst.append(p)  # 将元素增加到列表的最后
            lst.append(q)
        tree(lst, l * f, a, f)


def main():
    p = Turtle()
    p.color('green')
    p.pensize(5)
    p.hideturtle()
    # p.getscreen().tracer(30,0)
    p.speed(10)
    p.left(90)

    p.penup()
    p.goto(0, -200)
    p.pendown()

    t = tree([p], 200, 65, 0.6375)


if __name__ == '__main__':
    main()
