# student.py

class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    # group.py

    class Group:
        def __init__(self, name):
            self.name = name
            self.students = []

        def add_student(self, student):
            if student not in self.students:
                self.students.append(student)

        def delete_student(self, last_name):
            for student in self.students:
                if student.last_name == last_name:
                    self.students.remove(student)
                    return

        def find_student(self, last_name):
            for student in self.students:
                if student.last_name == last_name:
                    return student
            return None

        def __str__(self):
            student_list = ", ".join(str(student) for student in self.students)
            return f"Group {self.name}: {student_list}"