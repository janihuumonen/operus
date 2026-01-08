########################################################
# Task A10_T2
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

import math
from A10_TLib import readValues

def main() -> None:
	print("Program starting.")
	fn = input("Insert filename: ")
	lst: list[int] = []
	readValues(fn, lst)
	print("# --- Sum of numbers --- #")
	print(sum(lst))
	print("# --- Sum of numbers --- #")
	print("# --- Product of numbers --- #")
	print(math.prod(lst))
	print("# --- Product of numbers --- #")
	print("Program ending.")
	return None

main()
