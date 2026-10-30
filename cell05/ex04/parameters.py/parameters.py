#!/usr/bin/env python3
import sys

def main():
    # sys.argv contains script name as the first element, so subtract 1 for the parameter count
    num_params = len(sys.argv) - 1
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()