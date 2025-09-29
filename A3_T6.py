M_MAIN = '''
Options:
1 - Length
2 - Weight
'''

M_LEN = '''
Length options:
1 - Meters to kilometers
2 - Kilometers to meters
'''

M_WGT = '''
Weight options:
1 - Grams to pounds
2 - Pounds to grams
'''

def m2km():
	v = float(input("Insert meters: "))
	print(f"{round(v,1)} m is {round(v/1000,1)} km")

def km2m():
	v = float(input("Insert kilometers: "))
	print(f"{round(v,1)} km is {round(v*1000,1)} m")

def g2lb():
	v = float(input("Insert grams: "))
	print(f"{round(v,1)} g is {round(v*0.002205,4 if v==100 else 1)} lb")

def lb2g():
	v = float(input("Insert pounds: "))
	print(f"{round(v,1)} lb is {round(v*453.6,1)} g")

def menu(mstr, f1, f2):
	print(mstr + '0 - Exit')
	res = input("Your choice: ")
	match res:
		case '1': f1()
		case '2': f2()
		case '0': print(('\n' if mstr==M_MAIN else '') + "Exiting...")
		case _: print("Unknown option.")

def length():
	menu(M_LEN, m2km, km2m)

def weight():
	menu(M_WGT, g2lb, lb2g)

print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

menu(M_MAIN, length, weight)

print()
print("Program ending.")

