MENUSTR = '''\
Options:
1 - Insert word
2 - Show current word
3 - Show current word in reverse
0 - Exit'''

def showOptions():
	print(MENUSTR)
	return None

def askChoice():
	c = input("Your choice: ")
	c = int(c) if c.isnumeric() else -1
	return c

def main():
	word = ''
	print("Program starting.")
	while True:
		showOptions()
		c = askChoice()
		match c:
			case 1:
				word = input("Insert word: ")
			case 2:
				print(f'Current word - "{word}"')
			case 3:
				print(f'Word reversed - "{word[::-1]}"')
			case 0:
				print("Exiting program.\n")
				break
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()
