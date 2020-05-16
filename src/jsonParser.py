import json
import logging

logging.getLogger("awm-logger")

class jsonParser(object):
    '''
    Class responsible for creating
    the JSON object
    '''

    def __init__(self):
        pass

    def createJson(self, temperature, humidity, pressure):
        '''
        Function for creating a
        JSON string
        '''
        jsonData = {
                        "temperature": temperature,
                        "humidity": humidity,
                        "pressure": pressure,
        }

        jsonStr = json.dumps(jsonData)
        return jsonStr
