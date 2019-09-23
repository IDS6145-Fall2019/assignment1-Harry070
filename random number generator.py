#!/usr/bin/env python
# coding: utf-8

# In[160]:


import numpy as np
import matplotlib.pyplot as plt

fig,(ax1, ax2)=plt.subplots(nrows=2, ncols=5)


numbers=100
a=np.random.random(numbers)
b=np.random.random(numbers)
ax1.plot(a,b)
ax1.set_xlabel("Days of January")
ax1.set_ylabel("passenger number")


np.random.seed(1)
numbers=500
c=np.random.random((numbers))
d=np.random.random(numbers)
ax2.plot(c,d)
ax2.set_xlabel("Days of January")
ax2.set_ylabel("passenger number")


np.random.seed(1)
zion=1000
e=np.random.random((zion))
f=np.random.random(zion)
ax3.plot(e,f)
ax3.set_xlabel("Days of January")
ax3.set_ylabel("passenger number")

np.random.seed(1)
numbers=2000
g=np.random.random((numbers))
h=np.random.random(numbers)
ax4.plot(g,h)
ax4.set_xlabel("Days of January")
ax4.set_ylabel("passenger number")


np.random.seed(1)
numbers=5000
g=np.random.random(numbers)
h=np.random.random(numbers)
ax5.plot(g,h)
ax5.set_xlabel("Days of January")
ax5.set_ylabel("passenger number")


a=np.random.randint(15, size=100)
b=np.random.randint(15,size=100)
ax6.plot(a,b)
ax6.set_xlabel("Days of January")
ax6.set_ylabel("passenger number")


c=np.random.randint(15, size=500)
d=np.random.randint(15,size=500)
ax7.plot(c,d)
ax7.set_xlabel("Days of January")
ax7.set_ylabel("passenger number")

e=np.random.randint(15, size=1000)
f=np.random.randint(15,size=1000)
ax8.plot(e,f)
ax8.set_xlabel("Days of January")
ax8.set_ylabel("passenger number")

g=np.random.randint(15, size=2000)
h=np.random.randint(15,size=2000)
ax9.plot(g,h)
ax9.set_xlabel("Days of January")
ax9.set_ylabel("passenger number")


i=np.random.randint(15, size=5000)
j=np.random.randint(15,size=5000)
ax10.plot(i,j)
ax10.set_xlabel("Days of January")
ax10.set_ylabel("passenger number")


# In[ ]:





# In[ ]:





# In[ ]:




