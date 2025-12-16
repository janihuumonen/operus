print("Program starting.")
print("This program can read a file.")
fn = input("Insert filename: ")
with open(fn) as f:
	print(f'#### START "{fn}" ####')
	print(f.read())
	print(f'#### END "{fn}" ####')
print("Program ending.")

