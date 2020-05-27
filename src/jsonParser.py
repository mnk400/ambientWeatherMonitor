import json
import logging
from datetime import datetime

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
        #now = datetime.now()
        #timestamp = datetime.timestamp(now)
        #timestamp = timestamp * 1000000000
        #print(timestamp)
        jsonData = {
                        'measurement' : 'awm',
                        'tags' : {
                            'location' : 'home'
                        },
                        'fields' : {
                            'temperature' : temperature,
                            'humidity' : humidity,
                            'pressure' : pressure,
                        }#,
                        #'time' : round(timestamp)
        }

        jsonStr = json.dumps(jsonData)
        return jsonStr
