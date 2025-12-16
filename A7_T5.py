WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def main():
	print("Program starting.")
	fn = input("Insert filename: ")
	print(f'Reading file "{fn}".')

	days = { k:[0,0] for k in WEEKDAYS }
	with open(fn) as file:
		_ = file.readline()
		for line in file:
			v = line.strip().split(';')
			if len(v) == 4:
				days[v[0]][0] += int(v[2])
				days[v[0]][1] += int(v[2]) * float(v[3])

	print("Analysing timestamps.")
	print("Displaying results.")
	print("### Electricity consumption summary ###")
	for day,[cons,cost] in days.items():
		print(f" - {day} usage {cons:.2f} kWh, cost {cost:.2f} €")
	print("### Electricity consumption summary ###")
	print("Program ending.")

if __name__ == "__main__":
    main()
