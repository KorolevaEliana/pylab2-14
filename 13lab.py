#13.2 Найдите в сети интернет данные об источниках с открытыми API и создайте приложение,
# которое выводит любые другие данные из этих источников, например,
# 2 исторических файта (достопримечательности) в заданном городе и т.п

import requests
import json
ask1 = int(input("сколько шуток необходимо сгенерировать? " ))
limit = ask1
api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'LHem6s7ER/trir6E3PmoeA==HlWRh6ymAxIoI1l3'})
if response.status_code == requests.codes.ok:
    print("joke", response.text)
    data = {"joke": response.text}
else:
    print("Error:", response.status_code, response.text)
formatted_data = []
for item in response.text:
    formatted_data.append(json.dumps(item, ensure_ascii=False))
data = json.loads(response.text)
with open('result.json', 'w') as file:
    for item in data:
        file.write(json.dumps(item) + '\n')