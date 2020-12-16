from loa.team import Team
from .myunit import alpha
from .myunit import beta
from.myunit import Tanker

def get_team():
    return coronaxxx("coronaxxx")

class coronaxxx(Team):
    def initialize(self):
        self.units.append(alpha(self, "alpha", 0))
        self.units.append(beta(self, "beta", 1))
        self.units.append(beta(self, "beta", 2))
        self.units.append(Tanker(self, "Tanker", 3))
        self.units.append(Tanker(self, "Tanker", 4))
        self.units.append(Tanker(self, "Tanker", 5))
        self.units.append(Tanker(self, "Tanker", 6))
        self.units.append(Tanker(self, "Tanker", 7))
        self.units.append(beta(self, "beta", 8))
        self.units.append(beta(self, "beta", 9))
        
    def arrange(self, enemy: Team):
        pass
        first_unit = self.units[0]
        for i in range(self.num_positions - 1):
            j = i + 1
            self.units[i] = self.units[j]
            if self.units[i] != None:
                self.units[i].pos = i
        # end of for
        self.units[-1] = first_unit
        if self.units[-1] != None:
            self.units[-1].pos = self.num_positions - 1
