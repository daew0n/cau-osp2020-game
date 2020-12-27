from loa.unit import Unit


class Normalman(Unit):
    
    HP = 100
    ATT = 40
    ARM = 6.6666666
    EVS = 0
    
    def __init__(self,team,name,pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
class Empty(Unit):
     
    HP = 10
    ATT = 5
    ARM = 0
    EVS = 0
    
    def __init__(self,team,name,pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)
