from sense_hat import SenseHat


class sensorReader(object):
    """
    classdocs
    """

    def __init__(self):
        """
        constructor
        """
        self.sense = SenseHat()

    def getTemperature(self):
        """
        docs
        """
        return self.sense.get_temperature()

    def getHumidity(self):
        """
        docs
        """
        return self.sense.get_humidity()

    def getPressure(self):
        """
        docs
        """
        return self.sense.get_pressure()


if __name__ == "__main__":
    s = sensorReader()
    print(s.getPressure())
