from loa.team import Team
import random

from .myunit import Unit1, Unit2, Unit3

def get_team():
    return EZ("")


class EZ(Team):
    def initialize(self):
        for i in range(10):
            unit = Unit3(self, "Unit3", i)
            self.units.append(unit)

    def arrange(self, enemy: Team):
        pass
