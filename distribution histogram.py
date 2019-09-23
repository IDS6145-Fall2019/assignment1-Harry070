#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import matplotlib.pyplot as plt
##normal distribution
a=0
b=0.1
c=np.random.normal(a,b,100)
d=np.random.normal(a,b,500)
e=np.random.normal(a,b,1000)
f=np.random.normal(a,b,2000)
g=np.random.normal(a,b,5000)
plt.hist(c,bins=100)


#binomial

n=5
p=0.4
h=np.random.binomial(n,p,100)
i=np.random.binomial(n,p,500)
j=np.random.binomial(n,p,1000)
k=np.random.binomial(n,p,2000)
l=np.random.binomial(n,p,5000)



#uniform

m=np.random.uniform(-4,4,100)
n=np.random.uniform(-4,4,500)
q=np.random.uniform(-4,4,1000)
r=np.random.uniform(-4,4,2000)
s=np.random.uniform(-4,4,5000)


# In[ ]:




