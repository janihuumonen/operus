########################################################
# Task A10_T3
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

from A10_TLib import readValues, bubbleSort
import sys

def main() -> None:
	print("Program starting.")
	if len(sys.argv) == 2:
		fn = sys.argv[1].strip()
		print(f"The filename '{fn}' was passed via CLI.")
	else:
		fn = input("Insert filename: ")

	lst: list[int] = []
	readValues(fn, lst)

	print(f"Raw '{fn}' -> {', '.join(map(str,lst))}")
	bubbleSort(lst)
	print(f"Ascending '{fn}' -> {', '.join(map(str,lst))}")
	bubbleSort(lst, False)
	print(f"Descending '{fn}' -> {', '.join(map(str,lst))}")

	return None

if __name__ == "__main__":
	main()
