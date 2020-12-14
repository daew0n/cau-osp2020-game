from loa.unit import Unit


class Ga(Unit):
    
    HP = 1  # Hit Points (health points)    
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
    
        
class Na(Unit):
    
    HP = 1  # Hit Points (health points)    
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


class Da(Unit):
    
    HP = 1  # Hit Points (health points)    
    ATT = 0  # Attack
    ARM = 1  # Armor
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
       
        
class Ra(Unit):
    
    HP = 45  # Hit Points (health points)    
    ATT = 85  # Attack
    ARM = 52  # Armor
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


# class Ma(Unit):
    
#     HP = 10  # Hit Points (health points)    
#     ATT = 10  # Attack
#     ARM = 4  # Armor
#     EVS = 10 # Evasion
        
#     def __init__(self, team, name, pos):
#         cls = __class__
#         super().__init__(team,
#                           name,
#                           pos,
#                           hp=cls.HP,
#                           att=cls.ATT,
#                           arm=cls.ARM,
#                           evs=cls.EVS)


# class Ba(Unit):
    
#     HP = 9  # Hit Points (health points)    
#     ATT = 7  # Attack
#     ARM = 4  # Armor
#     EVS = 6 # Evasion
        
#     def __init__(self, team, name, pos):
#         cls = __class__
#         super().__init__(team,
#                           name,
#                           pos,
#                           hp=cls.HP,
#                           att=cls.ATT,
#                           arm=cls.ARM,
#                           evs=cls.EVS)
        

# class Sa(Unit):
    
#     HP = 9  # Hit Points (health points)    
#     ATT = 6  # Attack
#     ARM = 5  # Armor
#     EVS = 10 # Evasion
        
#     def __init__(self, team, name, pos):
#         cls = __class__
#         super().__init__(team,
#                          name,
#                          pos,
#                          hp=cls.HP,
#                          att=cls.ATT,
#                          arm=cls.ARM,
#                          evs=cls.EVS)


# class A(Unit):
    
#     HP = 9  # Hit Points (health points)    
#     ATT = 6  # Attack
#     ARM = 5  # Armor
#     EVS = 10 # Evasion
        
#     def __init__(self, team, name, pos):
#         cls = __class__
#         super().__init__(team,
#                          name,
#                          pos,
#                          hp=cls.HP,
#                          att=cls.ATT,
#                          arm=cls.ARM,
#                          evs=cls.EVS)
     
   
# class Ja(Unit):
    
#     HP = 9  # Hit Points (health points)    
#     ATT = 6  # Attack
#     ARM = 5  # Armor
#     EVS = 10 # Evasion
        
#     def __init__(self, team, name, pos):
#         cls = __class__
#         super().__init__(team,
#                          name,
#                          pos,
#                          hp=cls.HP,
#                          att=cls.ATT,
#                          arm=cls.ARM,
#                          evs=cls.EVS)
        
# class Cha(Unit):
    
#     HP = 9  # Hit Points (health points)    
#     ATT = 6  # Attack
#     ARM = 5  # Armor
#     EVS = 10 # Evasion
        
#     def __init__(self, team, name, pos):
#         cls = __class__
#         super().__init__(team,
#                          name,
#                          pos,
#                          hp=cls.HP,
#                          att=cls.ATT,
#                          arm=cls.ARM,
#                          evs=cls.EVS)