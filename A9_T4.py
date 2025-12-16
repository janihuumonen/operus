########################################################
# Task A9_T4
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
	v = input("Insert Celsius: ")
	try:
		v = float(v)
	except:
		raise ValueError(f"could not convert string to float: '{v}'")
	if v < TEMP_MIN or v > TEMP_MAX:
		raise Exception(f"{v} temperature out of range.")
	return v

def main() -> None:
	print("Program starting.")
	try:
		v = collectCelsius()
		print(f"You inserted {v} °C")
	except ValueError as e:
		print(e)
	except Exception as e:
		print(e)
	print("Program ending.")
	return None

main()
