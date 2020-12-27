from loa.unit import Unit
from loa.team import Team


def get_team():
    return MyTeam("Naega_Jeil_Jalnaga")


class MyUnit1(Unit):
    
    HP = 20  # Hit Points (health points)    
    ATT = 5  # Attack
    ARM = 0 # Armor
    EVS = 2.5 # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class MyUnit2(Unit):
    
    HP = 100 # Hit Points (health points)    
    ATT = 40 # Attack
    ARM = 6.6666  # Armor
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
        
class MyUnit3(Unit):
    
    HP  = 100  # Hit Points (health points) 
    ATT = 40  # Attack
    ARM = 0  # Armor
    EVS = 5  # Evasion
        
    def __init__(self, team, name, pos):
        cls = __class__
        super().__init__(team,
                         name,
                         pos,
                         hp=cls.HP,
                         att=cls.ATT,
                         arm=cls.ARM,
                         evs=cls.EVS)

class MyUnit4(Unit):
    
    HP = 50  # Hit Points (health points) 
    ATT = 5  # Attack
    ARM = 0 #Armor
    EVS = 10  # Evasion
        
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
        self.units.append(MyUnit1(self, "Unit1", 0))
        self.units.append(MyUnit1(self, "Unit1", 1))
        self.units.append(MyUnit1(self, "Unit1", 2))
        self.units.append(MyUnit1(self, "Unit1", 3))
        self.units.append(MyUnit2(self, "Unit2", 4))
        self.units.append(MyUnit2(self, "Unit2", 5))
        self.units.append(MyUnit2(self, "Unit2", 6))
        self.units.append(MyUnit2(self, "Unit2", 7))
        self.units.append(MyUnit2(self, "Unit2", 8))
        self.units.append(MyUnit2(self, "Unit2", 9))
        
    
    def arrange(self, enemy:Team):
        m_pos = None # my position
        t_pos = None # target position
        for i in range(self.num_positions):
            if (self.units[i]!=None) and (m_pos==None):
                m_pos = i
            elif (self.units[i]!=None) and (self.units[m_pos].att<self.units[i].att):
                m_pos = i
        for i in range(enemy.num_positions):
            if (enemy.units[i]!=None) and (t_pos==None):
                t_pos = i
            elif (enemy.units[i]!=None) and (enemy.units[i].hp-self.units[m_pos].att+enemy.units[i].arm<enemy.units[t_pos].hp-self.units[m_pos].att+enemy.units[t_pos].arm):
                t_pos = i

        new = self.units[t_pos]
        
        self.units[t_pos] = self.units[m_pos]
        self.units[m_pos] = new
        
        if (self.units[t_pos] != None):
            self.units[t_pos].pos = t_pos
        if (self.units[m_pos] != None):
            self.units[m_pos].pos = m_pos
    
