print("Program starting.\n")

s = int(input("Insert starting value: "))
e = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
for n in range(s,e+1):
	print(n, end = '\n' if n==e else ' ')

print("\nProgram ending.")
