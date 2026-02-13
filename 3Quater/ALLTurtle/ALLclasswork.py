import turtle
import turtle as t

t.speed("fastest")
# for _ in range(4):
#     for _ in range(3):
#         t.left(90)
#         t.forward(100)
#     turtle.left(180)


def draw_ch(r):
    t.penup()
    t.goto(-2*r, 0)
    t.pendown()
    t.left(90)
    t.circle(r)
    t.goto(2*r,0)
    t.left(180)
    t.circle(r)


# draw_ch(50)


def draw_spiral(count, a, r):
    t.penup()
    t.goto(a,0)
    t.pendown()
    t.left(90)
    for _ in range(count):
        t.forward(a+r)
        t.left(90)
        a=a+r

# draw_spiral(15,5,5)
# t.goto(0,0)

def draw_snowman(k,n,r):
    # t.circle(r)
    # t.left(180)
    for i in range(7):
        if(i==0):
            t.left(180)
        t.circle(r)
        t.left(90)
        t.penup()
        t.forward(2*r)
        t.pendown()
        t.right(90)
        r=n*r



# draw_snowman(1488,1488,1488)
def f(x):
    return x*x

def draw_Graph():
    t.penup()
    t.goto(0,0)
    t.pendown()

#draw_Graph()
def drawOne(str):
    for s in str:
        if(s =="F"):
            t.forward(10)
        if(s =="L"):
            t.left(60)
        if(s =="R"):
            t.right(60)

def draw_Kohssnowflake(str, n):
    if(n==0):
        drawOne(str)
        return
    for s in str:
        if(s == "F"):
         draw_Kohssnowflake(str,n-1)
        if (s == "L"):
            t.left(60)
        if (s == "R"):
            t.right(60)



def draw_Bigsnowflake(str,n):
    for i in range(3):
        draw_Kohssnowflake(str,n)
        t.right(120)

draw_Bigsnowflake("FLFRRFLF",2)







t.done()
