from Repository import *
from Student import *
from StudentController import *


class UI:
    def __init__(self):
        self.repo = TextRepository()
        self.studentController = StudentController(self.repo)

    def show_menu(self):
        print("1. Add student")
        print("2. Give bonus")
        print("3. Display all students including a string")
        print("0. Exit")

    def startup(self):
        self.show_menu()
        while True:
            try:
                n = int(input(">>"))
            except ValueError as e:
                print(e)
                continue

            if n == 0:
                break

            elif n == 1:
                _id = int(input("id: "))
                name = input("name: ")
                attendance = int(input("attendance: "))
                grade = int(input("grade: "))

                try:
                    self.studentController.add_student(Student(_id, name, attendance, grade))
                except ValueError as e:
                    print(e)

            elif n == 2:
                p = int(input("p: "))
                b = int(input("b: "))

                self.studentController.give_bonus(p, b)

            elif n == 3:
                string = input("string: ").lower()
                _list = self.repo.get_all()
                new = []

                for s in _list:
                    if string in s.name.lower():
                        new.append(s)

                for s in sorted(new):
                    print(s)

            else:
                print("[ERROR] Invalid Command!")
