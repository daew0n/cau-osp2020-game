from loa.team import Team


def get_team():
    return LittleLyrical("LittleLyrical")


class LittleLyrical(Team):
        
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
        
        minHP = 50
        for i in range(self.num_positions - 1):
            if self.units[i] != None:
                if self.units[i].hp < minHP: 
                    minHP = self.units[i].hp 
        
        for i in range(self.num_positions - 1):
            if self.units[i] != None:
                if self.units[i].hp == minHP:
                    minhpunit = self.units[i]
                    self.units[i] = self.units[i+1]
                    self.units[i+1] = minhpunit
                    
        
        for i in range(self.num_positions - 1):
            if self.units[i] != None:
               self.units[i].pos = i
           
        if self.units[-1] != None:
            self.units[-1].pos = 9
        
