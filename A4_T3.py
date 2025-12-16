print("Program starting.\n")

s = int(input("Insert starting value: "))
e = int(input("Insert stopping value: "))

print("\nStarting while-loop:")
n = s
while n<=e:
	print(n, end = '\n' if n==e else ' ')
	n += 1

print("\nProgram ending.")
