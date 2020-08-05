from bs4 import BeautifulSoup
import requests


response=requests.get('https://en.wikipedia.org/wiki/Brazil')

soup=BeautifulSoup(response.content,'html.parser')

result=soup.find_all(class_="toctext")
print(result)

for heading in result:
    print(heading)
   
