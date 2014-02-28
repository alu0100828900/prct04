#! /usr/bin/python

a = float(raw_input('valor de a: '))
b = float(raw_input('valor de b: '))

if a != 0:
   x = -b/a
   print 'solucion:', x
if a == 0 and b == 0:
   print 'la ecuacion tiebe infinitas soluciones.'
if a == 0 and b!=0:
   print 'la ecuacion no tiene solucion.'
