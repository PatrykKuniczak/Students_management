from datetime import datetime
from math import ceil


class Student:
    def __init__(self, first_name, last_name, birthday):
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name
        self.semester = 1
        self.student_date_list = []

    def go_high(self):
        self.semester += 1

    def go_down(self):
        self.semester -= 1

    def get_year(self):
        return ceil(self.semester / 2)

    def join_a_student(self):
        self.student_date_list.append(f"Imię:{self.first_name}, "
                                      f"Nazwisko:{self.last_name}, Data Urodzenia:{self.birthday}")
        return self.student_date_list

    # def print_a_student(self):
    #     for elem in self.student_date:
    #         print(f"Nr. {self.journal_number}: {elem}")


student_dict = {}


def make_a_new_student(student_journal_index):
    while True:
        try:
            new_student_first_name = input("Podaj imię: ").strip()
            new_student_last_name = input("Podaj nazwisko: ").strip()
            new_student_birthday = input("Podaj datę urodzenia[dd.mm.yyyy]: ")
            datetime.strptime(new_student_birthday, '%d.%m.%Y')
            break
        except ValueError:
            print("Któraś z podanych warości jest nieprawidłowa!")

    student = Student(new_student_first_name, new_student_last_name,
                      new_student_birthday)
    list_element = student.join_a_student()
    student_dict[student_journal_index] = list_element


student_index = 0

while True:
    student_index += 1
    question_about_add = input("Czy chcesz dodać studenta[Tak/Nie]: ").strip().lower()
    if question_about_add == "tak":
        make_a_new_student(student_index)
    elif question_about_add == "nie":
        break

print(f"Oto lista studentów: {student_dict}")