# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 00:12:35 2022

@author: eduar
"""

import math
import numpy as np
import matplotlib.pyplot as plt 
X1=[]
Y1=[]
Theta=[]
x=1
y=0.25
Vel=9.425
omega=12.43
theta=90
X1.append(x)
Y1.append(y)
Theta.append(theta)
espacio=np.arange(0, 1, 0.01)
thetaP=theta
xp=x
yp=y
for i in espacio:
    thetaA=thetaP+omega*0.01
    xa=xp+Vel*math.cos(thetaA)*0.01
    ya=yp+Vel*math.sin(thetaA)*0.01
    X1.append(xa)
    Y1.append(ya)
    Theta.append(thetaA)
    thetaP=thetaA
    xp=xa
    yp=ya
    
plt.plot(X1,Y1)
plt.axis('square')

plt.show()
print("el valor inicial de x es "+str(x)+" y su valor final es "+ str(xa))
print("el valor inicial de y es "+str(y)+" y su valor final es "+str (ya))