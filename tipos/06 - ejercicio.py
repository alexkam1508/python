n1 = input("Ingresa un numero: ")
n2 = input("Ingresa un numero: ")

n1 = int(n1) #Convertir a entero
n2 = int(n2)

suma =  n1 + n2
resta = n1 - n2
div =  n1 / n2
multi =  n1 * n2

mensaje = f"""
El resultado para los numeros  {n1} y {n2} es:
para la suma:  {suma},
para la resta:  {resta},
para la divicion:  {div},
para la multiplicacion:  {multi},
"""

print(mensaje)


