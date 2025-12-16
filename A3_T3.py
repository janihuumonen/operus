print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
print()
print('''
Options:
1 - Print welcome message
0 - Exit
''')
res = input("Your choice: ")
if res == '1': print(f"Welcome {name}!")
elif res == '0': print("Exiting...")
else: print("Unknown option.")
print()
print("Program ending.")

