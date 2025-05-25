
class Person:
    def __init__(self, name , age, classroom):
      self.name = name
      self.age = age
      self.classroom = classroom
    def display_info(self):
       print(self.name + ' ' + self.age)

class Student(Person):
    def __init__(self, name, age, classroom):
       Person.__init__(self, name, age)
       self.classroom = classroom
    def display_info(self):
      print(self.name + ' ' + self.age + ' ' + self.classroom)
      
      
      