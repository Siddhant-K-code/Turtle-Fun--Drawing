import turtle ,time,random,sys
'''
To Everyone who is looking at this, just hit run and it will say the controls, and there are some secret ones too!

AND DONT PRESS E

'''
tabli=0
pos=[90,180,270,360]

#Defines the turtle as gary
gary=turtle.Turtle()
gary.fillcolor('red')
#Sets his speed to 200
gary.speed(2000)
gary.shape('turtle')

#Defines the variable w as the Screen
w=turtle.Screen()

#Sets the background color to black
w.bgcolor('black')

#Sets the turtle's color to white
gary.color('white')
gary.penup()
gary.goto(-300,200)
gary.write("W - go forward",font=('Arial',10,'bold'))
gary.forward(120)
gary.write("S - go backward",font=('Arial',10,'bold'))
gary.forward(120)
gary.write("D - turn right",font=('Arial',10,'bold'))
gary.forward(120)
gary.write("A - turn left",font=('Arial',10,'bold'))
gary.goto(-300,150)
gary.write("1 - Clears the board",font=('Arial',10,'bold'))
gary.forward(150)
gary.write("Z - lifts the turtle's pen",font=('Arial',10,'bold'))
gary.forward(160)
gary.write("X - puts the turtle's pen down",font=('Arial',10,'bold'))
gary.forward(195)
gary.write("C - Make a circle",font=('Arial',10,'bold'))
gary.goto(-300,100)
gary.write("2 - marks the start point to fill in a shape",font=('Arial',10,'bold'))
gary.forward(300)
gary.write("3 - marks the end point to fill a shape",font=('Arial',10,'bold'))
gary.goto(-70,50)
gary.write("0 - Change Color",font=("Arial",10,"bold"))
gary.goto(0,0)
gary.down()
'''------------ONKEY FUNCTIONS---------------'''

#Function  f - forward command
def f():
  gary.speed(100)
  gary.forward(10)
#Function r - turns him right
def r():
  gary.speed(100)
  gary.right(10)
#Function l - turns him left
def l():
  gary.speed(100)
  gary.left(10)
#Function b - moves him backward
def b():
  gary.speed(100)
  gary.backward(10)
#Function ww- makes a semi-circle
semiii=0
def ww():
  global semiii
  semiii+=1
  if semiii ==1:
    print("You found a secret! Press \"Q\" to draw a semi-circle!")
  for i in range(18):
    gary.forward(10)
    gary.left(10)
#Function rt Resets the drawing, returning Mr.gary to the center of the screen 
def rt():
  global tabli
  tabli=0
  gary.reset()
  gary.pensize(1)
  gary.color("white")
  gary.speed(2000)
  gary.penup()
  gary.goto(-300,200)
  gary.write("W - go forward",font=('Arial',10,'bold'))
  gary.forward(120)
  gary.write("S - go backward",font=('Arial',10,'bold'))
  gary.forward(120)
  gary.write("D - turn right",font=('Arial',10,'bold'))
  gary.forward(120)
  gary.write("A - turn left",font=('Arial',10,'bold'))
  gary.goto(-300,150)
  gary.write("1 - Clears the board",font=('Arial',10,'bold'))
  gary.forward(150)
  gary.write("Z - lifts the turtle's pen",font=('Arial',10,'bold'))
  gary.forward(160)
  gary.write("X - puts the turtle's pen down",font=('Arial',10,'bold'))
  gary.forward(195)
  gary.write("C - Make a circle",font=('Arial',10,'bold'))
  gary.goto(-300,100)
  gary.write("2 - marks the start point to fill in a shape",font=('Arial',10,'bold'))
  gary.forward(300)
  gary.write("3 - marks the end point to fill a shape",font=('Arial',10,'bold'))
  gary.goto(-70,50)
  gary.write("0 - Change Color",font=("Arial",10,"bold"))
  gary.goto(0,0)
  gary.down()
#Function rt2()-stops gary from drawing
def rt2():
  gary.penup()
#Function rt3 - allows gary to draw again
def rt3():
  gary.pendown()
# function circle - makes a circle
def circle():
  for i in range(36):
    gary.forward(10)
    gary.right(10)
#function r90 - turns the turtle 90 degress right
therightie=0
def r90():
  global therightie
  therightie+=1
  if therightie==1:
    print("You found a secret! Press \"r\" to turn right 90 degrees!")
  if gary.heading() not in pos:
    gary.setheading(0)
  gary.right(90)
theleftie=0
def l90():
  global theleftie
  theleftie+=1
  if theleftie == 1:
    print("You found a secret! Press \"l\" to turn left 90 degrees!")
  if gary.heading() not in pos:
    gary.setheading(0)
  gary.left(90)
def idc():
  gary.begin_fill()
def idk():
  gary.end_fill()
stuffffff=["red","orange","yellow","green","blue","cyan","purple","pink","white"]
def ocom():
  global ghj
  ghj+=1
  if ghj==10:
    ghj=1
  stufffff=stuffffff[ghj]
  gary.color(stufffff)
varseverywhere=0
def qcom():
  global varseverywhere
  varseverywhere+=1
  if varseverywhere==1:
    print("You found a secret! Press \"9\" to set your color back to normal white!")
  gary.color("white")
idkrun=0
def werno():
  global idkrun
  idkrun+=1
  if idkrun == 1:
    print("You found a secret! Press \"Ctrl/Cmd\" to move backward a large distance")
  gary.up()
  gary.backward(300)
  gary.down()
ALTS=0
def weryes():
  global ALTS
  ALTS+=1
  if ALTS == 1:
    print("You found a secret! Press\"Alt\" to move forward a large distance!")
  gary.up()
  gary.forward(300)
  gary.down()
thingzzadsat=["We have only started.","The REAL battle finally begins.","Maze A Mortis","No u boiiiiiiii","Turtle Power :P","The name of your turtle is Gary!","Your turtle evolved into...\na circle???","Creators, @squidcoder @Muffinlavania","2TC","Made in Repl.it"]
g=0
def werbd():
  global g
  g+=1
  if g==1:
    print("You Have found a secret!(Press M for random text)")
  ret=random.choice(thingzzadsat)
  if ret=="Your turtle evolved into...\na circle???":
    gary.shape("circle")
    fffffff=True
  print("\n\nRandom Text: "+ret)
  if fffffff==True:
    thingzzadsat[6]="Your turtle lived the rest of its life as a circle :("
tyundb=0
def drrrrr():
  global tyundb
  tyundb+=1
  if tyundb==1:
    print("You found a secret! Press \"y\" to change into some shapes!")
  shapes=["arrow","classic","turtle"]
  gary.shape(random.choice(shapes))
tabli1=0
def tablist():
  global tabli1,tabli
  tabli+=1
  tabli1+=1
  if tabli1==1:
    print("You found a secret! Press \"Tab\" to increase your pen size!(1 to reset)")
  gary.pensize(tabli)
def lance():
  while True:
    gary.forward(1000)
    gary.hideturtle()
    print("You died")

#Trying to set his speed......
gary.speed(100)
ghj=0
'''------ONKEY COMMANDS--------'''
w.onkey(f, "w")
w.onkey(r, "d")
w.onkey(l, "a")
w.onkey(b, "s")
w.onkey(f,"Up Arrow")
w.onkey(r, "Right Arrow")
w.onkey(l, "Left Arrow")
w.onkey(b, "Down Arrow")
w.onkey(ww, "q")
w.onkey(circle,"c")
w.onkey(rt,"1")
w.onkey(rt2,"z")
w.onkey(rt3,'x')
w.onkey(r90,'r')
w.onkey(l90,'l')
w.onkey(idc,'2')
w.onkey(idk,'3')
w.onkey(ocom,'0')
w.onkey(qcom,"9")
w.onkey(werno,"CMD")
w.onkey(werno,"CTRL")
w.onkey(weryes,"ALT")
w.onkey(werbd,"m")
w.onkey(drrrrr,"y")
w.onkey(tablist,"TAB")
w.onkey(lance,"e")
#Tells the window to look out for these onkey commands
w.listen()



#Hide the turtle
'''hideturtle()'''

'''TURTLE REFRENCE'''
#https://docs.python.org/3/library/turtle.html





