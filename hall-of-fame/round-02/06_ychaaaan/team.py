from loa.team import Team
from loa.unit import Unit


def get_team():
    return Guineapig("Guineapig")


class atk(Unit):

    HP = 32.0015   # Hit Points (health points)
    ATT = 0   # Attack
    ARM = 11.999  # Armor
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


class tank(Unit):

    HP = 32.075 # Hit Points (health points)
    ATT = 0 # Attack
    ARM = 11.95  # Armor
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


class Guineapig(Team):
    def initialize(self):
        for i in range(5):
            A_unit = atk(self, "atk%02d"%(i+1), i)
            self.units.append(A_unit)

        for i in range(5):
            B_unit = tank(self, "tank%02d"%(i+1), i+5)
            self.units.append(B_unit)

    def arrange(self, enemy: Team):
        pass
