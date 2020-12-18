from loa.team import Team


def get_team():
    return LOOK("LOOK")


class LOOK(Team):

    def arrange(self, enemy: Team):
        UNIT = []
        result = [0 for i in range(10)]
        for i in range(10):
             for j in range(10):
                 if self.units[j] != None:
                     if self.units[j].pos == result[i]:
                         UNIT = self.units[i]
                         self.units[i] = self.units[j]
                         self.units[j] = UNIT

        for i in range(10):
            if self.units[i] != None:
                self.units[i].pos= i
