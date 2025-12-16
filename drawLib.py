from svgwrite import Drawing, Rect, Circle

def drawSquare(d, left, top, sideLength, color, strokeColor) -> None:
	d.add(Rect(left, top, sideLength, sideLength, color, strokeColor))

def drawCircle(d, centerX, centerY, radius, color, stroke)-> None:
	d.add(Circle(centerX, centerY, radius, color, stroke))

def saveSvg(d,fn):
	try:
		with open(fn,'w') as f:
			f.write(str(d))
		return True
	except IOError:
		return False

