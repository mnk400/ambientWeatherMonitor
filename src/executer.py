from httpServer import Server
from reader import Reader
from time import sleep
from configUtil import ConfigUtil
from mqttClient import client
from dbClient import dbClient
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
        self.interval   = self.cUtil.getIntegerValue('awm','interval') * 60
        self.enableReader = self.cUtil.getValue('awm','enableReader')

        #HTTP configuration
        self.enableHttp = self.cUtil.getValue('http','enable')
        self.httpPort   = self.cUtil.getIntegerValue('http','port')

        #MQTT configuration
        self.enableMqtt = self.cUtil.getValue('mqtt','enable')
        if self.enableMqtt:
            self.mqttHost   = self.cUtil.getValue('mqtt','host')
            self.mqttPort   = self.cUtil.getIntegerValue('mqtt','port')
            self.mqttTopic  = self.cUtil.getValue('mqtt','topic')

        #influxDB configuration
        self.enableDb   = self.cUtil.getValue('influxdb','enable')
        if self.enableDb:
            self.dbHost     = self.cUtil.getValue('influxdb','host')
            self.dbPort     = self.cUtil.getIntegerValue('influxdb','port')
            self.database   = self.cUtil.getValue('influxdb','database')
            self.dbUsername = self.cUtil.getValue('influxdb','username')
            self.dbPassword = self.cUtil.getValue('influxdb','password')

    
    def exec(self):
        '''
        Function to execute the program
        '''

        #Checking if HTTP is enabled
        if self.enableHttp == 'true':
            http = Server(self.httpPort)
            http.start()
            logging.info("HTTP Server starting")
        
        #Initializing a reader instance
        sensorReader = Reader(interval=self.interval)
        
        #Adding mqtt client to reader if enabled
        if self.enableMqtt == 'true':
            mqttClient = client(self.mqttHost, self.mqttPort, self.mqttTopic)
            sensorReader.mqttClient = mqttClient
            logging.info("MQTT Publisher starting")
        
        #Adding database  client to reader if enabled
        if self.enableDb == 'true':
            influxClient = dbClient(self.dbHost, self.dbPort, self.database, self.dbUsername, self.dbPassword)
            sensorReader.dbClient = influxClient
            logging.info("Influx Client starting")
        
        #Starting thread if reader enabled
        if self.enableReader == 'true':
            sensorReader.start()

if __name__ == "__main__":

    e = Executer()
    e.exec()
