class UndoController:
    def __init__(self):
        self._operations = []
        self._index = -1
        self._isUndoInstance = False

    def add_operation(self, operation):
        if self._isUndoInstance is True:
            return

        self._index += 1
        self._operations = self._operations[:self._index + 1]
        self._operations.append(operation)

    def undo(self):
        if self._index == -1:
            return False

        self._isUndoInstance = True
        self._operations[self._index].undo()
        self._isUndoInstance = False
        self._index -= 1
        return True

    def redo(self):
        if self._index >= len(self._operations):
            return False

        self._isUndoInstance = True
        self._index += 1
        self._operations[self._index].redo()
        self._isUndoInstance = False
        return True


class Operation:
    def __init__(self, undoFunc, redoFunc):
        self._undoFunction = undoFunc
        self._redoFunction = redoFunc

    def undo(self):
        self._undoFunction.call()

    def redo(self):
        self._redoFunction.call()


class CascadedOperation:
    def __init__(self):
        self._operations = []

    def add(self, oper):
        self._operations.append(oper)

    def undo(self):
        for i in self._operations:
            i.undo()

    def redo(self):
        for i in self._operations:
            i.redo()

    def get_all(self):
        return self._operations


class FunctionCall:
    def __init__(self, _function, *params):
        self._function = _function
        self._params = params

    def call(self):
        self._function(*self._params)