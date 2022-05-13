from werkzeug.utils import secure_filename
import os
import platform
import requests
import json

def save_file(file):
    """ Guarda un solo archivo en una carpeta en el servidor
    y devuelve la ruta del mismo. """
    filename = secure_filename(file.filename)
    uploads_dir = detect_system()
    file.save(os.path.join(uploads_dir, filename))
    return str(uploads_dir + '\\' + filename)


def detect_system():
    sistema = platform.system()
    uploads_dir = ""
    if sistema == "Windows":
        uploads_dir = 'C:\\Users\\AxlEs\\Desktop\\PruebaCoppel\\Back\\app\\uploadFiles'
    else:
        uploads_dir = "./uploads_files"
    
    return uploads_dir


def getDataApi(data):
    url = 'https://sentim-api.herokuapp.com/api/v1/'
    headers = {
        'Accept': 'application/json', 
        'Content-Type': 'application/json'
    }
    jsonDataRequest = {"text": data}
    response = requests.post(url, headers=headers, json=jsonDataRequest)
    jsonResponse = json.loads(response.content)
    return jsonResponse



def readFile(path):
    file = open(path, "r", encoding="utf-8")
    content = file.read()
    return content
