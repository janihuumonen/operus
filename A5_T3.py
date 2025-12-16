def greetUser(PName):
        print(f'Hello {PName}!')
        return None

def askName():
        return input("Insert name: ")

def main():
        print("Program starting.")
        greetUser(askName())
        print("Program ending.")
        return None

main()
