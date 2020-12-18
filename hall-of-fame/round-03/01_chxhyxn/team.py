from loa.unit import Unit
from loa.team import Team


def get_team():
    return MyTeam("▒~_~Q~Q")


class MyTeam(Team):

    def arrange(self, enemy: Team):
        for i in range(self.num_positions):
            if self.units[i]!=None:
                for j in range(enemy.num_positions):
                    if enemy.units[j]==None:
                        if self.units[j]==None:
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=None
                            break
        for i in range(self.num_positions):
            if self.units[i]!=None:
                for j in range(enemy.num_positions):
                    if enemy.units[j]!=None and enemy.units[j].att>self.units[i].arm+1:
                        if self.units[j]==None:
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=None
                            break
                        elif self.units[j]!=None and enemy.units[j].att>self.units[j].arm+1:
                            pass
                        else:
                            temp=self.units[j]
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=temp
                            self.units[i].pos=i
                            break
        for i in range(self.num_positions):
            if self.units[i]!=None:
                for j in range(enemy.num_positions):
                    if enemy.units[j]!=None and enemy.units[j].hp<=self.units[i].hp:
                        if self.units[j]==None:
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=None
                            break
                        elif self.units[j]!=None and self.units[j].hp>=self.units[i].hp:
                            pass
                        else:
                            temp=self.units[j]
                            self.units[j]=self.units[i]
                            self.units[j].pos=j
                            self.units[i]=temp
                            self.units[i].pos=i
                            break