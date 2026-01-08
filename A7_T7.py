fn = input("Insert config(filename): ")
unused = input("Insert plugs (y/n)?: ")
print("No extra plugs inserted.")
print("Enigma initialized.\n")

class Rotor:
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	def __init__(self, wiring):
		self.pos = 0
		self.len = len(self.alphabet)
		self.rtl = [ self.alphabet.index(x) for x in wiring ]
		self.ltr = [ wiring.index(x) for x in self.alphabet ]
		self.rtl, self.ltr = self.ltr, self.rtl #!!! invert the rotor (left-to-right becomes right-to-left and vice versa)
	def right(self, i):
		return ( self.rtl[(self.pos + i) % self.len] - self.pos ) % self.len
	def left(self, i):
		return ( self.ltr[(self.pos + i) % self.len] - self.pos ) % self.len
	def rotate(self, n=1):
		self.pos = (self.pos+n) % self.len
		return self.pos == 0 # notch+1, notch is at position Z
	def reset(self):
		self.pos = 0

# top line in the file is the rightmost rotor(the input/output side)
with open(fn) as f:
	rotors = [ Rotor(l.strip().split(':')[1]) for l in f.readlines() if ':' in l ]

def cipher(i, r=0):
	i = rotors[r].right(i) # forward substitute
	if r >= len(rotors)-1: return i # reflector
	i = cipher(i, r+1) # recurse into next rotor
	i = rotors[r].left(i) # bacward substitute
	return i

def cipherChar(c):
	i = Rotor.alphabet.index(c.upper())
	for r in rotors[:-1]:
		if not r.rotate(): break
	return Rotor.alphabet[cipher(i)]
	
def cipherText(s):
	s = [ cipherChar(x) if x.upper() in Rotor.alphabet else x for x in s ]
	for r in rotors: r.reset()
	return ''.join(s)

while inp := input("Insert row (empty stops): "):
	out = cipherText(inp)
	for i,o in zip(inp,out): print(f'Character "{i.upper()}" illuminated as "{o}"')
	print(f'Converted row - "{out}".\n')
	
print("\nEnigma closing.")

'''
ENIGMA MACHINE WORKING!
HXBCOJ BIDPGKF IMPTWWJ!

is the result of "inverted" rotors and signal flow:
input -> I -> II -> III -> REFLECTOR B -> III -> II -> I -> output
(iconf1.txt)

The inverting happens because the example code below does Rotor.indexOf() on forward pass and PRotors[i].charCodeAt() on reverse pass.

The python code above does the same inverting on purpose(the line is commented) in Rotor.__init__().
'''

'''
const ROTORS = [
"EKMFLGDQVZNTOWYHXUSPAIBRCJ", // Rotor I
"AJDKSIRUXBLHWTMCQGZNPYFVOE", // Rotor II
"BDFHJLCPRTXVZNYEIWGAKMUSQO"  // Rotor III
];
const REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"; // Reflector B

const cipherChar = (PChar, PPositions, PRotors, PReflector) => {
	// Step 0: Rotate rotors
	stepRotors(PPositions, PRotors);
	var Index = PChar.charCodeAt(0) - 'A'.charCodeAt(0);

	// Step 1: Forward pass through the rotors
	for (var i = 0; i < 3; i++) {
		var Rotor = PRotors[i];
		Index = (
				Rotor.indexOf(
					String.fromCharCode((Index + PPositions[i]) % CHARS.length + 'A'.charCodeAt(0))
				) - PPositions[i] + CHARS.length
			) % CHARS.length;
	}

	// Step 2: Reflector
	var _Char = PReflector[Index];
	Index = _Char.charCodeAt(0) - 'A'.charCodeAt(0);

	// Step 3: Reverse pass through the rotors
	for (var i = 2; i >= 0; i--) {
		var Offset = (PPositions[i] + Index) % CHARS.length;
		Index = (PRotors[i].charCodeAt(Offset) - 'A'.charCodeAt(0) - PPositions[i] + CHARS.length) % CHARS.length;
	}
	_Char = String.fromCharCode(Index + 'A'.charCodeAt(0));
	return _Char;
}
'''
