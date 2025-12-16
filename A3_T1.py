print("Program starting.")
print("Insert two integers.")
n1 = int(input("Insert first integer: "))
n2 = int(input("Insert second integer: "))
tot = n1 + n2
print("Comparing inserted integers.")
print(
	"First integer is greater." if n1 > n2 else
	"Integers are the same" if n1 == n2 else
	"Second integer is greater." )
print()
print("Adding integers together")
print(f"{n1} + {n2} = {tot}")
print()
print("Checking the parity of the sum...")
print(f"Sum is {'odd' if tot%2 else 'even'}.")
print("Program ending.")
