
import json
from ..models import *

newsAll = News.objects.all()
jsonDec = json.decoder.JSONDecoder()

for i in newsAll:

    keywordList = jsonDec.decode(i.keyword_list)
    i.keyword.add(keywordList)

'''
# 동작 안되면 이걸로 시도
for i in newsAll:

    keywordList = jsonDec.decode(i.keyword_list)

    for k in keywordList:
        keyword = Keyword.objects.get(name=k) 
        i.keyword.add(keyword.keyword_id)
'''