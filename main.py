class Student:

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):

        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Сравнение невозможно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):

        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            print('Сравнение невозможно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


lecturer_1 = Lecturer('Иван', 'Семенов')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Александр', 'Дегтярев')
lecturer_2.courses_attached += ['Java']

reviewer_1 = Reviewer('Денис', 'Давыдов')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Егор', 'Титов')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

student_1 = Student('Александр', 'Зуев')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Роман', 'Павлюченко')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Рамиз', 'Мамедов')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_2, 'Python', 7)
student_1.rate_hw(lecturer_2, 'Python', 5)
student_1.rate_hw(lecturer_2, 'Python', 7)

student_2.rate_hw(lecturer_1, 'Python', 7)
student_2.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 9)

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 9)

reviewer_1.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 7)
reviewer_2.rate_hw(student_3, 'Python', 9)


print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')
print()
print()

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}')
print()
print()

print(f'Перечень экспертов:\n\n{reviewer_1}\n\n{reviewer_2}')
print()
print()

print(f'Результат сравнения студентов (по средним оценкам): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

print(f'Результат сравнения лекторов (по средним оценкам): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} '
      f'{lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()

student_list = [student_1, student_2]

lecturer_list = [lecturer_1, lecturer_2]


