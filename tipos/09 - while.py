numero = 1 
while numero < 100:
    print(numero)
    numero *=  2  # incremento de 2 en 2

comando = ""

while comando.lower() != "salir":
    comando = input("Ingrese un comando: ")
    print(comando)


while  True:
    comando = input("Ingrese un comando: ")
    print(comando)
    if(comando.lower() == "salir"):
        break
