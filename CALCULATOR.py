def add(a,y):
    return a+y
def sub(a,y):
    return a-y
def mul(a,y):
    return a*y
def div(a,y):
    if y == 0:
        return  "no result"
    return a/y

print("select task")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")

choice = input("Enter Choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", mul(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Invalid input")
