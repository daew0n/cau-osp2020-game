from loa.team import Team
#Units
from .myunit import Mice
from .myunit import Adelie_Penguin
from .myunit import Cat
from .myunit import Fish


def get_team():
    return MyTeam("The Adelie Penguin")


        
    
class MyTeam(Team):
    def initialize(self):
        position = 6
        for i in range(position):
            unit = Mice(self,"Fish%02d"%(i+1),i)
            self.units.append(unit)

        unit = Cat(self,"Adelie Penguin",position)
        self.units.append(unit)
        
        for i in range(position+1,10):
            unit = Mice(self,"Fish%02d"%(i+1),i)
            self.units.append(unit)
        
        
    def arrange(self,enemy: Team):
        target_pos = None
        for i in range(self.num_positions):
            if (enemy[i] != None):
                 if (enemy.units[i].att > (Cat.ARM+1)):
                     target_pos=i
                     break
                 
        if (target_pos==None):
            for i in range(self.num_positions):
                if (enemy[i] != None):
                    if (enemy.units[i].hp != 0):
                        if (enemy.units[i].arm > Cat.ATT-1):
                            continue
                        target_pos=i
                        break
                    
        if (target_pos==None):
            for i in range(self.num_positions):
                if (enemy[i] != None):
                    if (enemy.units[i].hp != 0):
                        target_pos=i
                        break
                    
        
        for i in range(self.num_positions):
            if (self[i] != None):
                if (self.units[i].arm == (Cat.ARM)):
                    if (target_pos==i):
                        break
                    self.units[i],self.units[target_pos]=self.units[target_pos],self.units[i]
                    
                    self.units[target_pos].pos = target_pos
                    if (self[i] != None):
                        self.units[i].pos = i

                