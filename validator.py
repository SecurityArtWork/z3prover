#!/usr/bin/env python

def isLower(key):
	for letter in key:
		if ord(letter) <= 0x60 or ord(letter) >= 0x7B:
			return False

	return True

def isPal(key):
	for i in xrange(len(key) / 2):
		if key[i] != key[len(key) - 1 - i]:
			return False
	return True


def validate(key):
	if not isLower(key):
		return False
	if not isPal(key):
		return False
	return True
	

def main():

	key = raw_input("> Enter your key: ")

	if validate(key): 
		print "Valid key!"
	else: 
		print "Try again..."

if __name__ == "__main__":
	main()