#!/usr/bin/env python3
import sys

def main():
    # If any command-line arguments are passed (other than script name), print "none"
    if len(sys.argv) > 1:
        print("none")
        return

    i = 0
    while i <= 10:
        print(f"Table de {i}:", end="")
        j = 0
        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
        print()  # Newline after each row
        i += 1

if __name__ == "__main__":
    main()