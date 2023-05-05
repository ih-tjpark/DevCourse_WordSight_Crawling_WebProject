import json 
import re
with open('new_api/fixtures/keyword_data_real_final.json', 'r', encoding='UTF-8') as f:
    keyword_list = json.load(f)

new_list = []
for keyword in keyword_list:
    new_data = {"model": "new_api.keyword"}
    new_data["fields"] = {}
    new_data["fields"]['name'] = keyword
    new_data['fields']['count'] = keyword_list[keyword]['count']
    new_data['fields']['in_date'] = keyword_list[keyword]['in_date']
    new_list.append(new_data)


with open('new_api/fixtures/keyword_data_real_final_result.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)