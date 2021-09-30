class employee:
    def __init__ (self,empid,empname,empdept):
        self.empid=empid
        self.empname=empname
        self.empdept=empdept
    def display(self):
        print(self.empid,
        self.empname,
        self.empdept)
e=employee("20411","jack","ANALYST")
e.display()