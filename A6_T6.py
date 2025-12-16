LOWER_ALPHABETS = ''
UPPER_ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shiftCharacter(ch,_=''):
    o = ord('a') if ch.islower() else ord('A') if ch.isupper() else None
    return chr( o + (ord(ch) - o + 13) % 26 ) if o else ch

def rot13(s):
    return ''.join([shiftCharacter(ch) for ch in s])

def collectRows():
        l = []
        while s := input("Insert row(empty stops): "):
                l.append(s)
        return l

def writeFile(fn,s):
	with open(fn,'w',encoding='UTF-8') as f: f.write(s)

def main():
	print('Program starting.')
	print()
	print('Collecting plain text rows for ciphering.')
	text = '\n'.join(map(rot13,collectRows()))
	print()
	print('#### Ciphered text ####')
	print(text)
	print()
	print('#### Ciphered text ####')
	fn = input('Insert filename to save: ')
	writeFile(fn,text)
	print('Ciphered text saved!')
	print('Program ending.')

if __name__ == "__main__":
    main()
