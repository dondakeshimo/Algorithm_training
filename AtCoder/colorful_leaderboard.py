
# coding: utf-8

# In[1]:

number = int(input())
rate = [int(i) for i in input().split()]


# In[7]:

counter = {}
for r in rate:
    if 1 <= r < 400:
        counter["grey"] = counter.get("grey", 0) + 1
    if 400 <= r < 800:
        counter["brown"] = counter.get("brown", 0) + 1
    if 800 <= r < 1200:
        counter["green"] = counter.get("green", 0) + 1
    if 1200 <= r < 1600:
        counter["sky"] = counter.get("sky", 0) + 1
    if 1600 <= r < 2000:
        counter["blue"] = counter.get("blue", 0) + 1
    if 2000 <= r < 2400:
        counter["yellow"] = counter.get("yellow", 0) + 1
    if 2400 <= r < 2800:
        counter["orange"] = counter.get("orange", 0) + 1
    if 2800 <= r < 3200:
        counter["red"] = counter.get("red", 0) + 1
    if 3200 <= r:
        counter["color"] = counter.get("color", 0) + 1

answer = 0
for k, v in counter.items():
    if not v == 0:
        answer += 1
        
if counter.get("color", 0) == 0:
    print(str(answer) + " " + str(answer))
else:
    if answer == 1:
        print("1 " + str(counter["color"]))
    else:
        print(str(answer-1) + " " + str(answer-1+counter["color"]))


# In[ ]:



