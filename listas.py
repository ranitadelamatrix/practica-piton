# trabajamos con lista, tenemos que darle un nombre y luego le asignamos un valor abriendo corchetes []
#ingresando valores como string o numeros, booleanos, separados por ,

#ejemplo de listas

edades = [40, 39, 33, 34, 20] # este es una lista de numeros searados por una ,

grupo = ['carolina', 'victoria', 'lucas', 'santi', 'gaston'] #esto es una lista de string separados por ,

datosRandon = [22, 'hola', True] #este es una lista combinada con numeros string y boolean

misMascotas = ['fryda', 'nacho', 'toro', 'mileidy']

# ingresar a cada elemento de la lista de forma individual a esto se le llama objetos iterables

print(grupo[1]) # al poner el nombre de la variable abrir los corchetes y ponerles un indice me tirar dato de esa ubica

# para modificar un elemento de la lista, seleccionamos el indice a modificar y le asignamos el nuevo valor

grupo[1] = 'vic'
print(grupo)

# acceder a un rango de objetos
print(grupo[1:4]) # excluyendo el ultimo indice

print(grupo[0:])

# listas dentro de una lista

ingredientes = [['harina', 'agua','levadura', 'aceite'], ['tomate', 'cebolla', 'pimiento']]

# para ingresar a la ubicacion del tomate por ejemplo, ponemos la ubicaciones de esta lista primero
# osea el numer [1], seguido de la ubicacion del tomate [0] en otro corchete

print(ingredientes[1][0])

# agregamos elementos a la lista con el metodo .append(el elemento a agregar), seria la lista grupo.append()
grupo.append('jorge')
# de esta forma se agrega a la lista el nombre jorge
print(grupo)

misMascotas.append('jhon')

#para agregar varios elementos a la lista el metodo .extend([])

datosRandon.extend(['hello', False, 69, 22, 69])

print(datosRandon)

misMascotas.insert(1, 'patato')
print(misMascotas)

# para eliminar metodo remove  por su valor

misMascotas.remove('jhon')

print(misMascotas)

# ordenamiento de listas

edades.sort()
print(edades)

# contar las veces que se repite un elemento, abrimos una variable nueva

repetidos = datosRandon.count(69)
print(repetidos)
