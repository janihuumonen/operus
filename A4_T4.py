print("Program starting.\n")

n = 0
l = 0
while word := input("Insert word (empty stops): "):
	l += len(word)
	n += 1
print(f"\nYou inserted:\n- {n} words\n- {l} characters")

print("\nProgram ending.")
