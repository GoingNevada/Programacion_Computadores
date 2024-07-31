
# Desarrollar un algoritmo que calcule el producto 
# directo de dos arreglos de números reales de igual tamaño.
def main():
   # Se crea una función para calcular el producto
   def pd(conjunto1, conjunto2):
       # Se verifica que los conjuntos tengan el mismo tamaño
       if len(conjunto1) != len(conjunto2):
           raise ValueError("Los conjuntos deben tener el mismo tamaño")
    
       # Se asegura de que el resultado tenga la misma cantidad de números que los dos
       #conjuntos iniciales 
       resultado = [0] * len(conjunto1)
    
       # Se calcula el producto directo
       for i in range(len(conjunto1)):
           resultado[i] = conjunto1[i] * conjunto2[i]
    
       return resultado
   # Se establecen dos conjuntos de números reales aleatorios de igual tamaño
   conjunto1 = [6.0, 2.0, 7.0, 999.0]
   conjunto2 = [0.0, 1.0, 5.0, 4.0]
   # Se llama a la función pd para calcular el producto directo
   r = pd(conjunto1, conjunto2)
   print("El producto directo es:", r)

if __name__ == "__main__":
  main()