import pprint as pp
colores = {
    "red":[255,0,0],
    "blue":[0,0,255],
    0:"soy el key cero",
    3.14:"Esto es casi pi",
    "verde":"mi valor es un string color verde"

}




"Ejercicio sobre venta de una cafeteria"

"""
Item  |   Tamaño   |   Precio Unitario   |   Cantidad    |   Subtotal

cafe     ch              20                    5              100
te          m             31                    3              93



"""


bebidas= {
    "cafe":[20,30,50],
    "cafe con leche":[25,35,55],
    "refresco":[10,10,10],
    "galletas":[15,20,25],
    "te":[21,31,51]
}

keepbuying=True
cart =[]
sizes=("ch","m","g")
total=0


while keepbuying:
    #Preguntar que artículo quieres
    item = input("Que va a ordenar?")
    if item.lower() in bebidas.keys():
        ReqSize= input("De que tamaño lo quiere (ch/m/g)")
        #Preguntar tamaño
        if ReqSize in sizes:
            #obtener la bebida indicada
            bebidaSeleccionada =bebidas[item]
            #Esta variable está entre 0,1,y 2
            precioTamañoBebida =sizes.index(ReqSize)
            #Preguntar cantidad
            qty = input("Cuantos quiere?")
            subtotal = bebidaSeleccionada[int(precioTamañoBebida)]*int(qty)

            cart.append( (item, ReqSize, bebidaSeleccionada[int(precioTamañoBebida)], qty, subtotal) )

            ordenCompleta= input("Desea agregar algo más?(y/n)")
            if ordenCompleta.lower() in ("n","nel","no", "nelson", "nop"):
                keepbuying = False

        else:
            print("No manejamos ese tamaño, intenta otra vez")



    else:
        print("Ese artículo no lo manejamos joven, intenta otra vez")


#imprimir total
pp.pprint(cart)

#de cada pedido, tomar el 5to elemento
for element in cart:
#sumarlas a total
    total += element[4]
    #total = total + element[4]


print("Total: ",total)
print ("Hasta luego, vuelva pronto, consume mucha cafeina!")

    #Preguntar si quiere agregar
    #si si, regresa al inicio
    #si no, mostrar subtotal
    #preguntar confirmacion
    #si si, confirmar pago
    #si no, borrar el carrito
