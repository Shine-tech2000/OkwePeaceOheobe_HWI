# Read the first number, the second number and operation from standard input
num1 = float(input())
num2 = float(input())
op = input()

# Perform the specified operation on the numbers
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Division by 0!")
    else:
        result = num1 / num2
elif op == "mod":
    if num2 == 0:
        print("Division by 0!")
    else:
        result = num1 % num2
elif op == "pow":
    result = num1 ** num2
elif op == "div":
    if num2 == 0:
        print("Division by 0!")
    else:
        result = num1 // num2

# Output the result
print(result)


