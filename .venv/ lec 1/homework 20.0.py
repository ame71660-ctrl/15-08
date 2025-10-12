class TooManyStudentsError(Exception):
    """Виняток, якщо в групі більше 10 студентів."""
    def __init__(self, message= "У групі не може більше 10 студентів!"):
        super().__init__(message)
class Student:
    def __init__(self, name,surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'
class Group:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsError()
        self.students.append(student)
    def __str__(self):
        return f'{self.name}\n'+"\n".join([str(student) for student in self.students])
try:
    group = Group("Python Developers")
    for i in range(1, 12):
        group.add_student(Student(f"Student{i}", "Test"))
        print(f"Додано: Student{i}")
except TooManyStudentsError as e:
    print(f"Помилка: {e}")

print("\nПоточна група:")
print(group)