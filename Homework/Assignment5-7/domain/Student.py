class Student:
    def __init__(self, student_id, name):
        self._name = name
        self._id = student_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if isinstance(other, Student) is False:
            return False
        return self.id == other.id

    def __str__(self):
        return "StudentID: " + str(self._id).ljust(2) + "  Name: " + self._name

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.name < other.name

    def get_save_form(self):
        return "Student, " + self.id + ", " + self.name
