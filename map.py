#! /usr/bin/python3

def f2c(x):
	return( (float(9) / 5) * x+ 32)

cel_list = [2,34,4,45,20,-8]

cel = list(map(f2c,cel_list))

print(cel)
