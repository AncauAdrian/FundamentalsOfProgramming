from domain.Student import Student
from domain.StudentException import StudentException


class StudentValidator:
    def validate(self, student):
        """
        Validate if provided Student instance is valid
        student - Instance of Student type
        Return List of validation errors. An empty list if instance is valid.
        """
        if isinstance(student, Student) is False:
            raise StudentException("[ERROR] Not Student")

        if student.id < 0:
            raise StudentException("[ERROR] ID must not be negative")

        if len(student.name) == 0:
            raise StudentException("[ERROR] Student name can't be blank")
