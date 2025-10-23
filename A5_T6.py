MENUSTR = '''\
Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit'''

def showOptions():
	print(MENUSTR)
	return None

def askChoice():
	c = input("Your choice: ")
	c = int(c) if c.isnumeric() else -1
	return c

def main():
	count = 0
	print("Program starting.")
	while True:
		showOptions()
		c = askChoice()
		match c:
			case 1:
				print(f"Current count - {count}")
			case 2:
				print("Count increased!")
				count += 1
			case 3:
				print("Cleared count!")
				count = 0
			case 0:
				print("Exiting program.\n")
				break
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()
