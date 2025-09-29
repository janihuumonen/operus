print("Program starting.")
print('''
Options:
1 - Celsius to Fahrenheit
2 - Fahrenheit to Celsius
0 - Exit''')
res = input("Your choice: ")

match res:
	case '1':
		c = float(input("Insert the amount of Celsius: "))
		print(f"{round(c,1)} °C equals to {round(c*1.8+32,1)} °F")
	case '2':
		f = float(input("Insert the amount of Fahrenheit: "))
		print(f"{round(f,1)} °F equals to {round((f-32)/1.8,1)} °C")
	case '0':
		print("Exiting...")
	case _:
		print("Unknown option.")
print()
print("Program ending.")

