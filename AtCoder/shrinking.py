
# coding: utf-8

# In[53]:

strings = input()


# In[61]:

answers = []
temp_diff = 0

for s in strings:
    target_index = -1 
    answer = 0
    index = []
    while True:
        target_index = strings.find(s, target_index + 1)
        if target_index == -1:
            break
        else:
            index.append(target_index)
            if len(index) > 1:
                temp_diff = index[-1] - index[-2]
            else:
                temp_diff = index[0]
            if temp_diff > answer:
                answer = temp_diff
                
    answer -= 1
    temp_diff = len(strings) - index[-1] - 1
    print(answer, temp_diff)
    if temp_diff > answer:
        answer = temp_diff
        
    answers.append(answer)


# In[62]:

print(min(answers))


# In[ ]:



