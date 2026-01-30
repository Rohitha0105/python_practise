class Office:
    company="10k coders"
    def __init__(self, name, salary, id, department):
        self.my_name=name
        self.earning=salary
        self.id=id
        self.department = department
    def my_Details(self):
        return (self.my_name,self.id, self.earning, self.department)


emp1=Office("Rohi", 100000,1, "hr")
print(emp1.my_name)
emp2=Office ("Rohitha", 50000,2, "sales")
print(emp2.my_Details())
print(emp1.my_Details())