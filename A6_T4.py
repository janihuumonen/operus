print('Program starting.')
print('This program analyses a list of names from a file.')
fn = input('Insert filename to read: ')
print(f'Reading names from "{fn}".')
with open(fn) as file:
	lines = [len(line.rstrip('\n')) for line in file if line != '\n']
print('Analysing names...')
l = len(lines)
short = min(lines)
long = max(lines)
avg = sum(lines) / l
print('Analysis complete!')
print('#### REPORT BEGIN ####')
print(f'Name count - {l}')
print(f'Shortest name - {short} chars')
print(f'Longest name - {long} chars')
print(f'Average name - {avg:.2f} chars')
print('#### REPORT END ####')
print('Program ending.')

