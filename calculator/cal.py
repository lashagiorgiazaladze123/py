operator = input("please enter operator (+ - * /):")
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else :
    print("operator is wrong")

    

