import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam("👑")

class Queen(Unit):
    
    HP = 20.000000001  # Hit Points (health points)    
    ATT = 89.9999999905  # Attack
    ARM = 89.9999999905  # Armor
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
        
class Pawn(Unit):
    
    HP = 0.000000001  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 0.000000001  # Armor
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
        for i in range(1):
            unit = Queen(self, "Queen%02d"%(i+1), i)
            self.units.append(unit)
        for i in range(9):
            unit = Pawn(self, "Pawn%02d"%(i+1), 1+i)
            self.units.append(unit)
        
    
    def arrange(self, enemy: Team):
        Queenpos = 0
        Enemypos = 0
        Enemyatt = 0
        for i in range(enemy.num_positions):
            if enemy.units[i]!=None and enemy.units[i].att>=Enemyatt:
                Enemyatt=enemy.units[i].att
        if Enemyatt>90.9999999905:
            Enemypos=0
            Enemyatt=0
            for i in range(enemy.num_positions):
                if enemy.units[i]!=None and enemy.units[i].att>=Enemyatt:
                    Enemypos = i
            for i in range(self.num_positions):
                if self.units[i]!=None and self.units[i].att!=0:
                    Queenpos = i
            blank_unit=self.units[Enemypos]
            self.units[Enemypos]=self.units[Queenpos]
            if self.units[Enemypos]!=None:
                self.units[Enemypos].pos=Enemypos
            self.units[Queenpos]=blank_unit
            if self.units[Queenpos]!=None:
                self.units[Queenpos].pos=Queenpos
        else:
            Enemypos = 0
            Enemyarm = 200
            for i in range(enemy.num_positions):
                if enemy.units[i]!=None and enemy.units[i].arm<=Enemyarm:
                    Enemyarm=enemy.units[i].arm
                    Enemypos = i
            for i in range(self.num_positions):
                if self.units[i]!=None and self.units[i].att!=0:
                    Queenpos = i
            blank_unit=self.units[Enemypos]
            self.units[Enemypos]=self.units[Queenpos]
            if self.units[Enemypos]!=None:
                self.units[Enemypos].pos=Enemypos
            self.units[Queenpos]=blank_unit
            if self.units[Queenpos]!=None:
                self.units[Queenpos].pos=Queenpos
    
        
            
class TestTeam(unittest.TestCase):
    
    def test_team(self):
        team=MyTeam("👑")
        examiner=TeamExaminer()
        examiner.check(team)
        examiner.check(team)
        
if __name__ == "__main__":
    unittest.main()
