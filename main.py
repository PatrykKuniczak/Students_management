from math import ceil


class Student:
    def __init__(self, first_name, last_name, birthday, journal_number=0, age=0):
        self.age = age
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
        self.student_date.append(f"Imię:{self.first_name}, Nazwisko:{self.last_name}, "
                                 f"Wiek:{self.age} lat, Data Urodzenia:{self.birthday}")

        self.student_list.update({self.journal_number: self.student_date})

    def print_a_student(self):
        for elem in self.student_date:
            print(f"{self.journal_number}:", elem)


question = input("Czy chcesz dodać nowego studenta?: ")
if question.lower() == "tak":
    new_student_first_name = input("Podaj imię: ")
    new_student_last_name = input("Podaj nazwisko: ")
    new_student_age = input("Podaj wiek: ")
    new_student_birthday = input("Podaj datę urodzenia: ")
    # TU TERAZ KMINIE JAK ZROBIĆ,ABY ZA KAŻDYM OBIEGIEM PĘTLI TWORZYŁ SIĘ NOWY OBIEKT,CZYLI NOWY STUDENT,ŻEBY BYŁO
    # ŁATWIEJ MI SIĘ PÓŹNIEJ DO TEGO ODNOSIĆ,BĘDE NA CAŁYM OBIEKCIE OPEROWAŁ