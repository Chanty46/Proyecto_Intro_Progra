import tkinter as tk
from tkinter import ttk
import time 

"""

██╗░░░██╗░█████╗░██████╗░██╗░█████╗░██████╗░██╗░░░░░███████╗░██████╗
██║░░░██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔════╝
╚██╗░██╔╝███████║██████╔╝██║███████║██████╦╝██║░░░░░█████╗░░╚█████╗░
░╚████╔╝░██╔══██║██╔══██╗██║██╔══██║██╔══██╗██║░░░░░██╔══╝░░░╚═══██╗
░░╚██╔╝░░██║░░██║██║░░██║██║██║░░██║██████╦╝███████╗███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═════╝░

░██████╗░██╗░░░░░░█████╗░██████╗░░█████╗░██╗░░░░░███████╗░██████╗
██╔════╝░██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔════╝
██║░░██╗░██║░░░░░██║░░██║██████╦╝███████║██║░░░░░█████╗░░╚█████╗░
██║░░╚██╗██║░░░░░██║░░██║██╔══██╗██╔══██║██║░░░░░██╔══╝░░░╚═══██╗
╚██████╔╝███████╗╚█████╔╝██████╦╝██║░░██║███████╗███████╗██████╔╝
░╚═════╝░╚══════╝░╚════╝░╚═════╝░╚═╝░░=╚═╝╚══════╝╚══════╝╚═════╝░
"""
TAM = 40 # tamaño en pixels de las celdas a graficar 
matriz  = matriz = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,0,2,0,0,0,3,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,2,0,0,3,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,3,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,2,0,0,3,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,3,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0,0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,3,0,0,0,0,0,1,1,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,2,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,2,0,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,3,0,0,0,0,0,0,0],
    [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,3,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,0,0,0,3,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],]

"""
Info Matriz
0 = Vacio
1 = Bloque
2 = Escalera
3 = Kill Block
4 = balas_cañon
"""

# Ubicacion inicial del jugador
player_fila = len(matriz) -1 
player_col = 0

# Variables a usar del jugador
facing_right = True
is_dashing = False
dash_restante = 0

is_jumping = False
salto_garantizado = 0
salto_extendido = 0

# Set de teclas presionadas
teclas_presionadas = set() #Usamos un set que es una lista sin duplicados y en este caso sera mas eficiente para saber cuales teclas estan presionadas


#Constantes para el tiempo after()
gravedad = 80
tick_enemigos = 0
tick_limite = 3

#Temporal
letra = ">"

# Variable Para la ubicacion de balas_cañon
filas_balas_canon = [] #se van a ir agregando conforme los vamos leyendo
cols_balas_canon = []
direccion_balas_canon = []

# GUI 
ventana = tk.Tk() 
ventana.title("Juego de Canvas")
ventana.geometry("1920x1080")
"""

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔══██╗██╔════╝
██║░░╚═╝███████║██╔██╗██║╚██╗░██╔╝███████║╚█████╗░
██║░░██╗██╔══██║██║╚████║░╚████╔╝░██╔══██║░╚═══██╗
╚█████╔╝██║░░██║██║░╚███║░░╚██╔╝░░██║░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░
"""
canvas = tk.Canvas(
    ventana, 
    width=len(matriz[0]) * TAM, #Se hace el canvas en base al tamaño de la matriz
    height=len(matriz) * TAM, 
    bg = "White"
    )
canvas.place(relx = 0.09, rely= 0, anchor="nw")

#_ Dibujar mapa
def dibujar_mapa():
    canvas.delete("all") # reiniciar el mapa
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            x1 = j * TAM
            y1 = i* TAM
            x2 = x1 + TAM #Se hace pixeles hacia otro el otro lado
            y2 = y1 + TAM #Se hace cuarenta pixeles hacia un lado

            #Obtenemos el valor de la celda
            valor = matriz[i][j]
            color = "white" # Hacer un bitmap con imagenes para ponerle "Texturas"
            if valor == 1: #Se trata de bloque
                color = "grey"
            elif valor == 2: #Escalera
                color = "brown"
            elif valor == 3: #Bloque 
                color = "red"
         

            # Dibujamos el cuadrado de cada celda
            canvas.create_rectangle(x1,y1,x2,y2, fill=color, outline="black") #Borde negro de la matriz ELIMINAR al terminar

            if valor == 2:
                canvas.create_text(
                    x1 + TAM/2,
                    y1 + TAM/2,
                    text = "H",
                    fill = "yellow", 
                    font = ("Arial", 16, "bold")
                )
    dibujar_player() #Dibuja al player de una vez
    dibujar_enemigos() #Dibuja el enemigo

#Dibujar al jugador
def dibujar_player():
    global letra
    x1 = player_col * TAM + 5
    y1 = player_fila * TAM + 5
    x2 = x1 + TAM - 10
    y2 = y1 + TAM - 10
    canvas.create_oval(x1, y1, x2, y2, fill="Cyan", outline = "black")
    canvas.create_text(
        player_col * TAM + TAM/2,
        player_fila * TAM + TAM/2,
        text = letra,
        fill = "White",
        font = ("Arial", 16, "bold")
        )

#Dibujar a los enemigos 
#Primero encontramos sus posiciones
def encontrar_enemigos():
    global filas_balas_canon, cols_balas_canon
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 4: #Igual a un enemigo
                filas_balas_canon.append(i) #Guardamos la fila y la columna
                cols_balas_canon.append(j)
                direccion_balas_canon.append(-1)

#Luego los dibujamos // Por el momento seran dibujos
def dibujar_enemigos():
    global filas_balas_canon, cols_balas_canon 
    for i in range(len(filas_balas_canon)): #ambas tendran el mismo largo  
        x1 = cols_balas_canon[i] * TAM + 7
        y1 = filas_balas_canon[i] * TAM + 7
        x2 = x1 + TAM - 15
        y2 = y1 + TAM - 15
        canvas.create_oval(x1, y1, x2, y2, fill="black", outline = "black")
        canvas.create_text(
        x1 * TAM + TAM/2,
        y1 * TAM + TAM/2,
        )

def mover_balas_canon():
    global filas_balas_canon, cols_balas_canon 

    for i in range(len(filas_balas_canon)):
        nueva_col = cols_balas_canon[i] + direccion_balas_canon[i] )
        if puede_moverse(filas_balas_canon[i], nueva_col):
            if matriz[filas_balas_canon[i]][nueva_col] != 2: #Evitamos destruir una escalera
                if matriz[filas_balas_canon[i]][cols_balas_canon[i]] != 2 :#Verificar tanto antes de entrar como despues
                    matriz[filas_balas_canon[i]][cols_balas_canon[i]] = 0 #Eliminamos la vieja posicion
                    matriz[filas_balas_canon[i]][nueva_col] = 4 #Sustituimos la posicion
                else:
                    matriz[filas_balas_canon[i]][cols_balas_canon[i]] = 2
                    matriz[filas_balas_canon[i]][nueva_col] = 4
            else :
                matriz[filas_balas_canon[i]][nueva_col] = 2

            cols_balas_canon[i] = nueva_col #Sustituimos el valor de esta posicion
        else:
            direccion_balas_canon[i] *= -1
      

#Movimiento Jugador 
"""

███╗░░░███╗░█████╗░██╗░░░██╗██╗███╗░░░███╗██╗███████╗███╗░░██╗████████╗░█████╗░
████╗░████║██╔══██╗██║░░░██║██║████╗░████║██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██╔████╔██║██║░░██║╚██╗░██╔╝██║██╔████╔██║██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║
██║╚██╔╝██║██║░░██║░╚████╔╝░██║██║╚██╔╝██║██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║
██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║██║░╚═╝░██║██║███████╗██║░╚███║░░░██║░░░╚█████╔╝
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░

██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗ 
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""
def mover(event): 
    global player_col, player_fila, facing_right, is_jumping, salto_garantizado, dash_restante, is_dashing, letra, salto_extendido #Indicar que son variables globales
    nueva_fila = player_fila
    nueva_col = player_col
    #Movimiento Regular    
    if event.keysym == "a":
        nueva_col -= 1
        facing_right = False
        letra = "<"
    elif event.keysym == "d":
        nueva_col += 1
        facing_right = True #Cambiar esto nos permite saber si esta viendo a la izquierda o no
        letra = ">"
    elif event.keysym == "s":
        nueva_fila += 1 
    elif event.keysym == "w"and puede_escalar(nueva_fila, nueva_col) :  # Se pone la comprobacion de que pueda escalar en el evento que contenga una posible escalada
        nueva_fila -= 1
    
    #Salto
    elif event.keysym == "space" :
        if salto_garantizado == 0 and (not is_jumping) and not esta_en_aire(player_fila, player_col): # Verificar que no haya un salto en curso, y que no este en aire (tuve un bug en el que mi personaje podia empezar a caer y saltar en medio aire)
             salto_garantizado = 3
             salto_extendido = 3 #Por alguna razon, garantizado siempre le da uno al garantizado
             is_jumping = True  #Basicamente solo cambiamos los valores porque ya tenemos otras funciones que van a aplicar el salto
        else :
             pass # Si hay un salto pues se pasa
    
    #Dash direccion
    elif event.keysym == "q":
        facing_right = False
        letra = "<"
        if not is_dashing and dash_restante == 0:
            dash_restante = 3
            is_dashing = True
            salto_garantizado = 0
    elif event.keysym == "e":
        facing_right = True #Si bien ya esta arriba, seria contraituitivo que el personaje camine para la izquierda viendo a la derecha
        letra = ">"
        if not is_dashing and dash_restante == 0:
            dash_restante = 3
            is_dashing = True
            salto_garantizado = 0
    elif event.keysym == "Shift_L": 
        if not is_dashing and dash_restante == 0:
            dash_restante = 3
            is_dashing = True
            salto_garantizado = 0 # Le quito el salto, ya que hace que el dash sea mas manejable y me inspiro en titulos como hollow knight

    if puede_moverse(nueva_fila, nueva_col): #Como si se puede mover, se cambian los valores de las filas y cols
        player_fila = nueva_fila
        player_col = nueva_col

    dibujar_mapa()

# Logica del Dash
def aplicar_dash():
    global facing_right, player_fila, player_col, dash_restante, is_dashing
    if is_dashing and dash_restante > 0: 
            if facing_right:
                if player_col + 1 < len(matriz[0]): # Evitar out of range
                    if matriz[player_fila][player_col + 1] == 2: #Caso para detenernos con la escalera
                        player_col += 1
                        is_dashing = False
                        dash_restante = 0
                    elif puede_moverse(player_fila, player_col +1): #Caso en que nos podamos mover $ Si tocamos un borde, hace index out of
                        player_col += 1
                        dash_restante -= 1
                    else : #Caso de que NO nos podamos mover ni estemos llegando a una escalera
                        dash_restante = 0
                else:
                    is_dashing = False
                    dash_restante = 0
            else: # Ver a la izquierda
                    if player_col - 1 >= 0:
                        if matriz[player_fila][player_col - 1] == 2:
                            player_col -= 1
                            is_dashing = False
                            dash_restante = 0
                        elif puede_moverse(player_fila, player_col -1):
                            player_col -= 1
                            dash_restante -= 1
                        else :
                            dash_restante = 0
                    else:
                        is_dashing = False
                        dash_restante = 0
    else :
        if not esta_en_aire(player_fila, player_col): #Decimos que termino el dash hasta que toquemos el piso o un bloque
            is_dashing = False 



# Logica del salto
def aplicar_salto():
    global player_fila, player_col, salto_garantizado, is_jumping, teclas_presionadas, salto_extendido #tomamos variables
    nueva_fila = player_fila -1 #acortar la redaccion 
    if is_jumping and (salto_garantizado > 0 or salto_extendido > 0): #es un or ya que los 2 se gastan
        if salto_garantizado > 0: # Si tiene salto garantizado
            if puede_moverse(nueva_fila, player_col): #verificar que haya movimiento
                salto_garantizado -= 1
                player_fila = nueva_fila
            else:
                salto_extendido = 0 #Si no se puede mover, eliminar todo salto
                salto_garantizado = 0
        elif salto_extendido > 0 and "space" in teclas_presionadas: #Si se acabo el salto garantizado pero para extenderlo y presiono 0
            if puede_moverse(nueva_fila, player_col): 
                salto_extendido -= 1
                player_fila = nueva_fila
            else :
                salto_garantizado = 0 
                salto_extendido = 0
        elif "space" not in teclas_presionadas and salto_extendido > 0: #Caso en donde no hay salto extendido
            salto_extendido = 0

    elif is_jumping: #Resetear el salto hasta que toque una plataforma
        if not(esta_en_aire(player_fila, player_col)):
            is_jumping = False #hasta que toque algo que no sea aire

  
"""

██╗░░░██╗███████╗██████╗░██╗███████╗██╗░█████╗░░█████╗░██████╗░
██║░░░██║██╔════╝██╔══██╗██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗
╚██╗░██╔╝█████╗░░██████╔╝██║█████╗░░██║██║░░╚═╝███████║██████╔╝
░╚████╔╝░██╔══╝░░██╔══██╗██║██╔══╝░░██║██║░░██╗██╔══██║██╔══██╗
░░╚██╔╝░░███████╗██║░░██║██║██║░░░░░██║╚█████╔╝██║░░██║██║░░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███╗░░░███╗░█████╗░██╗░░░██╗██╗███╗░░░███╗██╗███████╗███╗░░██╗████████╗░█████╗░
████╗░████║██╔══██╗██║░░░██║██║████╗░████║██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██╔████╔██║██║░░██║╚██╗░██╔╝██║██╔████╔██║██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║
██║╚██╔╝██║██║░░██║░╚████╔╝░██║██║╚██╔╝██║██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║
██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║██║░╚═╝░██║██║███████╗██║░╚███║░░░██║░░░╚█████╔╝
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░
"""
# Verificacion de movimiento
def puede_moverse(fila, col):
    if fila < 0 or fila >= len(matriz):
        return False
    if col < 0 or col >= len(matriz[0]):
        return False
    if matriz[fila][col] == 3 or matriz[fila][col] ==1:
        return False
    return True

#Verificacion de escaleras
def puede_escalar(fila, col): #Verificamos si el jugador esta encima de una escalera o no
    try :
        if matriz[fila][col] == 2 or matriz[fila + 1][col] == 2: #Se pone fila - 1 para poder bajar incluso si se esta por encima de la escalera
            return True
    except:
         return False
    
#Verificar si esta en el aire o en una escalera
def esta_en_escalera(player_fila, player_col):
    if matriz[player_fila][player_col] == 2:
        return True
    return False # esto nos sirve para verificar que no se caiga el personaje mientras este en la escalera

def esta_en_aire(fila, col):
    try : #Use un try para evitar un outofbounds error
        if matriz[fila + 1 ][col] == 0: 
                return True
            
        else :
            return False #Si es diferente a 0, pues no esta en el aire
    except :
        return False #Si se salio, significa que esta en un borde
    

"""
██╗░░░░░░█████╗░░██████╗░██╗░█████╗░░█████╗░  ░██████╗░██████╗░░█████╗░██╗░░░██╗███████╗██████╗░░█████╗░██████╗░
██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗██╔══██╗  ██╔════╝░██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║░░░░░██║░░██║██║░░██╗░██║██║░░╚═╝███████║  ██║░░██╗░██████╔╝███████║╚██╗░██╔╝█████╗░░██║░░██║███████║██║░░██║
██║░░░░░██║░░██║██║░░╚██╗██║██║░░██╗██╔══██║  ██║░░╚██╗██╔══██╗██╔══██║░╚████╔╝░██╔══╝░░██║░░██║██╔══██║██║░░██║
███████╗╚█████╔╝╚██████╔╝██║╚█████╔╝██║░░██║  ╚██████╔╝██║░░██║██║░░██║░░╚██╔╝░░███████╗██████╔╝██║░░██║██████╔╝
╚══════╝░╚════╝░░╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░
"""
def aplicar_gravedad():
    global player_fila, player_col, salto_garantizado # Usar la variable global que contiene la posicion del jugador y el salto del jugador
    if salto_garantizado > 0 or salto_extendido > 0 or dash_restante > 0: #Para hacer el dash mas facil e intuitivo de usar, simplemente cancelamos la gravedad al hacer un dash
        pass # no hace nada, simplemente dejamos que suba 
             # En palabras simples, cancelamos la gravedad para aplicar el salto
    else :
        if esta_en_escalera(player_fila, player_col):
            pass
        elif player_fila + 1 >= len(matriz): #No es necesario dar el borde de arriba ya que no puede caer para arriba
            pass # simplemente, no pasa nada
        elif esta_en_aire(player_fila, player_col): #Comparar si la casilla debajo del jugador es una caida o no
            player_fila += 1
        else :
            pass 

def game_loop(): 
    global gravedad, tick_enemigos, tick_limite
    ventana.after(gravedad, game_loop)
    aplicar_salto()
    aplicar_dash()
    aplicar_gravedad() #primero activamos la gravedad
    tick_enemigos += 1
    if tick_enemigos >= tick_limite: #Basicamente, tiene que actualizarse la gravedad 3 veces para que los enemigos se empiezen a mover, esto lo hize porque son muy rapidos
        mover_balas_canon()
        tick_enemigos = 0
    dibujar_mapa() # luego dibujamos
"""

██╗░░░░░░█████╗░░█████╗░██████╗░░██████╗
██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░░░░██║░░██║██║░░██║██████╔╝╚█████╗░
██║░░░░░██║░░██║██║░░██║██╔═══╝░░╚═══██╗
███████╗╚█████╔╝╚█████╔╝██║░░░░░██████╔╝
╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═════╝░
"""

#Logica de teclas
def presionar_tecla(event):
    if event.keysym not in teclas_presionadas:
        mover(event) # llamamos al movimiento
        teclas_presionadas.add(event.keysym)

def soltar_tecla(event):
    teclas_presionadas.discard(event.keysym)

#Binds
ventana.bind("<KeyPress>", presionar_tecla)
ventana.bind("<KeyRelease>", soltar_tecla)
#Poblar lista de enemigos
encontrar_enemigos()
#Llamar al loop del juego
game_loop() 
#Main loop
ventana.mainloop()

# Para el chante del futuro
# Problemas
# Colision con enemigos y obstaculosd

#Enemigos que se mueven
#Rework a toda la gravedad 
#Gravedad especifica para el enemigo