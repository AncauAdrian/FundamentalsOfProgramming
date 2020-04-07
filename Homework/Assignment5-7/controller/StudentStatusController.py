class StudentStatusController:
    def __init__(self, studentRepo, disciplineRepo, gradeRepo):
        self._studentRepo = studentRepo
        self._disciplineRepo = disciplineRepo
        self._gradeRepo = gradeRepo

        self.enrollment = {}

    def get_enrollment(self):
        grades = self._gradeRepo.get_all()
        enrollment = {}

        for i in grades:
            if i.student_id in enrollment.keys():
                if i.discipline_id not in enrollment[i.student_id]:
                    enrollment[i.student_id].append(i.discipline_id)
                else:
                    pass
            else:
                cache = [i.discipline_id]
                enrollment[i.student_id] = cache

        return enrollment

    def get_discipline_average(self, student_id, discipline_id):
        grades = self._gradeRepo.get_all()
        grades_list = []

        for i in grades:
            if i.student_id == student_id and i.discipline_id == discipline_id:
                grades_list.append(i.grade)

        return sum(grades_list) / float(len(grades_list))

    def get_aggregated_average(self, student_id):
        enrollment = self.get_enrollment()
        grades_list = []
        for i in enrollment[student_id]:
            grades_list.append(self.get_discipline_average(student_id, i))

        return sum(grades_list) / float(len(grades_list))

    def get_failing_students(self):
        ret = []
        enrollment = self.get_enrollment()

        for key, value in enrollment.items():
            ok = 0
            cache = [self._studentRepo.find(key)]
            for i in value:
                if self.get_discipline_average(key, i) < 5.0:
                    cache.append(self._disciplineRepo.find(i))
                    ok = 1

            if ok:
                ret.append(cache)

        return ret

    def get_best_students(self):
        ret = []
        enrollment = self.get_enrollment()

        for i in enrollment:
            d = [self._studentRepo.find(i), self.get_aggregated_average(i)]
            ret.append(d)

        return sorted(ret, key=lambda x: x[1], reverse=True)

    def get_valid_disciplines(self):
        d = {}
        grades = self._gradeRepo.get_all()

        for i in grades:
            if i.discipline_id not in d.keys():
                d[i.discipline_id] = [i.grade]
            else:
                d[i.discipline_id].append(i.grade)

        return d

    def get_discipline_statistics(self):
        valids = self.get_valid_disciplines()
        ret = []

        for k, v in valids.items():
            ret.append([self._disciplineRepo.find(k), sum(v) / float(len(v))])

        return sorted(ret, key=lambda x: x[1], reverse=True)
