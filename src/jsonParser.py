import json
from sensorValueReader import sensorReader


class jsonParser(object):

    def __init__(self):
        self.sensorReader = sensorReader()
        pass

    def createJson(self, temperature, humidity, pressure):
        jsonData = {
                        "temperature": self.sensorReader.getTemperature(),
                        "humidity": self.sensorReader.getHumidity(),
                        "pressure": self.sensorReader.getPressure(),
        }

        jsonStr = json.dumps(jsonData)
        return jsonStr
