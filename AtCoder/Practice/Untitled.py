
# coding: utf-8

# In[1]:

num = int(input())
cards = [input() for i in range(num)]
x_num = []


# In[4]:

for card in cards:
    even_list = card[0:16:2]
    odd_list = card[1:16:2]
    


# In[6]:

even = sum([int(i) for i in even_list])


# In[8]:

l = [[1, 2, 3], [2,3,4]]


# In[9]:

for a, b, c in l:
    print(a, b, c)


# In[13]:

L_n_m = [int(i) for i in input().split()]
lines = []
position = 1
next_position = 1
height = L_n_m[0]

for l in range(L_n_m[2]):
    lines.append([int(i) for i in input().split()])
    
while not (height==0):
    for a, b, c in lines:
        if (position == a and height == b):
            next_position = a + 1
            next_height = c - 1
        elif (position == a+1 and height == b):
            next_position = a
            next_height = c -1 
    if (position == next_position):
        height -= 1
    else:
        position = next_position
        height = next_height
    print(position, height)
            
print(position)


# In[ ]:



