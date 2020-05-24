from httpServer import Server
from reader import Reader
from time import sleep
from configUtil import ConfigUtil
from mqttClient import client
import subprocess
import sys
import logging

logging.getLogger("awm-logger")
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("logs/awm.log"),
        logging.StreamHandler()
    ])

class Executer(object):
    '''
    Class to execute the HTTP server thread
    and the MQTT publisher thread.
    '''

    def __init__(self):
        '''
        Constructor responsible for reading configuration from
        the config file and initializing the program based on
        the config
        '''

        #Initialize the config reader
        self.cUtil = ConfigUtil()

        #Read the interval
        self.interval   = self.cUtil.getIntegerValue('awm','interval')

        #HTTP configuration
        self.enableHttp = self.cUtil.getValue('http','enable')
        self.httpPort   = self.cUtil.getIntegerValue('http','port')

        #MQTT configuration
        self.enableMqtt = self.cUtil.getValue('mqtt','enable')
        self.mqttHost   = self.cUtil.getValue('mqtt','host')
        self.mqttPort   = self.cUtil.getIntegerValue('mqtt','port')
        self.mqttTopic  = self.cUtil.getValue('mqtt','topic')

        #influxDB configuration
        self.enableDb   = self.cUtil.getValue('influxdb','enable')
        self.dbHost   = self.cUtil.getValue('influxdb','host')
        self.dbPort   = self.cUtil.getIntegerValue('influxdb','port')

    
    def exec(self):

        if self.enableHttp == 'true':
            http = Server(self.httpPort)
            http.start()
            logging.info("HTTP Server starting")
        

        sensorReader = Reader(interval=self.interval)
        if self.enableMqtt == 'true':
            mqttClient = client(self.mqttHost, self.mqttPort, self.mqttTopic)
            sensorReader.mqttClient = mqttClient
            logging.info("MQTT Publisher starting")
        sensorReader.start()

if __name__ == "__main__":

    e = Executer()
    e.exec()
