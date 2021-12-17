#Flask API
from flask import Flask, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
import urllib
import trial

#Password transfer and DB connection
passw=urllib.parse.quote_plus("password5453")
client = MongoClient(f"mongodb+srv://nandu:{passw}@cluster0.p2ij3.mongodb.net/Project?retryWrites=true&w=majority")
db =client.get_database('Project')

#Getting data from DB
priceg=db.Final.find_one()["lowg"]
prices=db.Final.find_one()["lows"]
pricep=db.Final.find_one()["lowp"]
priceg1=db.Final.find_one()["highg"]
prices1=db.Final.find_one()["highs"]
pricep1=db.Final.find_one()["highp"]

app = Flask(__name__,template_folder='template',static_folder="C:\\Users\\Nandu R R\\Desktop\\static")


@app.route('/')
def main():
    return render_template("home.html",final_priceg=priceg,final_prices=prices,final_pricep=pricep) 

@app.route('/chart')
def charts():
    val={'Material':['Lowest','Highest'],'Silver':[prices,prices1],'Platinum':[pricep,pricep1],'Gold':[priceg,priceg1],}
    return render_template("chart.html",data=val)

@app.route('/refresh')
def data():
    trial.fn()
    main()     



if __name__ == '__main__':
 	app.run()

