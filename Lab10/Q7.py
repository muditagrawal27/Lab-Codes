import json
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary
    def __str__(self):
        return f"Employee Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.doj}, Salary: {self.salary}"
    def to_dict(self):
        return {
            "empcode": self.empcode,
            "empname": self.empname,
            "doj": self.doj,
            "salary": self.salary
        }
    def from_dict(data):
        return Employee(data["empcode"], data["empname"], data["doj"], data["salary"])
    
def serialize_employee(employee, filename):
    with open(filename, 'w') as file:
        json.dump(employee.to_dict(), file)
    print("Employee data serialized successfully.")
def deserialize_employee(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    print("Employee data deserialized successfully.")
    return Employee.from_dict(data)
if __name__ == "__main__":
    emp = Employee(101, "John Doe", "2023-01-15", 50000)
    serialize_employee(emp, "employee_data.json")
    deserialized_emp = deserialize_employee("employee_data.json")
    print(deserialized_emp)