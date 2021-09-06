import requests,os,pprint, time, random
import json
from bs4 import BeautifulSoup

list1=[]
count=0
file1=json.load(open("web_task1.json","r"))
for i in file1:
    url=i["url"]
    dict1={}
    abc=random.randint(1,4)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")

    poster=soup.find("div",class_="ipc-poster").a["href"]
    

    # print(poster)

    poster1="https://www.imdb.com"+poster

    dict1["name"]=i["movies_name"]
    dict1["poster_image_url"]=poster1
    biodata=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA").text
    dict1["bio"]=biodata
    # list1.append(dict1)
    # print(list1)
    

    para1=soup.find_all('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    for i in para1:

        para2=para1.find_all('li')

    
    # runtime=soup.find("span",class_="ipc-metadata-list-item__content-container")
    # print(runtime)

        for i in para2:
            if "Language" in i.text:
                l=[]
                a=i.find_all('a')
                for n in a:
                    l.append(n.text)

                dict1["langauge"]=l
            elif 'Country of origin' in i.text:
                a=i.find('a').text
                dict1["country"]=a

    para1=soup.find('div', class_="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr")
    para=para1.find_all('li')
    para3=para[-1].text.split(' ')

    # runtime=0
    k=para3[0][0]
    if (len(para3)) >1:

        k1=para3[1].split('m')
        runtime=(int(k)*60)+int(k1[0])
    else:
        runtime=(int(k)*60)




    dict1['runtime']=runtime

    # print(para3[0][0])
    # print(dict1)
    dram=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all Storyline__StorylineMetaDataList-sc-1b58ttw-1 esngIX ipc-metadata-list--base")
    # print(dram)
    namedata=dram.find_all("li",class_="ipc-metadata-list__item")
    
    l1=[]
    for j in namedata:
        if "Genre" in j.text:
            k=j.find_all('a')
            for l in k:
                l1.append(l.text)
            break
    dict1['genres']=l1
    
    der=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt")
    der1=der.find_all('li')
    # print(der1[0])
    der2=der1[0].find_all('a')

    l2=[]
    for k in der2:
        l2.append(k.text)
    dict1['director']=l2
    list1.append(dict1)
    time.sleep(abc)
    # print(dict1)
    # e()
    print(list1)

file1=open("web_task5.json","w")
filedata=json.dump(list1,file1,indent=4)
file1.close()









































































