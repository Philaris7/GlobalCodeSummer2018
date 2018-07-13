#! /usr/bin/python
def printStar(num):
	for x in range(1,num+1):
		print(x * "*")
	while(num != 0):
		num  -= 1
		print(num * "*")

printStar(5)

