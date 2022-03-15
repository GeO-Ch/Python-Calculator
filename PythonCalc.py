import math

#Menu
print("------------------------------------------------------------------------------------------------")
print("Select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square root")
print("------------------------------------------------------------------------------------------------")


operation = input() #The user input is a string

if operation == "1": 
    num1 = input("Type first number ")
    num2 = input("Type second number ")
    print("The sum is " + str(int(num1) + int(num2)))#The output will be a string that concatanates the two int
    print("Youtube tutorial by Kindson The Tech Pro")
elif operation == "2":
    num1 = input("Type first number ")
    num2 = input("Type second number ")
    print("The difference is " + str(int(num1) - int(num2)))
    print("Youtube tutorial by Kindson The Tech Pro")
elif operation == "3":
    num1 = input("Type first number ")
    num2 = input("Type second number ")
    print("The product is " + str(int(num1) * int(num2)))
    print("Youtube tutorial by Kindson The Tech Pro")
elif operation == "4":
    num1 = input("Type first number ")
    num2 = input("Type second number ")
    print("The result is " + str(int(num1) / int(num2)))
    print("Youtube tutorial by Kindson The Tech Pro")
elif operation == "5":
    num = int(input("Type the number "))#The input will now be an int
    print("The result is " + str(math.sqrt(num)))
    print("Youtube tutorial by Kindson The Tech Pro")
else:
    print("Invalid Entry")