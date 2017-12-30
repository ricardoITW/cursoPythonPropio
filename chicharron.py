#!/usr/bin/python
import math
a=input("introduce a: ")
b=input("introduce b: ")
c=input("introduce c: ")

x1 = (-b+math.sqrt(pow(b,2)-(4*a*c)))/(2*a) 
x2 = (-b-math.sqrt(pow(b,2)-(4*a*c)))/(2*a)

print 'el valor de x1 es: ',float(x1)
print 'el valor de x2 es: ',float(x2)
