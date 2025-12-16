import hashlib

CREDENTIALS_FILE = 'credentials.txt'
#0;admin;58d613129c5e71de57ee3f44c5ce16bc

def md5(pw):
	return hashlib.md5(pw.encode()).hexdigest()

def readValues() -> list[list[str]]:
	try:
		with open(CREDENTIALS_FILE) as f:
			return [ [e.strip() for e in r] for l in f.readlines() if len(r := l.split(';')) ]
	except FileNotFoundError:
		return []

def writeValues(rows: list[list[str]]):
	with open(CREDENTIALS_FILE,'w') as f:
		f.write('\n'.join([ ';'.join(row) for row in rows ]))

def viewProfile(un):
	return [ (i,n) for i,n,p in readValues() if n==un ][0] 

def change_password(un,npw):
	writeValues(map(
		lambda r: [r[0],r[1],md5(npw)] if r[1]==un else r,
		readValues() ))

def login(un,pw):
	return bool(len([ 1 for i,n,p in readValues() if n==un and p==md5(pw) ]))

def newID(rows: list[list[str]]) -> int:
	return 0 if not len(rows) else 1 + int(max( rows, key=lambda row: int(row[0]) )[0])

def register(un,pw):
	with open(CREDENTIALS_FILE,'r+') as f:
		f.write(';'.join([
			str(newID([ l.split(';') for l in f.readlines() ])),
			un, md5(pw) ]))

