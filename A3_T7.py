print("Program starting.")
print("Testing decision structures.")
num = int(input("Insert an integer: "))

print('''\
Options:
1 - In one multi-branched decision
2 - In multiple independent if-statements
0 - Exit''')
res = input("Your choice: ")

match res:
	case '1':
		print("Using one multi-branched decision structure.")
		if num >= 400: num += 44
		elif num >= 200: num += 22
		elif num >= 100: num += 11
		else: pass
		print(f"Result is {num}")
	case '2':
		print("Using multiple independent if-statements structure.")
		if num >= 400: num += 44
		if num >= 200: num += 22
		if num >= 100: num += 11
		print(f"Result is {num}")
	case '0':
		print("Exiting...")
	case _:
		print("Unknown option.")

print()
print("Program ending.")

