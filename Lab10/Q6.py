file1='file1.txt'
file2='file2.txt'
output='output.txt'
with open(file1,'r') as f1,open(file2,'r') as f2,open(output,'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    max_len = max(len(lines1), len(lines2))   
    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])
