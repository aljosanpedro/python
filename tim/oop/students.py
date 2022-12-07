class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max):
        # passed in
        self.name = name
        self.max = max

        # unique to class
        self.students = []
        self.active = False

    def add_student(self, student):
        # return if successfully added
        if len(self.students) < self.max:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        grades = 0
        for student in self.students:
            grades += student.grade

        return grades / len(self.students)


def main():
    # students
    tim = Student("Tim", 19, 95)
    bill = Student("Bill", 19, 75)
    jill = Student("Jill", 19, 65)

    # courses
    science = Course("Science", 2)
    print(science.add_student(tim))
    print(science.add_student(bill))
    print(science.add_student(jill)) # False bc max = 2
    print(science.get_average_grade())

    # get specific info
    print(science.students[0].name) # Tim, bc 1st student's name

if __name__ == "__main__":
    main()
