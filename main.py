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
░╚═════╝░╚══════╝░╚════╝░╚═════╝░╚═╝░░=╚═╝╚══════╝╚══════╝╚═════╝░
"""
TAM = 40 # tamaño en pixels de las celdas a graficar 
matriz = matriz = matriz = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
    [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,3,0,0,0,0,0,0,0],
    [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,3,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,0,0,0,3,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
            ]


# Ubicacion inicial del jugador
player_fila = len(matriz) -1 
player_col = 0

# Variables a usar del jugador
facing_right = True
is_dashing = False
dash_restante = 0

letra = ">"

gravedad = 80
is_jumping = False
salto_restante = 0

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
#META, reworkear el movimiento para poder hacer mas de dos acciones a la vez, pero con el code que tenemos puede que sea suficiente
#Multiples comandos a la vez
    global player_col, player_fila, facing_right, is_jumping, salto_restante, dash_restante, is_dashing, letra#Indicar que son variables globales
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
        if salto_restante == 0 and (not is_jumping) and not esta_en_aire(player_fila, player_col): # Verificar que no haya un salto en curso, y que no este en aire (tuve un bug en el que mi personaje podia empezar a caer y saltar en medio aire)
             salto_restante += 5
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
            salto_restante = 0
    elif event.keysym == "e":
        facing_right = True #Si bien ya esta arriba, seria contraituitivo que el personaje camine para la izquierda viendo a la derecha
        letra = ">"
        if not is_dashing and dash_restante == 0:
            dash_restante = 3
            is_dashing = True
            salto_restante = 0
    elif event.keysym == "Shift_L": 
        if not is_dashing and dash_restante == 0:
            dash_restante = 3
            is_dashing = True
            salto_restante = 0 # Le quito el salto, ya que hace que el dash sea mas manejable y me inspiro en titulos como hollow knight

    if puede_moverse(nueva_fila, nueva_col): #Como si se puede mover, se cambian los valores de las filas y cols
        player_fila = nueva_fila
        player_col = nueva_col

    dibujar_mapa()

# Logica del Dash
def aplicar_dash():
    global facing_right, player_fila, player_col, dash_restante, is_dashing
    if is_dashing and dash_restante > 0: 
            if facing_right:
                if matriz[player_fila][player_col + 1] == 2: #Caso para detenernos con la escalera
                    player_col += 1
                    is_dashing = False
                    dash_restante = 0
                elif puede_moverse(player_fila, player_col +1): #Caso en que nos podamos mover
                    player_col += 1
                    dash_restante -= 1
                else : #Caso de que NO nos podamos mover ni estemos llegando a una escalera
                    dash_restante = 0
            else: # Ver a la izquierda
                 if matriz[player_fila][player_col - 1] == 2:
                    player_col -= 1
                    is_dashing = False
                    dash_restante = 0
                 elif puede_moverse(player_fila, player_col -1):
                    player_col -= 1
                    dash_restante -= 1
                 else :
                    dash_restante = 0
    else :
        if not esta_en_aire(player_fila, player_col): #Decimos que termino el dash hasta que toquemos el piso o un bloque
            is_dashing = False 



# Logica del salto
def aplicar_salto():
    global player_fila, player_col, salto_restante, is_jumping #tomamos variables
    if is_jumping and salto_restante > 0:
        if puede_moverse(player_fila  -1, player_col): #Verificar que no choque con algo
             player_fila -= 1
             salto_restante -= 1 #Siempre le bajamos al salto, si no flotariamos
        else : #Significa que el personaje choca, terminando el salto
             salto_restante = 0
    
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

"""
██╗░░░░░░█████╗░░██████╗░██╗░█████╗░░█████╗░  ░██████╗░██████╗░░█████╗░██╗░░░██╗███████╗██████╗░░█████╗░██████╗░
██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗██╔══██╗  ██╔════╝░██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║░░░░░██║░░██║██║░░██╗░██║██║░░╚═╝███████║  ██║░░██╗░██████╔╝███████║╚██╗░██╔╝█████╗░░██║░░██║███████║██║░░██║
██║░░░░░██║░░██║██║░░╚██╗██║██║░░██╗██╔══██║  ██║░░╚██╗██╔══██╗██╔══██║░╚████╔╝░██╔══╝░░██║░░██║██╔══██║██║░░██║
███████╗╚█████╔╝╚██████╔╝██║╚█████╔╝██║░░██║  ╚██████╔╝██║░░██║██║░░██║░░╚██╔╝░░███████╗██████╔╝██║░░██║██████╔╝
╚══════╝░╚════╝░░╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░
"""
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
    

def aplicar_gravedad():
    global player_fila, player_col, salto_restante # Usar la variable global que contiene la posicion del jugador y el salto del jugador
    if salto_restante > 0 or dash_restante > 0: #Para hacer el dash mas facil e intuitivo de usar, simplemente cancelamos la gravedad al hacer un dash
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
    global gravedad
    ventana.after(gravedad, game_loop)
    aplicar_salto()
    aplicar_dash()
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
game_loop() 
#Main loop
ventana.mainloop()

#Para el chante del futuro
# Trabajemos en una matriz mas grande y definamos salto y preguntemosle a julian como siente las mecanicas
# Luego empezemos con la vida, enemigos y obstaculos, jump_pad?
# Luego main menu
# Por ultimo constructor