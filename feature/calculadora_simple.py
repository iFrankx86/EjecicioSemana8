def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b


def main():
    print("Calculadora simple")
    print("Operaciones: +  -  *  /")
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            op = input("Ingrese la operación: ").strip()
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue

        if op == "+":
            resultado = sumar(a, b)
        elif op == "-":
            resultado = restar(a, b)
        elif op == "*":
            resultado = multiplicar(a, b)
        elif op == "/":
            resultado = dividir(a, b)
        else:
            print("Operación no válida.")
            continue

        print(f"Resultado: {resultado}")

        salir = input("¿Desea continuar? (s/n): ").strip().lower()
        if salir != "s":
            break


if __name__ == "__main__":
    main()