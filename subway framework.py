#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
class Escalator:
    def _init_(self,a=5.0,b=8.0,c=50.0):
        self.speed=a
        self.time=b
        self.riders=c
    
    def clock(self):
        return"time of day"
    def riders(self):
        print("number of people who ride")
    
class Hall:
    def _init_(self, d=4000):
        self.riders=d
    def capacity(self, e=5000):
        print("The amount of people the hall can hold")
    
class platform:
    def _init_(self,f=500):
        platcap=f
        print ("Amount of people that can be held ")
class train:
    def _init_(self, g="ID Number",h=8.0,i=500):
        self.id=g
        self.ontime=h
        self.passangers=i
class main():
        my_out_come=Hall
        print(my_out_come,"Hall is not filled to capacity")
        print(Escalator)


# In[ ]:





# In[ ]:




