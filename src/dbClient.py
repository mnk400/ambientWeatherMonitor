from influxdb import InfluxDBClient
import logging
import json
# Get a logger
logging.getLogger("db-logger")

class dbClient(object):
    '''
    Abstraction over influxDB to add data to
    the database
    '''

    def __init__(self, dbhost, dbport, db, uname, passwd):
        '''
        Constructor to initialize the database
        '''
        self.client = InfluxDBClient(host=dbhost , port=dbport, username= uname, password = passwd, database=db)
    
    def writetodb(self, jsonStr):
        '''
        Function to write data to the database
        '''
        string = json.loads(jsonStr)
        self.client.write_points([string])
        logging.info("InfluxDB:Written to database")


