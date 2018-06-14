
# coding: utf-8

# In[1]:

M_N = [int(i) for i in input().split()]
machine_num = M_N[0]
okashi_num = M_N[1]

m = [int(input()) for i in range(machine_num)]


# In[14]:

rest = 1000000
pack = 0
for i, num in enumerate(m, 1):
    if rest > okashi_num % num:
        rest = okashi_num % num
        pack = num
        answer = i
    elif rest == okashi_num % num:
        if pack < num:
            pack = num
            answer = i

print(answer, pack, rest)


# In[ ]:



