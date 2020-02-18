# While loop
j=0
while j< 100:
    print(j)
    j+=1

# 1er for loop
countingto100=[]
for j in range(100):
    countingto100.append(j)
    pass



# 2do for loop
for element in countingto100:
    print(element*10)

mochila={'Estuche', 'Lapiz', 'Cuaderno', 'lunch', 'cargador'}
for item in mochila:
    print (item)


#Bloque del sudoku
bloque= [[0,0,0],[0,0,0],[0,0,0]]
num=1
for fila in range(len(bloque)):
    for columna in range(len(bloque[fila])):
        bloque[fila][columna]=num
        num+=1

# print (bloque)


#Meses con R

meses=["Enero", "Febrero", "Marzo", 
       "Abril", "Mayo", "Junio", 
       "Julio", "Agosto", "Septiembre", 
       "Octubre", "Noviembre", "Diciembre"]
mesesConR=[]
mesesSinR=[]

#Pseudocodigo
#Checar cada mes
for mes in meses:
    #si el mes contiene una r,
    if mes.find('r') == -1:
        #guardarlo en lista mesesConR
        mesesSinR.append(mes)
    #si no contiene una r,
    else:
        #cuardarlo en mesesSinR
        mesesConR.append(mes)


print('Meses Con R: ',mesesConR)
print('Meses Sin R: ',mesesSinR)

# Tareas Domesticas
chores=["Sweeping",
       "Vacuuming", 
       "Washing dishes",
       "Feeding pets", 
       "Doing laundry", 
       "Preparing meals", 
       "Cleaning bathrooms",
       "Dusting",
       "Washing bedding",
       "Mopping floors",
       "Watering plants",
       "Mowing the lawn",
       "Weeding the garden",
       "Taking out the trash",
       "Wash the car",
       "Washing windows",
       "Bathing pets",
       "Clean refrigerator",
       "Change air filters on a furnace",
       "Clean blinds",
       "Vacuum curtains"]
lun=[]
mar=[]
mier=[]
jue=[]
vier=[]
sab=[]
dom=[]
choresOrdenado= sorted(chores)
print(choresOrdenado)


#contar las tareas
numDeTareas=len(chores)
#dividir el total entre 7
TareasXDia= numDeTareas//7
print('Numero de tareas por dia: ',TareasXDia)
#armar lista por cada dia
lun=choresOrdenado[0:TareasXDia]
mar=choresOrdenado[TareasXDia:2*TareasXDia]
mier=choresOrdenado[2*TareasXDia:3*TareasXDia]
jue=choresOrdenado[3*TareasXDia:4*TareasXDia]
vier=choresOrdenado[4*TareasXDia:5*TareasXDia]
sab=choresOrdenado[5*TareasXDia:6*TareasXDia]
dom=choresOrdenado[6*TareasXDia:7*TareasXDia]

print(lun)
print(mar)
print(mier)
print(jue)
print(vier)
print(sab)
print(dom)

#Diccionarios

miDiccionario = {'lapices':"si tengo", 
'cuadernos':'azul', 
'cargador':True}

miDiccionario['labial']='Frambuesa'

print(miDiccionario)

estudiantes= {
    'Beto':10,
    'MariToni':10,
    'Irex':miDiccionario,
    'Alicia':3.14**2
}

print(estudiantes['Irex'])
