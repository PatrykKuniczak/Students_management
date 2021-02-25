from datetime import datetime
from math import ceil


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
    return (isinstance(first_name, str)
            and isinstance(last_name, str)
            and date_valid(birthdate))


def student_add(index: int) -> None:
    new_student_first_name = input("Podaj imię: ").strip()
    new_student_last_name = input("Podaj nazwisko: ").strip()
    new_student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ")

    if data_correctness(new_student_first_name,
                        new_student_last_name,
                        new_student_birthdate):

        student = Student(new_student_first_name,
                          new_student_last_name,
                          new_student_birthdate)

        student_dict.update({index: student})

        print("Pomyślnie dodano nowego studenta.")
    else:
        if not new_student_first_name:
            print("Imię studenta jest błędne!")

        if not new_student_last_name:
            print("Nazwisko studenta jest błędne!")

        if not new_student_birthdate:
            print("Student musi posiadać 18 lat!")

        print("Nie udało się stworzyć studenta!")