#!/usr/bin/env python
# coding: utf-8

# calculate NPV. The rate is a float and the cash flows and investment are in a list.

# In[2]:


def npv(CFList, r):
    return (sum (f/((1 + r)** i)
for i, f in enumerate (CFList, 1)))-invest

CFList = [200,300,400,500]
r=0.02
invest = 1000
npv (CFList, r)


# create a function to calcule IRR. In order to calculate IRR you may aproximate the follwoing expression: rate= rate*(1-NPV(CFList, rate)/invest).

# In[5]:


IRR = r*(1-npv(CFList, r)/invest)
print (IRR)


# create a function for payback period

# In[4]:


def payback (invest,CFList):
    return ((invest/f)
for f in enumerate (CFList))
payback (invest, CFList)

