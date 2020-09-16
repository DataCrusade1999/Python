class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + "@gmail.com"


class Good(Student):
    def __init__(self, first, last, good):
        super().__init__(first, last)
        self.good = good


stu1 = Good('Norman', 'Lewis', 'yes')
print(stu1.last)
print(stu1.first)
print(stu1.email)
print(stu1.good)
