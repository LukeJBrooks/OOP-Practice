class Employee:

    def __init__(self,first, last, email, position, salary):
        self.first = first 
        self.last = last 
        self.email = first + last + '@company.com'
        self.position = position
        self.salary = salary

emp_1 = Employee('John', 'Jones', 'email', 'sales', 65000)

print (emp_1.email)