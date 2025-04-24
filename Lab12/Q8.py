class String:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        else:
            raise TypeError("Concatenation not possible.")
        return self
    def lowercase(self):
        self.value = self.value.lower()
        return self
    def uppercase(self):
        self.value = self.value.upper()
        return self
    def __str__(self):
        return self.value

s1 = String("Computer")
s2 = String(" Programming")
print("After concatenation:",s1.add(s2))
print("After Lower:",s1.lowercase())
print("After Upper:",s1.uppercase())