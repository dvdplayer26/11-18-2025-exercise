# 11-18-2025-exercise

x = float(input("Please type in the first number: "))
y = float(input("Please type in the second number: "))

if x > y:
    print(x," is greater than ",y)
elif y > x:
    print(y," is greater than ",x)
else:
    print("Both ",x," and ",y," are equal!")