MENU = '''Options:
1 - Read values
2 - Amount of values
3 - Calculate sum of values
4 - Calculate average of values
0 - Exit'''

def showOptions() -> None:
	print(MENU)
	return None

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def readValues(fn: str) -> list[float]:
	lst = []
	with open(fn) as f:
		for line in f.readlines():
			line = line.strip()
			if len(line): lst.append(float(line))
	return lst

def main() -> None:
	print("Program starting.")
	lst = []
	ch = -1
	while (ch):
		showOptions()
		match(ch := askChoice()):
			case 1:
				fn = input("Insert filename: ")
				lst = readValues(fn)
			case 2:
				print(f"Amount of values {len(lst)}")
			case 3:
				print(f"Sum of values {sum(lst):.1f}")
			case 4:
				l = len(lst) or 1
				print(f"Average of values {sum(lst)/l:.1f}")
			case 0:
				print("Exiting program.")
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()
