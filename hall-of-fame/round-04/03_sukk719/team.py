import unittest
import random

from loa.unit import Unit
from loa.team import Team


def get_team():
    return MyTeam1("Sweater")


class strong(Unit):
    
    HP = 100  # Hit Points (health points)    
    ATT = 40  # Attack
    ARM = 6 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class weak(Unit):
    
    HP = 20 # Hit Points (health points)    
    ATT = 5  # Attack
    ARM = 3  # Armor
    EVS = 0  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
class MyTeam1(Team):  
    def initialize(self):
        tmp = []
        for i in range(6):
            tmp.append(strong)
        for i in range(4):
            tmp.append(weak)
        random.shuffle(tmp)
        for i in range(10):
            unit = tmp[i](self, "A-Unit%02d"%(i+1), i)
            self.units.append(unit)   
    
    def arrange(self, enemy: Team):   
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
 
