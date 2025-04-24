from datetime import datetime
date1=(19,11,2023)
date2=(4,3,2025)

dt1=datetime(date1[2],date1[1],date1[0])
dt2=datetime(date2[2],date2[1],date2[0])
diff=(abs(dt1-dt2).days)
print("Date 1:",dt1)
print("Date 2:",dt2)
print("Difference between the dates is:",diff,"days")