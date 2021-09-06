
import json,os
f=open("web_task4.json","r")

data=json.load(f)
# print(data)
list1=[]
c=0
dict1={}
for i in data:
    l=i["langauge"]
    # print(l)
    if l not in list1:
        list1.append(l)
        
for j in list1:
    c=0
    for i in data:
        if j ==i["langauge"]:
            c+=1
    dict1[c]=j
    # list1.append(dict1)
    # break
    print(list1)
f=open("web_task6.json","w")
data=json.dump(list1,f,indent=5)
f.close()











































