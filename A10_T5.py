########################################################
# Task A10_T5
# Developer Jani Huumonen
# Date 2025-12-08
########################################################

def recursiveFactorial(PNum: int) -> int:
	return 1 if PNum <= 1 else PNum * recursiveFactorial(PNum-1)

def main() -> None:
	print("Program starting.")
	val = int(input("Insert factorial: "))
	print(f"Factorial {val}!")
	print(f"{'*'.join(map(str,range(1,val+1)))} = {recursiveFactorial(val)}")
	print("Program ending.")
	return None

main()
