import csv
data = [
    ["Name", "Age", "City"],
    ["Rishi", 30, "Mumbai"],
    ["Abhishek", 25, "Jaipur"],
    ["Shrishti", 35, "Chennai"]
]
file_path = "output.csv"
with open(file_path, mode='w', newline='',) as file:
    writer = csv.writer(file)
    writer.writerows(data)
