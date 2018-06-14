
# coding: utf-8

# In[5]:

vals = input().split()
a=int(vals[0])
b=int(vals[1])
c=int(vals[2])
d=int(vals[3])

if c==d:
    print('miss')
else:
    a1=(a-b*d)/(c-d)
    a2=(-a+b*c)/(c-d)

    #print(a1,a2)

    if a1>0 and a2>0 and a1==int(a1) and a2==int(a2):
        print(int(a1),int(a2))
    else:
        print('miss')


# In[ ]:



