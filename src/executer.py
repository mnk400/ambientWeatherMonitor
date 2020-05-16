from httpServer import Server
from mqttPublisher import Publisher
from time import sleep
import subprocess
import sys
import logging

logging.getLogger("awm-logger")
logging.basicConfig(filename="logs/awm.log",format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

class Executer(object):
    '''
    Class to execute the HTTP server thread
    and the MQTT publisher thread.
    '''
    def exec(self):
        s = Server()
        p = Publisher()

        s.start()
        logging.info("HTTP Server starting")
        p.start()
        logging.info("MQTT Publisher starting")

# if __name__ == "__main__":

#     e = Executer()
#     e.exec()
