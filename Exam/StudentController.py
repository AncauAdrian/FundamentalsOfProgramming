from StudentValidator import StudentValidator


class StudentController:
    def __init__(self, student_repo):
        self._repo = student_repo

    def add_student(self, student):
        """ Checks if the Students has valid arguments and adds the Student to the Repository"""

        try:
            StudentValidator.validate(student)
        except ValueError as e:
            raise e

        _list = self._repo.get_all()

        for s in _list:
            if s.id == student.id:
                raise ValueError("[ERROR] A student with the given ID already exists!")

        self._repo.store(student)

    def give_bonus(self, p, b):
        _list = self._repo.get_all()[:]

        for s in _list:
            if s.attendance >= p:
                s.grade += b

                if s.grade > 10:
                    s.grade = 10

        self._repo.update(_list)
