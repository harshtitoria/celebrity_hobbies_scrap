import pandas as pd
import requests
from bs4 import BeautifulSoup

url ="https://www.popxo.com/2018/08/bollywood-celebrities-and-their-hobbies-we-bet-you-didnt-know-/"
page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

hobbies = []
hobbies_elem = soup.findAll('p')

for item in hobbies_elem:
    hobbies.append(item.text)
hobbies = hobbies[2:30:3]

celebrity = []
celeb_name = soup.findAll('h3')
for item in celeb_name:
    celebrity.append(item.text)

celebrity = celebrity[0:10]

final_array = []
for celeb,hobbies in zip(celebrity,hobbies):
    final_array.append({'Celebrity':celeb,"Hobbies":hobbies})

df = pd.DataFrame(final_array)

#df.to_csv('celebrity_hobbies.csv', index=False)
