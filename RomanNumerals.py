#! /usr/bin/python

roman_num = None
num = input("Enter a number : ")
try:
    int(num)
except ValueError as err:
    print(err, "Enter an integer")

rnumerals = { 1 : "I", 5 : "V" ,  10 : "X", 50 : "L",100 : "C" , 500 :"D" , 1000 : "M" }
5

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000


i = ""
v = ""
x = ""
l = ""
c = ""
d = ""
m = ""


#8976

if len(num) ==4:
    num = int(num)
    msize = num // 1000
    mrem = num % 1000
    m =  msize * str(rnumerals[1000])
    

    dsize = num //500
    drem = num % 500
    d = dsize * str(rnumerals[500])
    
    csize = num // 100
    crem = num % 100
    c = csize * str(rnumerals[100])
    
    lsize = num // 50
    rem = num % 50
    l = lsize * str(rnumerals[50])

    xsize = num // 10
    xrem = num % 10
    x = xsize * str(rnumerals[10])
    
    vsize = num // 5
    vrem = num % 5
    v = vsize * str(rnumerals[5])

print(msize)

print(l + x + v + str(vrem))

