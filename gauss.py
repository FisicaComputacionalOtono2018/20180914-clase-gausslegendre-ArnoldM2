#Alumno: Arnold Morales Morales
#Fecha: 13 de Septiembre de 2018
#Gauss

n = int (input ('Dame un numero entre [0,3]:'))
x = int (input ('Dame el valor de x que quieres evaluar:'))

if n==1:
 Pn=x
else:
 Pn=((2*n-1)/2)*(x**n)-(2*(n-1)-1)/2

print 'La derivada',n,'de la funcion, evaluada en',x,'es:',Pn
