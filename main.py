from function import *


def main() -> None:
    student_index = 0
    while True:
        question = input("Czy chcesz dodać studenta?[Tak/Nie]: ").strip().lower()
        if question == "tak":
            student_index += 1
            student_add(student_index)
            continue
        elif question == "nie":
            break
        else:
            print("Wpisz 'Tak/Nie'")

    student_dict_formatted = {k: str(v) for k, v in student_dict.items()}

    if student_dict_formatted:
        print("Oto lista studentów:")
        for k, v in student_dict_formatted.items():
            print(f"{k}.{v}")


if __name__ == '__main__':
    main()