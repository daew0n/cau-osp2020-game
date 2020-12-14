import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return NoobTeam("newbie")

class Unit_V1(Unit):
    HP = 0   # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 1  # Armor
    EVS = 1  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)   
    
class Unit_S1(Unit):
    HP = 22   # Hit Points (health points)    
    ATT = 90  # Attack
    ARM = 77  # Armor
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
        
class Unit_M1(Unit):
    HP = 2   # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 1  # Armor
    EVS = 1  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
    
class NoobTeam(Team):
    def initialize(self):
        # Valance Unit
        # (In fact, is not alive unit. Just Used for filling NUM_UNITS)
        for i in range(8):
            unit = Unit_V1(self, "Unit-V1", i)
            self.units.append(unit)
        
        # Avoid Unit
        for i in range(8,9):
            unit = Unit_M1(self, "Unit-M1", i)
            self.units.append(unit)
        
        # Hunter Unit
        for i in range(9,10):
            unit = Unit_S1(self, "Unit-S1", i)
            self.units.append(unit)
            
    def arrange(self, enemy: Team):
        
        # Check Unit Position
        # x_pos = IndexValue if(each unit is alive) else -1
        e_pos = -1 # Position : Enemy Unit (Not NoneType)
        m_pos = -1 # Position : My Hunter Unit
        q_pos = -1 # Position : NoneType Enemy
        r_pos = -1 # Position : My Avoid Unit
        
        for i in range(10):
            if enemy.units[i] is None:
                q_pos = i
            if enemy.units[i] is not None:
                e_pos = i
            if self.units[i] is not None:
                if self.units[i].name == "Unit-S1": 
                    m_pos = i
                if self.units[i].name == "Unit-M1":
                    r_pos = i
                    
        # My Hunter Unit - Trace remained Unit
        if e_pos != -1 and m_pos != -1:
            self.units[m_pos], self.units[e_pos] = self.units[e_pos], self.units[m_pos]
            self.units[e_pos].pos = e_pos
            if self.units[m_pos] is not None:
                self.units[m_pos].pos = m_pos
        
        # My Avoid Unit - Move to NoneType Enemy Unit Position for Avoidance
        if r_pos != -1 and q_pos != -1:
            self.units[r_pos], self.units[q_pos] = self.units[q_pos], self.units[r_pos]
            self.units[q_pos].pos = q_pos
            if self.units[r_pos] is not None:
                self.units[r_pos].pos = r_pos
    
class TestTeam(unittest.TestCase):
    def test_team(self):
        team = NoobTeam("Hello LOA")
        examiner = TeamExaminer()
        examiner.check(team)

if __name__ == "__main__":
    unittest.main();