def promedionumreales(arreglo):#Define la función "promedionumreales" que calcula el promedio de una lista de números reales.
    if len(arreglo) == 0: #verifica si las lista esta vacia
        return 0  # Manejo de caso vacío para evitar división por cero
    suma = sum(arreglo) #calcula la suma de los valores ingresados 
    promedio = suma / len(arreglo) #divide la suma entre la cantidad de valores ingresados 
    return promedio #devuelve el promedio de los valores ingresados

def numero_real(valor): #Define la función "numero_real" que verifica si un valor puede convertirse en un número real (float).
    try:
        float(valor) #intenta convertir el valor ingresado a un numero real
        return True  # si la conversion es exitosa devuelve true lo cual valida que es un numero real  
    except ValueError: #maneja la excepcion si hay un error en la conversion 
        return False #
def main():
    # Solicitar entrada del usuario
    ingresonumreales = input("Ingrese los números reales separados por comas: ") #da a ntender a quien ingrese los valores los parametros con los que lo debe hacer y almacena la entrada en "ingresonumreales"

    # Convertir la entrada en una lista de números reales
    numeros_str = ingresonumreales.split(",") #divide la cadena de entrada en una lista de cadenas, usando la coma como separador, y almacena el resultado en numeros_str
    numeros = [] #crea una lista vacía "numeros" para almacenar los números reales válidos.

    # Verificar cada número y probar si es inválido
    for num in numeros_str:  #Itera sobre cada elemento "num" en la lista numeros_str.
        num = num.strip() #elimina los espacios en blanco 
        if numero_real(num): #verifica si es un numero real
            numeros.append(float(num))#si se valida que es un numero real lo convierte a float y lo agrega a la lista "num"
        else: #si no es un numero real valido hace que se imprima un mensaje indicandolo 
            print(f"'{num}' no es un número real válido y será omitido.") 

    # Calcular el promedio
    if numeros: #verifica que la lista no este vacia
        promedio = promedionumreales (numeros)#calcula el promedio de los numeros
        print(f"El promedio es: {promedio}")#imprime el promedio
    else: # si no se ingreso ningun numero real hace que se imprima un mensaje en el que se informe esto
        print("No se ingresaron números válidos.")

if __name__== '__main__':
    main()