"""
Ejercicio 3. Programa que compruebe si una variable esta vacia
y si esta vacia , rrellenarla con texto en minusculas y mostrarlo en mayusculas

"""

valor=""

if not valor:
    print("Esta vacia")
    rrelleno=input(" Dime algo para rrellenarla ").lower()
    print(rrelleno.upper())
else:
    print("variable llena")