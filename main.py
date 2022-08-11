import json
import requests

list_heros = ['Hulk', 'Captain America', 'Thanos']

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)

list_value_intelligence = []
new_dict_int = {}

# with open("heros1.txt", "w") as file:
#     file.write(response.text)

with open("heros.txt", 'r') as file:
    line = json.load(file)
    for i in range(0, len(line)):
        z = line[i]['name']
        if z in list_heros:
            value_intelligence = line[i]['powerstats']['intelligence']
            new_dict = {z: value_intelligence}
            new_dict_int.update(new_dict)
# print(new_dict_int)

d = max(new_dict_int.items())
print(f"Самый умный: {d[0]} - 'intelligence' равен: {d[1]} ")







