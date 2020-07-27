print("This is my Simple calculator ")
while True:
     print("press 1 for addition ")
     print("press 2 for subtraction ")
     print("press 3 for multiplication ")
     print("press 4 for division ")
     print("press 5 for modulus ")
     print("press 6 for power ")
     print("press 7 for floor ")
     print("press 8 for exit ")


     choice = input()
     if choice =='1':
         number1 = int(input("Please enter the number 1:  "))
         number2 = int(input("Please enter the number 2: "))
         print(f"the sum of {number1} and {number2} is ",number1+number2)
     elif choice=='2':
         number1 = int(input("Please enter the number 1:  "))
         number2 = int(input("Please enter the number 2: "))
         print(f"the sum of {number1} and {number2} is ", number1 - number2)

     elif choice == '3':
         number1 = int(input("Please enter the number 1:  "))
         number2 = int(input("Please enter the number 2: "))
         print(f"the sum of {number1} and {number2} is ", number1 * number2)
     elif choice == '4':
         number1 = int(input("Please enter the number 1:  "))
         number2 = int(input("Please enter the number 2: "))
         print(f"the sum of {number1} and {number2} is ", number1 / number2)
     elif choice == '5':
         number1 = int(input("Please enter the number 1:  "))
         number2 = int(input("Please enter the number 2: "))
         print(f"the sum of {number1} and {number2} is ", number1 % number2)
     elif choice == '6':
         number1 = int(input("Please enter the number 1:  "))
         number2 = int(input("Please enter the number 2: "))
         print(f"the sum of {number1} and {number2} is ", number1 ** number2)
     elif choice == '7':
         number1 = int(input("Please enter the number 1:  "))
         number2 = int(input("Please enter the number 2: "))
         print(f"the sum of {number1} and {number2} is ", number1 // number2)
     elif choice == '3':
         exit()
     else:
         print("Plese enter a valid choice ")

