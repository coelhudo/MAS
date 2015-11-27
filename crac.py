__author__ = 'coelhudo'

from agent import Agent
from resource import Resource

class CRACUnit(Resource):
    def __init__(self, environment):
        self.environment = environment
        self.fanWorking = False

    def readSensor(self):
        return self.environment.getTemperature()

    def executeAction(self, action):
        self.fanWorking = action

    def isFanWorking(self):
        return random.random()

    def __str__(self):
        return 'Fan working' if self.fanWorking else 'Fan not working'

class CRACUnitManager(Agent):

    def monitor(self):
        self.state = self.managedResource.readSensor()

    def actuate(self):
        if self.state > 20:
            self.managedResource.executeAction(True)
        else:
            self.managedResource.executeAction(False)