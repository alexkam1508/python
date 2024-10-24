animal = "  animal lEOn  "
print(animal.upper()) #convierte a mayusculas
print(animal.lower()) #covierte a minusculas
print(animal.strip().capitalize())  #elimina espacios en blanco y convierte la primera letra a mayuscula
print(animal.title())  #convierte la primera letra de cada palabra a mayuscula
print(animal.strip())   #elimina espacios en blanco
print(animal.find("a"))  #busca la posicion de la letra "a"
print(animal.replace("an","lo"))   #sustituye "an" por "lo"
print("an" in animal)   #busca si "an" esta en la cadena y devuelve un valor boleano
print("an" not in animal)   #busca si "an" no esta en la cadena y devuelve un valor boleano


