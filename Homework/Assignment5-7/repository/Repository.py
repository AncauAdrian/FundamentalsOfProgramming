from domain.Student import *
from domain.Discipline import *
from domain.Grade import *
from Ass9 import Structure, insertion_sort


class Repository:
    """
    Repository for storing domain objects
    """

    def __init__(self):
        # self._objects = []
        self._objects = Structure()

    def store(self, obj):
        """
        Stores the give object into the Repo
        """
        self._objects.append(obj)

    def update(self, obj):
        """
        Updates the given Object
        """
        for i in self._objects:
            if i == obj:
                i.name = obj.name

    def update_objects(self, new):
        """
        Updates all the objects from _objects with the new object list new
        """
        self._objects = new[:]

    def find(self, _id):
        """
        This function searches for a student with the given ID
        :param _id: a student ID
        :return: The student if found, None if not found
        """
        for i in self._objects:
            if i.id == _id:
                return i

        return None

    def search(self, string):
        """
        This function searches for the given string in all student names
        :param string: The string to search
        :return: Returns a repository that contains the matched students
        """
        empty = Repository()
        for i in self._objects:
            if string in i.name.lower():
                empty.store(i)

        return empty

    def delete(self, _id):
        """
        Deletes a student from the list
        :param _id: The id of the student we want to delete
        :return: None
        """
        i = 0
        while i < len(self._objects):
            if self._objects[i].id == _id:
                del self._objects[i]
            else:
                i += 1

    def get_all(self):
        return self._objects

    def __len__(self):
        return len(self._objects)

    def __str__(self):
        r = ""
        for e in self._objects:
            r += str(e)
            r += "\n"
        return r

    def __repr__(self):
        return str(self)

    def sort_(self):
        # return sorted(self._objects)
        return insertion_sort(self._objects, lambda x, y: x > y)

    def save_file(self):
        pass
