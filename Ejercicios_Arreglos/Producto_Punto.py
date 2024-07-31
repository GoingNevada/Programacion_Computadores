
# Problema: Desarrollar un algoritmo que calcule el producto punto de dos arreglos
# de numeros enteros (reales) de igual tamano. Sean v = [v0, v1, . . . , vn−1] y 
# w = [w0,w1, . . . ,wn−1] dos arreglos, el producto de v y w (notado v · w) es 
# el numero: v0 ∗ w0 + v1 ∗ w1 + · · · + vn−1 ∗ wn−1.

def is_int(num):  # FUNCION PARA LA COMPROBACION DE CONVERSION DE UN NUMERO A ENTERO
    try:        # UTILIZAMOS UN TRY PARA INTENTAR REALIZAR LA CONVERSION
        int(num)  # EN CASO DE EXITO, LA FUNCION RETORNARA UN VALOR 'TRUE'
        return True
    except ValueError:     # EN CASO CONTRARIO, RETORNARA UN VALOR 'FALSE'
        return False
    
def is_intarray(list): # FUNCION PARA LA COMPROBACION DE QUE UN ELEMENTO DENTRO DE LA LISTA SEA ENTERO
    for i in list:  # UTILIZAMOS UN CICLO FOR PARA ITERAR EN CADA ELEMENTO
        if is_int(i) != True:   # UTILIZAMOS LA FUNCION IS_INT PARA COMPROBAR QUE SEA CONVERTIBLE A ENTERO
            return False    # SI ENCUENTRA UN CASO QUE NO SEA CONVERTIBLE, RETORNA FALSE
        else:
            pass
    return True # RETORNA TRUE SI NO ENCUENTRA ALGUN ELEMENTO DISTINTO A ENTERO


def main():
    res = 0     # INICIALIZAMOS LA VARIABLE DE RESULTADO EN 0
    # INGRESO DE PRIMERA SECUENCIA DE NUMEROS
    v = input("Ingrese la primera serie de numeros enteros, separados con 1 espacio: ").split()
    if not(v):  # SI NO EXISTE EL ARREGLO
        print("No se ingreso ninguna serie de numeros")
        return None
    elif is_intarray(v) == False:   # SI EXISTE ALGUN ELEMENTO NO ENTERO
        print("La serie contiene elementos que no son numeros enteros")
        return None
    else:
        v = [int(i) for i in v ]

    # INGRESO DE SEGUNDA SECUENCIA DE NUMEROS
    w = input("Ingrese la segunda serie de numeros enteros, del mismo tamaño a la primera: ").split()
    if not(w):
        print("No se ingreso ninguna serie de numeros")
        return None
    elif is_intarray(w) == False:
        print("La serie contiene elementos que no son numeros enteros")
        return None
    else:
        w = [int(i) for i in w ]

    if len(v) != len(w):    # PREGUNTA SI EL TAMAÑO DE LOS ARREGLOS ES IGUAL
        print("El tamaño de los arreglos ingresados no coincide")
    else:
        for i in range(0, len(v)):
            res += v[i]*w[i]    # ACUMULAMOS LA SUMA DE LA MULTIPLICACION ENTRE ELEMENTOS DE LOS ARREGLOS
        print("El resultado del producto punto entre v y w, es: ",res)

if __name__ == '__main__':
    main()