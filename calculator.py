def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a * b

def division (a, b):
    if b != 0:
        return a/b
    else:
        return("you can't divide by zero")
        
        
def menu ():
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("0.exit")
    
while True:
    menu()
    choice = input("Выбери:")
    
    if choice == "1":
        try:
            a = int(input("Выбери первое число: "))
            b = int(input("Выбери второе число: "))
            
            print(f"Ваш результат: {addition(a,b)}")
        except ValueError:
            print("Введите число а не букву")
        
    elif choice == "2":
        try:
            a = int(input("Выбери первое число: "))
            b = int(input("Выбери второе число: "))
            
            print(f"Ваш результат: {subtraction(a,b)}")
        except ValueError:
            print("Введите число а не букву")
        
    elif choice == "3":
        try:
            a = int(input("Выбери первое число: "))
            b = int(input("Выбери второе число: "))
            print(f"Ваш результат: {multiplication(a,b)}")
        except ValueError:
            print("Введите число а не букву")
        
    elif choice == "4":
        try:
            a = int(input("Выбери первое число: "))
            b = int(input("Выбери второе число: "))
            print(f"Ваш результат: {division(a,b)}")
        except ValueError:
            print("Введите число а не букву")
        
    elif choice == "0":
        break
       