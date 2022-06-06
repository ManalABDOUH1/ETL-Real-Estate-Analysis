
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = "https://www.mubawab.ma/fr/sc/appartements-a-louer"
l = list()


html_text = requests.get(URL + "#catalog-listing").content

soup = bs(html_text,'html.parser')
links = soup.find_all('li',class_='listingBox w100')
for cont in links :
    try :
        title = cont.find('h2', class_='listingTit')
    except :
        title = 'not defined'

    try :
        link = title.find('a').attrs['href']
    except :
        link = 'not defined'
    print(link)
    

