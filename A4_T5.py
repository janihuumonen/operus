print("Program starting.\n")

s = int(input("Insert starting point: "))
e = int(input("Insert stopping point: "))
i = int(input("Insert inspection point: "))
valid = True
print()
if s >= e:
	print("Starting point value must be less than the stopping point value.")
	valid = False
if i < s or i > e:
	print("Inspection value must be within the range of start and stop.")
	valid = False
if valid:
	print("First loop - inspection with break:")
	l = []
	for n in range(s,e+1):
		if n == i: break
		l += [str(n)]
	print(' '.join(l))

	print("Second loop - inspection with continue:")
	l = []
	for n in range(s,e+1):
		if n == i: continue
		l += [str(n)]
	print(' '.join(l))

print("\nProgram ending.")
