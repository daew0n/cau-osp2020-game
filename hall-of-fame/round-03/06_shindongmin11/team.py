from loa.team import Team


def get_team():
    return Team1("CAN WIN")


class Team1(Team):
            
    def arrange(self, enemy: Team):
        first_unit = self.units[0]
        for i in range(self.num_positions - 1):
            j = i + 1 
            self.units[i] = self.units[j]
            if self.units[i] != None:
               self.units[i].pos = i 
        # end of for
        self.units[-1] = first_unit
        if self.units[-1] != None:
            self.units[-1].pos = self.num_positions - 1
            
        enemypos = 0
        enemyarm = 20
        myteampos = 0
        myteamatt = 0
        
        for i in range (enemy.num_positions):
            if enemy.units[i]!=None and enemy.units[i].arm<enemyarm:
                enemyarm = enemy.units[i].arm
                enemypos = enemy.units[i].pos
        
        for i in range (self.num_positions):
            if self.units[i]!=None and self.units[i].att>=myteamatt:
                myteamatt = self.units[i].att
                myteampos = self.units[i].pos
                
        change_unit = self.units[enemypos]
        self.units[enemypos] = self.units[myteampos]
        
        if self.units[enemypos]!=None:
            self.units[enemypos].pos = enemypos
            
        self.units[myteampos] = change_unit 
        if self.units[myteampos]!=None:
            self.units[myteampos].pos = myteampos
