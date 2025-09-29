print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")

print('''
Options:
1 - Print welcome message
2 - Print the name backwards
3 - Print the first character
4 - Show the amount of characters in the name
0 - Exit''')
res = input("Your choice: ")

opts = {
	'1': lambda: print(f"Welcome {name}!"),
	'2': lambda: print(f'Your name backwards is "{name[::-1]}"'),
	'3': lambda: print(f'The first character in name "{name}" is "{name[:1]}"'),
	'4': lambda: print(f'There are {len(name)} characters in the name "{name}"'),
	'0': lambda: print("Exiting..."),
	'_': lambda: print("Unknown option."),
}
opts.get(res, opts['_'])()

print()
print("Program ending.")

