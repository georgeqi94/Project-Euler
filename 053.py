"""
Project Euler Problem 53
========================

There are exactly ten ways of selecting three from five, 12345:

           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, nCr(5,3) = 10.

In general,

nCr(n,r) = n!/(r!(n-r)!), where r =< n, n! = n * (n1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: nCr(23,10) =
1144066.

How many values of nCr(n,r), for 1 =< n =< 100, are greater than one-million?
"""

import math

def nCr(n, r):
	return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

count = 0
mil = 10 ** 6
for n in xrange(23, 101):
	for r in xrange(1, n):
		if nCr(n,r) > mil: count += 1
print count