from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)

class HomePage(Resource):
    def get(self):
        endpoints = {
            "endpoints": {
                "/nobelPrizes": "Tüm nobel odullerinin bilgilerini verir",
                "/leatures": "Tüm nobel kazananlarinin bilgilerini verir",
                "/leature/id=<int:id>": "Girilen id'deki kazananin bilgilerini verir"
            }
        }
        return jsonify(endpoints)



class GetAllNobelPrizesInfo(Resource):
    def get(self):

        url = 'http://api.nobelprize.org/2.0/nobelPrizes'     

        resp = requests.get(url)
        data = resp.json()


        return {'data': data}, 200
    

class GetAllLeaturesInfo(Resource):
    def get(self):

        url = 'http://api.nobelprize.org/2.0/laureates'     

        resp = requests.get(url)
        data = resp.json()


        return {'data': data}, 200
    
class GetLeatureById(Resource):
    def get(self, id):  

        url = f'http://api.nobelprize.org/2.0/laureate/{id}'
        
        resp = requests.get(url)
        data = resp.json()

        return {'data': data}, 200

# Add URL endpoints
api.add_resource(HomePage, '/')
api.add_resource(GetAllNobelPrizesInfo, '/nobelPrizes')
api.add_resource(GetAllLeaturesInfo, '/leatures')
api.add_resource(GetLeatureById, '/leature/id=<int:id>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    app.run()

