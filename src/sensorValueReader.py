from sense_hat import SenseHat
import logging

logging.getLogger("awm-logger")

class sensorReader(object):
    '''
    Class to read sensor values
    from the senseHAT
    '''
    __instance = None
    __lock = False

    sense = SenseHat()

    @staticmethod 
    def getInstance():
        '''
        Static access method.
        '''
        if sensorReader.__instance == None:
            sensorReader()
        return sensorReader.__instance

    def __init__(self):
        '''
        Virtually private constructor.
        '''
        if sensorReader.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            sensorReader.__instance = self

    def getTemperature(self):
        '''
        get temperature value
        '''
        return round(self.sense.get_temperature(),1)

    def getHumidity(self):
        '''
        get humidity value
        '''
        return round(self.sense.get_humidity(),1)

    def getPressure(self):
        '''
        get pressure value
        '''
        return round(self.sense.get_pressure(),1)


# if __name__ == "__main__":
#     s = sensorReader()
#     print(s.getTemperature())
#     print(s.getHumidity())
#     print(s.getPressure())
