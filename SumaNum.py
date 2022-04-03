"""
Autor: Gabriela Hilario Acuapan
Fecha: 02/04/2022
Archivo: SumaNum.py
Descripción: Se define una función que suma 2 números enteros.
"""
def sum_num(a,b):
  suma = a + b
  return suma

print ("SUMA DE DOS NÚMEROS ENTEROS \n")

a = int(input("\t Introduzca el 1er número entero: "))
b = int(input("\t Introduzca el 2do número entero: "))

print("\nLa suma es: " + str(sum_num(a,b)))