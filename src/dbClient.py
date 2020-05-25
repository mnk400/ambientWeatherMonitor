from influxdb import InfluxDBClient
import logging
import json
# Get a logger
logging.getLogger("db-logger")

class dbClient(object):
    '''
    classdocs
    '''

    def __init__(self, dbhost, dbport, db, uname, passwd):
        self.client = InfluxDBClient(host=dbhost , port=dbport, username= uname, password = passwd, database=db)
    
    def writetodb(self, jsonStr):
        string = json.loads(jsonStr)
        self.client.write_points([string])
        logging.info("InfluxDB:Written to database")


