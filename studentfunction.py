from logging import debug, basicConfig, DEBUG
from datetime import datetime
from math import ceil

basicConfig(filename="logging.log", level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


class Student:
    def __init__(self, first_name: str, surname: str, birthdate: str) -> None:
        self.birthdate = birthdate
        self.first_name = first_name
        self.surname = surname

        self.semester = 1
        self.student_data_list = []

    @classmethod
    def first_name_valid(cls, first_name):
        if first_name.istitle() and 19 >= len(first_name) > 1:
            return True
        else:
            print("\nImię(Imiona) studenta jest/są nieprawidłowe!\n"
                  "Wzór:[Patryk / Patryk-Łukasz]")
            return False

    @classmethod
    def surname_valid(cls, surname):
        if surname.istitle() and 30 >= len(surname) > 1:
            return True
        else:
            print("\nNazwisko(Nazwiska) studenta jest/są nieprawidłowe!\n"
                  "Wzór:[Kowalski/ Kowalski-Malinowski}")
            return False

    @classmethod
    def date_valid(cls, date: str) -> bool:
        try:
            datetime_get = datetime.strptime(date, '%d.%m.%Y')
            actual_date = datetime.now()
            age = actual_date.year - datetime_get.year - \
                  ((actual_date.month, actual_date.day) <
                   (datetime_get.month, datetime_get.day))

            if 18 <= age <= 25:
                return True
            else:
                print("\nStudent musi posiadać 18 lat!")
                return False
        except ValueError:
            print("\nWpisana data jest niepoprawna Wzór:[dd-mm=yyyy]!")
            return False

    @classmethod
    def data_correctness(cls, first_name, surname, birthdate) -> bool:
        first_name_valid = cls.first_name_valid(first_name)
        surname_valid = cls.surname_valid(surname)
        date_valid = cls.date_valid(birthdate)

        if first_name_valid and surname_valid and date_valid:
            return True
        else:
            return False

    def change_a_semester(self, mode: str) -> str:
        if mode.lower() == 'high':
            self.semester += 1
        elif mode.lower() == 'low':
            self.semester -= 1
        else:
            return "Wybierz high(Semestr w górę) lub low(Semestr w dół)"

    def get_year(self) -> int:
        return ceil(self.semester / 2)

    def __str__(self) -> str:
        return f"Imię:{self.first_name}, Nazwisko:{self.surname}, Data Urodzenia:{self.birthdate}"


index = 0
student_dict = {}


def menu() -> bool:

    student_operation = input(
        '''1.Lista studentów
2.Dodaj studenta
3.Usuń studenta
4.Edytuj studenta
5.Wyświetl oceny
6.Dodaj oceny
7.Edytuj oceny
8.Wróć

Wybierz numer operacji spośród podanych: '''
    )
    try:
        if 0 < int(student_operation) <= 8:
            menu_dict = {'1': ("Wyświetlanie listy", display_student_dict),
                         '2': ("Dodawanie studenta", student_add),
                         '3': ("Usuwanie studenta", student_delete),
                         '4': ("Edycja studenta", student_edit),  # TODO: EDYTUJ DANE STUDENTA
                         '5': ("Wyświetlanie ocen", display_student_note),  # TODO: WYŚWIETLANIE OCEN
                         '6': ("Dodawanie ocen", student_note_add),  # TODO: DODAWANIE OCEN
                         '7': ("Edycja ocen", student_note_edit),  # TODO: EDYCJA OCEN
                         '8': ("Powrót", False)}

            menu_result, menu_chosen_func = menu_dict.get(student_operation)

            if not menu_chosen_func:
                print(f"\nWybrałeś '{menu_result}'\n")
                return False
            try:
                print(f"\nWybrałeś '{menu_result}'\n")
                menu_chosen_func()
            except Exception as m_ex:
                print("Wystąpił nieznany błąd")
                debug(m_ex)
        else:
            print("\nWybierz numer operacji z listy!")
    except ValueError:
        print("\nWybierz prawidłową operację!")


# TODO: DEKORATOR INDEX
def student_add() -> None:
    new_student_first_name = input("Podaj imię(imiona): ")
    new_student_surname = input("Podaj nazwisko(nazwiska): ")
    new_student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ")

    if Student.data_correctness(new_student_first_name,
                                new_student_surname,
                                new_student_birthdate):
        global index
        index += 1
        student = Student(new_student_first_name,
                          new_student_surname,
                          new_student_birthdate)

        student_dict[index] = student

        print("\nPomyślnie dodano nowego studenta.\n")
    else:
        print("\nNie udało się stworzyć studenta!\n")


def student_delete() -> None:
    try:
        student_del = int(input("Podaj numer studenta,którego chcesz usunąć: "))
        print()
        if student_del in student_dict.keys():
            student_dict.pop(student_del)
        else:
            print("Student o podanym numerze nie istnieje!\n")

    except ValueError:
        print("Wpisałeś błędną wartość,wpisz numer studenta z listy")


def student_edit() -> None:
    pass


def student_note_add() -> None:
    pass


def student_note_edit() -> None:
    pass


def student_dict_validate() -> bool:
    if len(student_dict) >= 1:
        return True
    else:
        return False


def display_student_dict() -> None:
    if student_dict_validate():
        student_dict_formatted = {k: str(v) for k, v in student_dict.items()}

        if student_dict_formatted:
            print("Oto lista studentów:")
            for k, v in student_dict_formatted.items():
                print(f"{k}.{v}")
            print()
    else:
        print("Na liście nie ma żadnego studenta!\n")
        menu()


def display_student_note() -> None:
    pass
