import loginLib

MAINMENU = '''Options:
1 - Login
2 - Register
0 - Exit'''

USERMENU = '''
User menu:
1 - View profile
2 - Change password
0 - Logout'''

def userPrompt() -> list[str]:
	un = input("Insert username: ")
	pw = input("Insert password: ")
	return un, pw

def askChoice() -> int:
	ch = input("Your choice: ")
	return int(ch) if ch.isnumeric() else -1

def user(id,name):
	ch = -1
	while (ch):
		print(USERMENU)
		match(ch := askChoice()):
			case 1:
				print(f"Profile ID {id} - {name}")
			case 2:
				loginLib.change_password(name, input("New password: "))
			case 0:
				print("Logging out...")
			case _:
				print("Unknown option!")

def main() -> None:
	print("Program starting.")
	ch = -1
	while (ch):
		print(MAINMENU)
		match(ch := askChoice()):
			case 1:
				if loginLib.login(*(c := userPrompt())):
					print("Authentication successful!")
					user(*c)
				else: print("Authentication failed!")
			case 2:
				loginLib.register(*userPrompt())
				print("User registration completed!")
			case 0:
				print("Exiting program.")
			case _:
				print("Unknown option!")
		print()
	print("Program ending.")
	return None

main()
