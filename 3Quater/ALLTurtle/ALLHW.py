import turtle as t

t.speed(10)
#square
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

# draw_Bigsnowflake("FLFRRFLF",2)

def draw_Dragon(str,n):
    if n==0:
        drawOne(str)
        return
    for s in str:
        if s == "X":
            draw_Dragon("XLYFL",n-1)
        if s == "Y":
            draw_Dragon("RFXRY",n-1)
        if s == "F":
            t.forward(1)
        if s == "L":
            t.left(60)
        if s == "R":
            t.right(60)





#draw_Dragon("FX",100)

def draw_ChristmasTree(distance, stick_size, n, m):
        t.right(150)
        t.forward(stick_size)
        t.goto(0,0)
        t.left(120)
        t.forward(stick_size)
        t.goto(0,0)
        t.right(60)
        t.forward(distance)
        apr = m
        for i in range(n-1):
            t.left(60)
            t.forward(stick_size + apr)
            t.left(180)
            t.forward(stick_size + apr)
            t.left(60)
            t.forward(stick_size + apr)
            t.left(180)
            t.forward(stick_size + apr)
            t.right(120)
            t.forward(distance)
            apr += m


draw_ChristmasTree(25, 15, 7,10)
t.done()

