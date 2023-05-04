import json 
import re
with open('WordSightProject/wordsight/new_api/news_data.json', 'r', encoding='UTF-8') as f:
    news_list = json.load(f)
# print(news_list)

new_list = []
for news in news_list:
    new_data = {"model": "new_api.news"}
    new_data["fields"] = {}
    new_data["fields"]["title"] = news["title"]
    new_data["fields"]["news_agency"] = news["news_agency"]
    new_data["fields"]["origin_address"] = news["origin_url"]
    new_data["fields"]["tag"] = ",".join(set(re.split(r'\s+', re.sub(r'[,\-?>|]',' ', news["tag"]))))
    new_data["fields"]["created_date"] = news["created_date"]
    # 이름, 이름1,이름2,이름3, 이름~~@.com, JTV 등등 유형이 다양함 ->      
    new_data["fields"]["reporter"] = news["reporter"]
    new_data["fields"]["image_link"] = news["image"]
    new_data["fields"]["news_contents"] = news["news_contents"]
    new_list.append(new_data)


with open('news_data_test.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
    
# reporter = ['김철수' ,'박민수|기자', '이진우|더벨 편집국장|','이수민(lee.sumin1@joongang.co.kr)','뉴욕=박준식|특파원|', '뉴욕=조슬기나','도병욱/오형주','조성호기자 csh@kwnews.co.kr']
# re.split(r'\s+', re.sub(r'[,\-?>|]',' ', news["tag"])


# for i in reporter:
#     res = re.sub(r'\b\w+@\w+\.\w+\b', '', i)
#     # res = re.sub(r'[^\w\s]', ' ', i)
#     print(res)