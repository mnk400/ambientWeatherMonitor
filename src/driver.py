from mqttClient import client
from sensorValueReader import sensorReader
from jsonParser import jsonParser


class driver(object):

    def __init__(self):
        self.client = client()
        self.sensor = sensorReader()
        self.parser = jsonParser()

    def run(self):
        self.client.connectMqtt()

        jsonStr = self.parser.createJson(self.sensor.getTemperature(),
                self.sensor.getHumidity(), self.sensor.getPressure())

        self.client.publishData(jsonStr)

        self.client.disconnect()

if __name__ == "__main__":
    dr = driver()
    dr.run()
