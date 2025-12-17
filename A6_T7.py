import os
import re

PALACES = [ 'home',
	"Galba's palace",
	"Otho's palace",
	"Vitellius' palace",
	"Vespasian's palace" ]

def rot13ch(ch):
    o = ord('a') if ch.islower() else ord('A') if ch.isupper() else None
    return chr( o + (ord(ch) - o + 13) % 26 ) if o else ch

def rot13(s: str) -> str:
	return ''.join([rot13ch(ch) for ch in s])

def validate(s: str) -> list[str]:
	r = [ e.strip() for e in s.split(';') ]
	return r if len(r)==3 and r[0].isnumeric() and r[1].isnumeric() and r[2] else []

def main():
	try:
		f = open("player_progress.txt",'r+')
		# read existing lines and advance cursor to end of file
		progress = [ r for l in f.readlines() if (r := validate(l)) ]
		cid,nid,cpp = progress[-1]
		ppp = rot13(cpp)
		pptxt = ppp[0].upper() + ppp[1:]
		curloc = PALACES[int(cid)]
		nextloc = PALACES[int(nid)]

		print("Travel starting.")
		print(f"Currently at {curloc}.")
		print(f"Travelling to {nextloc}...")
		print(f"...Arriving to the {nextloc}.")
		print("Passing the guard at the entrance.")
		print(f'"{pptxt}!"')
		print("Looking for the message in the palace...")

		fn = f"{nid}_{cpp}.gkg"
		files = os.listdir()
		if fn in files:
			with open(fn) as cf:
				gkg = cf.readlines()
		else: return
		print("Ah, there it is! Seems cryptic.")

		ncpp = None
		nnid = int(nid)+1
		pat = re.compile(rf"^{nnid}_(.*)\.gkg$")
		for fn in files:
			if m := re.search(pat, fn):
				ncpp = m.group(1)
				break

		if ncpp: f.writelines([';'.join([ nid, str(nnid), ncpp ])+'\n'])
		print("[Game] Progress autosaved!")

		print("Deciphering Emperor's message...")
		txt = [ rot13(l) for l in gkg[1:] ]

		with open(f"{nid}-{ppp}.txt",'w') as tf:
			tf.writelines(txt)
		print("Looks like I've got now the plain version copy of the Emperor's message.")

		print("Time to leave...")
		print("Travel ending.")
	finally:
		f.close()

if __name__ == "__main__":
    main()

