from loa.team import Team


def get_team():
    return MyTeam("원딜인권보호협회")


class MyTeam(Team):
        
    def arrange(self, enemy: Team):
        
        first_unit = self.units[0]
        second_unit = self.units[1]
        for i in range(self.num_positions - 2):
            j = i + 2
            self.units[i] = self.units[j]
            if self.units[i] != None:
               self.units[i].pos = i 
        # end of for
        self.units[-1] = first_unit
        self.units[-2] = second_unit
        if self.units[-1] != None:
            self.units[-1].pos = self.num_positions - 1
            
        if self.units[-2] != None:
            self.units[-2].pos = self.num_positions -2
