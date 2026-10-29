
#!/usr/bin/env python3

first = int(input("Enter the first number: \n"))
second = int(input("Enter the second number: \n"))

result = first * second

print(f"The result of {first} * {second} is {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")