#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Задача 1. Сигма ген совокупности известна, считаем критерий Z
import numpy as np
from scipy import stats

sima=16
z=1.96
m=80
n=256
t1=m+(z*16/np.sqrt(n))
t2=m-(z*16/np.sqrt(n))
t1, t2


# In[3]:


#Задача2. Сигма ген совокупности неизвестна, считаем критерий t
x=np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])


# In[5]:


#найдем среднее по выборке
x_mean=np.mean(x)
x_mean


# In[6]:


#найдем дисперсию
d_x=np.var(x,ddof=1)
d_x


# In[7]:


#найдем критерий стьюдента для доверительного интервала 95%, кол-во степеней  сравнения 10-1=9
t=stats.t.ppf(0.975,9)
t


# In[8]:


#найдем верхнюю границу интервала
t1=x_mean+t*d_x/np.sqrt(10)
t1


# In[9]:


#найдем нижнюю границу интервала
t2=x_mean-t*d_x/np.sqrt(10)
t2


# In[ ]:




