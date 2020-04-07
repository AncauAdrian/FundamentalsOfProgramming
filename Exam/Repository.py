from Student import *


class Repository:
    def __init__(self):
        self._obj = []

    def get_all(self):
        return self._obj

    def store(self, student):
        self._obj.append(student)

    def __len__(self):
        return len(self._obj)

    def update(self, new):
        self._obj = new


class TextRepository(Repository):
    def __init__(self, file="Repo.txt"):
        Repository.__init__(self)
        self._filename = file
        self.load_file()

    def load_file(self):
        try:
            f = open(self._filename, "r")
            line = f.readline()
            while len(line) > 2:
                sep = line.split(",")
                stud = Student(int(sep[0]), sep[1], int(sep[2]), int(sep[3].strip()))
                Repository.store(self, stud)
                line = f.readline()

            f.close()
        except IOError as e:
            raise e
