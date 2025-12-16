import A8_dlib as d

MENU = '''Options:
1 - Calculate amount of timestamps during year
2 - Calculate amount of timestamps during month
3 - Calculate amount of timestamps during weekday
0 - Exit'''

def showOptions() -> None:
	print(MENU)
	return None

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def main() -> None:
	print("Program starting.")
	fn = input("Insert filename: ")
	lst = []
	d.readTimestamps(fn,lst)
	ch = -1
	while (ch):
		showOptions()
		match(ch := askChoice()):
			case 1:
				yr = int(input("Insert year: "))
				print(f"Amount of timestamps during year '{yr}' is {d.calculateYears(yr,lst)}")
			case 2:
				mon = input("Insert month: ")
				print(f"Amount of timestamps during month '{mon}' is {d.calculateMonths(mon,lst)}")
			case 3:
				day = input("Insert weekday: ")
				print(f"Amount of timestamps during weekday '{day}' is {d.calculateWeekdays(day,lst)}")
			case 0:
				print("Exiting program.")
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None
main()
