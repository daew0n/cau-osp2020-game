from loa.team import Team
from .myunit import Normalman
from .myunit import Empty


def get_team():
    return MyTeam("JGJ")


class MyTeam(Team):
    def initialize(self):
             for i in range(6):
                 unit = Normalman(self, "Normal%02d"%(i+1), i)
                 self.units.append(unit)
             for i in range(6,10):
                 unit = Empty(self, "Empty%02d"%(i-5), i)
                 self.units.append(unit)
    
    def arrange(self, enemy: Team):
        pass