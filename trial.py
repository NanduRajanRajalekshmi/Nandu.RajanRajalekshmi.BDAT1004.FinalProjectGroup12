from bs4 import BeautifulSoup
import json
import requests
import urllib
from pymongo import MongoClient
import time
def fn():
    while True:
        #URL that needs to be scrapped.
        URL="https://www.kitco.com/market/"

        html_text= requests.get(URL).text

        soup=BeautifulSoup(html_text,'html.parser')

        #Gold

        low_price_gold=soup.find('td',id='wsp-AU-low').text

        high_price_gold=soup.find('td',id='wsp-AU-high').text

        #Silver

        low_price_silver=soup.find('td',id='wsp-AG-low').text

        high_price_silver=soup.find('td',id='wsp-AG-high').text

        #Platinum

        low_price_pt=soup.find('td',id='wsp-PT-low').text

        high_price_pt=soup.find('td',id='wsp-PT-high').text


        x='''{'''+f'''

            "Gold":1,

            "lowg":{low_price_gold},

            "highg":{high_price_gold},
                

            "Silver":2,

            "lows":{low_price_silver},

            "highs":{high_price_silver},


            "Platinum":3,

            "lowp":{low_price_pt},

            "highp":{high_price_pt}

                    '''+'''}'''             
        #file content deletion
        f=open("data.json","w")
        f.truncate()
        f.close()           
        #file creation and writing
        f=open("data.json","a")
        f.write(x)
        f.close()
        #file reading
        f=open("data.json","r")
        file_data=json.load(f) 
        #password parsing
        passw=urllib.parse.quote_plus("password5453")
        #connection to db
        client = MongoClient(f"mongodb+srv://nandu:{passw}@cluster0.p2ij3.mongodb.net/Project?retryWrites=true&w=majority")
        db =client.get_database('Project')
        #data insertion
        db.Final.insert_one(file_data)
        #per day updation
        time.sleep(1440)

    else:
        exit()     
