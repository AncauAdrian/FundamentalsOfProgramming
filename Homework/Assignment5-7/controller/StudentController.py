from domain.Student import Student
from domain.StudentException import StudentException
from controller.UndoController import *


class StudentController:
    def __init__(self, validator, repository, undoController):
        self.__validator = validator
        self.__repository = repository
        self.__undoController = undoController

    def create(self, student_id, name):
        for i in self.__repository.get_all():
            if student_id == i.id:
                raise StudentException("[ERROR] This ID is already in use")

        student = Student(student_id, name)

        self.__validator.validate(student)
        self.__repository.store(student)

        undo = FunctionCall(self.remove, student_id)
        redo = FunctionCall(self.create, student_id, name)
        operation = Operation(undo, redo)
        self.__undoController.add_operation(operation)

        return student

    def update(self, student_id, name):
        student = Student(student_id, name)
        self.__validator.validate(student)
        self.__repository.update(student)

    def remove(self, student_id):
        name = self.__repository.find(student_id).name
        if name is None:
            raise StudentException("[ERROR] No can do")

        self.__repository.delete(student_id)

        redo = FunctionCall(self.remove, student_id)
        undo = FunctionCall(self.create, student_id, name)
        operation = Operation(undo, redo)
        #self.__undoController.add_operation(operation)
        return operation

    def find(self, _id):
        return self.__repository.find(_id)

    def search(self, string):
        return self.__repository.search(string.lower())
