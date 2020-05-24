from sensorValueReader import sensorReader
from jsonParser import jsonParser
from time import sleep
import threading
import logging

logging.getLogger("awm-logger")

class Reader(threading.Thread):
    '''
    Threaded class to read SensorValues and store to database
    and publish using mqtt.
    '''

    def __init__(self,interval,mqttClient=None,dbClient=None):  
        threading.Thread.__init__(self)
        
        self.mqttClient = mqttClient
        self.dbClient   = dbClient

        self.sensor = sensorReader.getInstance()
        self.parser = jsonParser()
        self.interval = interval
        logging.info("Initializing MQTT publishing with interval " + str(self.interval))

    def run(self):
        '''
        run function to create JSONs using jsonParser
        and publish them using mqttClient
        '''
        while True:
            temp = self.sensor.getTemperature()
            hum = self.sensor.getHumidity()
            pres = self.sensor.getPressure()
            jsonStr = self.parser.createJson(temp, hum, pres)

            if self.mqttClient != None:
                self.mqttClient.connectMqtt()
                self.mqttClient.publishData(jsonStr)
            sleep(self.interval)

        self.client.disconnect()
    

# if __name__ == "__main__":
#     dr = Publisher()
#     dr.start()
