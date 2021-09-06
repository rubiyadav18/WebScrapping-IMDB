import json,os
from bs4 import BeautifulSoup
file1=open("web_task1.json","r")
data1=json.load(file1)
print(data1)
dict1={}
list1=[]
for i in data1:
    link=i['url']

    id=link[-10:-1]
    print(id)
    file2=open("task8/"+id+".json","w")
    data2=json.dump(i,file2,indent=3)
    file2.close()



# "here i am cheking id exists or not "
# if i put same id so output is came exists


user=input("enter a id----")
if os.path.exists("task8/"+ user+".json"):
    print("exists")
else:
    print("not")


    

