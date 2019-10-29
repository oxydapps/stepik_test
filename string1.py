import re

# print(re.match()) #проверяет подходит ли данная строка под данный шаблон
# print(re.search()) #находит первую подстроку, которая подходит под наш шаблон
# print(re.findall()) #все подстроки
# print(re.sub()) #заменить все вхождения чем-либо другим

# pattern = r'a[abc]c'
# string = 'acc'
# match_object = re.match(pattern, string)
# print(match_object)
#
#
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html

# 3.5
# import csv
# from collections import defaultdict, Counter
# crimes= defaultdict(int)
#
# with open("Crimes.csv", 'r') as fr:
#     reader_dict = csv.DictReader(fr)
#     for row_dict in reader_dict:
#         type = row_dict['Primary Type']
#         date = row_dict['Date'][6:10]
#         if date == '2005':
#             crimes[type] += 1
#
# x = Counter(crimes)
# print(x.most_common(1))

#3.6.1

# import requests
#
# api = 'http://numbersapi.com/'
# api2 = '/math?json=true'
#
# with open('dataset_24476_3.txt', 'r') as f:
#     for line in f:
#         number = line.strip()
#         res = requests.get(api + number + api2)
#         data = res.json()
#         if data["found"]:
#             print('Interesting')
#         else:
#             print('Boring')

#3.6.2
import requests
import json

client_id = 'db311cfe37ec4bc74a61'
client_secret = 'ba1d22427d386b0b79ce4403c063b2ec'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]

artists = []

with open('dataset_24476_4.txt') as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        url = 'https://api.artsy.net/api/artists/{}'.format(artist_id)
        params = {'xapp_token': token}
        resp = requests.get(url, params=params).text
        data = json.loads(resp)
        artists.append({'name': data['sortable_name'], 'birthday': data['birthday']})

for artist in sorted(artists, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])