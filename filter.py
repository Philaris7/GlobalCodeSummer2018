#! /usr/bin/python3

def too_old(x): return x > 30
ages = [20,34,45,3,65,5]
old = list(filter(too_old, ages))

print(old)
