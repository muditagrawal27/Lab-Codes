class Time:
    def __init__(self,hr,min,second):
        self.hr=hr
        self.min=min
        self.second=second
    def time(self):
        self.min+=self.second//60
        self.second%=60
        self.hr+=self.min//60
        self.min%=60
        self.hr%=24
    def addtime(self, other):
        newhr=self.hr+other.hr
        newmin=self.min+other.min
        newsec=self.second+other.second
        return Time(newhr,newmin,newsec)
    def subtime(self, other):
        totalsecself=self.hr * 3600 + self.min * 60 + self.second
        totalsecother=other.hr * 3600 + other.min * 60 + other.second
        diff=(totalsecself - totalsecother) % (24 * 3600)
        hr = diff // 3600
        min = (diff % 3600) // 60
        sec = diff % 60
        return Time(hr,min,sec)
    def __str__(self):
        return f"{self.hr:02}:{self.min:02}:{self.second:02}"

time1 = Time(10, 45, 30)
time2 = Time(2, 20, 40)
print("Time 1:", time1)
print("Time 2:", time2)
print("Added Time:",time1.addtime(time2))
print("Subtracted Time:",time1.subtime(time2))