
import json,os
file1=open("web_task4.json","r")
data=json.load(file1)
dir_list=[]
all_dir_list=[]
moves_dict={}
for i in data:
    # print(i)
    k=i["director"]
    # print(k)
    for j in k:
        if j not in dir_list:

            dir_list.append(j)
            # print(dir_list)
        else:

            all_dir_list.append(j)
            # print(all_dir_list)
for c in dir_list:
    print(c)
    moves_dict[c]=1

    # print(moves_dict)
    for l in dir_list:
        if c==l:
            moves_dict[c]+=1

    print(moves_dict)
f=open("web_task7.json","w")
data=json.dump(moves_dict,f,indent=5)
f.close()






















