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



print (Starbucks.keys())

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

    return items

def showSizes(store,item):
    """
    input: store str -> nombre de la tienda
    str -> el nombre del atrículo
    output: si hay mas de un tamaño, los muestra, si es único, lo elige automáticamente
    """
    #tomar la longitud del valor del articulo
    for tienda in sucursales:
        
    #buscar en cada tienda, como le hicimos en showStore

    #si len(item)==3:
        #imprimir "ch, m, g"
    #si len(item)==2:
        #imprimir "ch, g"
    #si len(item)==1:
        #imprimir seleccioar automáticamente


def placeOrder(store):
    """
    devuelve una lista parecida a:
    [tienda, item, size, p.unitario, qty, subtotal]
    """
    #Validar la tienda
    findStore(store)
    #Mostrar cosas de la tiendas



#Abrir cuenta
while keepbuying:
    #Preguntar de que tienda estamos ordenando
    tienda= input("De que tienda vas a comprar?")
    #Preguntar que articulo(s) quiere de esa tienda
    cosa=input("Que articulo deseas?")
    #Tamaños
    # if len()
    #cantidad

    placeOrder(tienda)
#Algo mas?
