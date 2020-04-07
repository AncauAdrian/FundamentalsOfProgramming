from domain.Grade import Grade
from domain.GradeException import GradeException

class GradeValidator:
    def validate(self, grade):
        """
        Validate if provided Grade instance is valid
        grade - Instance of Grade type
        Return List of validation errors. An empty list if instance is valid.
        """
        if isinstance(grade, Grade) is False:
            raise GradeException("[ERROR] Not Grade")

        if grade.grade < 1 or grade.grade > 10:
            raise GradeException("[ERROR] Invalid grade value")
