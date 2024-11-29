num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")

def sum(num1, num2):
    return num1 + num2
def sub(nm1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return abs(num1 / num2)

if op == "+":
    print(sum(num1, num2))
elif op == "-":
    print(sub(num1, num2))
elif op == "*":
    print(mul(num1, num2))
elif op == "/":
    print(div(num1, num2))
else:
    print("Invalid operator")