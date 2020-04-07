class StudentValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate(student):
        n = student.name.split()

        if len(n) < 2:
            raise ValueError("[ERROR] Name is not valid")

        if len(n[0]) < 3 or len(n[1]) < 3:
            raise ValueError("[ERROR] Name is not valid")

        if student.attendance < 0:
            raise ValueError("[ERROR] Attendance is not valid")

        if student.grade < 0 or student.grade > 10:
            raise ValueError("[ERROR] Grade is not valid")

        return None
