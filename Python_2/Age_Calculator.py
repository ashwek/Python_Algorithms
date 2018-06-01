import time

class Age_Calc:

    def __init__(self):
        print "\n\tEnter Your Birth Details Below" 
        self._year = int(input("\t\t-> Year = "))
        self._month = int(input("\t\t-> Month (Number) = "))
        self._day = int(input("\t\t-> Day/Date = "))
        self._Hour = int(input("\t\t-> Hour (24 Hours) = "))
        self._Min = int(input("\t\t-> Minute = "))
        self._Sec = int(input("\t\t-> Second = "))

        self.Convert(self._year, self._month, self._day, self._Hour, self._Min, self._Sec)
        del self._year, self._month, self._day, self._Hour, self._Min, self._Sec
        raw_input("Press any key to continue...")

    def Positive(self, Diff):
            if(Diff[5]<0):
                    while(Diff[5]<0):
                            Diff[4]-=1;Diff[5]+=60
            if(Diff[4]<0):
                    while(Diff[4]<0):
                            Diff[3]-=1;Diff[4]+=60
            if(Diff[3]<0):
                    while(Diff[3]<0):
                            Diff[2]-=1;Diff[3]+=24
            if(Diff[2]<0):
                    while(Diff[2]<0):
                            Diff[1]-=1;Diff[2]+=30
            if(Diff[1]<0):
                    while(Diff[1]<0):
                            Diff[0]-=1;Diff[1]+=12

    def Convert(self, y, M, d, h, m, s):
            now = time.localtime()
            second = list(now)
            second[0] = y; second[1] = M; second[2] = d
            second[3] = h; second[4] = m; second[5] = s
            second = time.struct_time(second)
            NowList = list(now)
            SecondList = list(second)

            for i in range(0,3):
                    NowList.pop();SecondList.pop()

            Diff=[]
            for i in range(0,len(NowList)):
                    Diff.append(NowList[i]-SecondList[i])
            del SecondList, NowList, second, now

            self.Positive(Diff)
            print "\n\tYour Age is :"
            print "\t\t -> Years = ",Diff[0] ;print "\t\t -> Months = ",Diff[1] ;
            print "\t\t -> Days = ",Diff[2] ;print "\t\t -> Hours = ",Diff[3] ;
            print "\t\t -> Minutes = ",Diff[4] ;print "\t\t -> Seconds = ",Diff[5] 
            

a = Age_Calc();
