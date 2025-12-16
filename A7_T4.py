class Row:
	def __init__(s, dy, hr, co, pr):
		s.dy = dy
		s.hr = hr
		s.co = int(co)
		s.pr = float(pr)
	def __str__(s):
		return f" - {s.dy} {s.hr}:00, price {s.pr:.2f}, consumption {s.co:.2f} kWh, total {s.pr*s.co:.2f} €"

TIMESTAMP=''

def readTimestamps(fn,rows):
	with open(fn) as file:
		header = file.readline().strip().split(';')
		for line in file:
			v = line.strip().split(';')
			if len(v) == 4: rows.append(Row(*v))

def displayTimestamps(rows):
	print("Electricity usage:")
	for row in rows:
		print(row)

def main():
	print("Program starting.")
	fn = input("Insert filename: ")
	print(f'Reading file "{fn}".')

	rows = []
	readTimestamps(fn,rows)
	displayTimestamps(rows)
	print("Program ending.")

if __name__ == "__main__":
    main()
