########################################################
# Task A9_T6
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

MAINMENU = '''Options:
1 - Insert line
2 - Save lines
0 - Exit'''

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def saveLines(lines: list[str]):
	fn = input("Insert filename: ") 
	with open(fn,'w',encoding='UTF-8') as f:
		f.writelines(lines)

def main() -> None:
	print("Program starting.")
	lines = []
	ch = -1
	try:
		while (ch):
			print(MAINMENU)
			match(ch := askChoice()):
				case 1:
					lines.append(input("Insert text: "))
				case 2:
					saveLines(lines)
				case 0:
					print("Exiting program.")
				case _:
					print("Unknown option!")
			print()
	except KeyboardInterrupt:
		if len(lines):
			print('Keyboard interrupt and unsaved progress!')
			if 'y' == input("Save before quit(y/n)?: "):
				saveLines(lines)
		else:
			print("Closing suddenly.")
	print("Program ending.")
	return None

if __name__ == "__main__":
    main()
