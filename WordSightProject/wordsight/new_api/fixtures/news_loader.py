import json 
import re
<<<<<<< HEAD:WordSightProject/wordsight/new_api/fixtures/news_loader.py
from datetime import datetime

with open('new_api/fixtures/crawling_data_real_final.json', 'r', encoding='UTF-8') as f:
   news_list = json.load(f)

def tag_reg(tag):
    tag = news["tag"]
    tag = tag.replace(' ','')
    tag = tag.replace('>',' ')
    tag = tag.replace('|',' ')
    tag = tag.split()
    return tag
=======
with open('crawling_data_real_final.json', 'r', encoding='UTF-8') as f:
    news_list = json.load(f)
# print(news_list)
>>>>>>> 0325a71cf69aa3e4b4613a8ca6af87c502172085:WordSightProject/wordsight/new_api/fixtures/news_loder.py

def tag_reg(tag):
    tag = news["tag"]
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
    new_data["fields"]["tag_list"] = json.dumps(tag)
    new_data["fields"]["created_date"] = news["created_date"]
    new_data["fields"]["reporter"] = news["reporter"]
    new_data["fields"]["image_link"] = news["image"]
    new_data["fields"]["news_contents"] = news["news_contents"]
    new_data["fields"]['keyword_list'] = json.dumps(news['keyword'])
<<<<<<< HEAD:WordSightProject/wordsight/new_api/fixtures/news_loader.py


    new_list.append(new_data)

=======

    new_list.append(new_data)


>>>>>>> 0325a71cf69aa3e4b4613a8ca6af87c502172085:WordSightProject/wordsight/new_api/fixtures/news_loder.py
with open('news_data_result.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)

