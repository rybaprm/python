import turtle
import math

if __name__ == "__main__":
	what_input_settings = (
		'введите радиус центральной окружности: ',
		'введите количество лепестков: '
		)
		
	tl = turtle.Turtle()
	tl.ht()

	def draw_leaves(radiusius,quantity_of_leaves):
		angle = 360/quantity_of_leaves
		radius_lep = math.sin(math.pi/quantity_of_leaves)*radius
		tl.lt(angle/2-90)
		tl.circle(radius_lep,180)
		tl.lt(angle/2-90)
		
	radius = int(input(what_input_settings[0]))
	quantity_of_leaves = int(input(what_input_settings[1]))
	tl.lt(-180)
	tl.circle(radius)
	
	for _ in range(quantity_of_leaves):
		draw_leaves(radius,quantity_of_leaves)

	input()
