
from loa.unit import Unit
from loa.team import Team
from loa.team import TeamExaminer

def get_team():
    return MyTeam("🍗HUNGRY🍗")

class Bye(Unit):
    
    HP = 0 # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 1 # Armor
    EVS = 2 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class Warrior1(Unit):
    
    HP = 14  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 10  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class Warrior2(Unit):
    
    HP = 12  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 12  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class Warrior3(Unit):
    
    HP = 15  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 10  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
class Warrior4(Unit):
    
    HP = 15 # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 10  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
    
class Warrior5(Unit):
    
    HP = 15  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 10  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class Warrior6(Unit):
    
    HP = 15 # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 10  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class Warrior7(Unit):
    
    HP = 14  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 10  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)     
        
class Warrior8(Unit):
    
    HP = 14  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 10  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class Tanker(Unit):
       
    HP = 15  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 9  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
class Super_Tanker(Unit):
       
    HP = 17  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 9  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
class Crazy_Tanker(Unit):
    
    HP = 17  # Hit Points (health points)    
    ATT = 0 # Attack
    ARM = 15  # Armor
    EVS = 10 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
 
class Super_Crazy_Unit(Unit):
    HP = 25  # Hit Points (health points)    
    ATT = 50 # Attack
    ARM = 116  # Armor
    EVS = 10 # Evasion
        
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
        for i in range(9):
            unit = Bye(self,"Sseong-Unit%02d"%(i+1),i)
            self.units.append(unit)
        unit = Super_Crazy_Unit(self, "Sseong-SuperUnit%02d"%10,9)
        self.units.append(unit)
            
    def arrange(self, enemy: Team):        
        M_hp = []
        T_hp = []
        for i in range(10):
            if(self.units[i] != None):
                M_hp.append(self.units[i].hp)
            else:
                M_hp.append(0.0)
                
        for i in range(10):
            if(enemy.units[i] != None):
                T_hp.append(enemy.units[i].hp)
        T_hp.sort()
        
        for j in range(10):
            for i in range(0,9-j):
                if(self.units[i] != None) & (self.units[i+1]!=None):
                    if(M_hp[i] > M_hp[i+1]):
                        change_units = self.units[i]
                        self.units[i] = self.units[i+1]
                        if(self.units[i] != None):
                            self.units[i].pos = i
                        self.units[i+1] = change_units
                        self.units[i+1].pos = i+1
                elif(self.units[i] != None) & (self.units[i+1] == None):
                    change_units = self.units[i]
                    self.units[i] = self.units[i+1]
                    self.units[i+1] = change_units
                    self.units[i+1].pos = i+1
                    
        for i in range(10):
            if(enemy.units[i] != None):
                if(T_hp[0] == enemy.units[i].hp):
                    change_units = self.units[i]
                    self.units[i] = self.units[9]
                    if(self.units[i] !=None):
                        self.units[i].pos = i
                    self.units[9] = change_units
                    break
                
                
if __name__ == "__main__":
    team = MyTeam("SSeong")
    examiner = TeamExaminer()
    examiner.check(team)
    examiner.check(team)
