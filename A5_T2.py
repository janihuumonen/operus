def frameWord(PWord):
	s = '*' * (len(PWord) + 4)
	print(s, f'* {PWord} *', s, sep='\n')
	return None

def main():
	print("Program starting.")
	w = input("Insert word: ")
	print()
	frameWord(w)
	print()
	print("Program ending.")
	return None

main()
