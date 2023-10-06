buscamina=[[1,0,0,1,0],
           [0,0,1,0,0],
           [0,1,0,0,0],
           [0,0,0,1,0],
           [0.1,0,0,1]]
usuario= [["-","-","-","-","-"],
          ["-","-","-","-","-"],
          ["-","-","-","-","-"],
          ["-","-","-","-","-"],
          ["-","-","-","-","-"]]

fila=0
columna=0

def mostrar_tablero(tablero):
    for f in enumerate (tablero):
        print(f)

print("bienvenido al buscamina")
print("este es su tablero↓")
mostrar_tablero(usuario)

while True:
    fila=int(input("ingrese una fila"))
    columna=int(input("ingrese una columna"))
    if buscamina[fila][columna]== 1:
        print("BOMBAA!!!!")
        usuario[fila][columna]="X"
    
        mostrar_tablero(usuario)
    else:
        usuario[fila][columna]="-"
        mostrar_tablero(usuario)
        print("no hay bomba")