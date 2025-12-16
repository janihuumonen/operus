print("Program starting.\n")

import math
print("Check multiplicative persistence.")
s = input("Insert an integer: ")
steps = 0
while len(s) > 1:
	print( ' * '.join(s), '=', s := str(math.prod(map(int,s))) )
	steps += 1
print("No more steps.")
print()
print(f"This program took {steps} step(s)")

print("\nProgram ending.")
