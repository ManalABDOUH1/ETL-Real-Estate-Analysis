
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
#from gazpacho import Soup

URL = "https://www.avito.ma/fr/maroc/appartements-%C3%A0_vendre?o="
l = list()
for page in  range(1,20) :
    html_text = requests.get(URL+str(page)).content
    soup = bs(html_text,'html.parser') 
    
    ###            Partie Links             ###
    links =soup.find('div', class_='sc-116g21e-0 dOAHev').find('div',class_='sc-1nre5ec-0 dBrweF listing')
    #print(links)

    for cont in links :
            #Lien du detail page
            try :
                Link = cont.find('a', class_='oan6tk-1 fFOxTQ').attrs['href']
            except :
                Link = 'Invalid'
            #print(Link)

            try :
                title = cont.find('span',class_='oan6tk-17 ewuNqy').text
            except :
                title = 'Invalid'
            #print(title)

            try:
                Price= cont.find('span',class_='sc-1x0vz2r-0 izsKzL oan6tk-15 cdJtEx').find('span').text
            except:
                Price ='Invalid'
            #print(Price)


            ###      Partie Liaison                  ###
            html_text2 = requests.get(Link).content
            soup2 = bs(html_text2,'html.parser')


            ###       Partie Content                 ###
            try:
                Ville = soup2.find('span',class_='sc-1x0vz2r-0 gCIGeB').text
            except:
                Ville = 'Invalid'
            #print(Ville)

            #Description
            try:
                description =soup2.find('p',class_='sc-ij98yj-0 iMUDvH').text
            except:
                description ='Invalid'
            #print(description)


            #surfaces
            try:
                surface = soup2.find('span',class_='sc-1x0vz2r-0 kUjmne').text
            except:
                surface ='Invalid'
            #print(surface)


            #nbr Chanmbres
            chambres= soup2.find('div', class_ = "sc-6p5md9-0 kqSvFR").find_all('div')[3].find('span',class_ = "sc-1x0vz2r-0 kUjmne").text.strip()
            #print(chambres)


            #Caractéristiques              
            features = soup2.find_all('li', class_='sc-qmn92k-0 bdihtW')
            caracList = list()
            for carac in features:
                try:
                    feature = carac.find('span',class_='sc-1x0vz2r-0 iVDpDk').text
                    caracList.append(feature)
                except :
                    feature = 'Invalid'
            #print(caracList)


            #Pictures
            content = soup2.find('div', class_='slick-list')
            photos = content.find_all('div', class_='slick-slide')
            if photos is not None:
                photoList = list()
                for photo in photos:
                    if photo is not None:
                        try:
                            picture = photo.find('picture').find('img').attrs['src']
                            photoList.append(picture)
                        except :
                            photoList = 'not defined'
                        print(photoList)


            data = {"Title":title, "Ville":Ville, "Chambres":chambres, "Surfaces":surface, "Price":Price, "Caractéristiques":converted_list,"Pictures":photoList, "Description":description}
            l.append(data) 
        
#df = pd.DataFrame(l)

#  # Storing in Excel File   
df.to_excel("Avito1_20.xlsx")


