#Arithmetic operators in python 

# + , - , * , / , % , ?, //
print(1+2)
print(5-3)
print(4*3)
print(8/2) #float division
print(7%3) #modulus operator
print(7//3) #floor division
print(2**3) #exponentiation operator    


#Creating a simple calculator

print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
print("Enter the operator")
op = input()

if op == "+":   
    print("The sum is:", num1 + num2)
elif op == "-":
    print("The difference is:", num1 - num2)
elif op == "*":
    print("The product is:", num1 * num2)
elif op == "/":
    print("The division is:", num1 / num2)
elif op == "%":
    print("The modulus is:", num1 % num2)
elif op == "//":
    print("The floor division is:", num1 // num2)
elif op == "**":
    print("The exponentiation is:", num1 ** num2)
else:
    print("Invalid operator")