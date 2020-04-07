class DisciplineException(Exception):
    def __init__(self, msg):
        self._message = msg

    def get_message(self):
        return self._message

    def __str__(self):
        return self._message
