
from loa.team import Team
from .myunit import YUnit, YUnit2, YUnit3, YUnit4, YUnit5, YUnit6, YUnit7, YUnit8, YUnit9, YUnit10

def get_team():
    return YTeam("세깅이")

class YTeam(Team):
    def initialize(self):
        self.units.append(YUnit(self,"A-Unit01",0))
        self.units.append(YUnit2(self,"A-Unit02",1))
        self.units.append(YUnit3(self,"A-Unit03",2))
        self.units.append(YUnit4(self,"A-Unit04",3))
        self.units.append(YUnit5(self,"A-Unit05",4))
        self.units.append(YUnit6(self,"A-Unit06",5))
        self.units.append(YUnit7(self,"A-Unit07",6))
        self.units.append(YUnit8(self,"A-Unit08",7))
        self.units.append(YUnit9(self,"A-Unit09",8))
        self.units.append(YUnit10(self,"A-Unit10",9))
        
            
    def arrange(self, enemy: Team): 
        UnitCopy=[]
        collist=[0 for col in range(10)]
        result=[0 for col in range(10)]
        selected=[0,0,0,0,0,0,0,0,0,0]
        HpConduct=[[[0, 0,0] for col in range(10)]for row in range(10)]
        
        
        for i in range(10):
            for j in range(10): #i번째 enemy의 위치(행)에 있는 값에 대한 j번째 나의 위치(열)에 있는 값의 계산
                if self.units[j] is not None and enemy.units[i] is not None: 
                    HpConduct[i][j][2]=j
                    HpConduct[i][j][1]=max(0, (enemy.units[i].hp - max(1, self.units[j].att - enemy.units[i].arm)))
                    if (self.units[j].hp - max(1, 0.5*enemy.units[i].att - self.units[j].arm))>0:
                        HpConduct[i][j][0]=self.units[j].hp - max(1, 0.5*enemy.units[i].att - self.units[j].arm)
                    else:
                        HpConduct[i][j][0]=0
                    
            # enemy1-self1 enemy1-self2 enemy1-self3...
            # enemy2-self1 enemy2-self2 enemy2-self3....
            # 0>myhp, 1>enemyhp
                    
        
        for i in range(10):
            collist[i]=HpConduct[i][:]
            collist[i].sort(key=lambda x:(x[1], -x[0]))
        
        #results[i][j]->i:myhp , j:enemyhp(최적위치)

        for i in range(10):
            results=[[],[],[],[],[],[],[],[],[],[]]
            for k in range(10):
                results[collist[k][i][2]].append(k)
            for j in range(10):
                if result[j]==0 :
                    if len(results[j])==1 and selected[results[j][0]]==0:
                        result[j]=results[j][0]
                        selected[results[j][0]]=1
                    if len(results[j])>1:
                        get=[]
                        for k in range(len(results[j])):
                            if selected[results[j][k]]==0:
                                get.append(HpConduct[j][results[j][k]])
                        if len(get)>1:
                            get.sort(key=lambda x:(x[1], -x[0]))
                            result[j]=get[0][2]
                            selected[get[0][2]]=1
                            
        
                
        for i in range(10):
            if result[i]==0:
                results=[[0,0,0] for col in range(10)]
                for k in range(10):
                    #HpConduct[j][i]
                    HpConduct[k][i][2]=k
                    results[k][0]=HpConduct[k][i][0]
                    results[k][1]=HpConduct[k][i][1]
                    results[k][2]=HpConduct[k][i][2]
                results.sort(key=lambda x:(x[1],-x[0]))
                
                get=[]
                for k in range(10):
                    if (results[k][2] not in result) or (selected[0]==0 and results[k][2]==0):
                        get.append(results[k])
                    if len(get)>=1:
                        get.sort(key=lambda x:(x[1],-x[0]))
                        result[i]=get[0][2]
                        selected[get[0][2]]=1
        
        for l in range(10):
             for m in range(10):
                 if self.units[m] is not None :
                     if self.units[m].pos==result[l]:
                         UnitCopy=self.units[l]
                         self.units[l]=self.units[m]
                         self.units[m]=UnitCopy

        for n in range(10):
            if self.units[n] is not None:
                self.units[n].pos=n
        
