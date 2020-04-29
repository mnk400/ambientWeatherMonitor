from http.server import HTTPServer, BaseHTTPRequestHandler
from sensorValueReader import sensorReader
from jsonParser import jsonParser
import threading

class RequestHandler(BaseHTTPRequestHandler):

    sensor = sensorReader.getInstance()
    parser = jsonParser()
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        temp = self.sensor.getTemperature()
        hum = self.sensor.getHumidity()
        pres = self.sensor.getPressure()
        jsonStr = self.parser.createJson(temp, hum, pres)
        self.wfile.write(jsonStr.encode())

        

    def do_POST(self):
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
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        httpd = HTTPServer(('0.0.0.0', 6969), RequestHandler)
        httpd.serve_forever()
    
    def stop(self):
        print("stopping mqtt publisher")
        self._stop.set()
        

if __name__ == "__main__":
    s = Server()
    s.start()
    print("http server started")