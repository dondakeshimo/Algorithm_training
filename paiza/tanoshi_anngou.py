
# coding: utf-8

# In[22]:

n_T = [i for i in input().split()]
number = int(n_T[0])
replacer = n_T[1]
strings = input()


# In[23]:

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = {" ": " "}
for i in range(26):
    key[alphabet[i]] = replacer[i]


# In[26]:

for n in range(number-1):
    temp_list = []
    for i in range(26):
        temp = key[replacer[i]]
        temp_list.append(temp)
    replacer = "".join(temp_list)


# In[27]:

reverse_key = {" ", " "}
for i in range(26):
    key[replacer[i]] = alphabet[i]


# In[28]:

answer = ""
for s in strings:
    answer = answer + key[s]

print(answer)


# In[ ]:



