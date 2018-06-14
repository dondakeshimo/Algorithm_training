
# coding: utf-8

# In[20]:

N = input()
N_list = [int(s) for s in N]
N = int(N)


# In[21]:

f_x = sum(N_list)


# In[22]:

if N % f_x == 0:
    print('Yes')
else:
    print('No')


# In[ ]:



