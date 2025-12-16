import random
random.seed(1234)

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
PAPER = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

MENU = '''
Options:
1 - Rock
2 - Paper
3 - Scissors
0 - Quit game'''

p1 = ''
p2 = 'RPS-3PO'
gfx = [ ROCK, PAPER, SCISSORS ]
txt = [ 'rock', 'paper', 'scissors' ]
score = { "w": 0, "l": 0, "t": 0 }

def menu():
	print(MENU)
	ch = input("Your choice: ")
	return int(ch)

def show(c,p):
	print("#########################")
	print(f"{p} chose {txt[c]}.")
	print(gfx[c])

def win(a,b):
	score['w'] += 1
	print(f"{p1} {txt[a]} beats {p2} {txt[b]}.")
def lose(a,b):
	score['l'] += 1
	print(f"{p2} {txt[b]} beats {p1} {txt[a]}.")
def tie(a,b):
	score['t'] += 1
	print(f"Draw! Both players chose {txt[a]}.")

print("Program starting.")
print("Welcome to the rock-paper-scissors game!")
p1 = input("Insert player name: ")
print(f"Welcome {p1}!")
print(f"Your opponent is {p2}.")
print("Game starts...")

while choice := menu():
	a,b = choice-1, random.randint(1,3)-1
	print("Rock! Paper! Scissors! Shoot!\n")
	show(a,p1)
	show(b,p2)
	print("#########################\n")
	(win,lose,tie,win,lose)[2+a-b](a,b)

print(f"""
Results:
{p1} - wins ({score['w']}), losses ({score['l']}), draws ({score['t']})
{p2} - wins ({score['l']}), losses ({score['w']}), draws ({score['t']})
\nProgram ending.
""")

