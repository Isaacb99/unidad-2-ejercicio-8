

class conjunto:
    __lista = []
    def _init_(self):
        self.__lista = []
    
    def carga(self):
        self.__lista = []
        while True:
            n = int(input("ingrese la componente a cargar (finalice con -1)"))
            if n == -1:
                break
            self.__lista.append(n)
            self.__lista.sort()
    
    def mostrar(self):
        print("CONJUNTO:")
        print(self.__lista)
    
    def __add__(self, otro):
        con = conjunto()
        for n in self.__lista:
            con.__lista.append(n)
        for elem in otro.__lista:
            if (elem not in con.__lista):
                con.__lista.append(elem)
        return con
    
    def __sub__(self, otro):
        con = conjunto()
        for elem in self.__lista:
            if (elem not in otro.__lista):
                con.__lista.append(elem)
        return con
    
    def __eq__(self, otro):
        for elem in self.__lista:
            if(elem not in otro.__lista):
                return False
        return True