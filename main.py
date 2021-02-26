from function import *


def main() -> None:
    student_index = 1
    while True:
        question = input("Czy chcesz dodać studenta?[Tak/Nie]: ").strip().lower()
        if question == "tak":
            student_add(student_index)
            student_index += 1
            continue
        elif question == "nie":
            break
        else:
            print("Wpisz 'Tak/Nie'")

    students_list()

if __name__ == '__main__':
    main()