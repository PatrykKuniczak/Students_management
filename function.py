from datetime import datetime
from math import ceil

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

            if age >= 18 and datetime_get:
                return True
        except ValueError:
            return False

    @classmethod
    def data_correctness(cls, first_name, last_name, birthdate) -> bool:

        if first_name.istitle() and last_name.istitle() and cls.date_valid(birthdate):
            return True

        else:
            if not first_name.istitle():
                print("Imię studenta jest błędne!\n"
                      "Wzór:[Patryk / Patryk-Łukasz]")

            if not last_name.istitle():
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

    def get_year(self) -> int:
        return ceil(self.semester / 2)

    def __str__(self) -> str:
        return f"Imię:{self.first_name}, Nazwisko:{self.last_name}, Data Urodzenia:{self.birthdate}"

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
    student_operation = input("1.Lista studentów\n"
                              "2.Dodaj studenta\n"
                              "3.Usuń studenta\n"
                              "4.Edytuj studenta\n"
                              "5.Wyświetl oceny\n"
                              "6.Dodaj oceny\n"
                              "7.Edytuj oceny\n"
                              "8.Wróć\n"
                              "Wybierz numer operacji spośród podanych: ")

    if student_operation.lower() == "1":
        if len(student_dict) >= 1:
            display_student_dict()

        else:
            print("Na liście nie ma żadnego studenta")
            menu()

    elif student_operation.lower() == "2":
        student_add()

    elif student_operation.lower() == "3":
        student_delete()

    elif student_operation.lower() == "4":
        student_edit() # TODO: EDYTUJ DANE STUDENTA

    elif student_operation.lower() == "5":
        display_student_note() # TODO: WYŚWIETLANIE OCEN

    elif student_operation.lower() == "6":
        student_note_add() # TODO: DODAWANIE OCEN

    elif student_operation.lower() == "7":
        student_note_edit() # TODO: EDYCJA OCEN

    elif student_operation.lower() == "8":
        general()

    else:
        print("Wybierz operację z listy!")
        menu()

student_dict = {}

index = 0
def student_add() -> int:
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
        return index
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

def display_student_dict() -> None:
    student_dict_formatted = {k: str(v) for k, v in student_dict.items()}

    if student_dict_formatted:
        print("Oto lista studentów:")
        for k, v in student_dict_formatted.items():
            print(f"{k}.{v}")

def display_student_note():
    pass