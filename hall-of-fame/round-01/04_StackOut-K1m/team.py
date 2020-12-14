from loa.team import Team

from .unitz import Sacrifice
from .unitz import Giant

def get_team():
    return MyTeam("FinalRoster")

def switch_pos(self,a=0,b=1):
    if self.units[a] == None:
        self.units[a] = self.units[b]
        self.units[a].pos = a
        self.units[b] = None
    
    elif self.units[b] == None:
        self.units[b] = self.units[a]
        self.units[b].pos = b
        self.units[a] = None
    
    else:
        Save_ = self.units[a]
        self.units[a] = self.units[b]
        self.units[b] = Save_
        self.units[a].pos = a
        self.units[b].pos = b

class MyTeam(Team):
    def initialize(self):
        for i in range(1):
            A_unit = Giant(self, "A-Unit%02d"%(i+1), i)
            self.units.append(A_unit)
            
        for i in range(9):
            B_unit = Sacrifice(self, "B-Unit%02d"%(i+1), i+1)
            self.units.append(B_unit)
            
    
    def arrange(self, enemy: Team):        
        
        ally_list = 0 #생존 아군 위치
        enemy_list = [] #생존 적군 위치

        for i in range(10):
            if (self.units[i] != None):
                ally_list = i
                break
                
        for i in range(10):
            if (enemy.units[i] != None):
                enemy_list.append(i)

        A_target = 0
        Max_ = 0
        
        for i in enemy_list:
            if (Max_ <= enemy.units[i].att):
                Max_ = enemy.units[i].att
                A_target = i
                
        switch_pos(self,ally_list,A_target)

            
