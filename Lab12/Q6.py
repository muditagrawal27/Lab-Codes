class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.date == other.date
        return False
    
date1 = Date(15, 10, 2023)
date2 = Date(15, 10, 2023)
date3 = Date(16, 10, 2023)
print(date1 == date2) 
print(date1 == date3)  