

def showWelcome():
    print("Hi")
showWelcome()


#Cal

def calculatorAdd(a,b):
    return a+b

a,b = int(input("Enter a:")), int(input("Enter b:"))
resp = calculatorAdd(a,b)

print(f"The add is {resp}")