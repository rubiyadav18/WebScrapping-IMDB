import json,os
f=open("web_task1.json","r")
data=json.load(f)
print(data)

empty=[]
dict1={}

for i in data:
    if int(i["year"]) not in empty:
        empty.append(int(i['year']))

empty.sort()
print(empty)

for j in  empty:
    store_year=[]
    for k in data:
        if j==int(k['year']):
            store_year.append(k)
    dict1[j]=store_year
file=open("web_task2.json","w")
fil1edata=json.dump(dict1,file,indent=4)
file.close()
# print(dict1)

    

