#!/usr/bin/env python
# coding: utf-8

# In[1]:


#problem 1
sum = 0
n = 11
for i in range(n):
    #userinput = input('enter a value : '')
    userinput = i
    sum = userinput + sum 
average = sum / (n-1)
print(average)
    


# In[2]:


#problem 2
l = [24,50,29]
result = 0
for val in l:
    print(end='\n')
    for i in range(1,11):
        result = val*i
        print('{} * {} = {}'.format(val,i,result))
        #'I love {} for "{}!"'.format('Geeks', 'Geeks')


# In[3]:


#problem 3
userinput= 1
while userinput != 'q':
    userinput = (input('enter a val : '))
    print("press 'q' to quit")
    if (userinput.isnumeric()):
        print('the value entered is :', userinput)    
    elif userinput == 'q' :
        print("you exited")
    elif not (userinput.isnumeric()) :
        print("enter an integer value")


# In[5]:


#problem 4
for val in range(100,501):
    length = len(str(val))
    sum1 = 0
    temp = val
    while temp > 0:
        last = temp%10
        sum1 += last**length
        temp//=10
    if val == sum1: 
        print(val,"is an ARMSTRONG number")  
    


# In[6]:


#problem 5
for i in range(1,51):
    if (i % 3 == 0 and i % 5 == 0):
        print('fizzbuzz')
    elif i%5==0:
        print('buzz')
    elif i%3==0:
        print('fizz')
    else:
        print(i)


# In[ ]:




