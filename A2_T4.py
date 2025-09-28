print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")
mins = [ int(input(f"A1_T{n}: ")) for n in range(1,8) ]
tot = sum(mins)
avg = tot / 7
print(f"\nIn total you spent {tot} minutes on programming.")
print(f"Average per task was {round(avg,2)} min and same rounded to the nearest integer {int(round(avg,0))} min.\n")
print("Program ending.")
