import unittest
from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return hunsu("hunsu")

class tensu(Unit):

    HP = 32.0014 # Hit Points (health points)
    ATT = 0.0001 # Attack
    ARM = 11.999 # Armor
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


class hunsu(Team):
    def initialize(self):
        for i in range(10):
            unit = tensu(self, "A-Unit%02d"%(i+1), i)
            self.units.append(unit)

    def arrange(self, enemy: Team):
        pass

class TestTeam(unittest.TestCase):

    def test_team(self):
        team = hunsu("MyTeam")
        examiner = TeamExaminer()
        examiner.check(team)
        examiner.check(team)


if __name__=="__main__":
    unittest.main()
