import turtle
import math
tl=turtle.Turtle()
tl.ht()

def lep(rad,kol_lep):
	angle=360/kol_lep
	rad_lep=math.sin(math.pi/kol_lep)*rad
	tl.lt(angle/2-90)
	tl.circle(rad_lep,180)
	tl.lt(angle/2-90)
	
rad=int(input('введите радиус центральной окружности: '))
kol_lep=int(input('введите количество лепестков: '))
tl.lt(-180)
tl.circle(rad)
for _ in range(kol_lep):
	lep(rad,kol_lep)

input()
