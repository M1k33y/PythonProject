import math

def linear_regression(x, y):
    n = len(x)
    if n < 2:
        raise ValueError("Sunt necesare cel puțin 2 puncte pentru regresie liniară.")

    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi*xi for xi in x)
    sum_xy = sum(xi*yi for xi, yi in zip(x, y))

    denom = n * sum_x2 - sum_x ** 2
    if denom == 0:
        raise ValueError("Toate valorile x sunt identice. Nu se poate face regresie liniară.")

    m = (n * sum_xy - sum_x * sum_y) / denom
    b = (sum_y - m * sum_x) / n

    y_pred = [m * xi + b for xi in x]
    residuals = [yi - ypi for yi, ypi in zip(y, y_pred)]

    mean_y = sum_y / n
    ss_tot = sum((yi - mean_y) ** 2 for yi in y)
    ss_res = sum(r ** 2 for r in residuals)
    r2 = 1 - ss_res / ss_tot if ss_tot != 0 else 0.0

    if n > 2:
        se = math.sqrt(ss_res / (n - 2))
    else:
        se = float('nan')

    return {
        "m": m,
        "b": b,
        "y_pred": y_pred,
        "residuals": residuals,
        "r2": r2,
        "standard_error": se,
    }


def log_regression(x, y):
    transformed_X = []
    valid_y = []
    for xi, yi in zip(x, y):
        if xi <= 0:
            # poți alege să ignori sau să ridici eroare
            # aici le vom ignora dar avertizăm
            print(f"Atenție: x={xi} <= 0 ignorat pentru regresia logaritmică.")
            continue
        transformed_X.append(math.log(xi))
        valid_y.append(yi)

    if len(transformed_X) < 2:
        raise ValueError("Insuficiente puncte valide pentru regresia logaritmică (x > 0).")

    result_lin = linear_regression(transformed_X, valid_y)
    # coeficienții se numesc acum a și b
    return {
        "a": result_lin["m"],
        "b": result_lin["b"],
        "y_pred": result_lin["y_pred"],
        "residuals": result_lin["residuals"],
        "r2": result_lin["r2"],
        "standard_error": result_lin["standard_error"],
    }
