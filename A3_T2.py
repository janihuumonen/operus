print("Program starting.")
print("String comparisons")

w1 = input("Insert first word: ")
ch = input("Insert a character: ")
print(
	f'Word "{w1}" contains character "{ch}"'
	if ch in w1 else
	f'Word "{w1}" doesn\'t contain character "{ch}"'
)

w2 = input("Insert second word: ")
print(
	f'The first word "{w1}" is before the second word "{w2}" alphabetically.'
	if w1 < w2 else
	f'Both inserted words are the same alphabetically, "{w1}"'
	if w1 == w2 else
	f'The second word "{w2}" is before the first word "{w1}" alphabetically.'
)

print("Program ending.")
