#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


df=pd.read_csv('ID.csv')
print(df)


# In[15]:


ide=list(df.ID)
print(ide)


# In[16]:


from urllib.request import urlopen


# In[17]:


u="http://api.icndb.com/jokes/"

ur=urlopen(u)
data =ur.read()
print(data)


# In[ ]:



'''
filename="chuck.csv"
import requests
import json
iden=[]
jokes=[]
with open(filename,'w',encoding='utf-8') as f:
    f.write("ID,Joke\n")

    r=requests.get(u)
    json_data=json.loads(r.content)
    j=list(json_data['value'])
    for i in j:
        for k in ide:
            if k==i['id']:
                iden.append(k)
                jokes.append(i['joke'])
                f.write(str(k)+",")
                i['joke']=i['joke'].replace(',','')
                i['joke']+=i['joke']+','
                i['joke']=i['joke'][:-1]
                f.write(i['joke'])
                f.write("\n")
                
f.close()
'''


# In[18]:


filename="chuck.csv"
import requests
import json
iden=[]
jokes=[]

r=requests.get(u)
json_data=json.loads(r.content)
j=list(json_data['value'])
for i in j:
    for k in ide:
        if k==i['id']:
            iden.append(k)
            jokes.append(i['joke'])

d={'ID':iden,'Joke':jokes}
df=pd.DataFrame(d)
df.to_csv("chuck2.csv",index=False)

