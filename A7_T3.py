WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

print("Program starting.")
fn = input("Insert filename: ")
print(f'Reading file "{fn}".')

days = { k:0 for k in WEEKDAYS }
with open(fn) as file:
	_ = file.readline()
	for line in file:
		v = line.strip().split(';')
		if len(v) == 4: days[v[0]] += 1

print("Analysing timestamps.")
print("Displaying results.")
print("### Timestamp analysis ###")
for day,num in days.items():
	print(f" - {day} {num} stamps")
print("### Timestamp analysis ###")
print("Program ending.")
