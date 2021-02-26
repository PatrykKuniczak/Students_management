from datetime import datetime
from math import ceil
import re
# TODO: DODAĆ WALIDACJĘ DO KLASY
class Student:
    def __init__(self, first_name: str, last_name: str, birthdate: str) -> None:
        self.birthdate = birthdate
        self.first_name = first_name
        self.last_name = last_name

        self.semester = 1
        self.student_data_list = []

    def change_a_semester(self, mode: str) -> None:
        if mode.lower() == 'high':
            self.semester += 1
        elif mode.lower() == 'low':
            self.semester -= 1

    def get_year(self) -> int:
        return ceil(self.semester / 2)

    def __str__(self) -> str:
        return f"Imię:{self.first_name}, Nazwisko:{self.last_name}, Data Urodzenia:{self.birthdate}"

student_dict = {}

def date_valid(date: str) -> bool:
    try:
        datetime_get = datetime.strptime(date, '%d.%m.%Y')
        actual_date = datetime.now()
        age = actual_date.year - datetime_get.year - \
              ((actual_date.month, actual_date.day) <
               (datetime_get.month, datetime_get.day))

        if age >= 18 and datetime_get:
            return True
    except ValueError:
        return False

def data_correctness(first_name, last_name, birthdate) -> bool:

    if re.match(r"^[A-Za-z]{2,}|[A-Za-z]\s[A-Za-z]{2,}$", first_name) \
            and re.match(r"^[A-Za-z]{2,}|[A-Za-z]\s[A-Za-z]{2,}$", last_name)\
            and date_valid(birthdate):

        return True

    else:
        if not re.match(r"^[A-Za-z]{2,}|[A-Za-z]\s[A-Za-z]{2,}$", first_name):
            print("Imię studenta jest błędne!")

        if not re.match(r"^[A-Za-z]{2,}|[A-Za-z]\s[A-Za-z]{2,}$", last_name):
            print("Nazwisko studenta jest błędne!")

        if not date_valid(birthdate):
            print("Student musi posiadać 18 lat!")

        return False

def student_add(index: int) -> None:
    new_student_first_name = input("Podaj imię(imiona): ")
    new_student_last_name = input("Podaj nazwisko: ")
    new_student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ")

    if data_correctness(new_student_first_name,
                        new_student_last_name,
                        new_student_birthdate):

        student = Student(new_student_first_name,
                          new_student_last_name,
                          new_student_birthdate)

        student_dict[index] = student

        print("Pomyślnie dodano nowego studenta.")
    else:
        print("Nie udało się stworzyć studenta!")

def students_list():
    student_dict_formatted = {k: str(v) for k, v in student_dict.items()}

    if student_dict_formatted:
        print("Oto lista studentów:")
        for k, v in student_dict_formatted.items():
            print(f"{k}.{v}")

def student_delete() -> None:
    try:
        student_del = int(input("Podaj numer studenta,którego chcesz usunąć: "))
        if student_del in student_dict.keys():
            student_dict.pop(student_del)

    except ValueError:
        print("Wpisałeś błędną wartość,wpisz numer studenta z listy")