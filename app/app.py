import json
from flask_restful import Api
from flask import Flask, request, render_template
from flask_cors import CORS
from source.routers import initializeRouter
import requests
from source.resources import save_file, readFile, getDataApi

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

filesList = []

@app.route('/')
def login():
    return render_template('login.html', titlePage="Login")

@app.route('/home')
def home():
    return render_template('index.html', titlePage="Home")

@app.route('/savedata', methods=['POST'])
def saveData():
    files = request.files.getlist('files')
    responseJson = {"resultado": ""}
    response = ()
    if len(files) < 1:
        responseJson["resultado"] = "no se recibio ningun archivo"
        response = (responseJson, 400)
        return response
    else:
        for file in files:
            saveFileName = save_file(file)
            filesList.append(saveFileName)
        
        responseJson["resultado"] = "ok"
        response = (responseJson,200)

    for path in filesList:
        data = readFile(path)
        jsonResponseApi = getDataApi(data)
        print(jsonResponseApi)

        
    return response


@app.route('/sendRequets')
def sendRequests():
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        url = "https://sentim-api.herokuapp.com/api/v1/"
        body = {
            "text": "I'm still waiting for my order which says that according to what they already delivered. I've been trying to solve things with you for three weeks and you don't answer anywhere, I'll have to submit my complaint to @Profeco in a more formal way, I hope for a solution or my money back. Thank you"
        }
        
        response = requests.post(url, headers=headers, json=body)
        jsonResponse = json.loads(response.content)
        return jsonResponse

if __name__ == '__main__':
    app.run(debug=True)