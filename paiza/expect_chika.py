
# coding: utf-8

# In[11]:

x, y = [int(i) for i in input().split()]
k = int(input())
N = int(input())

price = []
for j in range(N):
    x_i, y_i, p_i = [int(i) for i in input().split()]
    distance = (x - x_i)**2 + (y - y_i)**2
    price.append({"x": x_i, "y": y_i, "p": p_i, "dis": distance})
    
price = sorted(price, key=lambda x:x["dis"])


# In[13]:

temp = 0
for i in range(k):
    temp += price[i]["p"]
    
f = temp / k
i = temp // k

if int(f * 2) > i * 2:
    answer = i + 1
else:
    answer = i


print(answer)


# In[ ]:



