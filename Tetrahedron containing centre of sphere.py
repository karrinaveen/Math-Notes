# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:45:41 2022

@author: Navi
"""

import random
from math import pi
import math
import numpy as np

x1 = 0
count = 0
while (x1 < 10000):
    x1=x1+1
    angle1= [random.random()*2*pi for x in range(4)]
    angle2= [random.random()*pi for x in range(4)]
    p=[]
    for y in range(4): p.append((math.sin(angle1[y]),math.cos(angle1[y])*math.sin(angle2[y]),math.cos(angle1[y])*math.cos(angle2[y]),1))
    a_4_4= np.transpose(np.array(p))
    b=[0]*3+[1]  
    a_inverse=np.linalg.inv(a_4_4)
    k = np.linalg.inv(a_4_4).dot(b)
    if (k>0).all(): count+=1
    #if (k<0).all():count+=1
print(count)