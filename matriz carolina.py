matriz=[[1,2],
    [4,5],
    [7,8],
    ]

fila=0
columna=0
fila=int(input("ingrese una fila"))
columna=int(input("ingrese una columna"))
print("esa ubicacion esta en el num", matriz[fila][columna])
op=input("lo quiere cambiar SI/NO")
if op=="SI":
    num=int(input("ingrese su numero"))
    matriz[fila][columna]= num
    #print(matriz)
for fila in range(1,3):
    print(matriz[fila])


#print(mat)
#print(mat[1])
#print(mat[1][0])
