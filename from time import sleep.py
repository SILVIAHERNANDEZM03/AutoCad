from time import sleep

print("Ingrese los datos solicitados")

def CE(Celsius: float) -> float: return (Celsius + 273.15) 

def menu():
    sel = str(input("\n1.Pasar de grados celsius a kelvin \n2. Salir\n >>> "))
    while True:
        if all((sel != "1", sel != "2")): sel = str(input("Escoge una opción posible\n1.De Celsius a Kelvin \n2. Salir\n >>> "))
        else: break

    return sel

def ped_grados(escala: str) -> str:
    if escala == "1":
        CEL = float(input("Ingrese los grados Celsius para convertir a Kelvin >>> "))
        return f"{CEL}º Celsius equivalen a {CE(CEL)}º Kelvin"


def resultados(escala: str, grados: str):
    if escala == "1": print(grados)


while True:
    op = menu()
    if op == "1" or op == "2": resultados(op, ped_grados(op)); sleep(2)
    elif op == "2": print("Terminando ejecución...".center(30)); sleep(2); print("Fin del programa".center(30))
