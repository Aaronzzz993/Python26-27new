import turtle
bob=turtle.Turtle()
def polygon(sides, distance):
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def sky(x,y):
    jump(x,y)
    bob.width(1)
    bob.color("lightskyblue")
    polygon(4,1000)

def grass(x,y):
    jump(x,y)
    bob.width(5)
    bob.color("seagreen4")
    polygon(4,1000)

def mountain(x,y):
    jump(x,y)
    bob.color("slategray")
    bob.begin_fill()

    bob.goto(x+100,y+230)
    bob.goto(x+200,y+170)
    bob.goto(x+300,y+245)
    bob.goto(x+400,y+190)
    bob.goto(x+500,y+280)
    bob.goto(x+600,y+175)
    bob.goto(x+700,y+140)
    bob.goto(x+800,y+160)
    bob.goto(x+900,y+135)
    bob.goto(x+1000,y)
    bob.goto(x,y)

    bob.end_fill()

def tree1(x,y):
    jump(x,y)
    bob.color("lightsalmon4")
    bob.begin_fill()
    bob.goto(x+30,y)
    bob.goto(x+30,y+300)
    bob.goto(x,y+300)
    bob.goto(x,y)
    bob.end_fill()

    jump(x-10,y+280)
    bob.color("forestgreen")
    polygon(12,40)


def tree2(x,y):
    jump(x,y)
    bob.color("lightsalmon4")
    bob.begin_fill()
    bob.goto(x+30,y)
    bob.goto(x+30,y+250)
    bob.goto(x,y+250)
    bob.goto(x,y)
    bob.end_fill()

    jump(x-10,y+220)
    bob.color("forestgreen")
    polygon(12,40)






def sun(x,y):
    jump(x,y)
    bob.width(15)
    bob.color("darkgoldenrod1")
    for times in range(8):
        polygon(3,50)
        bob.forward(40)
        bob.right(45)
    jump(x,-90+y)
    polygon(8,40)


def cloud(x,y):
    jump(x,y)
    bob.color("white")

    bob.begin_fill()
    polygon(12,8)

    jump(x+8,y+3)
    polygon(12,10)

    jump(x+18,y+5)
    polygon(12,12)

    jump(x+50,y-2)
    polygon(12,10)

    jump(x+60,y)
    polygon(12,8)
    bob.end_fill()


def house(x,y):
    jump(x,y)
    bob.width(6)
    bob.color("Wheat")
    polygon(4,220)

    jump(x-40,y+220)
    bob.color("SaddleBrown")
    polygon(3,290)

    jump(x+85,y)
    bob.color("Chocolate")
    bob.begin_fill()
    bob.goto(x+135,y)
    bob.goto(x+135,y+100)
    bob.goto(x+85,y+100)
    bob.goto(x+85,y)
    bob.end_fill()

    jump(x+125,y+50)
    bob.dot(8,"Lemonchiffon")

    jump(x+25,y+120)
    bob.color("Lemonchiffon")
    polygon(4,45)

    jump(x+150,y+120)
    bob.color("lightyellow")
    polygon(4,45)


def flower1(x,y):
    jump(x,y)
    bob.color("firebrick1")

    for times in range(8):
        polygon(3,8)
        bob.forward(12)
        bob.left(45)

    jump(x+3,y+7)
    bob.color("yellow")
    polygon(8,6)

def flower2(x,y):
    jump(x,y)
    bob.color("deeppink")

    for times in range(8):
        polygon(3,8)
        bob.forward(12)
        bob.left(45)

    jump(x+3,y+7)
    bob.color("yellow")
    polygon(8,6)

def flower3(x,y):
    jump(x,y)
    bob.color("Hotpink2")

    for times in range(8):
        polygon(3,8)
        bob.forward(12)
        bob.left(45)

    jump(x+3,y+7)
    bob.color("yellow")
    polygon(8,6)

def flower4(x,y):
    jump(x,y)
    bob.color("maroon1")

    for times in range(8):
        polygon(3,8)
        bob.forward(12)
        bob.left(45)

    jump(x+3,y+7)
    bob.color("yellow")
    polygon(8,6)

def flower5(x,y):
    jump(x,y)
    bob.color("Orangered1")

    for times in range(8):
        polygon(3,8)
        bob.forward(12)
        bob.left(45)

    jump(x+3,y+7)
    bob.color("yellow")
    polygon(8,6)

def flower6(x,y):
    jump(x,y)
    bob.color("coral1")

    for times in range(8):
        polygon(3,8)
        bob.forward(12)
        bob.left(45)
    jump(x+3,y+7)
    bob.color("yellow")
    polygon(8,6)
   
def flower7(x,y):
    jump(x,y)
    bob.color("plum1")

    for times in range(8):
        polygon(3,8)
        bob.forward(12)
        bob.left(45)
    jump(x+3,y+7)
    bob.color("yellow")
    polygon(8,6)

def bird(x,y):
    jump(x,y)
    bob.color("black")
    bob.width(5)
    bob.penup()
    bob.goto(-50, 300)
    bob.pendown()
    bob.goto(-65, 315)
    bob.goto(-90, 300)

    bob.penup()
    bob.goto(120, 220)
    bob.pendown()
    bob.goto(135, 235)
    bob.goto(150, 220)    
    bob.penup()
    
    bob.goto(-150, 210)
    bob.pendown()
    bob.goto(-165, 225)
    bob.goto(-190, 210)
    bob.penup()
    bob.goto(500,500)

