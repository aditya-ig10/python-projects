def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mult(x,y):
    return x * y
def div(x,y):
    return x / y

while True:
    print("Calculator")
    print("Select any Operation: ")
    print("1. Addition ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")
    
    choice = input("Choose 1/2/3/4: ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("x = "))
        num2 = float(input("y = "))
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
        break
    elif choice == '2':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
        break
    elif choice == '3':
        print(f"{num1} * {num2} = {mult(num1, num2)}")
        break
    elif choice == '4':
        print(f"{num1} / {num2} = {div(num1, num2)}")
        break
    else: print("Choose the appropriate num")