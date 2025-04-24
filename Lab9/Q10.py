def frequency(str):
    words = str.split()
    freqdict = {}
    for i in words:
        if i in freqdict:
            freqdict[i] += 1
        else:
            freqdict[i] = 1
    sortedfreq = dict(sorted(freqdict.items()))
    return sortedfreq
str = input("Enter a string: ")
print(frequency(str))