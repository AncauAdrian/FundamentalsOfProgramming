from repository.Repository import *
from repository.RepositoryException import *


class TextRepository(Repository):
    def __init__(self, _type, fileName = "TextRepo.txt"):
        Repository.__init__(self)
        self._fileName = fileName
        self._type = _type

        if _type == "student" or _type == "discipline":
            self.rep_to_text = self.stud_disc_to_string
            self.text_to_rep = self.string_to_stud_disc
        elif _type == "grade":
            self.rep_to_text = self.grade_to_string
            self.text_to_rep = self.string_to_grade
        else:
            raise RepositoryException("[ERROR] Invalid repository type")

        self.load_file()

    def store(self, obj):
        Repository.store(self, obj)
        self.save_file()

    def save_file(self):
        try:
            f = open(self._fileName, "w")
            for c in self.get_all():
                f.write(self.rep_to_text(c) + '\n')

            f.close()
        except IOError as e:
            raise RepositoryException("[ERROR] Cannot open file " + str(e))

    def load_file(self):
        try:
            f = open(self._fileName, "r")  # "r" = reading. it is a mode
            line = f.readline()
            while len(line) > 2:
                Repository.store(self, self.text_to_rep(line))
                line = f.readline()

            f.close()
        except IOError as e:
            raise RepositoryException("[ERROR] Cannot load file - " + str(e))

    def stud_disc_to_string(self, obj):
        return str(obj.id) + ", " + str(obj.name)

    def grade_to_string(self, obj):
        return str(obj.discipline_id) + ", " + str(obj.student_id) + ", " + str(obj.grade)

    def string_to_stud_disc(self, string):
        tok = string.split(",")

        if self._type == "student":
            return Student(int(tok[0]), tok[1].strip())
        else:
            return Discipline(int(tok[0]), tok[1].strip())

    def string_to_grade(self, string):
        tok = string.split(",")
        return Grade(int(tok[0]), int(tok[1]), int(tok[2]))