from turtle import *
import time
import turtle
import turtle

turtle.setup( width = 800, height = 550, startx = None, starty = None)

turtle.bgcolor("blue")
counter = 6000
score = 0
RUNNING = True
scoreturtle = turtle.clone()
turtle.hideturtle()
turtle.pu()
turtle.goto(-390,240)
stamplist1 = []
scoreturtle.pu()
scoreturtle.hideturtle()
scoreturtle.goto(150,230)
turtle.addshape("goodbasket.gif")
turtle.addshape("player1.gif")
thrown=False
intro = turtle.clone()
turtle,ht()
intro.ht()
intro.pu()
intro.goto(-220,150)
intro.write('Instructions:',move=True ,align='left' , font=('Arial',55,'normal'))
intro.goto(-320,70)
intro.write('Get ready to play a basketball shooting game .',move=True, font=('Arial',17,'normal'))
intro.goto(-320,20)
intro.write('you are the player, move the arrows to adjust your shooting position.',move=True,font=('Arial',16,'normal'))
intro.goto(-320,-30)
intro.write('press the spacebar to shoot your ball.',move=True,font=('Arial',17,'normal'))
intro.goto(-320,-80)
intro.write('you have 60 seconds to score as many baskets as possible.',move=True,font=('Arial',17,'normal'))
intro.goto(-220,-180)
intro.write('HAVE FUN!!!',move=True,font=('Arial',55,'normal'))
time.sleep(1)
intro.clear()
pu()
goto(0,0)
write('3',move=True,align='center',font=('Arial',70,'normal'))
time.sleep(1)
clear()
pu()
write('2',move=True,align='center',font=('Arial',70,'normal'))
time.sleep(1)
clear()
pu()
write('1',move=True,align='center',font=('Arial',70,'normal'))
clear()
time.sleep(1)
turtle.bgpic("court2.gif")

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)
	def tside(self):
		tside = self.y+(self.r/2)
		return tside
	def bside(self):
		bside = self.ycor()-(self.r/2)
		return bside
	def lside(self):
		lside = self.xcor()-(self.r/2)
		return lside
	def rside(self):
		rside = self.x+(self.r/2)
		return rside
	# def move(self,width,height):
	# 	curentx=self.xcor()
	# 	new_x=curentx+self.dx
	# 	curenty=self.ycor()
	# 	new_y=curenty+self.dy
	# 	right_side_ball=new_x + self.r
	# 	left_side_ball=new_x -self.r
	# 	top_side_ball=new_y + self.r
	# 	bottom_side_ball = new_y - self.r
	# 	self.goto(new_x,new_y)


class Rectangle(Turtle):
	def __init__(self,width,height,x,y, color):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.color(color)
		self.height = height
		self.width = width
		self.shape("goodbasket.gif")
		# register_shape("myRectangle", ((0,0), (width,0), (width,height), (0,height)))
		# self.shape("myRectangle")
		self.goto(x,y)
def coliding_with_basket(ball,basket):
	if (ball.bside())<=(basket.ycor()+(basket.height/2)):
		# return("smaller - b side of the ball: " + str(ball.bside()) + "basket coiding point: " + str(basket.height/2))
		# return(" bigger - l side of the ball: " + str(ball.lside()) + "basket coiding point: " + str(basket.width/2))
		if ((ball.lside())>=(basket.xcor()-(basket.width/2))):
			return True
		else:
			return False
	else:
		return False
class player(Turtle):
	def __init__(self,x,y,dx,dy):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.shape("player1.gif")
		self.dx = dx
		self.dy = dy
	def getx(self):
		cx = self.xcor()
		return cx

basket1 = Rectangle(20,200, 320,100, "black")
player1 = player(0,-50,5,5)
ball1 = Ball(0,0,5,5,20, "orange")



def move_left(): 
	x=player1.getx()-player1.dx
 	y=player1.y
 	player1.goto(x,y)

def move_right(): 
 	x=player1.getx()+player1.dx
 	y=player1.y
 	player1.goto(x,y)

def spaceBar():
	global thrown
	thrown = True
	print(str(ball1.ycor()))
	if (ball1.ycor()<170):
		print("staff")
	elif(ball1.ycor()>10 and ball1.dy > 0):
		ball1.dy = -ball1.dy
	nx = ball1.xcor()+ball1.dx
	ny = ball1.ycor()+ball1.dy
	ball1.goto(nx,ny)
	if coliding_with_basket(ball1,basket1)==True:
 		ball1.penup()
 		score+=1
 		ball1.goto(player1.xcor()+15,player1.ycor()+15)





 	
tracer(0)
hideturtle()



# getcanvas().bind("<KeyPressed-Space>", power)
# getcanvas().bind("<KeyReleased-Space>", throw)
# listen()

while counter != 0:
	print(coliding_with_basket(ball1,basket1))
	goto(-340,230)
	stamp2 = turtle.write("time left: " +  str(counter/100), move=False, font=("Arial", 20, "bold"))
	stamplist1.append(stamp2)
	if thrown==False:
		ball1.goto(player1.getx()+25,-25)
	onkey(spaceBar, "space")
	onkey(move_left, "Left")
	onkey(move_right, "Right")
	listen()

	counter -= 1
	# time.sleep(1)
	clearstamp(stamp2)
	clear()
	if (coliding_with_basket(ball1,basket1)==True):
		score+=1
	scoreturtle.clear()
	scoreturtle.write("Your score is: " +str(score), move=False, font=("Arial", 20, "bold"))
	clear()
	if counter == 0:
		RUNNING = False
		print("GAME OVER")
		goto(-200,0)
		color("black")
		scoreturtle.goto(-200,0)
		write("GAME OVER, your score was: " + str(score), move=False, font=("Arial", 20, "bold"))
	update()

mainloop()
