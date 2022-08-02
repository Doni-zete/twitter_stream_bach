import os
import json
import pandas as pd

path_to_json = 'json/'
json_files = [pos_json for pos_json in os.listdir(
    path_to_json) if pos_json.endswith('.json')]
print(json_files)  # for me this prints ['foo.json']

all_json_files = []

for file_name in json_files:
  with open("json/{}".format(file_name), 'r', encoding='utf-8') as f:
    temp_read = json.load(f)
    for file_json in temp_read:
      all_json_files.append(file_json)

# print(all_json_files)

with open("all_json_files.json", 'w', encoding='utf-8') as f:
    json.dump(all_json_files, f, ensure_ascii=False, indent=4)
