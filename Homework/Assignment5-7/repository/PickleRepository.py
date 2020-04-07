from repository.Repository import *
from repository.RepositoryException import *
import pickle


class PickleRepository(Repository):
    def __init__(self, filename):
        Repository.__init__(self)
        self._filename = filename

        self.load_file()

    def save_file(self):
        try:
            f = open(self._filename, "wb")
            pickle.dump(self, f)
            f.close()
        except IOError as e:
            raise RepositoryException("[ERROR] Cannot load file - " + str(e))

    def load_file(self):
        try:
            f = open(self._filename, "rb")
            Repository.update_objects(self, pickle.load(f).get_all())
        except IOError as e:
            raise RepositoryException("[ERROR] Cannot load file - " + str(e))