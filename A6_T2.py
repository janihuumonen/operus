print("Program starting.")
n1 = input("Insert first name: ")
n2 = input("Insert last name: ")
fn = input("Insert filename: ")
with open(fn, "w") as f:
	f.write('{}\n{}\n\n'.format(n1,n2))
print("Program ending.")

