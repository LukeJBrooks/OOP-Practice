#first, define the upper class:
class Employee:

    #'class variables' are variables that are the same across each instance of a class, so they go outside the instance variable methods.
    #One example might be the follwoing empployee raise amount. Note that we will use this variable in the apply_raise method further down! 
    raise_amount = 1.05

    #another exmaple might be the follwing, where the number of employees would be the same regardless of instances
    num_of_emps = 0

    #next we put the instance variables into an init method
    def __init__(self,first,last,position,salary):
        self.first = first 
        self.last = last 
        self.position = position
        self.salary = salary
        self.email = first + '.' + last + "@companyname"

    #each time we create and instantiate a new employee, we can increment the num_of_emps variable: 
        Employee.num_of_emps +=1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return self.salary
    
    #a regular method automatically takes in the instance as the first argument 
    #class methods take the class as the first argument 
    #static methods  

    
    @classmethod
    def set_raise_amount(cls, new_amount):
        cls.raise_amount = new_amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, position, salary = emp_str.split('-')
        return cls(first, last, position, salary)
    
# a class can also inherit from a higher class: 
class Developer(Employee):

    def __init__(self,first,last,position,salary,lang):
        super().__init__(first,last,position, salary)
        self.lang = lang

emp_1 = Employee('Max','Smith','warehouse', 50000)
dev_1 = Developer('Luke','Brooks','sales', 90000,'java')
emp_str_1 = 'Luke-Brooks-coder-75000'


print(emp_1.last)
print (Employee.num_of_emps)
print (dev_1.lang)
print (emp_1.apply_raise())

# This is looking great!!


Employee.set_raise_amount(11)
print (emp_1.apply_raise())
print (emp_str_1)

new_emp_1 = Employee.from_string(emp_str_1)
print (new_emp_1.last)

