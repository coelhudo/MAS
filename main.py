__author__ = 'coelhudo'

import random
import time

from environment import Environment
from crac import CRACUnit, CRACUnitManager

if "__main__" == __name__:

    environment = Environment(18)
    crac_unit = CRACUnit(environment)
    crac_unit_manager = CRACUnitManager(crac_unit)

    while(True):
        environment.tick()
        crac_unit_manager.monitor()
        crac_unit_manager.actuate()

        if crac_unit.fanWorking:
            environment.temperatureFactor(-random.random())
        else:
            environment.temperatureFactor(random.random())

        print('---------- begin status ----------')
        print(environment)
        print(crac_unit)
        print('---------- end status ----------')
        time.sleep(2)