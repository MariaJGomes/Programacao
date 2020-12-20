#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Verify if a value is an integer


# In[1]:


a=2


# In[3]:


print (type (a))


# In[ ]:


#2. Verify if a value is even


# In[4]:


a=3


# In[5]:


a % 2 == 0


# In[6]:


#3. Insert two numbers. Is the first is bigger than the second?


# In[9]:


num1 = input ("primeiro numero")


# In[10]:


type (num1)


# In[11]:


num1 = int(num1)


# In[12]:


num2 = int(input ("segundo numero"))


# In[13]:


num1>num2


# In[3]:


#4. Verify if one value is multiple of another


# In[1]:


a=15


# In[2]:


a % 5 == 0


# In[ ]:


#correção aula


# In[3]:


num1 =2
num2 =4


# In[5]:


num1 % num2 == 0 or num2 % num1 == 0


# In[2]:


#5. Calculate the interest earn by an investor that invested an amount of capital of 200 during three years with an interest rate of 3%


# In[3]:


i = (200*0.03*3)


# In[4]:


print (i)


# In[ ]:


#correção aula


# In[9]:


capital = 200
rate = 0.03
time = 3
interest = capital*rate*time 


# In[11]:


print (interest)


# In[ ]:


#6. Capital that an investor obtained after investing an amount of capital of 200 during three years with an interest rate of 3% (compound interest).


# In[13]:


capitalAcum=capital*(1+rate)**time


# In[14]:


capitalAcum


# In[ ]:


#7. Calculate your BMI (Body Mass Index)


# In[8]:


BMI= (53/(1.67**2))


# In[9]:


print (BMI)


# In[ ]:


#correção aula


# In[15]:


M = 53
H = 1.67
BMI = M/(H**2)


# In[16]:


print (BMI)


# In[ ]:


#8. Calculate the Golden ration:


# In[10]:


gr=(1+(5**1/2))


# In[11]:


print (gr)


# In[ ]:


#9. Calculate the NPV (Net present value) of an investment, considering an initial investment of 10000, the following Cashflows 2000, 30000, 4000, 4000 and 50000 and a discount rate of 10%.


# In[4]:


a=(2000/(1+0.1))


# In[6]:


b=(3000/(1+0.1))


# In[7]:


d=(4000/(1+0.1))


# In[8]:


c=(5000/(1+0.1))


# In[9]:


print ((a+b+(2*d)+c)-10000)


# In[ ]:


#10. Ask the user to insert name and age. Calculate the birth year. Print a result saying the 'this person was born in.'


# In[34]:


n = input ("insert your name")


# In[40]:


x = int(input ("insert your age"))


# In[41]:


from datetime import date


# In[42]:


today = date.today()


# In[43]:


today.year


# In[44]:


a = today.year - x


# In[47]:


print ("this person was born in" + str(a))


# In[ ]:


#11. Ask the user to insert forenames, surnames. Create a new variable (name) with your complete name.


# In[2]:


n= input ("insert your forenames")


# In[4]:


x= input ("insert your surnames")


# In[5]:


name = n + x


# In[6]:


print (name)


# In[ ]:


#12. Use the following method to show in which character appears the first "da"


# In[1]:


str.find (sub, start, end)

