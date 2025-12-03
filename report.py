def format_linear_equation(m, b):
    return f"y = {m:.3f} * x + {b:.3f}"

def format_log_equation(a, b):
    return f"y = {a:.3f} * ln(x) + {b:.3f}"

def save_text_report(path, lin_res, log_res=None):
    lines = []
    lines.append("=== Raport regresie ===\n")

    # Regresie liniară
    lines.append("Regresie liniară:")
    lines.append(f"  Ecuație: {format_linear_equation(lin_res['m'], lin_res['b'])}")
    lines.append(f"  R² = {lin_res['r2']:.3f}")
    lines.append(f"  Eroare standard = {lin_res['standard_error']:.3f}")
    lines.append("")

    # Regresie logaritmică (opțional)
    if log_res is not None:
        lines.append("Regresie logaritmică:")
        lines.append(f"  Ecuație: {format_log_equation(log_res['a'], log_res['b'])}")
        lines.append(f"  R² = {log_res['r2']:.3f}")
        lines.append(f"  Eroare standard = {log_res['standard_error']:.3f}")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
