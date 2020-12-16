import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam3("NotImplementedError")

class Defender1(Unit):
    HP = 30.5  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 13  # Armor
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


class Defender2(Unit):
    HP = 40.0000000001  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 6.6666666666  # Armor
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
class Defender3(Unit):
    HP = 32.0000000001  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 11.9999999999  # Armor
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
        n = 8
        for i in range(n):
            unit = Defender1(self, "A-Unit%02d" % (i + 1), i)
            self.units.append(unit)
        for i in range (n,10):
            unit = Defender2(self, "A-Unit%02d" % (i + 1), i)
            self.units.append(unit)
            
    def arrange(self, enemy: Team):
        pass
            
class MyTeam2(Team):
    def initialize(self):
        for i in range(10):
            unit = Defender1(self, "A-Unit%02d" % (i + 1), i)
            self.units.append(unit)
            
    def arrange(self, enemy: Team):
        pass
            
class MyTeam3(Team):
    def initialize(self):
        for i in range(10):
            unit = Defender3(self, "A-Unit%02d" % (i + 1), i)
            self.units.append(unit)

    def arrange(self, enemy: Team):
        pass


if __name__ == "__main__":
    team1 = MyTeam1("Team#1")
    team2 = MyTeam2("Team#2")
    team3 = MyTeam3("Team#3")
    
    examiner = TeamExaminer()
    examiner.check(team1, "ROUND-02")
    examiner.check(team2, "ROUND-02")
    examiner.check(team3, "ROUND-02")

