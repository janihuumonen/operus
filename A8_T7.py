import math

MAINMENU = '''Options:
1 - Draw square
2 - Draw circle
3 - Draw hexagon
4 - Save svg
0 - Exit
'''
tag_svg_b = f'<svg width="100" height="100">'
tag_svg_e = '</svg>'

def drawSquare() -> str:
	print("Insert square")
	x = input("- Left edge position: ")
	y = input("- Top edge position: ")
	w = h = input("- Side length: ")
	fill = input("- Fill color: ")
	stroke = input("- Stroke color: ")
	return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" />'

def drawCircle() -> str:
	print("Insert circle")
	cx = input("- Center X coord: ")
	cy = input("- Center Y coord: ")
	r = input("- Radius: ")
	fill = input("- Fill color: ")
	stroke = input("- Stroke color: ")
	return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" />'

def drawHexagon() -> str:
	print("Insert hexagon details:")
	x = float(input("Middle point X: "))
	y = float(input("Middle point Y: "))
	r = float(input("Apothem length: "))
	fi = input("Insert fill: ")
	st = input("Insert stroke: ")

	R = r / math.cos(math.pi/6) # R = circumradius
	a = r * math.tan(math.pi/6) # a = half of side length
	# clockwise starting at top-right of hexagon (0,0 = top-left of canvas)
	pts = [ x+a,y-r, x+R,y, x+a,y+r, x-a,y+r, x-R,y, x-a,y-r ]

	s = ' '.join(map(str,map(round,pts)))
	return f'<polygon points="{s}" fill="{fi}" stroke="{st}" />'

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def writeSVG(fn: str, el: list[str]):
	el = ['  '+e for e in el]
	try:
		with open(fn,'w') as f:
			f.write('\n'.join([tag_svg_b, *el, tag_svg_e]) + '\n')
		return True
	except IOError:
		return False

def save(el):
	fn = input("Insert filename: ")
	print(f'Saving file to "{fn}"')
	yes = 'y' == input("Proceed (y/n)?: ")
	if yes and writeSVG(fn,el):
		print("Vector saved successfully!")
	elif not yes:
		pass
	else:
		print("Vector not saved: IOError")

def main() -> None:
	print("Program starting.")
	elems = []
	ch = -1
	while (ch):
		print(MAINMENU)
		match(ch := askChoice()):
			case 1:
				elems.append(drawSquare())
			case 2:
				elems.append(drawCircle())
			case 3:
				elems.append(drawHexagon())
			case 4:
				save(elems)
			case 0:
				print("Exiting program.")
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()
