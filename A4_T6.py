print("Program starting.")

n = int(input("Insert a positive integer: "))
l = [n]
while True:
	l.append(n := 3*n+1 if n%2 else int(n/2))
	if n == 1: break
print(' -> '.join(map(str,l)))
print(f"Sequence had {len(l)-1} total steps.")

print("\nProgram ending.")
