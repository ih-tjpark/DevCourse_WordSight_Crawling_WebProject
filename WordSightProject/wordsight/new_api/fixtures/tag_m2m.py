import json
from new_api.models import *

newsAll = News.objects.all()
jsonDec = json.decoder.JSONDecoder()

for i in newsAll:
    tagList = jsonDec.decode(i.tag_list)
    print(tagList)
    if tagList and tagList[0]!='미분류' :
        for j in range(0,len(tagList),2):
            tag = Tag.objects.get(class1=tagList[j], class2=tagList[j+1]) 
            i.tag.add(tag.tag_id)
    else:
        tag = Tag.objects.get(class1='미분류')
        i.tag.add(tag.tag_id)

