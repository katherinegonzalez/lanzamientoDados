# ----------------------------------------------------------------------------------------
# MODULO: Clases Dado y Caras
# ----------------------------------------------------------------------------------------
# Descripción: En este módulo se encuentran la definición de las clases Dado y Cara.
# ----------------------------------------------------------------------------------------
# Autores: Lorena Patricia Mora Hernandez y Katherine Xiomar González Santacruz
# Version: 1.0
# [18.10.2022]
# ----------------------------------------------------------------------------------------

import random
# ------------------------------------------------------
# Definición una clase Dado - Tiene como
# atributos caras, nCaras y resultadoLanzamiento
# ------------------------------------------------------
class Dado:
    def __init__(self, caras):
        self.caras = caras
        self.nCaras = len(caras)
        self.resultadoLanzamiento = None

    def get_nCaras(self):
        return self.nCaras

    def set_nCaras(self, nCaras):
        self.nCaras = nCaras

    def get_caras(self):
        return self.caras

    def set_caras(self, caras):
        self.caras = caras

    def get_resultadoLanzamiento(self):
        return self.resultadoLanzamiento

    def set_resultadoLanzamiento(self, resultadoLanzamiento):
        self.resultadoLanzamiento = resultadoLanzamiento

    def lanzarDado(self):
        numeroRandom = random.randint(0, self.nCaras - 1)
        self.resultadoLanzamiento = self.caras[numeroRandom]

    def __str__(self):
        return 'Dado de ' + str(self.nCaras) + ' caras'

# ------------------------------------------------------
# Definición una clase Caras - Tiene como
# atributos nCara, cimbolo y caraCoNsimbolos
# ------------------------------------------------------
class Caras:
    def __init__(self, nCara, simbolo):
        self.nCara = nCara
        self.simbolo = simbolo
        self.caraConSimbolos = ''

    def get_nCara(self):
        return self.nCara

    def set_nCara(self, nCara):
        self.nCara = nCara

    def get_simbolo(self):
        return self.simbolo

    def set_simbolo(self, simbolo):
        self.simbolo = simbolo

    def get_caraConSimbolos(self):
        return self.caraConSimbolos

    def set_caraConSimbolos(self, caraConSimbolos):
        self.caraConSimbolos = caraConSimbolos

    def obtenerCaraConSimbolos(self):
        for i in range(self.nCara):
            self.caraConSimbolos = self.caraConSimbolos + self.simbolo

    def __str__(self):
        return self.caraConSimbolos







