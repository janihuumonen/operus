#Insert config(filename): iconf1.txt
fn = "iconf1.txt"
#Insert plugs (y/n)?: n
#No extra plugs inserted.
print("Enigma initialized.")

class Rotor:
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	def __init__(self, wiring):
		self.pos = 0
		self.len = len(self.alphabet)
		self.rtl = [ self.alphabet.index(x) for x in wiring ]
		self.ltr = [ wiring.index(x) for x in self.alphabet ]
	def right(self, i):
		return ( self.ltr[(self.pos + i) % self.len] - self.pos ) % self.len
	def left(self, i):
		return ( self.rtl[(self.pos + i) % self.len] - self.pos ) % self.len
	def rotate(self, n=1):
		self.pos = (self.pos+n) % self.len
		return self.pos == 0 # notch+1
	def reset(self):
		self.pos = 0

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

while s := input("Insert row (empty stops): "):
	print(f'Converted row - "{cipherText(s)}".')
	
print("Enigma closing.")

'''a-f       01234567890123456789012345
             ABCDEFGHIJKLMNOPQRSTUVWXYZ
Q Rotor1:    EKMFLGDQVZNTOWYHXUSPAIBRCJ
E Rotor2:    AJDKSIRUXBLHWTMCQGZNPYFVOE
V Rotor3:    BDFHJLCPRTXVZNYEIWGAKMUSQO
Reflector:   YRUHQSLDPXNGOKMIEBFZCWVJAT

ENIGMA MACHINE WORKING!
HXBCOJ BIDPGKF IMPTWWJ!
Character "H" illuminated as "E"
Character "E" illuminated as "C"
Character "L" illuminated as "M"
Character "L" illuminated as "A"
Character "O" illuminated as "M"

def rotate_list_r(l,n):
	return l[n:] + l[:n]
def rotate_list_l(l,n):
	return l[-n:] + l[:-n]

def cip(r,i):
	i = rs[r][0][ i+os[r] ] # forward substitute
	if r >= len(rs)-1: return i # reflector
	i = cip(r+1, i) # next rotor
	i = rs[r][1][ i+os[r] ] # bacward substitute
	return i
'''


'''
const ENIGMA_ELEM_ID = {
INPUT: "inputMessage",
OUTPUT: "outputMessage",
START_POS_0: "startPos0",
START_POS_1: "startPos1",
START_POS_2: "startPos2",
END_POS_0: "endPos0",
END_POS_1: "endPos1",
END_POS_2: "endPos2"
}
const CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const ROTORS = [
"EKMFLGDQVZNTOWYHXUSPAIBRCJ", // Rotor I
"AJDKSIRUXBLHWTMCQGZNPYFVOE", // Rotor II
"BDFHJLCPRTXVZNYEIWGAKMUSQO"  // Rotor III
];
const REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"; // Reflector B
const stepRotors = (PPositions, PRotors) => {
	PPositions[0] = (PPositions[0] + 1) % PRotors[0].length;
	if (PPositions[0] === 0) {
		PPositions[1] = (PPositions[1] + 1) % PRotors[1].length;
		if (PPositions[1] === 0) {
			PPositions[2] = (PPositions[2] + 1) % PRotors[2].length;
		}
	}
}
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
const cipherText = (PPlainText, PPositions, PRotors, PReflector) => {
	var CipheredText = '';
	for (var i = 0; i < PPlainText.length; i++) {
		var Letter = PPlainText[i];
		if (/[A-Za-z]/.test(Letter)) {
			CipheredText += cipherChar(Letter.toUpperCase(), PPositions, PRotors, PReflector);
		} else {
			CipheredText += Letter;
		}
	}
	return CipheredText;
}
const POSITIONS = [0, 0, 0];
const cipher = () => {
	var inputText = document.getElementById('inputMessage').value;
	let pos0 = document.getElementById(ENIGMA_ELEM_ID.START_POS_0).innerText;
	let pos1 = document.getElementById(ENIGMA_ELEM_ID.START_POS_1).innerText;
	let pos2 = document.getElementById(ENIGMA_ELEM_ID.START_POS_2).innerText;
	POSITIONS[0] = parseInt(pos0, 10);
	POSITIONS[1] = parseInt(pos1, 10);
	POSITIONS[2] = parseInt(pos2, 10);
	if (POSITIONS[0] === -1 || POSITIONS[1] === -1 || POSITIONS[2] === -1) {
		alert('Invalid rotor position(s). Please enter letters A-Z.');
		return;
	}
	var cipheredText = cipherText(inputText, POSITIONS, ROTORS, REFLECTOR);
	document.getElementById(ENIGMA_ELEM_ID.END_POS_0).innerText = POSITIONS[0];
	document.getElementById(ENIGMA_ELEM_ID.END_POS_1).innerText = POSITIONS[1];
	document.getElementById(ENIGMA_ELEM_ID.END_POS_2).innerText = POSITIONS[2];
	document.getElementById(ENIGMA_ELEM_ID.OUTPUT).value = cipheredText;   
}
const resetEnigmaRotorPositions = () => {
	document.getElementById(ENIGMA_ELEM_ID.OUTPUT).value = "";
	document.getElementById(ENIGMA_ELEM_ID.INPUT).value = "";
	POSITIONS[0] = 0;
	POSITIONS[1] = 0;
	POSITIONS[2] = 0;
	document.getElementById(ENIGMA_ELEM_ID.END_POS_0).innerText = POSITIONS[0];
	document.getElementById(ENIGMA_ELEM_ID.END_POS_1).innerText = POSITIONS[1];
	document.getElementById(ENIGMA_ELEM_ID.END_POS_2).innerText = POSITIONS[2];
}
const KEYBOARD_CHAR_MAP = new Map([
['^', 'caret'],
['<', 'anglebracket'],
['>', 'anglebracket'],
[' ', 'space'],
["'", 'singlequote'],
['.', 'dot'],
[',', 'comma'],
['-', 'dash']
]);
/**
* @param {KeyboardEvent} event
*/
const onEnigmaKeyboardPress = (event) => {
console.log(`Key: "${event.key}"`);
const _key = event.key.toLocaleUpperCase();
/** @type {HTMLTextAreaElement} */
const _enigma_output = document.getElementById(ENIGMA_ELEM_ID.OUTPUT);
/** @type {HTMLTextAreaElement} */
const _enigma_input = document.getElementById(ENIGMA_ELEM_ID.INPUT);
if (event.key === "Enter") {
event.preventDefault(); // Prevents adding a new line in the textarea
cipher(); // Calls the cipher function
} else if (event.key === 'Backspace') {
_enigma_output.value = _enigma_output.value.slice(0, (_enigma_input.value.length - 1));
} else if (CHARS.includes(_key)) {
// console.log("Key: " + event.key);
console.log("1 - Rotate, 2 - Illuminate, 3 - Dimm with delay");
const _cchar = cipherChar(_key, POSITIONS, ROTORS, REFLECTOR);
const _elem = document.getElementById(`key-${_cchar}`);
console.log(`Key "${_key}" illuminated as "${_cchar}"`);
_elem.classList.add("glow-key");
_enigma_output.value += _cchar;
setTimeout(() => _elem.classList.remove("glow-key"), 1000);
} else if (_key.length == 1) {
_enigma_output.value += _key;
console.log(`Key "${_key}" illuminated as "${_key}"`);
if ("^'<>,.- ".includes(_key)) {
let symbol_name = KEYBOARD_CHAR_MAP.get(_key);
const _elem = document.getElementById(`key-${symbol_name}`);
_elem.classList.add("glow-key");
setTimeout(() => _elem.classList.remove("glow-key"), 1000);
}
} else {
console.log("skip?");
}
document.getElementById(ENIGMA_ELEM_ID.END_POS_0).innerText = POSITIONS[0];
document.getElementById(ENIGMA_ELEM_ID.END_POS_1).innerText = POSITIONS[1];
document.getElementById(ENIGMA_ELEM_ID.END_POS_2).innerText = POSITIONS[2];
};
'''
