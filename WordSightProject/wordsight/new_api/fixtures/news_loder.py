import json 
import re
with open('crawling_data_real_final.json', 'r', encoding='UTF-8') as f:
    news_list = json.load(f)
# print(news_list)

def tag_reg(tag):
    tag = tag.replace(' ','')
    tag = tag.replace('>',' ')
    tag = tag.replace('|',' ')
    tag = tag.split()
    return tag

new_list = []
for news in news_list:
    new_data = {"model": "new_api.news"}
    news_keyword_data = {"model": "new_api.news_keyword"}
    new_data["fields"] = {}
    new_data["fields"]["title"] = news["title"]
    new_data["fields"]["news_agency"] = news["news_agency"]
    new_data["fields"]["origin_address"] = news["origin_url"]
    new_data["fields"]["tag_list"] = json.dumps(tag_reg(news['tag']))
    new_data["fields"]["created_date"] = news["created_date"]
    # 이름, 이름1,이름2,이름3, 이름~~@.com, JTV 등등 유형이 다양함 ->      
    new_data["fields"]["reporter"] = news["reporter"]
    new_data["fields"]["image_link"] = news["image"]
    new_data["fields"]["news_contents"] = news["news_contents"]

    new_list.append(new_data)


with open('news_data_result.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
