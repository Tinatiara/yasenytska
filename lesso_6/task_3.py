a = int(input("Enter the first number of the range: "))
b = int(input("Enter the second number of the range: "))

for i in range(a,b):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)