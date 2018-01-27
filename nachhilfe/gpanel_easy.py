from gpanel import *

makeGPanle(Size(501, 501))
window(0,501, 501, 0)
bm = GBitmap(500, 500)
for x in range(500):
	for y in range(500):
		red = 255
		green = 0
		blue = 0
		bm.setPixelColor(x,y, makeColor(red, green, blue))
image(bm, 0, 500)
