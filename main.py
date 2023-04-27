import problema1
from alumnos import alumnos
"""
Hasta ahora hemos trabajado con variables que opermiten almacenar un unico valor
"""

edad = 12
altura = 1.85
nombre = 'Drow'
estado = True

"""
En Python podemos usar una variabel que almacena una coleccion de gdatos y luego accedelrla usando un subindice
"""

#Lista de enteros
lista1 = [10, 5, 3, 9]
lista2 = [1.78, 2.66, 1.55, 89.4]
lista3 = ['Lunes', 'Martes', 'Miercoles']

"""
Lista de elementos de distinto tipo
"""

lista4 = ['Juan',45,1.92,False]




if __name__ == '__main__':

    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print(lista1)

    print()

    problema1.sumar_5_enteros()

    print()

    alumnos()