#!/usr/bin/env python
# -*- encoding:utf8 -*-

from z3 import *
import sys

def getSolutions(l, found):

	result = []
	s = Solver()
	X = IntVector('x', l)

	s.add(X[0] * X[7] == 0x2250)
	s.add(X[1] * X[8] == 0xa29)
	s.add(X[2] * X[9] == 0x2341)
	s.add(X[3] * X[10] == 0x2832)
	s.add(X[4] * X[11] == 0x1089)
	s.add(X[5] * X[12] == 0x2d46)
	s.add(X[6] * X[13] == 0x2610)
	s.add(X[7] * X[14] == 0x948)
	s.add(X[0] + X[14] == 0x9b)
	s.add(X[1] + X[13] == 0x87)
	s.add(X[2] + X[12] == 0xd9)
	s.add(X[3] + X[11] == 0x9c)

	for i in xrange(l):
		s.add(X[i] >= 0) 
		s.add(X[i] <= 256) 

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
	getSolutions(15, 0)
	


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)