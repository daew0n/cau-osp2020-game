import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer
from operator import itemgetter

def get_team():
    return MyTeam("Null")

class KillerUnit(Unit):
    HP = 21
    ATT = 91
    ARM = 61
    EVS = 10
 
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team, name, pos, hp=cls.HP, att=cls.ATT, arm=cls.ARM, evs=cls.EVS)
        
class RemainUnit(Unit):
    HP = 2
    ATT = 0
    ARM = 1
    EVS = 2
    
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team, name, pos, hp=cls.HP, att=cls.ATT, arm=cls.ARM, evs=cls.EVS)

class MyTeam(Team):
    def initialize(self):
        for i in range(9):
            unit = RemainUnit(self, "Remain-%02d"%(i+1), i)
            self.units.append(unit)
        self.units.append(KillerUnit(self, "Killer", 9))
        
    def arrange(self, enemy: Team):
        killerIndex = -1
        isAliveKiller = False
        for i in self.units:
            if i is None:
                continue
            else:
                if i.att == 91:
                    killerIndex = i.pos
                    isAliveKiller = True
        findStrong = []
        for i in range(10):
            if enemy[i] is None:
                findStrong.append([i,-1,-1])
            else:
                findStrong.append([i, enemy[i].hp + enemy[i].arm])
        findStrong.sort(key=itemgetter(1), reverse=True)
        if isAliveKiller:
            targetIndex = findStrong[0][0]
            copyKiller = self.units[killerIndex]
            del self.units[killerIndex]
            self.units.insert(targetIndex, copyKiller)
            for i in range(10):
                if self.units[i] is None:
                    continue
                else:
                    self.units[i].pos = i
