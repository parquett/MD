# from turtle import*
# speed(500)
# right(30)
# shape('triangle')
# hideturtle()
#
# def sierpinski(depth):
#     length=depth*pow(2,depth)+9
#     if depth == 0:
#         pd()
#         stamp()
#         pu()
#         return
#     else:
#         pu()
#         for i in range(0, 3):
#             forward(length)
#             sierpinski(depth - 1)
#             backward(length)
#             left(120)
# n=int(input('enter the depth '))
# sierpinski(n)
#
# done()

def sierpinski(n):
    y=n-1
    while(y >= 0):
        i, x = 0, 0
        while(i<y):
            print(" ", end="")
            i=i+1
        while(x+y<n):
            if ((x & y) != 0): print(" ", end=" ")
            else: print("* ", end="")
            x=x+1
        print()
        y=y-1

n=int(input("enter the depth: "))
sierpinski(n)