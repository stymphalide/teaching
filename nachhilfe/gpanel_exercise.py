from gpanel import *


def create_panel(width=500, height=500):
	makeGPanel(Size(width + 1, height + 1))
	window(0, width+1, height +1, 0)
	return GBitmap(width, height)

def flag_of_italy(width=600, height=400):
	bm = create_panel(width, height)
	for y in range(height):
		for x in range(int(width/3)):	
			color = makeColor(0, 146, 70)
			bm.setPixelColor(x,y, color) # Green
		for x in range(int(width/3), 2*int(width/3)):
			color = makeColor(241, 242, 241)
			bm.setPixelColor(x,y, color) # White
		for x in xrange(2*int(width/3),width):
			color = makeColor(206, 43, 55)
			bm.setPixelColor(x,y, color) # Red
	image(bm, 0,height)
def flag_of_france(width=600, height=400):
	bm = create_panel(width, height)
	for y in range(height):
		for x in range(int(width/3)): # Paint one third of the width
			color = makeColor(0, 85, 164)
			bm.setPixelColor(x,y, color) # Blue
		for x in xrange(int(width/3), 2*int(width/3)): # Paint the second third
			color = makeColor(255, 255, 255)
			bm.setPixelColor(x,y, color) # White
		for x in range(2*int(width/3),width): # Paint the last third
			color = makeColor(239, 65, 53)
			bm.setPixelColor(x,y, color) # Red
	image(bm, 0,height)
def flag_of_germany(width=500, height=300):
	bm = create_panel(width, height)
	for x in range(width):
		for y in range(int(height/3)): # Go to one third of the height
			color = makeColor(0,0,0)
			bm.setPixelColor(x,y, color) # Black
		for y in range(int(height/3),2*int(height/3)): # Paint the second third of the height
			color = makeColor(255, 0,0)
			bm.setPixelColor(x,y, color) # Red
		for y in range(2*int(height/3),height): #Paint the rest
			color = makeColor(255, 204, 0)
			bm.setPixelColor(x,y, color) # Gold
	image(bm, 0, height)

flag_of_italy()
# flag_of_france()
# flag_of_germany()