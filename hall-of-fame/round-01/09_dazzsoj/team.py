from loa.team import Team

from .units import Ga
from .units import Na
from .units import Da
from .units import Ra


def get_team():
    return Hangeul("Hangeul")

class Hangeul(Team):
    
    def initialize(self):
        self.units.append(Ga(self, "Ga", 0))
        self.units.append(Ga(self, "Ga", 1))
        self.units.append(Ga(self, "Ga", 2))
        self.units.append(Ga(self, "Ga", 3))
        self.units.append(Ga(self, "Ga", 4))
        self.units.append(Ga(self, "Ga", 5))
        self.units.append(Ga(self, "Ga", 6))
        self.units.append(Na(self, "Na", 7))
        self.units.append(Da(self, "Da", 8))
        self.units.append(Ra(self, "Ra", 9))
      
        
      
    def arrange(self, enemy:Team):
    
        # maxATT vs maxATT       
        maxATT_pos = None
        enemy_maxATT_pos = None
       

        for i in range(enemy.num_positions):
            
            if enemy.units[i] != None:
                
                if enemy_maxATT_pos == None:
                    enemy_maxATT_pos = i
                    
                elif enemy.units[i].att > enemy.units[enemy_maxATT_pos].att:
                        enemy_maxATT_pos = i

           
        for i in range(self.num_positions):
            
            if self.units[i] != None:
                
                if maxATT_pos == None:
                    maxATT_pos = i
                    
                elif self.units[i].att > self.units[maxATT_pos].att:
                        maxATT_pos = i

            
        temp01 = self.units[enemy_maxATT_pos]
        self.units[enemy_maxATT_pos] = self.units[maxATT_pos]
        self.units[maxATT_pos] = temp01
        
        self.units[enemy_maxATT_pos].pos = enemy_maxATT_pos
            
        if self.units[maxATT_pos] != None:
            self.units[maxATT_pos].pos = maxATT_pos
            
       


                