num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input(f"Operator(+,-,*,/): ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

else: 
    print("Input a valid operator")

