from operations import *


def show_menu():
    print("1: Add an animal")
    print("2: Modify Type")
    print("3: Change all types")
    print("4: Print animals of type sorted by name")
    print("5: Print all animals")
    print("0: Exit")


def print_animals(animal_list):
    for i in animal_list:
        print("Code: " + get_code(i) + "  Name: " + get_name(i) + "  Type: " + get_type(i) + "  Species: " + get_species(i))


def print_animals_of_type(animal_list, _type):
    sorted_list = sort_list(animal_list)
    for i in sorted_list:
        if get_type(i) == _type:
            print("Code: " + get_code(i) + "  Name: " + get_name(i) + "  Type: " + get_type(i) + "  Species: " + get_species(i))


def init_animal_list():
    _list = []
    add_animal(_list, 'Z01', 'Alex', 'herbivore', 'zebra')
    add_animal(_list, 'L01', 'Kevin', 'carnivore', 'lion')
    add_animal(_list, 'Z02', 'Diana', 'herbivore', 'zebra')
    add_animal(_list, 'L02', 'Lorena', 'carnivore', 'lion')
    add_animal(_list, 'M01', 'Abcd', 'omnivore', 'monkey')
    add_animal(_list, 'M02', 'Wwww', 'omnivore', 'monkey')
    add_animal(_list, 'M03', 'Sortme', 'omnivore', 'monkey')
    add_animal(_list, 'M04', 'Rightnow', 'omnivore', 'monkey')

    return _list


def main():
    animal_list = init_animal_list()
    show_menu()

    while True:
        n = int(input(">> "))

        if n == 1:
            code = input("Enter the code: ")
            name = input("Enter the name: ")
            _type = input("Enter the type: ")
            species = input("Enter the specie: ")
            try:
                add_animal(animal_list, code, name, _type, species)
            except ValueError as e:
                print(e)

        elif n == 2:
            code = input("Enter the code: ")
            _type = input("Enter the type: ")
            try:
                modify_type(animal_list, code, _type)
            except ValueError as e:
                print(e)

        elif n == 3:
            species = input("Enter the specie: ")
            _type = input("Enter the type: ")
            try:
                modify_all_types(animal_list, species, _type)
            except ValueError as e:
                print(e)

        elif n == 4:
            _type = input("Enter the type: ")
            print_animals_of_type(animal_list, _type)

        elif n == 5:
            print_animals(animal_list)

        elif n == 0:
            break


main()