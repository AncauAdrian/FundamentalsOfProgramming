from random import randint

def randomise():
    first_names = ["Adrian", "John", "Steven", "Clay", "Kevin", "Robert", "George", "Matthew", "Joshua", "William",
                   "Kevin", "Mary", "Jane", "Alexa", "Bridget", "Jessie", "Jack"]

    last_names = ["Smith", "Lee", "White", "Black", "Johnson", "Brown", "Williams", "Jones", "Miller", "Davis",
                  "Wilson", "Anderson", "Jackson", "Scott", "Green", "Baker", "Adams"]

    for _id in range(1, 9):
        print(str(_id) + ", " + first_names[randint(0, len(first_names) - 1)] + " " +
                    last_names[randint(0, len(last_names) - 1)])


    for i in range(1, 101):
        print(str(randint(1, 8)) + ", " + str(randint(1, 8)) + ", " + str(randint(1, 10)))




randomise()