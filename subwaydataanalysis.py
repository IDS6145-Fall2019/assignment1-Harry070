#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
data1=pd.read_csv("Desktop//CTA_-_Ridership_-_Daily_Boarding_Totals.csv")
##print(data1)
r=data1.rail_boardings.iloc[0:6]
b=data1.bus.iloc[0:6]
rm=statistics.mean(r)
rst=statistics.stdev(r)
print("subway data",r)
print("rail passanger mean:",rm)
print("rail passanger standard deviation:", rst)
bm=statistics.mean(b)
print("Bus passanger mean:",bm)
print("Bus passanger standard deviation", bm)
plt.plot(r)
plt.plot(b)
plt.xlabel("Days of January")
plt.ylabel("passenger number")
plt.show()


# In[ ]:




