import A8_mlib as m

MENU = '''Options:
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
0 - Exit'''

def showOptions() -> None:
	print(MENU)
	return None

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def askValue(PPrompt: str) -> float:
	return float(input(PPrompt + ": "))

def main() -> None:
	print("Program starting.")
	ch = -1
	while (ch):
		showOptions()
		match(ch := askChoice()):
			case 1:
				a = askValue("Insert first addend value")
				b = askValue("Insert second addend value")
				r = m.add(a,b)
				print(f"{a} + {b} = {r}")
			case 2:
				a = askValue("Insert minuend value")
				b = askValue("Insert subtrahend value")
				r = m.subtract(a,b)
				print(f"{a} - {b} = {r}")
			case 3:
				a = askValue("Insert multiplicand value")
				b = askValue("Insert multiplier value")
				r = m.multiply(a,b)
				print(f"{a} * {b} = {r}")
			case 4:
				a = askValue("Insert dividend value")
				b = askValue("Insert divisor value")
				r = m.divide(a,b)
				print(f"{a} / {b} = {r}")
			case 0:
				print("Exiting program.")
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()
