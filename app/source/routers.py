from .DataRequest import DataRequest

def initializeRouter(api):
    api.add_resource(DataRequest, 'api/sendData')
    