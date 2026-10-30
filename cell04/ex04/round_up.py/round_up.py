#!/usr/bin/env python3
import math

def main():
    try:
        user_input = input("Give me a number: ")
        num = float(user_input)
        print(math.ceil(num))
    except ValueError:
        print("Invalid number.")

if __name__ == "__main__":
    main()