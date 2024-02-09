#My notes for OOP learning

#What is a class? A template that defines the methods or variables that fall under that class
#Classes help us logically organize data that we can reuse later in clever ways 
#Every class will have specific methods and attributes
#Each specific person in the following class "Person" will be an 'instance' of that class

class Person:
#the following is the method we'll need to initialize every time a new object is created
    def __init__(self,first,last,eye_color,hair_color,age,hobby,job,email):
#note that by convention, a method takes the instance as its first argument, 'self'
#the following are the attributes 
        
        self.first=first
        self.last=last
        self.eye_color=eye_color
        self.hair_color=hair_color
        self.age=age
        self.hobby=hobby
        self.job=job
        self.email=first+'.'+last+'@python.com'

#here's one method that does something, gets the full name
    def get_full_name(self):
        return '{} {}'.format(self.first,self.last)
    
#here's a method that gives someone a personalized birthday greeting
    def birthday_message(self):
        return 'Happy Birthday ' + self.first + "!" +'\n' + "I can't believe you are " + str(self.age) +' already!'

#and a method that return a person's name and job, in caps  
    def cap_name_and_job(self):
        return '{} {} {}'.format(self.first,self.last,self.job).upper()

#now we need some objects, or instances within the class
me = Person('luke','brooks','blue','brown',43,'guitar','wanna be software guy','email')
person_2 = Person('John','Smith','brown','black',27,'fishing','sales','email')
person_3 = Person('Katie','Jones','green','blonde',35,'reading','lawyer','email')

#try it out!
print(me.email)
print(person_2.hobby)
print(person_3.age)

#now try the first method...
print(me.get_full_name())

#the second method...
print(person_2.birthday_message())

#and finally
print (me.cap_name_and_job())




