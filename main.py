import tkinter as tk
import copy 
from tkinter import ttk
import time 
import variables 
from variables import *


# Se define root
root = tk.Tk() 
root.title("GatoAventuras")
root.geometry("600x800")


"""

░██████╗░░█████╗░███╗░░░███╗███████╗  ██╗░░░░░░█████╗░░██████╗░██╗░█████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░░░░██║░░██║██║░░██╗░██║██║░░╚═╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░░░░██║░░██║██║░░╚██╗██║██║░░██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ███████╗╚█████╔╝╚██████╔╝██║╚█████╔╝
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚══════╝░╚════╝░░╚═════╝░╚═╝░╚════╝░
"""

print(teclas_presionadas)

"""

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔══██╗██╔════╝
██║░░╚═╝███████║██╔██╗██║╚██╗░██╔╝███████║╚█████╗░ 
██║░░██╗██╔══██║██║╚████║░╚████╔╝░██╔══██║░╚═══██╗
╚█████╔╝██║░░██║██║░╚███║░░╚██╔╝░░██║░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░
"""
#_ Dibujar mapa
def dibujar_mapa():
    global objetos_a_recolectar, player_hp_label, player_puntos_label, player_objetivos_label, player_casillas_restantes_label
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
            elif valor == 5:
                color = "yellow"
                

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
    dibujar_enemigos()

    #Actualizamos los labels
    player_hp_label.config(text=f"Vidas : {player_hp}")
    player_casillas_restantes_label.config(text=f"Energia : {player_casillas_restantes}")
    player_objetivos_label.config(text=f"Objetos por recolectar : {objetos_a_recolectar}")
    calculo_puntos_continuo() #Esta funcion hara el calculo y refrescara el label

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

"""

██████╗░░█████╗░██╗░░░░░░█████╗░  ██████╗░███████╗  ░█████╗░░█████╗░███╗░░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗  ██╔══██╗██╔════╝  ██╔══██╗██╔══██╗████╗░██║██╔══██╗████╗░██║
██████╦╝███████║██║░░░░░███████║  ██║░░██║█████╗░░  ██║░░╚═╝███████║██╔██╗██║██║░░██║██╔██╗██║
██╔══██╗██╔══██║██║░░░░░██╔══██║  ██║░░██║██╔══╝░░  ██║░░██╗██╔══██║██║╚████║██║░░██║██║╚████║
██████╦╝██║░░██║███████╗██║░░██║  ██████╔╝███████╗  ╚█████╔╝██║░░██║██║░╚███║╚█████╔╝██║░╚███║
╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═════╝░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝
"""
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
        nueva_col = cols_balas_canon[i] + direccion_balas_canon[i] 
        if puede_moverse(filas_balas_canon[i], nueva_col):
            if puede_destruir(filas_balas_canon[i], nueva_col): #Evitamos destruir una escalera
                if puede_destruir(filas_balas_canon[i], cols_balas_canon[i]):#Verificar tanto antes de entrar como despues
                    matriz[filas_balas_canon[i]][cols_balas_canon[i]] = 0 #Eliminamos la vieja posicion
                    matriz[filas_balas_canon[i]][nueva_col] = 4 #Sustituimos la posicion
                else:
                    matriz[filas_balas_canon[i]][nueva_col] = 4 #Rebota ante el objetivo
                cols_balas_canon[i] = nueva_col #Sustituimos el valor de esta posicion
            else:
                direccion_balas_canon[i] *= -1
      
        else:
            direccion_balas_canon[i] *= -1

# Importante, verificar si puede o no alterar la matriz que se esta usando

def puede_destruir(fila, col):
    if matriz[fila][col] == 2 or matriz[fila][col] == 5 or matriz[fila][col] == 3:
        return False
    return True  

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
#Logica de eventos
def presionar_tecla(event):
    if event.keysym not in teclas_presionadas:
        mover(event) # llamamos al movimiento
        teclas_presionadas.append(event.keysym)
def soltar_tecla(event):
    if event.keysym in teclas_presionadas:
        teclas_presionadas.remove(event.keysym)

#Logica para detectar eventos y mover
def mover(event): 
    global player_col, player_fila, facing_right, is_jumping, salto_garantizado, dash_restante, is_dashing, letra, salto_extendido, paused_game, player_casillas_restantes #Indicar que son variables globales
    nueva_fila = player_fila
    nueva_col = player_col
    #Movimiento Regular    
    if not paused_game:   
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
                player_casillas_restantes -= 3
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
                player_casillas_restantes -= 2
        elif event.keysym == "e":
            facing_right = True #Si bien ya esta arriba, seria contraituitivo que el personaje camine para la izquierda viendo a la derecha
            letra = ">"
            if not is_dashing and dash_restante == 0:
                dash_restante = 3
                is_dashing = True
                salto_garantizado = 0
                player_casillas_restantes -= 1
        elif event.keysym == "Shift_L": 
            if not is_dashing and dash_restante == 0:
                dash_restante = 4
                is_dashing = True
                salto_garantizado = 0 # Le quito el salto, ya que hace que el dash sea mas manejable y me inspiro en titulos como hollow knight
                player_casillas_restantes -= 3

        if puede_moverse(nueva_fila, nueva_col): #Como si se puede mover, se cambian los valores de las filas y cols
            player_fila = nueva_fila
            player_col = nueva_col
            player_casillas_restantes -= 1

    dibujar_mapa() #dibujamos el mapa por cada movimiento que haga nuestro jugador

# Logica del Dash
def aplicar_dash():
    global facing_right, player_fila, player_col, dash_restante, is_dashing, player_casillas_restantes
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
    global player_fila, player_col, salto_garantizado, is_jumping, teclas_presionadas, salto_extendido, player_casillas_restantes #tomamos variables
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
        elif "space" not in teclas_presionadas and salto_extendido > 0: #Caso en donde no hay salto extendido, es decir queremos un salto mas corto
            salto_extendido = 0

    elif is_jumping: #Resetear el salto hasta que toque una plataforma
        if not(esta_en_aire(player_fila, player_col)):
 
            is_jumping = False #hasta que toque algo que no sea aire
#Gravedad
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
# Verificacion de movimiento normal
def puede_moverse(fila, col):
    if fila < 0 or fila >= len(matriz):
        return False
    if col < 0 or col >= len(matriz[0]):
        return False
    if matriz[fila][col] ==1:
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
        if matriz[fila + 1 ][col] == 0 or matriz[fila +1][col] == 3: 
                return True
        else :
            return False #Si es diferente a 0, pues no esta en el aire
    except :
        return False #Si se salio, significa que esta en un borde
    
"""

██████╗░██╗░░░██╗███╗░░██╗████████╗░█████╗░░██████╗  ██╗░░░██╗
██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔══██╗██╔════╝  ╚██╗░██╔╝
██████╔╝██║░░░██║██╔██╗██║░░░██║░░░██║░░██║╚█████╗░  ░╚████╔╝░
██╔═══╝░██║░░░██║██║╚████║░░░██║░░░██║░░██║░╚═══██╗  ░░╚██╔╝░░
██║░░░░░╚██████╔╝██║░╚███║░░░██║░░░╚█████╔╝██████╔╝  ░░░██║░░░
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═════╝░  ░░░╚═╝░░░

░█████╗░░█████╗░███╗░░██╗██████╗░██╗░█████╗░██╗░█████╗░███╗░░██╗███████╗░██████╗  ██████╗░███████╗
██╔══██╗██╔══██╗████╗░██║██╔══██╗██║██╔══██╗██║██╔══██╗████╗░██║██╔════╝██╔════╝  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║██║░░██║██║██║░░╚═╝██║██║░░██║██╔██╗██║█████╗░░╚█████╗░  ██║░░██║█████╗░░
██║░░██╗██║░░██║██║╚████║██║░░██║██║██║░░██╗██║██║░░██║██║╚████║██╔══╝░░░╚═══██╗  ██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚███║██████╔╝██║╚█████╔╝██║╚█████╔╝██║░╚███║███████╗██████╔╝  ██████╔╝███████╗
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░  ╚═════╝░╚══════╝

██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░██╗░█████╗░
██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗
╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝██║███████║
░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗██║██╔══██║
░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║██║██║░░██║
░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝
"""
def encontrar_objetivos():
    global objetos_a_recolectar
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 5:
                objetos_a_recolectar += 1

def hay_colision_enemigos():
    if matriz[player_fila][player_col] == 3: #Si comparte ubicacion con un enemigo
        return True
    if matriz[player_fila][player_col] == 4:
        return True
    return False


def calculo_puntos_base():
    global player_puntos, puntos_base
    puntos_base = 0# Resetearlo cada vez que lo calculemos
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1 or matriz[i][j] == 2:
                puntos_base -= 2
            if matriz[i][j] == 3:
                puntos_base += 20
            if matriz[i][j] == 4:
                puntos_base += 50

def calculo_puntos_continuo(): #Esta la llamamos al final
    global player_puntos, player_casillas_restantes, player_hp, puntos_base, player_puntos_label
    player_puntos = puntos_base
    bonus = player_casillas_restantes*2 + player_hp*30 #Vidas y movimientos
    player_puntos += bonus
    player_puntos_label.config(text=f"Puntos : {player_puntos}")


def eliminar_enemigo():
    global player_puntos, filas_a_mantener, cols_a_mantener, direccion_a_mantener, cols_balas_canon, filas_balas_canon, direccion_balas_canon, player_fila, player_col, is_jumping, salto_garantizado, player_casillas_restantes
    filas_a_mantener = [] #hacemos variables temporales ya que si alteramos las que son globales, hay bugs en la iteracion
    cols_a_mantener = []
    direccion_a_mantener = []

    for i in range(len(filas_balas_canon)):
        if player_fila + 1 < len(matriz): #Verificar si es una casilla valida, esto evita que el canvas explote  o que tengmaos index out of bounds
            if not((filas_balas_canon[i] == player_fila +1) and (cols_balas_canon[i] == player_col)) :#Si el player no tiene algo por debajo, mantengalo
                filas_a_mantener.append(filas_balas_canon[i]) #no se elimina el enemigo
                cols_a_mantener.append(cols_balas_canon[i])
                direccion_a_mantener.append(direccion_balas_canon[i])
            else: #Si tiene algo por debajo, eliminelo
                matriz[player_fila + 1][player_col] = 0
                is_jumping =True  
                salto_garantizado = 2 #Pequeño salto al chocar
                player_casillas_restantes += 10 #Cada enemigo eliminado nos da 10 casillas más
                player_puntos += 25 #Dar veinticinco puntos cada vez que eliminamos un enemigo
        else: # Si esta en el piso, entonces no va a agregar nada, meter los enemigos
            filas_a_mantener.append(filas_balas_canon[i])
            cols_a_mantener.append(cols_balas_canon[i])
            direccion_a_mantener.append(direccion_balas_canon[i])

    filas_balas_canon = filas_a_mantener
    cols_balas_canon = cols_a_mantener
    direccion_balas_canon = direccion_a_mantener
    
  

def hay_colision_objetivo():
    if matriz[player_fila][player_col] == 5:
        return True
    return False

def comprobacion_ganar_perder():
    global player_hp, objetos_a_recolectar , paused_game, player_casillas_restantes, puntos_finales, player_puntos
    puntos_finales = 0
    eliminar_enemigo()
    if hay_colision_enemigos():
        player_hp -= 1 # Si tenemos una colision, perdemos puntos
        if player_hp == 0: #Si nos quedamos sin vidas o sin energia :(
            ventana_actual.after(1, perdiste_default) # Asegurarnos de que game loop no se ejecte mientras cambiamos de ventana
            reset_game()
        else:
            paused_game = True
            reset_game()
            
    elif player_casillas_restantes == 0 and objetos_a_recolectar != 0: #Es decir que no perdamos por una milesima
        ventana_actual.after(1, perdiste_default)

    elif hay_colision_objetivo(): #Si compartimos ubicacion con el objetivo
        objetos_a_recolectar -= 1
        matriz[player_fila][player_col] = 0 #eliminamos el objetivo a recolectar
        if objetos_a_recolectar == 0:
            puntos_finales = player_puntos
            reset_game() # por si quiere volver a intentarlo
            ventana_actual.after(1, victoria_default)


"""
Fundamental :
Game Loop, actualiza el juego y lo hace funcionar!!
"""
def game_loop(): 
    global gravedad, tick_enemigos, tick_limite, juego_activo
    if not juego_activo:
        return #Cortamos game loop
    ventana_actual.after(gravedad, game_loop)
    aplicar_salto()
    aplicar_dash()
    aplicar_gravedad() #primero activamos la gravedad
    tick_enemigos += 1
    if tick_enemigos >= tick_limite: #Basicamente, tiene que actualizarse la gravedad 3 veces para que los enemigos se empiezen a mover, esto lo hize porque son muy rapidos
        mover_balas_canon()
        tick_enemigos = 0
    comprobacion_ganar_perder() #Si se mueven volver a comprobar, para evitar bugs
    dibujar_mapa() # Dibujar de ultimo, primero refrescar 

"""

███████╗██╗░░░██╗███╗░░██╗░█████╗░██╗░█████╗░███╗░░██╗███████╗░██████╗  ██╗░░██╗
██╔════╝██║░░░██║████╗░██║██╔══██╗██║██╔══██╗████╗░██║██╔════╝██╔════   ╚██╗██╔╝
█████╗░░██║░░░██║██╔██╗██║██║░░╚═╝██║██║░░██║██╔██╗██║█████╗░░╚█████╗░  ░╚███╔╝░
██╔══╝░░██║░░░██║██║╚████║██║░░██╗██║██║░░██║██║╚████║██╔══╝░░░╚═══██   ░██╔██╗░
██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝██║╚█████╔╝██║░╚███║███████╗██████╔   ██╔╝╚██╗
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝   ╚═╝░░╚═╝

██╗░░░██╗███████╗███╗░░██╗████████╗░█████╗░███╗░░██╗░█████╗░░██████╗
██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░███████║██╔██╗██║███████║╚█████╗░
░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██╔══██║██║╚████║██╔══██║░╚═══██╗
░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░██║░░██║██║░╚███║██║░░██║██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░
"""

def reset_game(): #Al cerrar o perder vidas, debemos reiniciar el juego
    global filas_a_mantener, cols_a_mantener, direccion_a_mantener, player_fila, matriz, matriz_original, player_col, facing_right, objetos_a_recolectar, is_dashing, dash_restante, is_jumping, salto_extendido, salto_garantizado, paused_game, player_casillas_restantes, filas_balas_canon, cols_balas_canon, direccion_balas_canon
    matriz = copy.deepcopy(matriz_original)
    player_fila = len(matriz) -1 
    player_col = 0
    facing_right = True
    is_dashing = False
    dash_restante = 0
    is_jumping = False
    salto_garantizado = 0
    salto_extendido = 0
    player_casillas_restantes = 90 
    filas_balas_canon = [] 
    cols_balas_canon = []
    objetos_a_recolectar = 0
    direccion_balas_canon = []
    paused_game = False
    player_casillas_restantes = 90
    filas_a_mantener = []
    cols_a_mantener = []
    direccion_a_mantener = []
   
    #Llamar funciones
    encontrar_objetivos()
    encontrar_enemigos()
    dibujar_mapa()
    calculo_puntos_base()


def reintentar():
    global ventana_actual, objetos_a_recolectar
    ventana_actual.destroy()
    objetos_a_recolectar = 0
    iniciar_juego_default()
  
"""

▒█▄░▒█ ▀█▀ ▀█░█▀ █▀▀ █░░ 　 ▒█▀▀▄ █▀▀ █▀▀ █▀▀█ █░░█ █░░ ▀▀█▀▀ 
▒█▒█▒█ ▒█░ ░█▄█░ █▀▀ █░░ 　 ▒█░▒█ █▀▀ █▀▀ █▄▄█ █░░█ █░░ ░░█░░ 
▒█░░▀█ ▄█▄ ░░▀░░ ▀▀▀ ▀▀▀ 　 ▒█▄▄▀ ▀▀▀ ▀░░ ▀░░▀ ░▀▀▀ ▀▀▀ ░░▀░░
"""
def iniciar_juego_default():
    global juego_activo, player_hp_label, player_puntos_label, player_casillas_restantes_label, player_objetivos_label, player_hp, player_casillas_restantes
    #Primero creamos un TopLevel
    global canvas, default_game 
    global ventana_actual
    default_game = tk.Toplevel()
    ventana_actual = default_game
    ventana_actual.title("Juego")
    ventana_actual.geometry("1700x900")
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()
    juego_activo = True

    #Asegurarnos de que para el default si existan suficientes movimientos
    player_hp = 3
    player_casillas_restantes = 90
    
    #Hacemos que la ventana actual sea la que se esta usando para poder tener la logica para el constructor de mapas

    #Creamos el Canvas
    canvas = tk.Canvas(
    ventana_actual, 
    width=len(matriz[0]) * TAM, #Se hace el canvas en base al tamaño de la matriz
    height=len(matriz) * TAM, 
    bg = "White"
    )
    canvas.place(relx= 0.03, anchor="nw")
    
    #Key Binds del game
    ventana_actual.bind("<KeyPress>", presionar_tecla)
    ventana_actual.bind("<KeyRelease>", soltar_tecla)
    #Poblar lista de enemigos
    encontrar_enemigos()
    #Definir cuantos enemigos tenemos que encontrar
    encontrar_objetivos()
    #Definir puntos iniciales
    calculo_puntos_base()

    
    # Crear botones y elementos
    fin_juego = tk.Button(ventana_actual, text="Salir a menú principal", command= lambda: finalizar_juego_default())
    fin_juego.place(anchor="nw", rely= 0)

    #Creamos labels para mostrar la informacion 
    player_hp_label = tk.Label(ventana_actual, text=f"Vidas : {player_hp}", relief="groove")
    player_hp_label.place(relx= 0.1, rely = 0.9)
    
    player_casillas_restantes_label = tk.Label(ventana_actual, text=f"Energia : {player_casillas_restantes}", relief= "groove")
    player_casillas_restantes_label.place(relx = 0.3, rely = 0.9)

    player_puntos_label = tk.Label(ventana_actual, text=f"Puntos : {player_puntos}", relief="groove")
    player_puntos_label.place(relx= 0.5 , rely =0.9)
    
    player_objetivos_label = tk.Label(ventana_actual, text=f"Objetos por recolectar : {objetos_a_recolectar}", relief= "groove")
    player_objetivos_label.place(relx = 0.7, rely= 0.9)

    #Llamar al loop del juego
    game_loop() 

def perdiste_default():
    global game_over, ventana_actual, player_hp, juego_activo, puntos_finales
    juego_activo = False
    ventana_actual.destroy()
    game_over = tk.Toplevel()
    ventana_actual = game_over
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()

    #Config de la ventana : 
    ventana_actual.title("GameOver -- GatoAventuras")
    ventana_actual.geometry("600x800")

    #Widgets
    perdiste_label = tk.Label(ventana_actual, text="Perdiste : (")
    perdiste_label.pack()
    perdiste_boton = tk.Button(ventana_actual, text="regresar a menu", command=lambda: ventana_actual.destroy())
    perdiste_boton.pack()
    reintentar_default_boton = tk.Button(ventana_actual, text="Reintentar", command=lambda:reintentar())
    reintentar_default_boton.pack()
    perdiste_puntos_label = tk.Label(ventana_actual, text="No obtuviste ningun punto")
    perdiste_puntos_label.pack()
   
def victoria_default():
    global ganar, ventana_actual, juego_activo, player_puntos_final, puntos_finales
    juego_activo = False
    ventana_actual.destroy()
    ganar = tk.Toplevel()
    ventana_actual = ganar 
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()

    #Config de la ventana : 
    ventana_actual.title("Victoria -- GatoAventuras")
    ventana_actual.geometry("600x800")

    #Widgets 
    ganaste_label = tk.Label(ventana_actual, text="Ganaste : )")
    ganaste_label.pack()
    ganaste_boton = tk.Button(ventana_actual, text="regresar a menu", command=lambda: ventana_actual.destroy())
    ganaste_boton.pack()
    reintentar_default_boton = tk.Button(ventana_actual, text="Reintentar", command=lambda:iniciar_juego_default())
    reintentar_default_boton.pack()
    ganaste_puntos_label = tk.Label(ventana_actual, text=f"Puntos Obtenidos: {puntos_finales}")
    ganaste_puntos_label.pack()

def finalizar_juego_default(): #salirnos del Juego
    global player_hp
    player_hp = 3
    reset_game()
    objetos_a_recolectar = 0
    encontrar_enemigos()
    encontrar_objetivos()
    dibujar_mapa()
    ventana_actual.destroy()

boton_inicio_juego = tk.Button(root, text="Iniciar Juego Predeterminado",command= lambda: iniciar_juego_default())
boton_inicio_juego.pack()

#Main loop
root.mainloop()

