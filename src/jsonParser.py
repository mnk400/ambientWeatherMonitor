import json


class jsonParser(object):

    def __init__(self):
        pass

    def createJson(self, temperature, humidity, pressure):
        jsonData = {
                        "temperature": temperature,
                        "humidity": humidity,
                        "pressure": pressure,
        }

        jsonStr = json.dumps(jsonData)
        return jsonStr
