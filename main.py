import tkinter as tk

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
░╚═════╝░╚══════╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░
"""
TAM = 40 # tamaño en pixels de las celdas a graficar 
matriz = matriz = [ # Matriz Lógica 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 2, 0, 3, 0, 0],
    [0, 0, 0, 0, 1, 2, 0, 3, 0, 0], # Matriz Lógica
    [0, 3, 0, 0, 1, 2, 0, 0, 0, 0], # 0 = Vacio, 1 = Bloque, 2 = escalera, 3 = obstaculo
    [0, 3, 0, 0, 0, 2, 1, 1, 1, 0],
    [0, 0, 0, 3, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 2, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 3, 0, 0],]
# Ubicacion inicial del jugador
player_fila = len(matriz) -1 
player_col = 0
facing_right = True

# GUI 
ventana = tk.Tk() 
ventana.title("Juego de Canvas")

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
canvas.pack()

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

def dibujar_player():

    x1 = player_col * TAM + 5
    y1 = player_fila * TAM + 5
    x2 = x1 + TAM - 10
    y2 = y1 + TAM - 10
    canvas.create_oval(x1, y1, x2, y2, fill="Cyan", outline = "black")
    canvas.create_text(
        player_col * TAM + TAM/2,
        player_fila * TAM + TAM/2,
        text = "P",
        fill = "White",
        font = ("Arial", 16, "bold")
        )

"""

███╗░░░███╗░█████╗░██╗░░░██╗██╗███╗░░░███╗██╗███████╗███╗░░██╗████████╗░█████╗░
████╗░████║██╔══██╗██║░░░██║██║████╗░████║██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██╔████╔██║██║░░██║╚██╗░██╔╝██║██╔████╔██║██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║
██║╚██╔╝██║██║░░██║░╚████╔╝░██║██║╚██╔╝██║██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║
██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║██║░╚═╝░██║██║███████╗██║░╚███║░░░██║░░░╚█████╔╝
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░

██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗
██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""
def mover(event):
    global player_col, player_fila, facing_right #Indicar que son variables globales
    nueva_fila = player_fila
    nueva_col = player_col

    #Movimiento Regular    
    if event.keysym == "a":
        nueva_col -= 1
        facing_right = False
    elif event.keysym == "d":
        nueva_col += 1
        facing_right = True #Cambiar esto nos permite saber si esta viendo a la izquierda o no
    elif event.keysym == "s" and puede_escalar(nueva_fila, nueva_col) : # Se pone la comprobacion de que pueda escalar en el evento que contenga una posible escalada
        nueva_fila += 1 
    elif event.keysym == "w"and puede_escalar(nueva_fila, nueva_col) :
        nueva_fila -= 1
    
    #Paso Rapido
    elif event.keysym == "q":
        facing_right = False
    elif event.keysym == "e":
        facing_right = True #Si bien ya esta arriba, seria contraituitivo que el personaje camine para la izquierda viendo a la derecha

    elif event.keysym == "Shift_L": 
        if facing_right == True:
            if puede_dash_full(nueva_fila, nueva_col):
                nueva_col += 2
            else :
                nueva_col += 1
        else :
            if puede_dash_full(nueva_fila, nueva_col):
                nueva_col -= 2
            else : 
                nueva_col -= 1

    if puede_moverse(nueva_fila, nueva_col): #Como si se puede mover, se cambian los valores de las filas y cols
        player_fila = nueva_fila
        player_col = nueva_col

    dibujar_mapa()

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
    if matriz[fila][col] == 2 or matriz[fila - 1][col] == 2: #Se pone fila - 1 para poder bajar incluso si se esta por encima de la escalera
        return True
    return False

#Verificacion de un dash completo
def puede_dash_full(fila, col):
     global facing_right

    # Verificar tanto casilla intermedia como casilla derecha  
     if facing_right == True:
        if col + 2 < 0 or col + 2 >= len(matriz[0]): # No es necesario ver bordes verticales al tratarse de un movimiento horizontal
             return False
        if (matriz[fila][col+1] == 2 or matriz[fila][col +1] == 0) and (matriz[fila][col+2] == 2 or matriz[fila][col+2] == 0):
             return True # Basicamente si la casilla destino e intermedia esten ambas vacias para hacer el dash completo
        else :
             return False
     else :
         if col - 2 < 0 or col - 2 >= len(matriz[0]): # No es necesario ver bordes verticales al tratarse de un movimiento horizontal
            return False
         if (matriz[fila][col-1] == 2 or matriz[fila][col -1] == 0) and (matriz[fila][col-2] == 2 or matriz[fila][col-2] == 0):
            return True # Basicamente si la casilla destino e intermedia esten ambas vacias para hacer el dash completo
         else :
            return False

# gravedad

def aplicar_gravedad():
    global player_fila, player_col # Usar la variable global que contiene la posicion del jugador
    if player_fila + 1 >= len(matriz): #No es necesario dar el borde de arriba ya que no puede caer para arriba
        pass # simplemente, no pasa nada
    elif matriz[player_fila + 1][player_col] == 0: #Comparar si la casilla debajo del jugador es una caida o no
        player_fila += 1
    else :
        pass 

def gravedad_loop(): 
    ventana.after(250, gravedad_loop)
    aplicar_gravedad() #primero activamos la gravedad
    dibujar_mapa() # luego dibujamos
"""

██╗░░░░░░█████╗░░█████╗░██████╗░░██████╗
██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░░░░██║░░██║██║░░██║██████╔╝╚█████╗░
██║░░░░░██║░░██║██║░░██║██╔═══╝░░╚═══██╗
███████╗╚█████╔╝╚█████╔╝██║░░░░░██████╔╝
╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═════╝░
"""
ventana.bind("<Key>", mover) # Detecta un evento, llama a la funcion "mover"
#Llamar a la funcion de dibujo de mapa
dibujar_mapa()
#Llamar a la funcion de gravedad
gravedad_loop() 
#Main loop
ventana.mainloop()