import re, logging
from datetime import datetime
from math import ceil

logging.basicConfig(filename="logging.log", level=logging.DEBUG,format='%(asctime)s:'
                               '%(levelname)s:%(message)s')

class Student:
    def __init__(self, first_name: str, last_name: str, birthdate: str) -> None:
        self.birthdate = birthdate
        self.first_name = first_name
        self.last_name = last_name

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

    @classmethod
    def data_correctness(cls, first_name, last_name, birthdate) -> bool:

        if re.match(r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", first_name) and re.match(r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", last_name) and cls.date_valid(birthdate):
            return True

        else:
            if not re.match(r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", first_name):
                print("Imię studenta jest błędne!\n"
                      "Wzór:[Patryk / Patryk-Łukasz]")

            if not re.match(r"^[A-Z][a-z]{1,19}|[A-Z]\s[a-z]{1,19}$", last_name):
                print("Nazwisko studenta jest błędne!\n"
                      "Wzór[Kowalski/ Kowalski-Malinowski}")

            if not cls.date_valid(birthdate):
                print("Student musi posiadać 18 lat!")

            return False

    def change_a_semester(self, mode: str) -> None:
        if mode.lower() == 'high':
            self.semester += 1
        elif mode.lower() == 'low':
            self.semester -= 1
        else:
            print("Wy")

    def get_year(self) -> int:
        return ceil(self.semester / 2)

    def __str__(self) -> str:
        return f"Imię:{self.first_name}, Nazwisko:{self.last_name}, Data Urodzenia:{self.birthdate}"

index = 0
student_dict = {}

def general() -> bool:
    general_question = input("1.Klasy\n"
                             "2.Studenci\n"
                             "3.Zakończ program\n"
                             "Wybierz numer operacji spośród podanych: ")

    if general_question.lower() == "1":
        pass # TODO: STWÓRZ KLASĘ 'CLASS'

    elif general_question.lower() == "2":
        menu()

    elif general_question.lower() == "3":
        return False

    else:
        print("Wybierz operację z listy!")
        general()

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
                 '4': ("Edycja studenta",student_edit), # TODO: EDYTUJ DANE STUDENTA
                 '5': ("Wyświetlanie ocen", display_student_note), # TODO: WYŚWIETLANIE OCEN
                 '6': ("Dodawanie ocen", student_note_add), # TODO: DODAWANIE OCEN
                 '7': ("Edycja ocen", student_note_edit), # TODO: EDYCJA OCEN
                 '8': ("Powrót",general),
                 'default': ("Wybierz operację z listy!", False)}

    result, chosen_func = menu_dict.get(student_operation, menu_dict["default"])
    if not chosen_func:
        print(result)
        return

    print(f"Wybrałeś {result}")

    try:
        chosen_func()
    except Exception as ex:
        print("Wystąpił nieznany błąd")
        logging.debug(ex)

# TODO: DEKORATOR INDEX
def student_add() -> None:
    new_student_first_name = input("Podaj imię(imiona): ")
    new_student_last_name = input("Podaj nazwisko: ")
    new_student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ")

    if Student.data_correctness(new_student_first_name,
                        new_student_last_name,
                        new_student_birthdate):
        global index
        index += 1
        student = Student(new_student_first_name,
                          new_student_last_name,
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

def display_student_note() -> None:
    pass
