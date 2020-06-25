print("Select the operation: ")
print("1. Show the list")
print("2. From the biggest number to the smallest")
print("3. All number devided on 7")
print("4. All number devided on 5")

while True:
    choice=input("Enter choice(1/2/3/4): ")
    
    if choice in ("1", "2", "3", "4"):
        a = int(input("Enter the first number of the range: "))
        b = int(input("Enter the second number of the range: "))
        if choice == "1": 
            for i in range(a, b):
               print(i, end=" ")
               
        if choice == "2":
            for i in range(b-1, a-1, -1):
               print(i, end=" ")
               
        if choice == "3":
            for i in range(a, b):
               if i % 7 == 0:
                  print(i, end=" ")
                  
        if choice == "4":
            for i in range(a, b):
               if i % 5 == 0:
                  print(i, end=" ")