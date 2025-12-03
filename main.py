from data_io import read_points_from_console, read_points_from_csv
from regression import linear_regression, log_regression
from report import save_text_report

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

    print("Puncte încărcate:", list(zip(x, y)))

    # --------------------------
    # aici fac regresiile
    # --------------------------
    lin_res = linear_regression(x, y)
    print("Regresie liniară: m =", lin_res["m"], "b =", lin_res["b"], "R² =", lin_res["r2"])

   
    try:
        log_res = log_regression(x, y)
    except ValueError:
        log_res = None

    choice_report = input("Doriți să salvați un raport? (y/n): ").lower()
    if choice_report == "y":
        path = input("Introduceți numele fișierului (ex: raport.txt): ")
        save_text_report(path, lin_res, log_res)
        print("Raport salvat.")

    

if __name__ == "__main__":
    main()
