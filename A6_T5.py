def readValues(fn):
	with open(fn) as file:
		return [int(line.rstrip('\n')) for line in file if line != '\n']

def analyseValues(nums):
	l = len(nums)
	avg = sum(nums) / l
	return f'Count;Sum;Greatest;Average\n{l};{sum(nums)};{max(nums)};{avg:.2f}\n'

def main():
	print('Program starting.')
	fn = input('Insert filename: ')
	nums = readValues(fn)
	print('#### Number analysis - START ####')
	print(f'File "{fn}" results:')
	print(analyseValues(nums))
	print('#### Number analysis - END ####')
	print('Program ending.')

if __name__ == "__main__":
    main()
