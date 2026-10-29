#!/usr/bin/env python3

def main():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        if number == 0:
            print("This number is equal to zero.")
        else:
            print("This number is different from zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()