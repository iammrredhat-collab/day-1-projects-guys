# day 1 calculator project

num1= int(input("enter the first number: "))
num2= int(input("enter the second number: "))
ask = input("which operation do you want to perform?: ")

if ask == "add" or ask == "addition":
    print(num1 + num2)

elif ask == "subtract" or ask == "substraction":
    print(num1 - num2)

elif ask == "multiply" or ask == "scale" or ask == "multiplication":
    print(num1 * num2)

elif ask == "divide" or ask == "division":
    print(num1/num2)

else:
    print("valid operations are add,subtract,multiply,divide(please write in lower case)")           
