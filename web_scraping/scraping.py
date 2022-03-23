
import requests 
from bs4 import BeautifulSoup
import pandas as pd

header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}
f_lis=[]
for page_no in range(1,40):
    url=f'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_no}'


    page=requests.get(url,headers=header)
    soup=BeautifulSoup(page.content,'html.parser')

    main_=soup.find('div',class_='_1YokD2 _3Mn1Gg')
    


    for i in main_.find_all('div',class_='_1AtVbE col-12-12')[:-2]:
        title=i.find('div',class_='_4rR01T').text

        # desc=i.find('ul',class_='_1xgFaf').text

        price=i.find('div',class_='_30jeq3 _1_WHN1').text.replace('₹','').replace(',','')
        price=int(price)

        off=i.find('div',class_='_3Ay6Sb').text

     
        rating=i.find('div',class_='_3LWZlK')
        if rating is not None:
            rating=float(rating.text)
        else:
            rating=""
        
        link=i.find('img',class_='_396cs4 _3exPp9')
        link=link['src']


        lis=[title,rating,off,price,link]
         
        f_lis.append(lis)
    
    if page_no==2:
        break

    
df=pd.DataFrame(f_lis,columns=['Title','Rating','OFF percentage' ,'Price','Img_link'])

df.to_excel('data2.xlsx',index=None)
