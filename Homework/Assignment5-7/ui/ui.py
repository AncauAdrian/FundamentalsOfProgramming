from domain.StudentValidator import StudentValidator
from domain.DisciplineValidator import DisciplineValidator
from domain.GradeValidator import GradeValidator
from controller.StudentStatusController import *
from controller.DisciplineController import *
from controller.GradeController import *
from controller.StudentController import *
from repository.TextRepository import *
from repository.PickleRepository import *


class UI:
    def __init__(self, settings):
        self._settings = settings
        print("repo_type is: " + settings["repo_type"])
        if settings["repo_type"] == "memory":
            self.studentRepo = Repository()
            self.disciplineRepo = Repository()
            self.gradeRepo = Repository()
        elif settings["repo_type"] == "text":
            self.studentRepo = TextRepository("student", settings["student"])
            self.disciplineRepo = TextRepository("discipline", settings["discipline"])
            self.gradeRepo = TextRepository("grade", settings["grade"])

            self.writeToBinaryFile("students.pickle", self.studentRepo)
            self.writeToBinaryFile("disciplines.pickle", self.disciplineRepo)
            self.writeToBinaryFile("grades.pickle", self.gradeRepo)
        elif settings["repo_type"] == "pickle":
            self.studentRepo = PickleRepository(settings["student"])
            self.disciplineRepo = PickleRepository(settings["discipline"])
            self.gradeRepo = PickleRepository(settings["grade"])

        self.undoController = UndoController()

        self.studentValidator = StudentValidator()
        self.studentController = StudentController(self.studentValidator, self.studentRepo, self.undoController)

        self.disciplineValidator = DisciplineValidator()
        self.disciplineController = DisciplineController(self.disciplineValidator, self.disciplineRepo, self.undoController)

        self.gradeValidator = GradeValidator()
        self.gradeController = GradeController(self.gradeValidator, self.gradeRepo, self.disciplineRepo, self.studentRepo, self.undoController)

        self.statusController = StudentStatusController(self.studentRepo, self.disciplineRepo, self.gradeRepo)

    def writeToBinaryFile(self, _filename, obj):
        f = open(_filename, "wb")
        pickle.dump(obj, f)
        f.close()

    def showmenu(self):
        print("Commands: ")
        print("1. add")
        print("2. remove")
        print("3. update")
        print("4. list")
        print("5. grade")
        print("6. search")
        print("7. statistics")
        print("8. undo")
        print("9. redo")
        print("99. halp")
        print("0. exit")

    def main_loop(self):
        self.showmenu()
        while True:
            self.studentRepo.save_file()
            self.disciplineRepo.save_file()
            self.gradeRepo.save_file()

            try:
                n = int(input(">>"))
            except ValueError:
                print("[ERROR] Invalid Command")
                continue

            if n == 0:
                break
            elif n == 1:
                print("-- add --")
                try:
                    m = int(input("1. Student - 2. Discipline  >>"))
                except ValueError:
                    print("[ERROR] Invalid entry!")
                    continue
                if m == 1:
                    try:
                        _id = int(input("Enter Student_ID: "))
                    except ValueError:
                        print("[ERROR] ID must be a number")
                        continue
                    _name = input("Enter Student_Name: ")

                    try:
                        self.studentController.create(_id, _name)
                    except StudentException as e:
                        print(e)

                elif m == 2:
                    try:
                        _id = int(input("Enter Discipline_ID: "))
                    except ValueError:
                        print("[ERROR] ID must be a number")
                        continue

                    _name = input("Enter Discipline_Name: ")

                    try:
                        self.disciplineController.create(_id, _name)
                    except DisciplineException as e:
                        print(e)
                else:
                    print("[ERROR] Invalid Command")
            elif n == 2:
                print("-- remove --")
                try:
                    m = int(input("1. Student - 2. Discipline  >>"))
                except ValueError:
                    print("[ERROR] Invalid entry!")
                    continue
                except AttributeError:
                    print("[ERROR] Couldn't find student")
                if m == 1:
                    try:
                        _id = int(input("Enter Student_ID: "))
                    except ValueError:
                        print("[ERROR] ID must be a number")
                        continue

                    try:
                        co = CascadedOperation()

                        co.add(self.studentController.remove(_id))
                        listt = self.gradeController.remove_by_student(_id)
                        for i in listt:
                            co.add(i)

                        self.undoController.add_operation(co)
                    except GradeException as e:
                        print(e)

                elif m == 2:
                    try:
                        _id = int(input("Enter Discipline_ID: "))
                    except ValueError:
                        print("[ERROR] ID must be a number")
                        continue

                    try:
                        co = CascadedOperation()
                        co.add(self.disciplineController.remove(_id))
                        listt = self.gradeController.remove_by_discipline(_id)
                        for i in listt:
                            co.add(i)

                        self.undoController.add_operation(co)
                    except GradeException as e:
                        print(e)
                else:
                    print("[ERROR] Invalid Command")

            elif n == 3:
                print("-- update --")
                try:
                    m = int(input("1. Student - 2. Discipline  >>"))
                except ValueError:
                    print("[ERROR] Invalid entry!")
                    continue
                if m == 1:
                    try:
                        _id = int(input("Enter Student_ID: "))
                    except ValueError:
                        print("[ERROR] ID must be a number")
                        continue

                    name = input("Enter New Name: ")

                    try:
                        self.studentController.update(_id, name)
                    except StudentException as e:
                        print(e)

                elif m == 2:
                    try:
                        _id = int(input("Enter Discipline_ID: "))
                    except ValueError:
                        print("[ERROR] ID must be a number")
                        continue

                    name = input("Enter New Name: ")

                    try:
                        self.disciplineController.update(_id, name)
                    except DisciplineException as e:
                        print(e)

            elif n == 4:
                print("-- list --")
                try:
                    m = int(input("1. Student - 2. Discipline - 3. Grades   >>"))
                except ValueError:
                    print("[ERROR] Invalid entry!")
                    continue
                if m == 1:
                    print(self.studentRepo)

                elif m == 2:
                    print(self.disciplineRepo)

                elif m == 3:
                    print(self.gradeRepo)

            elif n == 5:
                print("-- grade --")
                try:
                    disc = int(input("Discipline ID: "))
                    stud = int(input("Student ID: "))
                    grade = int(input("Grade: "))
                except ValueError:
                    print("[ERROR] Invalid input!")
                    continue

                self.gradeController.create(disc, stud, grade)

            elif n == 6:
                print("-- search --")
                try:
                    m = int(input("1. By ID - 2. By Name  >>"))
                except ValueError:
                    print("[ERROR] Invalid entry!")
                    continue
                if m == 1:
                    try:
                        _id = int(input("Enter ID: "))
                    except ValueError:
                        print("[ERROR] ID must be a number")
                        continue

                    print("____________________Students____________________")
                    print(self.studentController.find(_id))
                    print()
                    print("___________________Disciplines__________________")
                    print(self.disciplineController.find(_id))

                elif m == 2:
                    string = input("Enter a string to search by: ")
                    print("____________________Students____________________")
                    print(self.studentController.search(string))
                    print()
                    print("___________________Disciplines__________________")
                    print(self.disciplineController.search(string))

            elif n == 7:
                msg = "Students enrolled to each discipline sorted by name:"
                print(msg.rjust(70 + len(msg)//2, '>').ljust(150 - len("msg")//2, '<'))
                d = self.gradeController.all_disciplines()
                for i in d.keys():
                    print('_' * 20 + self.disciplineController.find(i).name + '_' * 20)
                    for j in d[i]:
                        print(j)

                listt = self.statusController.get_failing_students()
                print('\n')

                msg = "Students failing at a discipline"
                print(msg.rjust(70 + len(msg)//2, '>').ljust(150 - len("msg")//2, '<'))
                for i in listt:
                    student = i[0]
                    fails = i[1:]
                    print(str(student) + "  FAILING AT:")
                    for j in fails:
                        print(j)

                    print()

                print('\n')
                msg = "Students with the best school situation sorted by aggregated average grade"
                print(msg.rjust(70 + len(msg)//2, '>').ljust(150 - len("msg")//2, '<'))
                listt = self.statusController.get_best_students()

                for i in listt:
                    print(str(i[0]) + ' ------- Grade: ' + str(i[1]))

                print('\n')
                listt = self.statusController.get_discipline_statistics()
                msg = "Disciplines sorted by the average of the grades of all students at that discipline"
                print(msg.rjust(70 + len(msg) // 2, '>').ljust(150 - len("msg") // 2, '<'))
                for i in listt:
                    print(str(i[0]) + ' -------- Average: ' + str(i[1]))

            elif n == 8:
                try:
                    self.undoController.undo()
                except Exception:
                    pass

            elif n == 9:
                try:
                    self.undoController.redo()
                except Exception:
                    pass

            elif n == 99:
                self.showmenu()

            else:
                print("Invalid command!")
