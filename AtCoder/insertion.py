
# coding: utf-8

# In[38]:

number = int(input())
strings = input()


# In[39]:

while True:
    counter = 0

    for s in strings:
        if s == "(":
            counter += 1
        else:
            if counter > 0:
                counter -= 1
            else:
                strings = "(" + strings
                counter = -1
                break
        
    if counter > 0:
        strings = strings + ")" * counter
        
    if counter == 0:
        break

print(strings)


# In[ ]:



