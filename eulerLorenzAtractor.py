#coding:utf-8
import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.mplot3d import Axes3D

class LorenzAtractor(object):
    def __init__(self,p,r,b,t,dt,x,y,z):
        self._p=p
        self._r=r
        self._b=b
        self._t=t
        self._dt=dt
        self._x=x
        self._y=y
        self._z=z
    def calc(self):
        resultx=[]
        resulty=[]
        resultz=[]
        F_dx=lambda value: -self._p*value[0]+self._p*value[1]
        F_dy=lambda value: -value[0]*value[2]+self._r*value[0]-value[1]
        F_dz=lambda value: value[0]*value[1]-self._b*value[2]
        for i in range(0,len(self._t)):
            xx=F_dx([self._x,self._y,self._z])*self._dt
            yy=F_dy([self._x,self._y,self._z])*self._dt
            zz=F_dz([self._x,self._y,self._z])*self._dt
            self._x+=xx
            self._y+=yy
            self._z+=zz
            resultx.append(self._x)
            resulty.append(self._y)
            resultz.append(self._z)
        self.show(resultx,resulty,resultz)
    def show(self,x,y,z):
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        ax.plot(x,y,z,'o')
        plt.show()
p=10.0
r=28.0
b=8/3.0
x=0.1
y=0.1
z=0.1
dt=0.01
t=numpy.arange(0,100,dt)
LorenzAtractor(p,r,b,t,dt,x,y,z).calc()
