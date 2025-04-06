def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"Error. {mensaje}: "))
    return n

def leer_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"Error. {mensaje}: "))
    return n