



def promedionumreales(arreglo):
    if len(arreglo) == 0:
        return 0  # Manejo de caso vacío para evitar división por cero
    suma = sum(arreglo)
    promedio = suma / len(arreglo)
    return promedio

def numero_real(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
def main():
    # Solicitar entrada del usuario
    entrada = input("Ingrese los números reales separados por comas: ")

    # Convertir la entrada en una lista de números reales
    numeros_str = entrada.split(",")
    numeros = []

    # Verificar cada número y notificar si es inválido
    for num in numeros_str:
        num = num.strip()
        if numero_real(num):
            numeros.append(float(num))
        else:
            print(f"'{num}' no es un número real válido y será omitido.")

    # Calcular el promedio
    if numeros:
        promedio = promedionumreales (numeros)
        print(f"El promedio es: {promedio}")
    else:
        print("No se ingresaron números válidos.")

if __name__== '__main__':
    main()