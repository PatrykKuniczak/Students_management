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


janko = Student("Janek", "Obibok", "18.12.2002", 1, 18)
franko = Student("Franek", "Giżioletti", "15.02.2000", 2, 20)
basia = Student("Basia", "Kowalska", "12.04.2001", 3, 19)

janko.join_a_student()
janko.print_a_student()
franko.join_a_student()
franko.print_a_student()
basia.join_a_student()
basia.print_a_student()
