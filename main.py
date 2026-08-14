class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    school_name = "Generic University"

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def display_info(self):
        if not self.courses:
            course_list = "None"
        else:
            course_list = str(self.courses)
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, School: {self.school_name}, Courses: {course_list}")

if __name__ == "__main__":
    s = Student("Ben", 20, "S1234")
    s.display_info()
    s.enroll_course("Math 101")
    s.enroll_course("History 202")
    s.display_info()

    Student.school_name = "Tech Institute"
    s.display_info()
