
# coding: utf-8

# In[34]:

import numpy as np


# In[35]:

N = int(input())
trees = [[int(j) for j in input().split(" ")] for i in range(N)]


# In[71]:

street = [0 for i in range(10001)]


# In[72]:

def calc_intersection(a, b, r):
    if b > r:
        return -1
    else:
        x_1 = int(np.ceil(a - np.sqrt(r**2 - b**2)))
        x_2 = int(np.floor(a + np.sqrt(r**2 - b**2)))
        return x_1, x_2 


# In[74]:

def count_trees(tree, street):
    if tree[0] < 0:
        tree[0] = 0
    if tree[1] > 10000:
        tree[1] = 10000

    if tree[0] == tree[1]:
        street[tree[0]] += 1
    else:
        for i in range(tree[0], tree[1]):
            street[i] += 1
    return street


# In[75]:

for tr in trees:
    tree = calc_intersection(tr[0], tr[1], tr[2])
    street = count_trees(tree, street)


# In[76]:

answer = max(street)


# In[77]:

print(answer)


# In[ ]:



