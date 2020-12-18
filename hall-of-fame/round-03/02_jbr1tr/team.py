from loa.team import Team

def get_team():
    return MyTeam("AGANG")


class MyTeam(Team):
    def initialize(self):
        pass

    def arrange(self, enemy:Team):
        m_pos = None
        e_pos = None
        for i in range(self.num_positions):
                if self.units[i] != None and m_pos == None:
                    m_pos = i
                elif self.units[i] != None and self.units[i].att > self.units[m_pos].att:
                    m_pos = i
        for i in range(enemy.num_positions):
            if enemy.units[i] != None and e_pos == None:
                    e_pos = i
            elif enemy.units[i] != None and enemy.units[i].hp-self.units[m_pos].att+enemy.units[i].arm < enemy.units[e_pos].hp-self.units[m_pos].att+enemy.units[e_pos].arm :
                    e_pos = i

        self.units[m_pos] ,self.units[e_pos] = self.units[e_pos],self.units[m_pos]

        if self.units[e_pos] != None:
            self.units[e_pos].pos = e_pos
        if self.units[m_pos] != None:
            self.units[m_pos].pos = m_pos
