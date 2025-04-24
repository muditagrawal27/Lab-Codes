import csv
data_dict = []
with open('C:\\Users\\Admin\\Desktop\\Python\\Lab10\\data.csv', mode='r') as f:
  r = csv.reader(f,delimiter=',')
  for i in r:
     record = {
         'RollNo': int(i[0]),
            'Name': i[1],
            'Subject1': int(i[2]),
            'Subject2': int(i[3]),
            'Subject3': int(i[4]),
            'Total': int(i[2]) + int(i[3]) + int(i[4])
        }
     data_dict.append(record)
for record in data_dict:
    print(record)