# Employee Details

class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  
        self.salary = salary
        self.post = post

    def display(self):
        super().display()
        print("Salary:", self.salary)
        print("Post:", self.post)


Person1 = Employee("Gyanendra", 234876, 200000, "Developer")
Person2 = Employee("Rishi", 234876, 250000, "Senior Developer")
Person3 = Employee("Sita", 234876, 100000, "Intern")
Person4 = Employee("Stuti", 234876, 270000, "CEO")
Person5 = Employee("Shubh", 234876, 300000, "Manager")

Person1.display()
print()
Person2.display()
print()
Person3.display()
print()
Person4.display()
print()
Person5.display()
