#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Задача 3. Используя эти данные построить 95% доверительный интервал для разности среднего
#роста родителей и детей.

import numpy as np
from scipy import stats

mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers, daughters


# In[2]:


#найдем среднее по выборкам
m_mean=np.mean(mothers)
d_mean=np.mean(daughters)
d_mean, m_mean


# In[3]:


#найдем несмещенную дисперсию в выборках
d_var=np.var(daughters, ddof=1)
m_var=np.var(mothers, ddof=1)
m_var, d_var


# In[4]:


#найдем кол-во элементов в выборке
m_len=len(mothers)
d_len=len(daughters)
m_len, d_len


# In[5]:


#найдем дельту разности средних
delta=m_mean-d_mean
delta


# In[6]:


#найдем общую дисперсию по выборкам
D=(d_var+m_var)/2
D


# In[10]:


#Найдем стандартную ошибку разницы средних
SE=np.sqrt(D/m_len+D/d_len)
SE


# In[11]:


#Сигма ген совокупности неизвестна, считаем критерий t 95%, кол-во степеней сравнения=2*(n-1)
t=stats.t.ppf(0.975,18)
t


# In[12]:


#Найдем интервал для выборок
t1=delta-t*SE
t2=delta+t*SE
t1, t2


# In[ ]:




