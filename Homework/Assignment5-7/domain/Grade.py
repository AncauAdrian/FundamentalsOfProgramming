class Grade:
    def __init__(self, discipline_id, student_id, grade):
        self._disc_id = discipline_id
        self._stud_id = student_id
        self._grade = grade

    @property
    def discipline_id(self):
        return self._disc_id

    @property
    def student_id(self):
        return self._stud_id

    @property
    def grade(self):
        return self._grade

    def __eq__(self, other):
        if isinstance(other, Grade) is False:
            return False
        return self.discipline_id == other.discipline_id and self.student_id == other.student_id

    def __str__(self):
        return "DisciplineID: " + str(self._disc_id) + "  StudentID: " + str(self._stud_id) + "  Grade: " + str(self._grade)

    def __repr__(self):
        return str(self)
