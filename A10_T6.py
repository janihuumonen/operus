########################################################
# Task A10_T6
# Developer Jani Huumonen
# Date 2025-12-12
########################################################

import copy
from inspect import cleandoc
from A10_TLib import readValues, measureExecTime, bubbleSort, quickSort

MAINMENU = '''Options:
1 - Read dataset values
2 - Measure speeds
3 - Save results
0 - Exit'''

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def main() -> None:
	print("Program starting.")
	res = ''
	data = []
	ch = -1
	while (ch):
		print(MAINMENU)
		match(ch := askChoice()):
			case 1:
				fn = input("Insert dataset filename: ") 
				readValues(fn, data)
			case 2:
				r_builtin = measureExecTime(sorted, copy.deepcopy(data))
				r_bubble = measureExecTime(bubbleSort, copy.deepcopy(data))
				r_quick = measureExecTime(quickSort, copy.deepcopy(data))
				res = cleandoc(f"""\
				Measured speeds for dataset '{fn}':
				 - Built-in sorted {r_builtin} ns
				 - Buble sort {r_bubble} ns
				 - Quick sort {r_quick} ns""")
				print(res)
			case 3:
				ofn = input("Insert results filename: ") 
				with open(ofn,'w') as f: f.write(res+'\n')
			case 0:
				print("Exiting program.")
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()

