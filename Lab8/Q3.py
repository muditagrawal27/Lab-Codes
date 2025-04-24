def calminmaxsal(deptdata):
    minmaxsal={}
    for deptno,emp in deptdata.items():
        sal=list(emp.values())
        minmaxsal[deptno]=[min(sal),max(sal)]
    return minmaxsal

deptdata={
    "D001": {"E001": 45000, "E002": 35000, "E003": 40000},
    "D002": {"E004": 50000, "E005": 60000, "E006": 55000},
    "D003": {"E007": 65000, "E008": 70000, "E009": 75000}
}
calminmaxsal(deptdata)
for deptno,sal in calminmaxsal(deptdata).items():
    print("Department:",deptno)
    print("Minimum Salary:",sal[0])
    print("Maximum Salary:",sal[1])