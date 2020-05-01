#!/usr/bin/python3

from sys import argv

def main():
	if len(argv) == 1:
		print("{} arguments.".format(len(argv) - 1))
	elif len(argv) == 2:
		print(':')
	else:
		print('s:')
	for i in range(1, len(argv)):
		print('{:d}: {:s}'.format(i, argv[i]))	
if __name__ == "__main__":
	main()				
