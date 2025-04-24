src="source.txt"
dest="destination.txt"
with open(src,'r') as s,open(dest,'w') as d:
        for line in s:
            d.write(line.upper())
print("File copied successfully with lowercase converted to uppercase.")