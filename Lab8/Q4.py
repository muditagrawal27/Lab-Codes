def frequencychar(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print("Frequency of each character in the string is: ",freq)
string=input("Enter the string: ")
frequencychar(string)