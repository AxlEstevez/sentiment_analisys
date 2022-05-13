import requests
import json
from flask_restful import Resource

class DataRequest(Resource):

    def post(self):
        headers = {
            'Accept': 'application/json',
            'content-type': 'application/json'
        }
        url = "https://sentim-api.herokuapp.com/api/v1/"
        body = {
            "text": "Sigo esperando mi pedido el cual dice que según ya me entregaron. llevo tres semanas tratando de solucionar las cosas con ustedes y no contestan por ningún lado,tendré que meter mi queja a @Profeco de manera más formal, espero una solución o la devolución de mi dinero.Gracias"
        }
        
        response = requests.post(url, headers=headers, data=body)
        return response.text