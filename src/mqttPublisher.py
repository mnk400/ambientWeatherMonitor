from mqttClient import client
from sensorValueReader import sensorReader
from jsonParser import jsonParser
from time import sleep
import threading


class Publisher(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.client = client()
        self.sensor = sensorReader.getInstance()
        self.parser = jsonParser()
        self._stop = threading.Event()

    def run(self):
        self.client.connectMqtt()
        while True:
            temp = self.sensor.getTemperature()
            hum = self.sensor.getHumidity()
            pres = self.sensor.getPressure()
            jsonStr = self.parser.createJson(temp, hum, pres)

            self.client.connectMqtt()
            self.client.publishData(jsonStr)
            sleep(300)

        self.client.disconnect()
    
    def stop(self):
        print("stopping mqtt publisher")
        self._stop.set()

if __name__ == "__main__":
    dr = Publisher()
    dr.start()
