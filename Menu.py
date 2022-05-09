from ast import If
from claseConjunto import conjunto
import os

class menu:
    __a = conjunto()
    __b = conjunto()
    __op = 0
    def __init_(self, op=0):
        self.__op = op
    def suma(self):
        print("suma de conjuntos")
        suma = self.__a + self.__b
        suma.mostrar()
        print("suma realizada")
    
    def resta(self):
        print("diferencia de conjuntos")
        resta = self.__a - self.__b
        resta.mostrar()
        print("diferencia realizada")
    
    def comparacion(self):
        if (self.__a == self.__b):
            print("los conjuntos son iguales")
        else: 
            print("los conjuntos no son guales")

    def opciones(self):
        print("carga del primer conjunto")
        self.__a.carga()
        print("carga del segundo conjunto")
        self.__b.carga()
        salir = True
        while salir:
            print("/// MENU DE OPCIONES ///")
            print("opcion 1: unir dos conjuntos")
            print("opcion 2: sacar la diferencia de dos conjuntos")
            print("opcion 3: verificar si los dos conjuntos son iguales")
            print("opcion 4: SALIR")
            self.__op = int(input("ingrese opcion"))
            if (self.__op == 1):
                self.suma()
            elif (self.__op == 2):
                self.resta()
            elif (self.__op == 3):
                self.comparacion()
            elif (self.__op == 4):
                print("finalizar programa")
                salir = not salir
            else: 
                print("OPCION INCORRECTA")
    