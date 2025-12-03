from data_io import read_points_from_console, read_points_from_csv

def main():
    print("Alege sursa de date:")
    print("1. Introducere de la tastatură")
    print("2. Import din fișier CSV")
    choice = input("Opțiune (1/2): ")

    if choice == "1":
        x, y = read_points_from_console()
    elif choice == "2":
        path = input("Introdu calea către fișierul CSV: ")
        x, y = read_points_from_csv(path)
    else:
        print("Opțiune invalidă.")
        return

    # aici vei apela ulterior funcțiile de regresie
    print("Puncte încărcate:", list(zip(x, y)))

if __name__ == "__main__":
    main()