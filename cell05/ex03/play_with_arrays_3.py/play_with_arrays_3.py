#!/usr/bin/env python3

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = {x + 2 for x in original_array if x > 5}

    print(original_array)
    print(new_array)

if __name__ == "__main__":
    main()