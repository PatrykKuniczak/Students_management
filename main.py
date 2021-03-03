from logging import debug, basicConfig, DEBUG
from studentfunction import menu

basicConfig(filename="logging.log", level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


# TODO: ZRÓB DEKORATOR KTÓRY OTWIERA I ZAMYKA JSON
def main() -> None:
    while True:
        general_question = input("1.Klasy\n"
                                 "2.Studenci\n"  # TODO: STWÓRZ KLASĘ 'CLASS'
                                 "3.Zakończ program\n"
                                 "Wybierz numer operacji spośród podanych: ")

        general_dict = {"1": ("Klasa", None), "2": ("Student", menu)}

        try:
            if 0 < int(general_question) <= 2:
                general_result, general_chosen_func = general_dict.get(general_question)
                print(f"Wybrałeś '{general_result}'")
                try:
                    general_chosen_func()
                except Exception as g_ex:
                    print("Wystąpił nieznany błąd")
                    debug(g_ex)

            elif int(general_question) == 3:
                print("Do widzenia!")
                break
            else:
                print("Wybierz numer operacji z listy!")
        except ValueError:
            print("Wpisz poprawny numer operacji!")


if __name__ == '__main__':
    main()
