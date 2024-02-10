#first, define the upper class:

class Employee:

    #'class variables' are variables that are shared among each variable of a class, so they go outside the methods:
    raise_amount = 1.05
    num_of_emps = 0

    #next we put the intsance variables into an init method
    def __init__(self,first,last,email,position,salary):
        self.first = first 
        self.last = last 
        self.email = first + last + '@company.com'
        self.position = position
        self.salary = salary

        Employee.num_of_emps +=1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return self.salary

class Developer(Employee):

    def __init__(self,first,last,email,position,salary,lang):
        super().__init__(first,last,email,position, salary)
        self.lang = lang

emp_1 = Employee('Max', 'Smith', 'email','warehouse', 50000)
dev_1 = Developer('Luke','Brooks','email','sales',90000,'java')

print (emp_1.raise_amount)
print (Employee.num_of_emps)
print (dev_1.lang)
print (emp_1.apply_raise())




