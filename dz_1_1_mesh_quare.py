import turtle
import math
tl=turtle.Turtle()
tl.ht()
tl.speed(10000) 

def dr_sq(dist):
	for _ in range(4):
		tl.fd(dist)
		tl.left(90)

def dr_mesh(dist,n):
	for i in range(n):
		if (i+1)==n and int(tl.heading())==180:
			break
		tl.up()
		tl.fd(dist/n)
		tl.left(135)
		tl.down()
		tl.fd((i+1)*dist/n/math.cos(math.pi/4))
		tl.up()
		tl.bk((i+1)*dist/n/math.cos(math.pi/4))
		tl.left(-135)
	
dist=int(input('Введите длинну сторны квадрата: '))
dr_sq(dist)
mesh=int(input('Введите нечетное количество наклонных линий для штриховки: '))
if (mesh%2)!=0:
	dr_mesh(dist,mesh)
	tl.goto(dist,dist)
	tl.left(180)
	dr_mesh(dist,mesh)
else:
	print('Вы ввели четное количество наклонных линий для штриховки, штриховать не будем')

input()


