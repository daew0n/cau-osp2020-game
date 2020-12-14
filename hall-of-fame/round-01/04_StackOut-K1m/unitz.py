from loa.unit import Unit


class Soldier(Unit):
    
    HP = 21  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 6  # Armor
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
        
class Elite(Unit):
    
    HP = 21  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 7  # Armor
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
        
class Giant(Unit):
    
    HP =  21 # Hit Points (health points)    
    ATT = 90  # Attack
    ARM = 80  # Armor
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
        
class Sacrifice(Unit):
    
    HP = 0  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 1  # Armor
    EVS = 1 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class T_Soldier(Unit):
    
    HP = 18  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 6  # Armor
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
        
class T_Elite(Unit):
    
    HP = 19  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 6  # Armor
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
        
class T_Sacrifice(Unit):
    
    HP = 0  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 1  # Armor
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