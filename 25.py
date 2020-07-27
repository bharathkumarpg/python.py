def add():
     print(x+y)

def subtract(a,b):
     print(a-b)
def mul(a,b):
    c = a * b
    return c
def div(a, b):
    c = a / b
    return c
def modulus(a,b):
    print(a%b)
def power(a, b):
    c = a ** b
    return c

def floor(a, b):
    c = a // b
    return c
print("calculator with functions")



while True:
     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\5.Modulus\6.Power\7.Floor\8.Exit")
     choice = input()
     if choice == '1':
         x = int(input("Please enter the first number "))
         y = int(input("Please enter the second number "))
         add()
     elif choice == '2':
         x = int(input("Please enter the first number "))
         y = int(input("Please enter the second number "))
         if x>=y:
             subtract(x,y)
         else:
             subtract(y,x)
     elif choice=='3':
         x = int(input("Please enter the first number "))
         y = int(input("Please enter the second number "))
         print(mul(x, y))
     elif choice == '4':
         x = int(input("Please enter the first number "))
         y = int(input("Please enter the second number "))
         print(div(x, y))
     elif choice == '5':
         x = int(input("Please enter the first number "))
         y = int(input("Please enter the second number "))
         modulus(x,y)
     elif choice == '6':
         x = int(input("Please enter the first number "))
         y = int(input("Please enter the second number "))
         print(power(x, y))
     elif choice == '7':
         x = int(input("Please enter the first number "))
         y = int(input("Please enter the second number "))
         print(floor(x, y))
     elif choice == '8':
         exit()



     else:
         print("Please enter a valid choice ")

