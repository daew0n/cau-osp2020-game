from loa.unit import Unit

class Tanker(Unit):

    HP = 32.015  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 11.99  # Armor
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

class alpha(Unit):

    HP = 32.015  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 11.99  # Armor
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

class beta(Unit):

    HP = 32.015  # Hit Points (health points)
    ATT = 0  # Attack
    ARM = 11.99  # Armor
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

