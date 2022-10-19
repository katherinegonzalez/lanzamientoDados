# ----------------------------------------------------------------------------------------
# PROGRAMA: Dados de diferente número de caras
# ----------------------------------------------------------------------------------------
# Descripción: Este programa permite simular el lanzamiento de un par de dados.
# ----------------------------------------------------------------------------------------
# Autor: Lorena Patricia Mora Hernandez y Katherine Xiomar González Santacruz
# Version: 1.0
# [18.10.2022]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from clases import *

# ----------------------------------------------------------------------------------------
# FUNCIÓN: esNumeroCarasValido
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar si el valor recibido es un número válido de caras:
# es un número y es 4, 6 u 8
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) numero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es número, y es 4, 6 u 8 retorna True, de lo contrario retorna False
#       Valor de retorno: bool (True o False)
# ----------------------------------------------------------------------------------------
def esNumeroCarasValido(numero):
    return numero.isdigit() and (int(numero) == 4 or int(numero) == 6 or int(numero) == 8)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: isSalir
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar si la opción es si o no, para salir del programa
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) opcion
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es si o no retorna True, de lo contrario retorna False
#       Valor de retorno: bool (True o False)
# ----------------------------------------------------------------------------------------
def isSalir(opcion):
    return opcion == 'si' or opcion == 'no'

# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar el valor ingresado por el usuario
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje, (function) condicion
#       variable auxiliar: (bool) seguirPreguntando
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguir preguntando es false, el ciclo se rompe y se retorna el valor ingresado
#           por el usuario.
#           Si la condición no se cumple imprime un mensaje en pantalla
#       Valor de retorno: (str) opcionIngresada
# ----------------------------------------------------------------------------------------
def validarInput (mensaje, condicion):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (condicion(opcionIngresada)):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada

# ----------------------------------------------------------------------------------------
# FUNCIÓN: descripcionMenu
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para imprimir la descripción del menú
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
#           Imprime la descripción del menú del programa
# ----------------------------------------------------------------------------------------
def descripcionMenu():
    print('¡Bienvenido al programa de lanzamiento de dados!' )
    print('\n')
    print('A continuación se lanzaran un par de dados de las características que usted desee (Los dados solo pueden tener 4, 6 u 8 caras). ')
    print('\n')

# ----------------------------------------------------------------------------------------
# FUNCIÓN: ejecutarLanzamiento
# ----------------------------------------------------------------------------------------
# Descripción: función para hacer la simulación del lanzamiento de los dos dados.
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
#           Imprime el resultado del lanzamiento
# ----------------------------------------------------------------------------------------
def ejecutarLanzamiento(numeroCarasDado1, numeroCarasDado2):
    # Dado 1
    carasDado1 = []
    for i in range(1, numeroCarasDado1 + 1):
        cara = Caras(i, '@')
        cara.obtenerCaraConSimbolos()
        carasDado1.append(cara)

    # Dado 2
    carasDado2 = []
    for j in range(1, numeroCarasDado2 + 1):
        cara = Caras(j, '*')
        cara.obtenerCaraConSimbolos()
        carasDado2.append(cara)

    dado1 = Dado(carasDado1)
    dado1.lanzarDado()

    dado2 = Dado(carasDado2)
    dado2.lanzarDado()

    print('El resultado de su lanzamiento fue: ')
    print(dado1, ': ', dado1.get_resultadoLanzamiento())
    print(dado2, ': ', dado2.get_resultadoLanzamiento())


# ----------------------------------------------------------------------------------------
# Ejecución del programa
# ----------------------------------------------------------------------------------------

salir = 'no'
while (salir != 'si'):
    descripcionMenu()
    numeroCarasDado1 = int(validarInput('Ingrese el número de caras del primer dado: ', esNumeroCarasValido))
    numeroCarasDado2 = int(validarInput('Ingrese el número de caras del segundo dado: ', esNumeroCarasValido))
    ejecutarLanzamiento(numeroCarasDado1, numeroCarasDado2)
    salir = validarInput('Si desea Finalizar el programa escriba si, de lo contrario escriba no: ', isSalir)

    print('\n')
