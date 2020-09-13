from scrapy import Selector
import requests
import scrapy
from scrapy.crawler import CrawlerProcess
html = '''
<html>
<body>
<div class="Hello Ashutosh">
<p>Hello AP!</p>
</div>
<p>Enjoy The Course!</p>
</body>
</html>
'''
sel=Selector(text=html)
print(sel.xpath("//div/@class"))
print(sel.css(" p ")) 
print(sel.css("div>p")) 
print(sel.css("div>p").extract()) 
print(sel.css("div ::text"))
print(sel.xpath("//p")) #<--This Gives Us Selector List
print(sel.xpath("//p//text()"))
print(sel.xpath("//p").extract())
print(sel.xpath("//p").extract_first()) #<---Gives Us Only The First Element Of The Selector List
Lists=sel.xpath("//p")
List=Lists[1] #<--Using List To Select A Particular Element
print(List.extract())
print(len(sel.xpath("//p"))) #<--This Gives Us The Length Of The Selector List
url='https://twitter.com/home'
html=requests.get(url).content
sel=Selector(text=html)
print(sel.xpath("//link").extract())
print(sel.xpath("//link").extract()[2])

#Creating A Spider

class Spider1(scrapy.Spider):

    name='Spider_1'

    def start_requests(self):
        urls=['https://www.songspk2.info/']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        html_file='TOI'
        with open(html_file,'wb') as fout:
            fout.write(response.body)
  

