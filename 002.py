"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""

def gen_fib(n):
	fib_values = [1,2]
	for i in range(2, n+1):
		fib_values.append(fib_values[i-1] + fib_values[i-2])
	return fib_values[n]

def find_index(upper):
	index = 0
	while(gen_fib(index) < upper):
		index += 1
	return index

print sum([gen_fib(n) for n in range(32) if gen_fib(n) % 2 == 0])