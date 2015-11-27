__author__ = 'coelhudo'

class Environment:
    def __init__(self, temperature):
        self.temperature = temperature
        self.factor = 0

    def temperatureFactor(self, factor):
        self.factor = factor

    def tick(self):
        self.temperature += self.factor

    def getTemperature(self):
        return self.temperature

    def __str__(self):
        return str(self.temperature) + ' Degree Celcius'