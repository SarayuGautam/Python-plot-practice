import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2*np.pi,2*np.pi,100)
y=3*x*np.sin(x)-2*x
z=3*np.sin(x)+3*np.cos(x)*x-2
plt.figure(1)
plt.plot(x,y,'r',x,z,'k')
plt.title('Plot of a function and its derivative')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(('$f(x)$',"$f'(x)$"))
plt.show()

t=np.linspace(0,7,50)
x=0.4*t**3-2*t**2-5*t+13
v=0.4*3*t**2-2*2*t-5
a=0.4*6*t-4*t

plt.figure(2)
plt.subplot(5,1,1)
plt.plot(t,x,'g')
plt.title('Position, velocity and acceleration of particle wrt time')
plt.xlabel('time')
plt.ylabel('p ($m$)')


plt.subplot(5,1,3)
plt.plot(t,v,'b')
plt.xlabel('time')
plt.ylabel('v ($ms^-1$)')



plt.subplot(5,1,5)
plt.plot(t,a,'r')
plt.xlabel('time')
plt.ylabel('a ($ms^-2$)')
plt.show()


theta = np.linspace(0,np.pi*0.5,50)
g= 9.8
v1 = 50
v2 = 75
v3 = 100
plt.figure(3)

r1= (v1**2/(g))*np.sin(2*theta)
r2= (v2**2/(g))*np.sin(2*theta)
r3= (v3**2/(g))*np.sin(2*theta)

plt.plot(theta,r1,'r',theta,r2,'g',theta,r3,'b')
plt.legend(('R1','R2','R3'))
plt.title('Range of Projectile projected at diiferent initial velocity(m$s^-1$)')
plt.xlabel('theta in radian')
plt.ylabel('Range in meters')
plt.show()



t=np.linspace(0,20,50)
plt.figure(4)

x=(2+4*np.cos(t))*np.cos(t)
y=(2+4*np.cos(t))*np.sin(t)
z=t**2

plt.plot(t,x,label='x')
plt.plot(t,y,label='y')
plt.plot(t,z,label='z')
plt.legend(('x','y','z'))
plt.title('Position of a particle with respect to time')
plt.xlabel('time(t)')
plt.ylabel('position')
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(5)
ax = Axes3D(fig)
x=np.linspace(-3,3,300)
y=x
x,y=np.meshgrid(x,y)
z=(x*y*(x**2-y**2))/(x**2+y**2)
ax.plot_surface(x,y,z)
plt.title('3d plot of a function')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.ylabel('z-axis')
plt.show()


fig = plt.figure(6)
ax = Axes3D(fig)
x=np.linspace(-5,5,200)
y=x
x,y=np.meshgrid(x,y)
z=np.cos(x)*np.cos(y)*np.e**(-((x**2+y**2)**0.5)*0.25)
ax.plot_surface(x,y,z,cmap='gist_earth')
plt.title('3d plot of function with exponential and trigonometric functions')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.ylabel('z-axis')
plt.show()












