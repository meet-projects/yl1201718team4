import time
import turtle
counter = 3
score = 0
RUNNING = True
scoreturtle = turtle.clone()
while counter != 0:
    print(counter)
    counter -= 1
    time.sleep(1)

if counter == 0:
	RUNNING = False
	print("GAME OVER")
	turtle.goto(-200,0)
	turtle.color("black")
	turtle.write("GAME OVER", move=False, font=("Arial", 50, "bold"))


turtle.hideturtle()
while RUNNING == True:
	if(coliding_with_basket()==True):
		score+=1
		scoreturtle.clear()
		scoreturtle.write("Your score is: " +str(score), move=False, font=("Arial", 50, "bold"))

