#!/usr/bin/env python
# -*- encoding:utf8 -*-

from z3 import *
import sys

def getSolutions(l, found):

	result = []
	s = Solver()
	X = IntVector('x', l)


	for i in xrange(l):
		s.add(X[i] == X[len(X) - 1 - i])
		s.add(X[i] > 0x60)
		s.add(X[i] < 0x7B)


	while s.check() == sat:
		m = s.model()

		key = ""
		for i in xrange(l):
			key += chr(m[X[i]].as_long())
		print "Found len %d key (item nº%d)! -> %s" % (l, found + len(result), key)

		result.append(m)

		block = []
		for d in m:
			c = d()
			block.append(c != m[d])

		s.add(Or(block))

		result.append(m)

	return len(result) + found


def main():
	f = 0
	for i in xrange(30, 40):
		f = getSolutions(i, f)
	


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)