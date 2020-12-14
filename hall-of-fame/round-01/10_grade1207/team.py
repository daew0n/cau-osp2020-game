import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam1("loa mang gam")

class MyUnit1(Unit):
    
    HP = 0  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 0.01  # Armor
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

class MyUnit2(Unit):
    
    HP = 60  # Hit Points (health points)    
    ATT = 79  # Attack
    ARM = 60  # Armor
    EVS = 10  # Evasion
        
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
        self.units.append(MyUnit2(self, "Unit2-01", 0))
        
        self.units.append(MyUnit1(self, "Unit1-01", 1))
        self.units.append(MyUnit1(self, "Unit1-01", 2))
        self.units.append(MyUnit1(self, "Unit1-01", 3))
        self.units.append(MyUnit1(self, "Unit1-01", 4))
        self.units.append(MyUnit1(self, "Unit1-01", 5))                                        
        self.units.append(MyUnit1(self, "Unit1-01", 6))
        self.units.append(MyUnit1(self, "Unit1-01", 7))
        self.units.append(MyUnit1(self, "Unit1-01", 8))
        self.units.append(MyUnit1(self, "Unit1-01", 9))
            
    def arrange(self, enemy: Team):
        index = 0
        for i in range(enemy.num_positions):
             if(enemy.units[i] != None):
                 if enemy.units[i].ATT < 80:
                     index = i
                     break

        f_unit_i = 0    
        for i in range(self.num_positions):
            if(self.units[i] != None):
                if(self.units[i].name == "Unit2-01"):
                    f_unit_i=i

        first_unit = self.units[index]
        self.units[index] = self.units[f_unit_i]
        self.units[f_unit_i] = first_unit

        for i in range(self.num_positions):
            if(self.units[i] != None): 
                self.units[i].pos = i
                
if __name__ =="__main__":
    unittest.main()

