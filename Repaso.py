"""
1. Una frutería ofrece las manzanas con descuento según la siguiente tabla:
NUM. DE KILOS COMPRADOS % DESCUENTO
0 - 2 0%
2.01 - 5 10%
5.01 - 10 15%
10.01 en adelante 20% 

"""
# Solicita al usuario la cantidad de kilos de manzanas que desea comprar
kilos = float(input("Ingrese la cantidad de kilos de manzanas que desea comprar: "))

# Inicializa el descuento en 0%
descuento = 0

# Aplica el descuento según la cantidad de kilos comprados
if kilos <= 2:
    descuento = 0
elif kilos <= 5:
    descuento = 10
elif kilos <= 10:
    descuento = 15
else:
    descuento = 20

# Calcula el precio total teniendo en cuenta el descuento
precio_por_kilo = 1  # Precio por kilo (puedes ajustarlo según tus necesidades)
precio_total = kilos * precio_por_kilo * (1 - descuento / 100)

# Muestra el resultado
print(f"Usted compró {kilos} kilos de manzanas.")
print(f"Su descuento es del {descuento}%.")
print(f"El precio total a pagar es: ${precio_total:.2f}")


""" 
2. Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un medico determina
si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de
su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se
determina su resultado como positivo y en caso contrario como negativo. La tabla en la que el medico se basa
para obtener el resultado es la siguiente:
EDAD NIVEL HEMOGLOBINA
0 - 1 mes 13 - 26 g%
> 1 y < = 6 meses 10 - 18 g%
> 6 y < = 12 meses 11 - 15 g%
> 1 y < = 5 años 11.5 - 15 g%
> 5 y < = 10 años 12.6 - 15.5 g%
> 10 y < = 15 años 13 - 15.5 g%
mujeres > 15 años 12 - 16 g%
hombres > 15 años 14 - 18 g% 
"""


# Solicita al usuario su edad, género y nivel de hemoglobina
edad = input("Ingrese su edad en años: ")
genero = input("Ingrese su género (hombre/mujer): ").lower()
nivel_hemoglobina = float(input("Ingrese su nivel de hemoglobina en g%: "))

# Inicializa la variable de resultado como "Negativo" (sin anemia)
resultado = "Negativo"

# Determina si la persona tiene anemia según la tabla
if edad == "0 - 1 mes" and (nivel_hemoglobina < 13 or nivel_hemoglobina > 26):
    resultado = "Positivo"
elif edad == "> 1 y <= 6 meses" and (nivel_hemoglobina < 10 or nivel_hemoglobina > 18):
    resultado = "Positivo"
elif edad == "> 6 y <= 12 meses" and (nivel_hemoglobina < 11 or nivel_hemoglobina > 15):
    resultado = "Positivo"
elif edad == "> 1 y <= 5 años" and (nivel_hemoglobina < 11.5 or nivel_hemoglobina > 15):
    resultado = "Positivo"
elif edad == "> 5 y <= 10 años" and (nivel_hemoglobina < 12.6 or nivel_hemoglobina > 15.5):
    resultado = "Positivo"
elif edad == "> 10 y <= 15 años" and (nivel_hemoglobina < 13 or nivel_hemoglobina > 15.5):
    resultado = "Positivo"
elif edad == "> 15 años":
    if genero == "mujer" and (nivel_hemoglobina < 12 or nivel_hemoglobina > 16):
        resultado = "Positivo"
    elif genero == "hombre" and (nivel_hemoglobina < 14 or nivel_hemoglobina > 18):
        resultado = "Positivo"

# Muestra el resultado
print(f"Resultado del análisis: {resultado}")


"""
. Una institución educativa estableció un programa para estimular a los alumnos con buen
rendimiento académico
"""

# Solicita al usuario su promedio, tipo de alumno y número de materias reprobadas
promedio = float(input("Ingrese su promedio: "))
tipo_alumno = input("Ingrese su tipo de alumno (preparatoria/profesional): ").lower()
materias_reprobadas = int(input("Ingrese el número de materias reprobadas: "))

# Inicializa las variables de unidades y descuento
unidades = 0
descuento = 0

# Determina la cantidad de unidades y descuento según las condiciones proporcionadas
if tipo_alumno == "preparatoria":
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.25  # 25% de descuento
    elif 9 <= promedio < 9.5:
        unidades = 50
        descuento = 0.10  # 10% de descuento
    elif 7 <= promedio < 9:
        unidades = 50
    elif promedio <= 7 and 0 <= materias_reprobadas <= 3:
        unidades = 45
    elif promedio <= 7 and materias_reprobadas >= 4:
        unidades = 40
else:  # Alumno de profesional
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.20  # 20% de descuento
    else:
        unidades = 55

# Calcula el total a pagar según las unidades y el descuento
precio_por_unidad = 300 if tipo_alumno == "profesional" else 180
total_pagar = unidades * (1 - descuento) * precio_por_unidad

# Muestra el resultado
print(f"Unidades a cursar: {unidades}")
if descuento > 0:
    print(f"Descuento aplicado: {descuento * 100}%")
print(f"Total a pagar: ${total_pagar:.2f}")


"""
4. Que lea tres números diferentes y determine el numero medio del conjunto de los tres números (el numero
medio es aquel numero que no es ni mayor, ni menor) 

"""

# Solicita al usuario ingresar tres números diferentes
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Determina el número medio
if num1 < num2 < num3 or num3 < num2 < num1:
    numero_medio = num2
elif num2 < num1 < num3 or num3 < num1 < num2:
    numero_medio = num1
else:
    numero_medio = num3

# Muestra el número medio
print(f"El número medio del conjunto es: {numero_medio}")


"""
5. El gobierno del estado de México desea reforestar un bosque que mide determinado numero de hectáreas.
Si la superficie del terreno excede a 1 millón de metros cuadrados, entonces decidirá sembrar de la sig.
manera: 

"""

# Solicita al usuario la superficie del bosque en hectáreas
superficie_hectareas = float(input("Ingrese la superficie del bosque en hectáreas: "))

# Convierte la superficie de hectáreas a metros cuadrados (1 hectárea = 10,000 metros cuadrados)
superficie_metros_cuadrados = superficie_hectareas * 10000

# Inicializa las cantidades de pinos, oyameles y cedros
cantidad_pinos = 0
cantidad_oyameles = 0
cantidad_cedros = 0

# Determina el tipo de plantación según la superficie del terreno
if superficie_metros_cuadrados > 1000000:
    # Plantación para superficies mayores a 1 millón de metros cuadrados
    cantidad_pinos = (0.7 * superficie_metros_cuadrados) // 10
    cantidad_oyameles = (0.2 * superficie_metros_cuadrados) // 15
    cantidad_cedros = (0.1 * superficie_metros_cuadrados) // 18
else:
    # Plantación para superficies iguales o menores a 1 millón de metros cuadrados
    cantidad_pinos = (0.5 * superficie_metros_cuadrados) // 10
    cantidad_oyameles = (0.3 * superficie_metros_cuadrados) // 15
    cantidad_cedros = (0.2 * superficie_metros_cuadrados) // 18

# Muestra el número de árboles a plantar de cada tipo
print(f"Número de pinos a plantar: {cantidad_pinos}")
print(f"Número de oyameles a plantar: {cantidad_oyameles}")
print(f"Número de cedros a plantar: {cantidad_cedros}")

"""
6. Elaborar un algoritmo que permita encontrar el valor menor entre un grupo de datos
y el número de veces que éste se presenta.

"""

# Solicita al usuario ingresar una serie de números separados por espacios
datos = input("Ingrese una serie de números separados por espacios: ")

# Divide los datos en una lista de números
numeros = [float(numero) for numero in datos.split()]

# Inicializa las variables para el valor mínimo y la cuenta
valor_minimo = None
conteo_minimo = 0

# Itera a través de los números para encontrar el valor mínimo y contar su frecuencia
for numero in numeros:
    if valor_minimo is None or numero < valor_minimo:
        valor_minimo = numero
        conteo_minimo = 1
    elif numero == valor_minimo:
        conteo_minimo += 1

# Muestra el valor mínimo y su frecuencia
print(f"El valor mínimo es: {valor_minimo}")
print(f"Se presenta {conteo_minimo} veces en la serie de números.")


"""
7. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 250

"""

# Itera a través de los números del 25 al 250
for numero in range(25, 251):
    # Verifica si el número termina en 6
    if numero % 10 == 6:
        print(numero)


"""
8. En un supermercado una ama de casa pone en su carrito los artículos que va
tomando de los estantes. La señora quiere asegurarse de que el cajero le cobre
bien lo que ella ha comprado, por lo que cada vez que toma un artículo anota su
precio junto con la cantidad de artículos iguales que ha tomado y determina
cuánto dinero gastara en ese artículo; a esto le suma lo que ira gastando en los
demás artículos, hasta que decide que ya tomo todo lo que necesitaba. Ayúdale
a esta señora a obtener el total de sus compras. 

"""

#alamacernar la informacion de las ventas de indefinido numero de clientes (while)

#Numero de productos a comprar por el cliente

#En pantalla deberá mostrar el valor total de la compra

#almacenar en una lista el valor total de cada venta realizada en la Ferretería


def prom(valorTotal):
  promN = sum(valorTotal) / len(valorTotal)
  PromedioVenta = print(f"el promedio de ventas es de {promN}")
  return PromedioVenta


def VentaMayor(valorTotal):
  MayorVenta = max(valorTotal)
  return MayorVenta


def VentaMenor(valorTotal):
  MenorVenta = min(valorTotal)
  return MenorVenta


productos = {}
valorTotal = []
suma = 0

print("*****Tienda la canasta*****")

while True:
  numProductos = int(input("cuantos productos desea comprar: "))
  for i in range(numProductos):
    nombreProducto = input(f"ingrese el nombre del producto {i+1}: ")
    cantidad = int(input("ingrese la cantidad que desea comprar: "))
    valorProducto = float(input(f"ingrese el valor del producto {i+1}: "))
    productos[f"producto {i+1}"] = nombreProducto
    productos[f"valor del producto {i+1}"] = valorProducto

    neto = cantidad * valorProducto

    if neto < 100000:
      valorTotal.append(neto)
      pass

    elif neto >= 10000 and neto <= 5000000:
      neto - 0.20
      valorTotal.append(neto)
    elif neto > 500000:
      neto - 0.35
      valorTotal.append(neto)
      print(valorTotal)

  break

print(productos)

print(
  f" el valor mas alto es {VentaMayor(valorTotal)} y el menor es {VentaMenor(valorTotal)}"
)
