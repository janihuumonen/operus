########################################################
# Task A10_T1
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

from A10_TLib import readValues

def main() -> None:
	print("Program starting.")
	fn = input("Insert filename: ")
	lst: list[int] = []
	readValues(fn, lst)
	lst = list(map(str, lst))
	print("# --- Vertically --- #")
	print('\n'.join(lst))
	print("# --- Vertically --- #")
	print("# --- Horizontally --- #")
	print(', '.join(lst))
	print("# --- Horizontally --- #")
	print("Program ending.")
	return None

main()
