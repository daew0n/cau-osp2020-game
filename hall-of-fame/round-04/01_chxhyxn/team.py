import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam("👑")

class Pawn(Unit):
    
    HP = 20.0001 # Hit Points (health points)    
    ATT = 10  # Attack
    ARM = 0 # Armor
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

class Queen(Unit):
    
    HP = 100 # Hit Points (health points)    
    ATT = 40  # Attack
    ARM = 6.6666 # Armor
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
        
        

class MyTeam(Team):
    def initialize(self):
        for i in range(4):
            unit = Pawn(self, "Pawn%02d"%(i+1), i)
            self.units.append(unit)
        for i in range(6):
            unit = Queen(self, "Queen%02d"%(i+1), i+4)
            self.units.append(unit)
       
    
    def arrange(self, enemy: Team):
        for i in range(self.num_positions):
            e_att=0
            e_pos=0
            if self.units[i]!=None:
                if self.units[i].att==40:
                    for j in range(enemy.num_positions):
                        if enemy.units[j]!=None:
                            if enemy.units[j].att>=e_att:
                                if self.units[j]!=None:
                                    if self.units[j].att!=40:
                                        e_att=enemy.units[j].att
                                        e_pos=j
                                elif self.units[j]==None:
                                    e_att=enemy.units[j].att
                                    e_pos=j
                    if self.units[e_pos]!=None:
                        temp=self.units[e_pos]
                        self.units[e_pos]=self.units[i]
                        self.units[e_pos].pos=e_pos
                        self.units[i]=temp
                        self.units[i].pos=i
                    else:
                        self.units[e_pos]=self.units[i]
                        self.units[e_pos].pos=e_pos
                        self.units[i]=None
                         
            
class TestTeam(unittest.TestCase):
    
    def test_team(self):
        team=MyTeam("👑")
        examiner=TeamExaminer()
        examiner.check(team)
        examiner.check(team)
        
if __name__ == "__main__":
    unittest.main()
