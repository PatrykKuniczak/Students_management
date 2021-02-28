from studentfunction import general

# TODO: ZRÓB DEKORATOR KTÓRY OTWIERA I ZAMYKA JSONA
def main() -> None:
    while True:
        generalfunc = general()
        if not generalfunc:
            break

if __name__ == '__main__':
    main()