import json
from new_api.models import *

newsAll = News.objects.all()
jsonDec = json.decoder.JSONDecoder()

for i in newsAll:

    keywordList = jsonDec.decode(i.keyword_list)

    for k in keywordList:
        keyword = Keyword.objects.get(name=k) 
        i.keyword.add(keyword.keyword_id)
