import matplotlib.pyplot as plt 
import numpy
import math
from pylab import *

def parabola(x,a,b,c):
	return a*x**2+b*x+c

#Takes 3 input values
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = b**2-4*a*c #calculating determinant

#vertex of a parabola gives highest and lowest points on it
x_ver = -b/(2*a)
y_ver = a*x_ver**2+b*x_ver+c
vertex = [x_ver,y_ver]
print('The calculated vertex is ',vertex)

if d < 0:
	print('This Quadratic equation has no real solution ')
elif d == 0:
	x = (-b + math.sqrt(d))/(2*a)
	print('This Quadratic equation has one solution: ',x)
else: 
	x1 = (-b + math.sqrt(d))/(2*a)
	x2 = (-b - math.sqrt(d))/(2*a)
	print('This Quadratic equation has two solutions: ', x1, 'and ', x2)

x = np.linspace(-10,10,1000)
y = parabola(x,a,b,c)

plt.plot(x,y)
plt.plot([x_ver],[y_ver],marker = 'o',color = 'red',linestyle = 'none')
plt.plot([0],[c],marker = 'o',color = 'green',linestyle = 'none')
plt.axvline(x = x_ver)
plt.grid(True)
plt.gca().spines['left'].set_position(('data',0))
plt.gca().spines['bottom'].set_position(('data',0))
plt.xlim((-10,10))
plt.ylim((-10,10))
plt.show()
plt.close()


