import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam("h4x")

class Ace(Unit):
    
    HP = 21  # Hit Points (health points)    
    ATT = 90.4  # Attack
    ARM = 88.4  # Armor
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
        
class Bait(Unit):
    
    HP = 0.01  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 0.01  # Armor
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

        unit = Ace(self, "Ace", 0)
        self.units.append(unit)

        for i in range(1, 10):
            unit = Bait(self, "Bait", i)
            self.units.append(unit)



   
            
    def arrange(self, enemy: Team):
        Acepos = 0
        Enemypos = 0

        for i in range(enemy.num_positions):
            if enemy.units[i]!=None:
                Enemypos = i

        for i in range(self.num_positions):
            if self.units[i]!=None and self.units[i].att!=0:
                Acepos = i

        if self.units[Enemypos]!=None:
            temp = self.units[Enemypos]
            self.units[Enemypos]=self.units[Acepos]
            self.units[Enemypos].pos=Enemypos
            self.units[Acepos]=temp
            self.units[Acepos].pos=Acepos
        else:
            temp = self.units[Enemypos]
            self.units[Enemypos]=self.units[Acepos]
            self.units[Enemypos].pos=Enemypos
            self.units[Acepos]=temp



class TestTeam(unittest.TestCase):
    
    def test_team(self):
        team=MyTeam("h4x")
        examiner=TeamExaminer()
        examiner.check(team)
        examiner.check(team)
        
if __name__ == "__main__":
    unittest.main()