########################################################
# Task A9_T3
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

def main() -> None:
	print("Program starting.")
	fn = input("Insert filename: ")
	try:
		with open(fn) as f:
			print('\n'.join([
				f"## {fn} ##",
				*[l.strip() for l in f.readlines()],
				f"## {fn} ##"
			]))
	except FileNotFoundError:
		print(f'''Couldn't read file "{fn}".''')
	print("Program ending.")
	return None

main()

