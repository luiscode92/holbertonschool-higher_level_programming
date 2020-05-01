#!/usr/bin/python3
from sys import argv
#update
def main():
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(sum)

if __name__ == "__main__":
    main()        
