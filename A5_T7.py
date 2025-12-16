DELIMITER = ','

def collectWords() -> str:
	l = []
	while word := input("Insert word(empty stops): "):
		l.append(word)
	return DELIMITER.join(l)

def analyseWords(l):
	n = [len(x) for x in l.split(DELIMITER)]
	Avg = sum(n) / len(n)
	print(f"- {len(n)} Words")
	print(f"- {sum(n)} Characters")
	print("- {:.2f} Average word length".format(Avg))
	return None

def main():
	print("Program starting.")
	s = collectWords()
	analyseWords(s)
	print("Program ending.")
	return None

main()
