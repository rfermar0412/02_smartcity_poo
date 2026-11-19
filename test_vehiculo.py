from vehículo import Vehiculo

# 1. CREACIÓN (INSTANCIACIÓN): Llamamos al nombre de la clase con sus datos
auto1 = Vehiculo("1234-BBB", "Urban-E", 40.0)
auto2 = Vehiculo("5678-FFF", "EcoVan", 75.0)

# 2. ACCESO A ATRIBUTOS: Usamos el operador punto (objeto.atributo)
print(auto1.matricula) # Muestra: 1234-BBB
print(auto1.nivel_bateria) # Muestra: 100.0
