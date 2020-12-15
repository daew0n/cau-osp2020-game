import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return RAKSTeam("cau.ac.kr")

class Myunit(Unit):

    HP = 31.706451612 # Hit Points (health points)
    ATT = 0 # Attack
    ARM = 12.195698924666666666666666666667 # Armor
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

class Myunit2(Unit):

    HP = 32.000000001 # Hit Points (health points)
    ATT = 0 # Attack
    ARM = 11.999999999333334  # Armor
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



class RAKSTeam(Team):
    def initialize(self):
        for i in range(10):
            unit = Myunit2(self, "Myunit%02d"%(i+1), i)
            self.units.append(unit)

    def arrange(self, enemy: Team):
        lifecount = 0
        survivecount = 0
        for i in range(self.num_positions):
            if (self.units[i] != None):
                lifecount += 1
        for i in range(self.num_positions):
            if (self.units[i] != None and enemy.units[i] != None):
                if (self.units[i].hp - (enemy.units[i].att - self.units[i].arm) <= 0):
                    survivecount +=1

        if (survivecount > (lifecount/2 - 1)):
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

class Testteam(unittest.TestCase):

    def test_team(self):
        team = RAKSTeam("RAKSTeam")
        examiner = TeamExaminer()
        examiner.check(team, "ROUND-02")
        examiner.check(team, "ROUND-02")

if __name__ == "__main__":
    unittest.main()
