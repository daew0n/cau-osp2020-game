from loa.team import Team
from loa.unit import Unit

        
def get_team():
    return MyTeam("fighting")

        
class first(Unit):
    
    HP = 100  # Hit Points (health points)    
    ATT = 39.99995  # Attack
    ARM = 6.6667 # Armor
    EVS = 0 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
        
class second(Unit):
    
    HP = 100  # Hit Points (health points)    
    ATT = 36.6667  # Attack
    ARM = 8.888866666666667  # Armor
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

class third(Unit):
    
    HP = 55.00005  # Hit Points (health points)    
    ATT = 26.66654  # Attack
    ARM = 0  # Armor
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
        
class weak(Unit):
    
    HP =10  # Hit Points (health points)    
    ATT = 5  # Attack
    ARM = 0 # Armor
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

class MyTeam(Team):
    def initialize(self):        
        self.units.append(second(self,"Second-01", 0))
        self.units.append(weak(self,"Weak-01", 1))
        self.units.append(second(self,"Second-02", 2))
        self.units.append(second(self,"Second-03", 3))
        self.units.append(weak(self,"Weak-02", 4))
        self.units.append(second(self,"Second-04", 5))
        self.units.append(third(self,"Third-01", 6))
        self.units.append(weak(self,"Weak-03", 7))
        self.units.append(second(self,"Second-05", 8))
        self.units.append(second(self,"Second-06", 9))
            
    def arrange(self, enemy: Team):
        pass