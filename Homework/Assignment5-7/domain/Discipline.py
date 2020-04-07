class Discipline:
    def __init__(self, discipline_id, name):
        self._name = name
        self._id = discipline_id

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
        if isinstance(other, Discipline) is False:
            return False
        return self.id == other.id

    def __str__(self):
        return "DisciplineID: " + str(self._id).ljust(2) + "  Name: " + self._name

    def __repr__(self):
        return str(self)