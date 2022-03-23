

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://in.seamsfriendly.com/collections/shorts/'
data=[]
for i in range(1,4):
    page=requests.get(url+f'?page={i}')
    
    soup=BeautifulSoup(page.content,'html.parser')
    lis=soup.find_all('div',class_='Grid__Cell 1/2--phone 1/2--tablet-and-up 1/3--desk')

    for i in lis:
        title=i.find('h2',class_='ProductItem__Title Heading').text.replace('\n','')

        c_lis=title.split()
        color=c_lis[0]+' ' +c_lis[1]

        imag=i.find('noscript')
        l=imag.find('img')
        imag_link='https:'+l['src']
        
        price=i.find('span',class_='ProductItem__Price Price Text--subdued').text.replace('₹','')
        reviews=i.find('span',class_='jdgm-prev-badge__text').text
        
        desc=title + ',' +reviews+ ', Price : rs. '+price
        f_price=int(price.replace(',',''))

        lis1=[title,desc,f_price,color,imag_link]
        
        data.append(lis1)
        
df=pd.DataFrame(data,columns=['Title','Description','Price','Color','Image_url'])
df.to_csv('output.csv',index=None)


