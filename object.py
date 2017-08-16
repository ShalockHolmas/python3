import sys


class people:
    age = 0
    name = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("people-name=", self.name, 'age=', self.age)


class student(people):
    grade = 0
    __sex = True

    def __init__(self, name, age, grade):
        people.__init__(self, name, age)
        self.grade = grade

    def speak(self):
        print("student-name=", self.name, 'age=', self.age, 'grade=', self.grade)

    def getSex(self):
        return self.__sex

    def setSex(self, sex):
        self.__sex = sex

p = people('gu',13)
p.speak()

s = student('jie', 23, 2)
s.speak()
print(s.getSex())
s.setSex(False)
print(s.getSex())

