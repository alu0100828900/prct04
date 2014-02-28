#! /usr/bin/python
from math import sqrt

a = float(raw_input('valor de a:'))
b = float(raw_input('valor de b:'))
c = float(raw_input('valor de c:'))

if a == 0 and b==0 and c==0:
  print ' la ecuacion tiene infinitas soluciones'
elif a == 0 and b==0:
     print ' la ecuacion no tiene solucion' 
elif a == 0:
      x=-c/b
      print 'la solucion de la ecuacion es: x=%4.3f' % x

else:
       x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
       x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
       print 'las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)
