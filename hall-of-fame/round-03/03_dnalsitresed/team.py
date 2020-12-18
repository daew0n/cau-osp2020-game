from loa.team import Team


def get_team():
    return tresed("▒~O~D▒~D▒~\~Y▒~B▒")


class tresed(Team):

    def arrange(self, enemy:Team):
        first_unit = self.units[0]
        second_units = self.units[1]
        for i in range(8):
            j = i +2
            self.units[i] = self.units[j]
            if self.units[i] != None:
                self.units[i].pos = i

        self.units[-2] = first_unit
        self.units[-1] = second_units
        if self.units[-2] != None:
            self.units[-2].pos = 8
        if self.units[-1] != None:
            self.units[-1].pos = 9