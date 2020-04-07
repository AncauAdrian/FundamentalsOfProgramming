from domain.Discipline import Discipline
from domain.DisciplineException import DisciplineException
from controller.UndoController import *

class DisciplineController:
    def __init__(self, validator, repository, undoController):
        self.__validator = validator
        self.__repository = repository
        self.__undoController = undoController

    def create(self, discipline_id, name):
        for i in self.__repository.get_all():
            if discipline_id == i.id:
                raise DisciplineException("[ERROR] This ID is already in use")

        discipline = Discipline(discipline_id, name)

        self.__validator.validate(discipline)
        self.__repository.store(discipline)

        undo = FunctionCall(self.remove, discipline_id)
        redo = FunctionCall(self.create, discipline_id, name)
        operation = Operation(undo, redo)
        self.__undoController.add_operation(operation)

        return discipline

    def update(self, discipline_id, name):
        discipline = Discipline(discipline_id, name)
        self.__validator.validate(discipline)
        self.__repository.update(discipline)

    def remove(self, discipline_id):
        name = self.__repository.find(discipline_id).name
        if name is None:
            raise DisciplineException("[ERROR] No can do")

        self.__repository.delete(discipline_id)

        redo = FunctionCall(self.remove, discipline_id)
        undo = FunctionCall(self.create, discipline_id, name)
        operation = Operation(undo, redo)
        #self.__undoController.add_operation(operation)
        return operation

    def find(self, _id):
        return self.__repository.find(_id)

    def search(self, string):
        return self.__repository.search(string)