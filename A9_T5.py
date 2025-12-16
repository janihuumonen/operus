########################################################
# Task A9_T5
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

def askByte(name) -> int:
	v = input(f"Insert {name}: ")
	try:
		v = int(v)
	except ValueError:
		raise ValueError(f'"{v}" is non-numeric value.')
	if v < 0 or v > 255:
		raise ValueError(f'Value "{v}" is out of the range 0-255.')
	return v

def main() -> None:
	print("Program starting.")
	names = ['Red','Green','Blue']
	try:
		r,g,b = [ askByte(n.lower()) for n in names ]
		print("RGB Details:")
		print('\n'.join(f"- {n} {v}" for n,v in zip(names,[r,g,b])))
		print(f"- Hex #{r:02x}{g:02x}{b:02x}")
		print('\n'.join(f'- {n[0]}-byte(base-2): {v:08b}' for n,v in zip(names,[r,g,b])))
	except ValueError as e:
		print(e)
		print("Couldn't perform the designed task due to the invalid input values.")
	print("Program ending.")
	return None

if __name__ == "__main__":
    main()

