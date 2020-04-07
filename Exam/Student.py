class Student:
    def __init__(self, _id, _name, _attendance, _grade):
        self._id = _id
        self._name = _name
        self._attendance = _attendance
        self._grade = _grade

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def attendance(self):
        return self._attendance

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new):
        self._grade = new

    def __str__(self):
        return str(self.id) + ", " + self.name + ", " + str(self.attendance) + ", " + str(self.grade)

    def __lt__(self, other):
        if self.name < other.name:
            return True

        return False
