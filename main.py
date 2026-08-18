import copy


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

        # Each Student gets an independent courses list.
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def display_info(self):
        course_list = ", ".join(self.courses)

        print(
            f"Name: {self.name}, Age: {self.age}, "
            f"ID: {self.student_id}, School: {self.school_name}, "
            f"Courses: [{course_list}]"
        )


if __name__ == "__main__":
    # Creating and displaying a Person
    p = Person("Cleo", 45)
    p.display_info()

    # Creating and displaying a Student
    s = Student("Dana", 22, "S9876")
    s.enroll_course("Biology")
    s.enroll_course("Chemistry")
    s.display_info()

    # Changing the class variable
    Student.school_name = "Tech Institute"

    s2 = Student("Eli", 21, "S2222")
    s2.display_info()

    # Demonstrating deep copy
    s3 = copy.deepcopy(s)
    s3.enroll_course("Physics")

    print("\nOriginal student:")
    s.display_info()

    print("\nDeep-copied student:")
    s3.display_info()
