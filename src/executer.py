from httpServer import Server
from mqttPublisher import Publisher
from time import sleep
import subprocess
import sys
import logging

logging.getLogger("awm-logger")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Executer(object):

    def exec(self):
        s = Server()
        p = Publisher()

        s.start()
        logging.info("HTTP Server starting")
        p.start()
        logging.info("MQTT Publisher starting")

if __name__ == "__main__":

    e = Executer()
    e.exec()

    