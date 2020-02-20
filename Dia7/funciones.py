
#Ejemplo de binvenida
def bienvenida(hora,nombre):
    print("Buenas "+hora+nombre)

tarde="Tardes "
noche="Noches "

nombre1="Alicia"
nombre2="Beto"
nombre3="Irex"
nombre4="Maritoni"
nombre5="Ricardo"


# bienvenida(tarde, nombre2)
# bienvenida(noche, nombre3)
# bienvenida(tarde, nombre1)
# bienvenida(noche, nombre4)
# bienvenida(tarde, nombre5)

propina="hello"

def calcular_propina(subtotal):
    propina=subtotal*.15
    total=round(subtotal*1.15)
    print("Su propina es de: ",propina)
    print("Su total es de: ",total)
    return [propina,total]

micuenta=calcular_propina(100)




# print(calcular_propina(100))
