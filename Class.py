def main():
    class Student:
        def __init__(self, first, last, age):
            self.first = first
            self.last = last
            self.age = age

        def get_mail(self):
            self.email = self.first + self.last + '@gmail.com'
            return self.email

        @classmethod
        def age(cls, first, last, age):
            return cls(first, last, age)

        """Above Method Is Called An Alternative
             Contructor"""

        @staticmethod
        def good_or_not(age):
            if age > 18:
                print('good')
            else:
                print('bad')

    Student_1 = Student('Ashutosh', 'Pandey', 90)
    print(Student_1.get_mail())
    Student_str = 'Ashutosh-Pandey'
    New_Student = Student.age('Ashutosh', 'Pandey', 22)
    print(New_Student.age)
    print(Student_1.age)
    print(Student_1.good_or_not(60))


if __name__ == '__main__':
    main()
