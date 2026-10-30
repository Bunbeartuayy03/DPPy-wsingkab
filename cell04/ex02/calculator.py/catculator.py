#!/usr/bin/env python3

def main():
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 // num2 if num1 % num2 == 0 else num1 / num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

if __name__ == "__main__":
    main()