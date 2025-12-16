print('Program starting.')
s = input("Insert comma separated integers: ")
ints = []
for v in s.split(','):
	try:
		n = int(v)
		ints.append(n)
	except ValueError:
		print(f"Invalid value '{v}' detected.")
if len(ints):
	print(f'There are {len(ints)} integers in the list.')
	si = sum(ints)
	print(f'Sum of the integers is {si} and it\'s {"odd" if si%2 else "even"}')
else:
	print("No values to analyse.")
print('Program ending.')
