from loa.unit import Unit

class Unit1(Unit):

    HP = 30.5 # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 13  # Armor
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
class Unit2(Unit):

    HP = 41  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 6  # Armor
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

class Unit3(Unit):

    HP = 32.01  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 11.993  # Armor
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