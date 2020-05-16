from mqttClient import client
from sensorValueReader import sensorReader
from jsonParser import jsonParser
from time import sleep
import threading
import logging

logging.getLogger("awm-logger")

class Publisher(threading.Thread):
    '''
    Threaded class to publish MQTT
    messages
    '''

    interval = 600
    def __init__(self):
        logging.info("Initializing MQTT publishing with interval " + str(self.interval))
        threading.Thread.__init__(self)
        self.client = client()
        self.sensor = sensorReader.getInstance()
        self.parser = jsonParser()

    def run(self):
        '''
        run function to create JSONs using jsonParser
        and publish them using mqttClient
        '''
        self.client.connectMqtt()
        while True:
            temp = self.sensor.getTemperature()
            hum = self.sensor.getHumidity()
            pres = self.sensor.getPressure()
            jsonStr = self.parser.createJson(temp, hum, pres)

            self.client.connectMqtt()
            self.client.publishData(jsonStr)
            sleep(self.interval)

        self.client.disconnect()
    

# if __name__ == "__main__":
#     dr = Publisher()
#     dr.start()
