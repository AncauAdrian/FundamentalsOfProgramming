from domain.StudentValidator import StudentValidator
from domain.DisciplineValidator import DisciplineValidator
from domain.GradeValidator import GradeValidator
from controller.DisciplineController import *
from controller.GradeController import *
from controller.StudentController import *
from repository.Repository import Repository
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.undoController = UndoController()

        self.studentRepo = Repository()
        self.studentValidator = StudentValidator()
        self.studentController = StudentController(self.studentValidator, self.studentRepo, self.undoController)

        self.disciplineRepo = Repository()
        self.disciplineValidator = DisciplineValidator()
        self.disciplineController = DisciplineController(self.disciplineValidator, self.disciplineRepo, self.undoController)

        self.gradeRepo = Repository()
        self.gradeValidator = GradeValidator()
        self.gradeController = GradeController(self.gradeValidator, self.gradeRepo, self.disciplineRepo, self.studentRepo, self.undoController)

    def test_student(self):
        stud = Student(1, "Ancau")
        self.assertTrue(stud.id == 1 and stud.name == "Ancau")

        self.assertTrue(len(self.studentRepo) == 0)

        anca = self.studentController.create(1, "Ancau Adrian")
        popa = self.studentController.create(2, "Popa Cristian")

        self.assertRaises(StudentException, self.studentController.create, 2, "Niganinga")

        self.assertTrue(self.studentController.find(1) == anca)
        self.assertTrue(self.studentRepo.find(2) == popa)

        self.assertEqual(len(self.studentRepo), 2)
        cascade_remove(self.studentController, self.gradeController, self.undoController, 2)

        self.assertTrue(len(self.studentRepo), 1)
        self.undoController.undo()

        self.assertTrue(len(self.studentRepo), 2)
        self.undoController.redo()
        self.assertTrue(len(self.studentRepo), 1)

    def test_discipline(self):
        math = self.disciplineController.create(1, "Math")
        engl = self.disciplineController.create(2, "English")

        self.assertEqual(len(self.disciplineRepo), 2)
        self.assertEqual(self.disciplineRepo.find(1), math)

        self.assertEqual(self.disciplineController.find(2), engl)
        self.disciplineController.update(2, 'History')
        self.assertEqual(self.disciplineController.find(2), Discipline(2, 'History'))

    def test_grade(self):
        first = self.gradeController.create(1, 1, 10)
        second = self.gradeController.create(2, 1, 7)
        self.assertRaises(GradeException, self.gradeController.create, 1, 1, 12)

        self.gradeController.remove_single_grade(1, 1, 10)
        self.assertNotIn(first, self.gradeController.all_students(1))

    def undo_test(self):
        self.disciplineController.create(3, "Undo test")
        self.undoController.undo()
        self.assertNotIn(Discipline(3, "Undo test"), self.disciplineRepo.get_all())

        self.undoController.redo()
        self.assertIn(Discipline(3, "Undo test"), self.disciplineRepo.get_all())


def cascade_remove(studentController, gradeController, undoController, _id):
    co = CascadedOperation()

    co.add(studentController.remove(_id))
    listt = gradeController.remove_by_student(_id)
    for i in listt:
        co.add(i)

    undoController.add_operation(co)


t = Test()
t.setUp()
t.test_student()
t.test_discipline()
t.test_grade()
