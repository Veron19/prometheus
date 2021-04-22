import math
import sys

#a = int(input("input a: "))         # input ai
a = sys.argv[1]
#b = int(input("input b: "))          # input b
b = sys.argv[2]
print ("b= "+str(b))
#print (b)
if int(b) < 0:                                  # if n<0 then n! is undefined
  print('b should not be less than zero')
  exit ()
#x = a*b + b


# z = (a*b) ** (1./2)/math.exp( a )*b
# print ("z= "+str(z))
# k = a*math.exp( 2*a/b )
# print ("k= "+str(k))
# h = z + k
# print ("h= "+str(h))
t = (a*b) ** (1./2)/math.exp( a )*b + a*math.exp( 2*a/b )
print ("t= "+str(t))
