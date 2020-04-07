class BoardException(Exception):
    def __init__(self, msg):
        self._message = msg

    def __str__(self):
        return self._message
