import re, logging
from datetime import datetime
from math import ceil

logging.basicConfig(filename="logging.log", level=logging.DEBUG, format='%(asctime)s:'
                                                                        '%(levelname)s:%(message)s')


class Student:
    def __init__(self, first_name: str, surname: str, birthdate: str) -> None:
        self.birthdate = birthdate
        self.first_name = first_name
        self.surname = surname

        self.semester = 1
        self.student_data_list = []

    @classmethod
    def date_valid(cls, date: str) -> bool:
        try:
            datetime_get = datetime.strptime(date, '%d.%m.%Y')
            actual_date = datetime.now()
            age = actual_date.year - datetime_get.year - \
                  ((actual_date.month, actual_date.day) <
                   (datetime_get.month, datetime_get.day))

            if 18 <= age <= 25 and datetime_get:
                return True
        except ValueError:
            return False

    # TODO: DO NAPRAWIENIA TE REGEX
    @classmethod
    def data_correctness(cls, first_name, surname, birthdate) -> bool:

        if re.match(r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", first_name) and re.match(
                r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", surname) and cls.date_valid(birthdate):
            return True

        else:
            if not re.match(r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", first_name):
                print("Imię studenta jest błędne!\n"
                      "Wzór:[Patryk / Patryk-Łukasz]")

            if not re.match(r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", surname):
                print("Nazwisko studenta jest błędne!\n"
                      "Wzór[Kowalski/ Kowalski-Malinowski}")

            if not cls.date_valid(birthdate):
                print("Student musi posiadać 18 lat!")

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


def general() -> None:
    general_question = input("1.Klasy\n"
                             "2.Studenci\n"
                             "3.Zakończ program\n"
                             "Wybierz numer operacji spośród podanych: ")

    general_dict = {"1": ("Klasa", None), "2": ("Student", menu), "3": ("Wyjście", False),  # TODO:NAPRAW WYCHODZENIE
                    'default': ("Wybierz operację z listy!", False)}

    # TODO: STWÓRZ KLASĘ 'CLASS'

    general_result, general_chosen_func = general_dict.get(general_question, general_dict["default"])

    print(f"Wybrałeś {general_result}")

    try:
        general_chosen_func()

    except Exception as g_ex:
        print("Wystąpił nieznany błąd")
        logging.debug(g_ex)


def menu() -> None:
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

    menu_dict = {'1': ("Wyświetlanie listy", display_student_dict),
                 '2': ("Dodawanie studenta", student_add),
                 '3': ("Usuwanie studenta", student_delete),
                 '4': ("Edycja studenta", student_edit),  # TODO: EDYTUJ DANE STUDENTA
                 '5': ("Wyświetlanie ocen", display_student_note),  # TODO: WYŚWIETLANIE OCEN
                 '6': ("Dodawanie ocen", student_note_add),  # TODO: DODAWANIE OCEN
                 '7': ("Edycja ocen", student_note_edit),  # TODO: EDYCJA OCEN
                 '8': ("Powrót", general),
                 'default': ("Wybierz operację z listy!", False)}

    menu_result, menu_chosen_func = menu_dict.get(student_operation, menu_dict["default"])

    if not menu_chosen_func:
        print(menu_result)
        menu()

    print(f"Wybrałeś {menu_result}")

    try:
        menu_chosen_func()
    except Exception as m_ex:
        print("Wystąpił nieznany błąd")
        logging.debug(m_ex)


# TODO: DEKORATOR INDEX
def student_add() -> None:
    new_student_first_name = input("Podaj imię(imiona): ")
    new_student_surname = input("Podaj nazwisko: ")
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

        print("Pomyślnie dodano nowego studenta.")
    else:
        print("Nie udało się stworzyć studenta!")


def student_delete() -> None:
    try:
        student_del = int(input("Podaj numer studenta,którego chcesz usunąć: "))
        if student_del in student_dict.keys():
            student_dict.pop(student_del)

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
    else:
        print("Na liście nie ma żadnego studenta!")
        menu()


def display_student_note() -> None:
    pass
