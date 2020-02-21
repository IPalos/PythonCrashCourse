import pprint as pp
keepbuying=True
cart =[]
total=0

Starbucks= {
    "name":"starbucks",
    "cafe":[20,30,50],
    "cafe con leche":[25,35,55],
    "refresco":[10,20],
    "galletas":[15],
    "te":[21,31,51]
}

Cassava= {
    "name":"cassava",
    "te":[1,3,6],
    "pokis":[26],
}


sucursales=[Starbucks,Cassava]
nombre_de_sucursal=[tienda["name"] for tienda in sucursales]

print(nombre_de_sucursal)


def findStore(tienda):
    if tienda in nombre_de_sucursal:
        print("si existe la tienda")
        return tienda
    else:
        print("Esa tienda no existe")
        return False

#input -> str - nombre de la tienda
#output -> lista - articulos de esa tienda
def showStore(store):
    items=[]
    #mostrar los artículos de la tienda
    for tienda1 in sucursales:
        if store == tienda1["name"]:
            print("encontre la tienda")
            for k,v in tienda1.items():
                if k !="name":
                    items.append(k)
    print (items)
    return items

def showSizes(store,item):
    """
    input: store str -> nombre de la tienda
    str -> el nombre del atrículo
    output: si hay mas de un tamaño, los muestra, si es único, lo elige automáticamente
    """
    #tomar la longitud del valor del articulo
    #buscar en cada tienda, como le hicimos en showStore
    for tienda in sucursales:
        if store == tienda["name"]:
            sizes=tienda[item]

    #si len(item)==3:
    if len(sizes)== 3:
        #imprimir "ch, m, g"
        print("'ch', 'm', 'g'")
        return [item,("ch","m","g")]
    #si len(item)==2:
    if len(sizes)== 2:
        print("'ch', 'g'")
        return [item,("ch","g")]
        #imprimir "ch, g"
    #si len(item)==1:
    if len(sizes)== 1:
        print("Tamaño unico")
        return [item,("u")]
        #imprimir seleccioar automáticamente

def calculateSubtotal(storeDict,item,tamanio,cantidad):
    """
    input: storeDict -> diccionario de la tienda seleccionada
            item -> string con el nombre del articulo selecccionado
            tamanio -> int, el indice del tamanio seleccionado
            cantidad -> int, la cantidad que el usuario nos da
    output: precio de la orden actual
    """
    return storeDict[item][tamanio] *cantidad




#Abrir cuenta
while keepbuying:
    #Preguntar de que tienda estamos ordenando
    tienda= input("De que tienda vas a comprar?")
    store = findStore(tienda)
    if store:
        storeDict=sucursales[nombre_de_sucursal.index(store)]
        articulos=showStore(store)
        #Preguntar que articulo(s) quiere de esa tienda
        cosa=input("Que articulo deseas?")
        # verificar si lo que pide el usuario existe
        if cosa in articulos:
            tamanios=showSizes(store,cosa)
            userSize = input("Que tamanio?")
            numTamanio = tamanios[1].index(userSize)
            cantidad = input("Cuantos quieres?")
            precioUnitario=storeDict[cosa][numTamanio]
            subtotal=calculateSubtotal(storeDict,cosa,numTamanio,int(cantidad))
            orden =[tienda, cosa, userSize, precioUnitario,cantidad, subtotal]

            cart.append(orden)
            ordenCompleta= input("Desea agregar algo más?(y/n)")
            if ordenCompleta.lower() in ("n","nel","no", "nelson", "nop"):
                keepbuying = False

        else:
            print("articulo invalido, vuelve a intentarlo")

    else:
        print("tienda invalida, vuelve a intentarlo")

pp.pprint(cart)

for element in cart:
    print(element)
    total += element[5]

print("Total: ",total)
print ("Hasta luego, vuelva pronto, consume mucha cafeina!")
