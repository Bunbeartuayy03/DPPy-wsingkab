#!/usr/bin/env python3

def main():
    try:
        user_input = input("Give me a number: ")
        num = float(user_input)
        
        # Check if the float is equal to its integer conversion
        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("Invalid number.")

if __name__ == "__main__":
    main()