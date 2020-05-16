from http.server import HTTPServer, BaseHTTPRequestHandler
from sensorValueReader import sensorReader
from jsonParser import jsonParser
import threading
import logging

logging.getLogger("awm-logger")

class RequestHandler(BaseHTTPRequestHandler):
    '''
    Request Handler for the HTTP server
    '''
    sensor = sensorReader.getInstance()
    parser = jsonParser()

    def do_GET(self):
        '''
        Method to handle a GET request
        '''
        logging.info("Recieved a HTTP GET request")
        self.send_response(200)
        self.end_headers()
        temp = self.sensor.getTemperature()
        hum = self.sensor.getHumidity()
        pres = self.sensor.getPressure()
        jsonStr = self.parser.createJson(temp, hum, pres)
        self.wfile.write(jsonStr.encode())
        logging.info("Response to the HTTP request sent")



    def do_POST(self):
        '''
        Method to handle a POST request
        '''
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

class Server(threading.Thread):
    '''
    Class to create the HTTP server
    '''

    def __init__(self):
        '''
        Constructor
        '''
        logging.info("Initializing HTTP Server")
        threading.Thread.__init__(self)

    def run(self):
        '''
        run function for the thread to start the
        HTTP server
        '''
        httpd = HTTPServer(('0.0.0.0', 6969), RequestHandler)
        httpd.serve_forever()
        logging.info("HTTP Server starter")



# if __name__ == "__main__":
#     s = Server()
#     s.start()
