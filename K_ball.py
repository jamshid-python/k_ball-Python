from turtle import Turtle, Screen
oyna = Screen()
oyna.title('Asab Chiqganida')
chiziq = Turtle()
chiziq.color('blue')
chiziq.pensize(4)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(650, 330)
chiziq.down()
chiziq.goto(650, -330)
chiziq.goto(-650, -330)
chiziq.goto(-650, 330)
chiziq.goto(650, 330)

koptok = Turtle()
koptok.shape('circle')
koptok.color('black')
koptok.up()
koptok.goto(0, 0)
koptok.speed(-1)



qadam = 5
qadam2 = 3

while True:
	x, y = koptok.position()

	if x + qadam >=650 or x + qadam <= -650:
		qadam = -qadam
	if y + qadam2 >=330 or y + qadam2 <= -330:
		qadam2 = -qadam2

	koptok.goto(x + qadam, y + qadam2)

oyna.mainloop()