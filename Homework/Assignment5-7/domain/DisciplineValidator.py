from domain.Discipline import Discipline
from domain.DisciplineException import DisciplineException


class DisciplineValidator:
    def validate(self, discipline):
        """
        Validate if provided Discipline instance is valid
        discipline - Instance of Discipline type
        Return List of validation errors. An empty list if instance is valid.
        """
        if isinstance(discipline, Discipline) is False:
            raise DisciplineException("[ERROR] Not Discipline")

        if discipline.id < 0:
            raise DisciplineException("[ERROR] ID must not be negative")

        if len(discipline.name) == 0:
            raise DisciplineException("[ERROR] Discipline name cannot be blank")
