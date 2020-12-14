from loa.unit import Unit


        
class Fish(Unit):
    
    HP = 1.000005
    ATT = 0
    ARM = 0.000005
    EVS = 0
    
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         )
        

    
        

        
class Adelie_Penguin(Unit):
    
    HP = 21
    ATT = 0.001
    ARM = 120
    EVS = 10
    
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         )
        
class Cat(Unit):
    
    HP = 20.444
    ATT = 90.555
    ARM = 89
    EVS = 10
    
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         )
        
class Mice(Unit):
    
    HP = 0.000005
    ATT = 0
    ARM = 0.000005
    EVS = 0
    
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         )