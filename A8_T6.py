from svgwrite import Drawing
from drawLib import drawSquare, drawCircle, saveSvg

MAINMENU = '''Options:
1 - Draw square
2 - Draw circle
3 - Save svg
0 - Exit
'''

def promptSquare(d) -> str:
	print("Insert square")
	drawSquare(d,
		input("- Left edge position: "),
		input("- Top edge position: "),
		input("- Side length: "),
		input("- Fill color: "),
		input("- Stroke color: ") )

def promptCircle(d) -> str:
	print("Insert circle")
	drawCircle(d,
		input("- Center X coord: "),
		input("- Center Y coord: "),
		input("- Radius: "),
		input("- Fill color: "),
		input("- Stroke color: ") )

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def save(d):
	fn = input("Insert filename: ")
	print(f'Saving file to "{fn}"')
	yes = 'y' == input("Proceed (y/n)?: ")
	if yes and saveSvg(d,fn):
		print("Vector saved successfully!")
	elif not yes:
		pass
	else:
		print("Vector not saved: IOError")

def main() -> None:
	print("Program starting.")
	dwg = Drawing()
	ch = -1
	while (ch):
		print(MAINMENU)
		match(ch := askChoice()):
			case 1:
				promptSquare(dwg)
			case 2:
				promptCircle(dwg)
			case 3:
				save(dwg)
			case 0:
				print("Exiting program.")
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()
