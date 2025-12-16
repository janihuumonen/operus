########################################################
# Task A9_T2
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

import sys

def main() -> None:
	print("Program starting.")
	c = int(input("Insert exit code(0-255): "))
	if c == 0:
		print("Clean exit")
		sys.exit(0)
	else:
		print("Error code")
		sys.exit(c)
	return None

main()
