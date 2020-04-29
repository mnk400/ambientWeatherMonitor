from sense_hat import SenseHat


class sensorReader(object):
    """
    classdocs
    """
    
    __instance = None
    __lock = False

    sense = SenseHat()

    @staticmethod 

    def getInstance():
        """ 
        Static access method.
        """
        if sensorReader.__instance == None:
            sensorReader()
        return sensorReader.__instance

    def __init__(self):
        """ 
        Virtually private constructor.
        """
        if sensorReader.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            sensorReader.__instance = self

    def getTemperature(self):
        """
        docs
        """
        
        return round(self.sense.get_temperature(),1)

    def getHumidity(self):
        """
        docs
        """
        return round(self.sense.get_humidity(),1)

    def getPressure(self):
        """
        docs
        """
        return round(self.sense.get_pressure(),1)


if __name__ == "__main__":
    s = sensorReader()
    print(s.getTemperature())
    print(s.getHumidity())
    print(s.getPressure())
