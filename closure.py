#! /usr/bin/python3

def  f(a):
	def g(b,c):
		return a * (b+c)

	return g	

x = f(1)
print(x(2,3))

k = f(1)(2,3)

print(k)
