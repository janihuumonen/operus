import time

MENU = '''Options:
1 - Set pause duration
2 - Activate pause
0 - Exit'''

print("Program starting.")

ch = '_'
val = ''
while ch:
	print(MENU)
	ch = input("Your choice: ")
	match(ch):
		case '1':
			val = input("Insert pause duration (s): ")#0.1
		case '2':
			if len(val):
				fval = float(val)
				print(f"Pausing for {fval:.1f} seconds.")
				time.sleep(fval)
				print("Unpaused.")
			else:
				print("Pause is not set.")
				print("Set pause first.")
		case '0':
			ch = None
			print("Exiting program.")
		case _:
			print("Unknown option!")
	print()

print("Program ending.")

