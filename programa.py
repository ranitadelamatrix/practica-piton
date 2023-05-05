# REALIZAR UN PROGRAMA EN DONDE ME PIDA LA EDAD Y SI ES MAYOR A 18 ME PIDA EL NOMBRE, UNA VEZ INGRESADO
# EL NOMBRE ME DIGA BIENVENIDO NOMBRE
# SI LA EDAD ES MENOR A 18 QUE ME DIGA TOMATE EL PALO PORQUE SOS MENOR

#edad = int(input('ingrese su edad '))


"""if(edad > 18):
    nombre = input('ingrese su nombre ')
    print('benvenido al bar ' + nombre)
else:
    print('tomate el palo porque sos menor culiado')
    """

    # 5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
# el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
# de cambio quiere, si de dólares a pesos o viceversa.

def pesosDolares(cantidad):
    
    pesosDolare = cantidad / 300
    print("cantidad de dolares es ", pesosDolare)

def dolaresPesos(cantidad):
    dolaresPeso = 300 * cantidad
    print("cantidad de pesos es ", dolaresPeso)

moneda = input("a que moneda quiere cambiar pesos o dolares ")

if(moneda == "pesos"):
    dolares = int(input("ingrese dolares: "))
    dolaresPesos(dolares)
else:
    pesos = int(input("ingrese pesos: "))
    pesosDolares(pesos)