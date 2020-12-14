import unittest

from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

from operator import itemgetter

def get_team():
    return MyTeam("🥈")

class TrashUnit(Unit):
    
    HP = 0
    ATT = 0 
    ARM = 1
    EVS = 2
        
    def __init__(self, team, name, pos):
        cls = __class__
        self.type = "trash"
        super().__init__(team, name,pos, hp=cls.HP, att=cls.ATT, arm=cls.ARM, evs=cls.EVS)

class KillerUnit(Unit):
    
    HP = 21
    ATT = 94
    ARM = 76
    EVS = 10
        
    def __init__(self, team, name, pos):
        cls = __class__
        self.type = "killer"
        super().__init__(team, name,pos, hp=cls.HP, att=cls.ATT, arm=cls.ARM, evs=cls.EVS)


class MyTeam(Team):
    def initialize(self):
        self.units.append(KillerUnit(self, "Firestorm-KillerA", 0))
        for i in range(9):
            unit = TrashUnit(self, "Firestorm-Trash%02d"%(i+1), i+1)
            self.units.append(unit)
            
    def arrange(self, enemy: Team):
        enemyData = list()
        index = -1
        for k in enemy.units:
            index += 1
            if k is None:
                enemyData.append((index, 0, 0, 0))
                continue
            enemyData.append((index, k.hp, k.att, k.arm, k.evs))
        enemyData.sort(key=itemgetter(1, 2), reverse=True)

        killerIndex = 0
        l = 0
        for k in self.units:
            if k is None:
                l += 1
                continue
            if k.type == "killer":
                killerIndex = l
                break
            l += 1
        
        killer = self.units[killerIndex]
        del self.units[killerIndex]
        self.units.insert(enemyData[0][0], killer)
    
        for i in range(10):
            if self.units[i] is None: continue
            self.units[i].pos = i
