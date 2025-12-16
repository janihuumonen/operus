########################################################
# Task A9_T1
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

def main() -> None:
	print("Program starting.")
	lst = []
	while '0' != (ch := input("Insert a floating-point value (0 to stop): ")):
		try:
			lst.append(float(ch))
		except:
			print(f"Error! '{ch}' couldn't be converted to float.")
	print(f"Final sum is {sum(lst):.2f}")
	print("Program ending.")
	return None

main()
