#Alumno: Arnold Morales Morales
#Fecha: 14 de Septiembre de 2018
#Diferenciacion de gauss

import numpy as np

n = float (input ('Dame el grado del polinomio entre [0,3]:'))
x = float (input ('Dame el valor de x que quieres evaluar:'))

if n==1:
 Pn = x
 dPn = 1
else:
 Pn = ((2*n-1)/2)*(x**n)-(2*(n-1)-1)/2
 dPn = (n/2)*(2*n-1)*(x**(n-1))

print 'La derivada',n,'de la funcion, evaluada en',x,'es:',Pn
print 'La derivada del polinomio de Legendre, evaluada en',x,'es:',dPn

if x==1:
 peso=0
else:
 peso = 2/((1-x**2)*(dPn**2))
print 'El peso es:',peso

b=1
a=-1
n=1000
dex=(b-a)/2






