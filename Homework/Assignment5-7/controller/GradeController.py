from domain.Grade import Grade
from domain.GradeException import GradeException
from repository.Repository import *
from controller.UndoController import *


class GradeController:
    def __init__(self, validator, repository, disciplineRepository, studentRepository, undoController):
        self.__validator = validator
        self.__repository = repository
        self.__disciplineRepository = disciplineRepository
        self.__studentRepository = studentRepository
        self.__undoController = undoController

    def create(self, discipline_id, student_id, val):
        """
        Creates the grade and adds it to the repository
        :param discipline_id: The id of the discipline
        :param student_id: The id of the student
        :param val: The grade
        :return: The grade obj which was added
        """
        grade = Grade(discipline_id, student_id, val)

        if self.__disciplineRepository.find(discipline_id) is None:
            raise GradeException("[ERROR] Can't find the discipline with the ID given")

        if self.__studentRepository.find(student_id) is None:
            raise GradeException("[ERROR] Can't find the student with the given ID")

        self.__validator.validate(grade)
        self.__repository.store(grade)

        undo = FunctionCall(self.remove_single_grade, discipline_id, student_id, val)
        redo = FunctionCall(self.create, discipline_id, student_id, val)
        operation = Operation(undo, redo)
        self.__undoController.add_operation(operation)

        return grade

    def remove_single_grade(self, discipline_id, student_id, grade):
        _obj = self.__repository.get_all()[:]
        i = 0
        while i < len(_obj):
            if _obj[i].discipline_id == discipline_id and _obj[i].student_id == student_id and _obj[i].grade == grade:
                del _obj[i]
                break
            else:
                i += 1

        self.__repository.update_objects(_obj)

    def remove_by_discipline(self, discipline_id):
        """
        Removes the grades that are at the given discipline
        :param discipline_id: The id of the discipline
        :return: None
        """
        _obj = self.__repository.get_all()[:]
        co = CascadedOperation()
        listt = []
        i = 0
        while i < len(_obj):
            if _obj[i].discipline_id == discipline_id:
                undo = FunctionCall(self.create, discipline_id, _obj[i].student_id, _obj[i].grade)
                redo = FunctionCall(self.remove_single_grade, discipline_id, _obj[i].student_id, _obj[i].grade)
                op = Operation(undo, redo)
                listt.append(op)
                del _obj[i]
            else:
                i += 1

        self.__repository.update_objects(_obj)

        return listt

    def remove_by_student(self, student_id):
        """
        Removes all the grades that the student at student_id has
        :param student_id: The id of the student obj
        :return: None
        """
        _obj = self.__repository.get_all()[:]
        listt = []
        i = 0
        while i < len(_obj):
            if _obj[i].student_id == student_id:
                undo = FunctionCall(self.create, _obj[i].discipline_id, student_id, _obj[i].grade)
                redo = FunctionCall(self.remove_single_grade, _obj[i].discipline_id, student_id, _obj[i].grade)
                op = Operation(undo, redo)
                listt.append(op)
                del _obj[i]
            else:
                i += 1

        self.__repository.update_objects(_obj)

        return listt

    def all_students(self, discipline_id):
        """
        This function returns a repository that contains all the students that have a grade at the given discipline
        :param discipline_id: The id of the discipline
        :return: A Repository containing the students sorted by student name
        """
        full = self.__repository.get_all()
        new = Repository()
        for i in full:
            if i.discipline_id == discipline_id:
                ret = new.get_all()
                s = self.__studentRepository.find(i.student_id)
                if s not in ret:
                    new.store(s)

        return new.sort_()

    def all_disciplines(self):
        """
        This function goes through all the disciplines and returns a dict containing all the students that have a grade
        at that discipline.
        :return: A dictionary that has discipline_id as the key and a Repository of students which have that a grade
        at the discipline
        """
        _dict = {}
        for i in self.__repository.get_all():
            if i.discipline_id not in _dict.keys():
                _dict[i.discipline_id] = self.all_students(i.discipline_id)

        return _dict
