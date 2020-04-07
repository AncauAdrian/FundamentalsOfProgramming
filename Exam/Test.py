import unittest
from Student import *
from Repository import Repository
from StudentController import *


class StudentTestCase(unittest.TestCase):
    def test_student(self):
        s = Student(0, "Ana Maria", 9, 10)
        self.assertEqual(s.name, "Ana Maria")
        repo = Repository()
        cont = StudentController(repo)

        cont.add_student(s)
        self.assertRaises(ValueError, cont.add_student, Student(0, "New Name", 0, 0))
        self.assertRaises(ValueError, cont.add_student, Student(1, "Invalid", 0, 0))
        self.assertRaises(ValueError, cont.add_student, Student(1, "New Name", -1, 0))
        self.assertRaises(ValueError, cont.add_student, Student(1, "New Name", 0, 12))
        cont.add_student(Student(1, "New Name", 0, 0))
        self.assertEqual(len(repo), 2)