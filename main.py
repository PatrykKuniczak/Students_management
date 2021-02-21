from datetime import datetime
from math import ceil


class Student:
    def __init__(self, first_name, last_name, birthday, journal_number=0):
        self.birthday = birthday
        self.journal_number = journal_number
        self.first_name = first_name
        self.last_name = last_name
        self.semester = 1
        self.student_list = {}
        self.student_date = []

    def go_high(self):
        self.semester += 1

    def go_down(self):
        self.semester -= 1

    def get_year(self):
        return ceil(self.semester / 2)

    def join_a_student(self):
        self.student_date.append(f"Imię:{self.first_name}, Nazwisko:{self.last_name}, Data Urodzenia:{self.birthday}")

        self.student_list.update({self.journal_number: self.student_date})

        return self.student_list

    # def print_a_student(self):
    #     for elem in self.student_date:
    #         print(f"Nr. {self.journal_number}: {elem}")


student_list = {}


def make_a_new_student():
    while True:
        try:
            new_student_first_name = input("Podaj imię: ").strip()
            new_student_last_name = input("Podaj nazwisko: ").strip()
            new_student_birthday = input("Podaj datę urodzenia[dd.mm.yyyy]: ")
            datetime.strptime(new_student_birthday, '%d.%m.%Y')
            new_student_journal_number = int(input("Podaj numer do dziennika: "))
            break
        except ValueError:
            print("Któraś z podanych warości jest nieprawidłowa!")

    student = Student(new_student_first_name, new_student_last_name,
                      new_student_birthday, new_student_journal_number)
    list_element = student.join_a_student()
    student_list.update(list_element)


while True:
    question_about_add = input("Czy chcesz dodać studenta: ").strip().lower()
    if question_about_add == "tak":
        make_a_new_student()
    elif question_about_add == "nie":
        break

print(f"Oto lista studentów: {student_list}")
