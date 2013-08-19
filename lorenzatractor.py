#coding:utf-8
import unittest
import scipy.integrate
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class LorenzAtractor(object):
    def __init__(self,p,r,b,t,x,y,z):
        self._p=p
        self._r=r
        self._b=b
        self._t=t
        self._x=x
        self._y=y
        self._z=z

    def Func(self,result,t0):
        F_dx=lambda result: -self._p*result[0]+self._p*result[1]
        F_dy=lambda result: -result[0]*result[2]+self._r*result[0]-result[1]
        F_dz=lambda result: result[0]*result[1]-self._b*result[2]
        return [F_dx(result),F_dy(result),F_dz(result)]
       
    def calc(self):
        initval=[self._x,self._y,self._z]
        result=scipy.integrate.odeint(self.Func,initval,self._t)
        self.show(result[:].T[0],result[:].T[1],result[:].T[2])
        return 0
    def show(self,x,y,z):
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        ax.plot(x,y,z,'o',ms=4,mew=0.5)
        plt.show()
#p=10.0
#r=28.0
#b=8/3.0
##b=2.6666
#x=0.1
#y=0.1
#z=0.1
#tt=numpy.arange(0,10,1)
#lorenz=LorenzAtractor(p,r,b,tt,x,y,z)
#lorenz.calc()

class LorenzTest(unittest.TestCase):
    p=10.0
    r=28.0
    b=8/3.0
    x=0.1
    y=0.1
    z=0.1
    t=numpy.arange(0,100,0.01)
    lorenz=LorenzAtractor(p,r,b,t,x,y,z)
    def test_param(self):
        self.assertEqual(10,self.lorenz._p)
        self.assertEqual(28,self.lorenz._r)
        self.assertEqual(8/3.0,self.lorenz._b)
        self.assertEqual(self.x,self.lorenz._x)
        self.assertEqual(self.y,self.lorenz._y)
        self.assertEqual(self.z,self.lorenz._z)
        self.assertEqual(self.t[0],self.lorenz._t[0])
    def test_calc(self):
        self.assertEqual(0,self.lorenz.calc())
unittest.main()
