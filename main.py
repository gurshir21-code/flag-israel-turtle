import turtle

def pasim(m = 90, x = 80):
  for i in range(2):
    t.left(m)
    t.forward(x + 440)
    t.left(m)
    t.forward(x)

def meshulash(m = 120, x = 220):
  for i in range(3):
    t.left(m)
    t.forward(x)
    
t = turtle.Turtle()
t.speed(5)
t.penup()

t.goto(260, 290)
t.color("blue")
t.left(90)
t.pendown()
t.begin_fill()
pasim()
t.end_fill()

t.penup()

t.goto(260, -210)
t.pendown()
t.begin_fill()
pasim()
t.end_fill()
t.penup()

t.pensize(10)
t.goto(0, 120)
t.pendown()
t.left(30)
meshulash()
t.penup()

t.goto(0, -130)
t.pendown()
t.left(180)
meshulash()
