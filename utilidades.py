EURO_BITCOIN_RATE = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

def euros_a_bitcoins(euros: int | float):
  '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44471.78'''
  bitcoins:int|float = round(euros/44471.78,2)
  return bitcoins

def bitcoins_a_euros(bitcoins: int | float) -> int | float:
  '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44471.78 €'''
  euros = bitcoins*44471.78
  return euros

def contar_vocales(texto: str):
  '''Devuelve el número de vocales que tiene el texto dado.'''
  contador:int = 0
  vocales:list = ["a","e","i","o","u"]
  texto = texto.lower() #tomar en cuenta las mayúsculas
  for letra in texto: #para cada letra del texto dado revisar si está en la lista vocales
    if letra in vocales:
      contador +=1
  return contador

def es_palindromo(texto: str):
  '''Detecta si un texto es palíndromo o no'''
  texto:str = texto.replace(" ", "") #eliminamos espacios en el string para comparar solo los caracteres válidos
  if texto == texto[::-1]: #slicing (en reversa)
    return True
  else: 
    return False
def max_temperaturas(temperaturas: list[float], umbral: int) -> list[float]:
  '''Detecta qué mediciones de temperatura han superado el umbral dado'''
  temperatura_mayor:list = []
  for temperatura in temperaturas:
    if temperatura > umbral :
      temperatura_mayor.append(temperatura)
  return temperatura_mayor

productos: list[str] = []
def insertar(producto: str) -> None:
  '''Añade un producto a la lista'''
  productos.append(producto)
def borrar(numero: int) -> None:
  '''Borra el producto en el índice dado de lista de productos.'''
  del productos[numero]
  
def mostrar_productos() -> None:
  '''Muestra la lista de productos con sus índices.'''
  if len(productos) == 0:
    print("No hay productos.")
  else:
    for posicion, producto in enumerate(productos):
      print(f"{posicion}: {producto}")
      
def cantidad(productos:list[str]) -> int:
  '''Devuelve el número de productos.'''
  cantidad:int= len(productos)
  return cantidad
def cifrar(texto: str, desplazamiento: int) -> str:
  cifras = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z Á É Í Ó Ú"
  cifra_lista:list[str] = cifras.split()
  texto_cifrado:str = ""
  for letra in texto.upper(): #mayúsculas para saber que pertenece a cifras
    if letra in cifra_lista:
      #obtenemos la posicion de letra
      posicion_actual:int = cifra_lista.index(letra)
      #calculamos la nueva posicion de la letra original
      desplazamiento_total:int = (posicion_actual + desplazamiento) % len(cifra_lista) # con % calculamos el residuo y se "reinicia" la lista sumando dicho resto
      texto_cifrado +=cifra_lista[desplazamiento_total]
    else:
      texto_cifrado += letra
  return texto_cifrado
def descifrar(cifrado:str, desplazamiento:int)->str:
  cifras = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z Á É Í Ó Ú"
  cifra_lista:list[str] = cifras.split()
  texto_descifrado:str = ""
  for letra in cifrado.upper():
    if letra in cifra_lista:
      posicion_actual:int = cifra_lista.index(letra)
      desplazamiento_total:int = (posicion_actual - desplazamiento) %len(cifra_lista)
      texto_descifrado += cifra_lista[desplazamiento_total]
    else:
      texto_descifrado += letra
  return texto_descifrado
      
def menu() -> None:
  while True: 
    ordenes = input("¿Qué quieres que haga?: ")
    orden:list = ordenes.split()
    if orden[0] == "convertir":
      valor = int(orden[3])
      if orden[1] == "euros":
        print(euros_a_bitcoins(valor))
      else:
        print(bitcoins_a_euros(valor))
    elif "contar" == orden[0]:
      del orden[0]
      para_contar = str(orden)
      print(contar_vocales(para_contar))
    elif "temperaturas" == orden[0]:
      del orden[0]
      umbral:int = int(orden.pop(-1))
      ordenes_flotantes = list(map(float, orden)) #convertimos cada cadena en la lista "orden" a un float y obtenemos una nueva lista con esos números flotantes
      temperaturas_mayores = max_temperaturas(ordenes_flotantes, umbral)
      if temperaturas_mayores: #comprueba si supera el umbral
        print(temperaturas_mayores)
      else:
        print("No hay temperaturas que superen el umbral.")
    elif "productos"==orden[0]:
      if len(orden) == 1:
        mostrar_productos()  # Mostrar la lista si no se da más información
      elif "nuevo" == orden[1]:
        producto = " ".join(orden[2:])  # Unir el resto de la orden como nombre del producto
        if producto:
          insertar(producto)  # Insertar el producto
          mostrar_productos()  # Mostrar la lista de productos después de añadir
      elif "borrar" == orden[1]:
        indice = int(orden[2])
        borrar(indice)  # Borrar el producto
        # Mostrar la lista de productos después de borrar
      else:
        mostrar_productos()
    elif "cifrar" == orden[0]:
      desplazamiento = int(orden[1])
      texto = " ".join(orden[2:])
      print(cifrar(texto, desplazamiento))
    elif "descifrar" == orden[0]:
      desplazamiento = int(orden[1])
      texto = " ".join(orden[2:])
      print(descifrar(texto,desplazamiento))
    elif "salir" == orden[0]:
      print("Cerrando programa... \n ADIOS D':")
      break
    else:            
      print("comando no reconocido")
      
if __name__ == "__main__":
  menu()
  