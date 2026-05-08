import tkinter as tk
import copy 
from tkinter import ttk
import time 
import variables 
import pygame
import PIL
from PIL import Image, ImageTk 
from variables import * #Importamos todo 

pygame.mixer.init()
pygame.mixer.music.load(canciones[0])
pygame.mixer.music.play(-1)

def toggle_musica():
    global reproducir_musica
    if pygame.mixer.music.get_busy() and reproducir_musica: #Get Busy return true si esta reproduciendo musica
        pygame.mixer.music.pause()
        reproducir_musica = False
    else:
        pygame.mixer.music.unpause()
        reproducir_musica = True

# Acceder a la informacion al abrir el documento
def leer_archivo_highscores():
    global saved_highscores, saved_puntos
    try: #Se intenta por si este esta vacio
        file = open("high_scores.txt", "r") #R es read
        for jugador in file:
            datos = jugador.strip().split(",") #Para cada_jugador, se parte los datos en 3 separados por slash/  y para evitar bugs hacemos strip "Eliminar espacios"
            saved_highscores.append(datos)
            saved_puntos.append(int(datos[1]))
        file.close() #Cerrar el archivo es buena practica
    except :
        pass #Significa que no hay un archivo

leer_archivo_highscores()
def cargar_imagenes():
    global img_bloque, img_escalera, img_obstaculo, img_enemigo, img_pescado, img_fondo_derrota, img_gato_der, img_gato_izq, img_fondo_canvas, img_fondo_juego, img_fondo_main, img_fondo_victoria
    img_bloque = ImageTk.PhotoImage(Image.open("Assets/Sprites/bloque.png"))
    img_escalera = ImageTk.PhotoImage(Image.open("Assets/Sprites/escalera.png"))
    img_obstaculo = ImageTk.PhotoImage(Image.open("Assets/Sprites/obstaculo.png"))
    img_enemigo = ImageTk.PhotoImage(Image.open("Assets/Sprites/enemigo.png"))
    img_pescado = ImageTk.PhotoImage(Image.open("Assets/Sprites/pescado.png"))
    img_gato_der = ImageTk.PhotoImage(Image.open("Assets/Sprites/GatoDer.png"))
    img_gato_izq = ImageTk.PhotoImage(Image.open("Assets/Sprites/GatoIzq.png"))
    img_fondo_canvas = ImageTk.PhotoImage(Image.open("Assets/Sprites/fondo_canvas.png"))
    img_fondo_juego = ImageTk.PhotoImage(Image.open("Assets/Sprites/fondo_juego.png"))
    img_fondo_main = ImageTk.PhotoImage(Image.open("Assets/Sprites/fondo_main.png"))
    img_fondo_victoria = ImageTk.PhotoImage(Image.open("Assets/Sprites/fondo_ganaste.png"))
    img_fondo_derrota = ImageTk.PhotoImage(Image.open("Assets/Sprites/fondo_derrota.png"))

# Se define root
root = tk.Tk() 
root.title("GatoAventuras")
root.geometry("600x800")
root.resizable(False,False)
root.grab_set()
root.focus()
cargar_imagenes()

bg_label_main = tk.Label(root, image=img_fondo_main)
bg_label_main.place(x= 0, y=0)

"""

░██████╗░░█████╗░███╗░░░███╗███████╗  ██╗░░░░░░█████╗░░██████╗░██╗░█████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░░░░██║░░██║██║░░██╗░██║██║░░╚═╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░░░░██║░░██║██║░░╚██╗██║██║░░██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ███████╗╚█████╔╝╚██████╔╝██║╚█████╔╝
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚══════╝░╚════╝░░╚═════╝░╚═╝░╚════╝░
"""


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
    canvas.delete("all")
    canvas.create_image(0, 0, image=img_fondo_canvas, anchor=tk.NW)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            x1 = j * TAM
            y1 = i * TAM
            valor = matriz[i][j]

            if valor == 1:
                canvas.create_image(x1, y1, anchor="nw", image=img_bloque)
            elif valor == 2:
                canvas.create_image(x1, y1, anchor="nw", image=img_escalera)
            elif valor == 3:
                canvas.create_image(x1, y1, anchor="nw", image=img_obstaculo)
            elif valor == 4:
                canvas.create_image(x1, y1, anchor="nw", image=img_enemigo)
            elif valor == 5:
                canvas.create_image(x1, y1, anchor="nw", image=img_pescado)

    dibujar_player() #Dibuja al player de una vez
    dibujar_enemigos()

    #Actualizamos los labels
    player_hp_label.config(text=f"Vidas : {player_hp}")
    player_casillas_restantes_label.config(text=f"Energia : {player_casillas_restantes}")
    player_objetivos_label.config(text=f"Objetos por recolectar : {objetos_a_recolectar}")
    calculo_puntos_continuo() #Esta funcion hara el calculo y refrescara el label

#Dibujar al jugador
def dibujar_player():
    global letra, facing_right, img_gato_izq, img_gato_der
    x1 = player_col * TAM 
    y1 = player_fila * TAM 
    if facing_right:
        img = img_gato_der
    else:
        img = img_gato_izq
    canvas.create_image(x1, y1, anchor="nw", image=img)

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
    global filas_balas_canon, cols_balas_canon, img_enemigo
    for i in range(len(filas_balas_canon)): #ambas tendran el mismo largo  
        x1 = cols_balas_canon[i] * TAM 
        y1 = filas_balas_canon[i] * TAM 
        canvas.create_image(x1, y1, anchor="nw", image=img_enemigo)


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
            if event.keysym != "space":
                player_casillas_restantes -= 1
        comprobacion_ganar_perder() #Al moverse, comprobar si perdimos o ganamos ok

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
        if matriz[fila + 1 ][col] == 0 or matriz[fila +1][col] == 3 or matriz[fila +1][col] == 6 or matriz[fila +1][col] == 5: 
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
            if not((filas_balas_canon[i] == player_fila +1) and (cols_balas_canon[i] == player_col)):#Si el player no tiene algo por debajo, mantengalo
                filas_a_mantener.append(filas_balas_canon[i]) #no se elimina el enemigo
                cols_a_mantener.append(cols_balas_canon[i])
                direccion_a_mantener.append(direccion_balas_canon[i])
            elif salto_garantizado == 0 and salto_extendido == 0: #Si tiene algo por debajo, eliminelo
                matriz[player_fila + 1][player_col] = 0
                is_jumping =True  
                salto_garantizado = 2 #Pequeño salto al chocar
                player_casillas_restantes += 10 #Cada enemigo eliminado nos da 10 casillas más
                player_puntos += 25 #Dar veinticinco puntos cada vez que eliminamos un enemigo\
            else :
                filas_a_mantener.append(filas_balas_canon[i]) #no se elimina el enemigo
                cols_a_mantener.append(cols_balas_canon[i])
                direccion_a_mantener.append(direccion_balas_canon[i]) #Mantener, estamos subiendo
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
    global player_hp, objetos_a_recolectar , paused_game, player_casillas_restantes, player_puntos_finales, player_puntos
    eliminar_enemigo()
    if hay_colision_enemigos():
        player_hp -= 1 # Si tenemos una colision, perdemos puntos
        if player_hp == 0: #Si nos quedamos sin vidas o sin energia :(
            ventana_actual.after(1, perdiste) # Asegurarnos de que game loop no se ejecte mientras cambiamos de ventana
            reset_game()
            return
        else:
            paused_game = True
            reset_game()
            
    elif player_casillas_restantes <= 0:
        if objetos_a_recolectar == 0: #Que nos quedamos sin energia pero llegamos a la meta
            reset_game() # por si quiere volver a intentarlo
            ventana_actual.after(1, victoria)
            return
        else: 
            player_hp -= 1
            reset_game()
            if player_hp == 0:
                ventana_actual.after(1, perdiste) # Asegurarnos de que game loop no se ejecte mientras cambiamos de ventana
                reset_game()
    
        
    elif hay_colision_objetivo(): #Si compartimos ubicacion con el objetivo
        objetos_a_recolectar -= 1
        matriz[player_fila][player_col] = 0 #eliminamos el objetivo a recolectar
        if objetos_a_recolectar == 0:
            player_puntos_finales = player_puntos
            reset_game() # por si quiere volver a intentarlo
            ventana_actual.after(1, victoria)
            return 

def victoria():
    pygame.mixer.music.load(canciones[3])
    pygame.mixer.music.play(-1)
    global ganar, ventana_actual, juego_activo, player_puntos_finales, puntos_finales, mapa_actual
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

    #Bg 
    bg_label = tk.Label(ventana_actual, image=img_fondo_victoria)
    bg_label.place(x=0, y=0)
    #Widgets 
    if mapa_actual == "Predeterminado":
        ganaste_boton = tk.Button(ventana_actual, text="Regresar al Menú Principal", command=lambda: finalizar_juego())
        ganaste_boton.place(relx = 0.5, rely = 0.535,anchor="center")

    reintentar_default_boton = tk.Button(ventana_actual, text="Reintentar", command=lambda:reintentar())
    reintentar_default_boton.place(relx = 0.5, rely = 0.57,anchor="center")
    ganaste_puntos_label = tk.Label(ventana_actual, text=f"Puntos Obtenidos: {player_puntos_finales}")
    ganaste_puntos_label.place(relx=0.5, rely=0.7, anchor="center")
    mapa_actual_label = tk.Label(ventana_actual, text=f"Has ganado en el mapa: {mapa_actual}")
    mapa_actual_label.place(relx= 0.5, rely= 0.65, anchor="center")
    boton_musica = tk.Button(ventana_actual, text="Música", command=lambda: toggle_musica())
    boton_musica.place(relx=0.5, rely=0.9, anchor="center")

    if verificar_top5(): #Si el puntaje actual es posible highscore, todo bien
        escribir_high_score = tk.Button(ventana_actual, text="¿Guardar HighScore?", command=lambda: pantalla_escritura_highscore())
        escribir_high_score.place(relx = 0.5, rely= 0.2, anchor="center")
  
    if mapa_actual == "Constructor":
        volver_constructor_boton = tk.Button(ventana_actual, text="Volver al Constructor", command=lambda: volver_al_constructor())
        volver_constructor_boton.place(relx = 0.5, rely = 0.538,anchor="center")
        guardar_1 = tk.Button(ventana_actual, text="Guardar en Slot 1", command=lambda: guardar_nivel(1))
        guardar_1.place(relx= 0.25, rely= 0.78, anchor="center")
        guardar_2 = tk.Button(ventana_actual, text="Guardar en Slot 2", command=lambda: guardar_nivel(2))
        guardar_2.place(relx= 0.5, rely =0.78, anchor="center")
        guardar_3 = tk.Button(ventana_actual, text="Guardar en Slot 3", command=lambda: guardar_nivel(3))
        guardar_3.place(relx= 0.75, rely =0.78, anchor="center")
    
    ventana_actual.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

def perdiste():
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

    #Bg
    bg_label = tk.Label(ventana_actual, image=img_fondo_derrota)
    bg_label.place(x=0, y=0)

    #Widgets
    pygame.mixer.music.load(canciones[4])
    pygame.mixer.music.play(-1)
    if mapa_actual == "Predeterminado":
        perdiste_boton = tk.Button(ventana_actual, text="Regresar al Menú Principal", command=lambda: finalizar_juego())
        perdiste_boton.place(relx = 0.5, rely = 0.53,anchor="center")
    reintentar_default_boton = tk.Button(ventana_actual, text="Reintentar", command=lambda:reintentar())
    reintentar_default_boton.place(relx=0.5 , rely=0.7, anchor="center")
    perdiste_puntos_label = tk.Label(ventana_actual, text="No obtuviste ningun punto")
    perdiste_puntos_label.place(relx=0.5, rely=0.65, anchor="center")
    mapa_actual_label = tk.Label(ventana_actual, text=f"Has perdido en el mapa : {mapa_actual}")
    mapa_actual_label.place(relx= 0.5, rely= 0.6, anchor="center")
    ventana_actual.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    boton_musica = tk.Button(ventana_actual, text="Música", command=lambda: toggle_musica())
    boton_musica.place(relx=0.5, rely=0.8, anchor="center")
    if mapa_actual == "Constructor":
        volver_constructor_boton = tk.Button(ventana_actual, text="Volver al Constructor", command=lambda: volver_al_constructor())
        volver_constructor_boton.place(relx = 0.5, rely = 0.55,anchor="center")

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
    comprobacion_ganar_perder() #Si se mueven volver a comprobar, para evitar bugs
    tick_enemigos += 1
    if tick_enemigos >= tick_limite: #Basicamente, tiene que actualizarse la gravedad 3 veces para que los enemigos se empiezen a mover, esto lo hize porque son muy rapidos
        mover_balas_canon()
        tick_enemigos = 0
        comprobacion_ganar_perder() #Si se mueven volver a comprobar, para evitar bugs
    dibujar_mapa() # Dibujar de ultimo, primero refrescar 

"""
██╗░░██╗██╗░██████╗░██╗░░██╗░░░░░░░██████╗░█████╗░░█████╗░██████╗░███████╗░██████╗
██║░░██║██║██╔════╝░██║░░██║░░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██║██║░░██╗░███████║█████╗╚█████╗░██║░░╚═╝██║░░██║██████╔╝█████╗░░╚█████╗░
██╔══██║██║██║░░╚██╗██╔══██║╚════╝░╚═══██╗██║░░██╗██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
██║░░██║██║╚██████╔╝██║░░██║░░░░░░██████╔╝╚█████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░░░░╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
"""
def pantalla_escritura_highscore():
    global juego_activo, ventana_actual, nuevo_nombre, mapa_actual, digitar_nombre
    juego_activo = False
    ventana_actual.destroy()
    highscore_pantalla = tk.Toplevel()
    ventana_actual = highscore_pantalla
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()

    #Config de la ventana : 
    ventana_actual.title("Guardar_HighScore -- GatoAventuras")
    ventana_actual.geometry("600x200")


    #Widgets 
    digitar_nombre = tk.Entry(ventana_actual)
    digitar_nombre.config(font=("Arial, 14"), justify="center")
    digitar_nombre.pack()
    digitar_nombre.insert(0,"Inserte su nombre")

    boton_confirmar_nombre = tk.Button(ventana_actual, text="Confirmar Nombre", command=lambda: verificar_nombre())
    boton_confirmar_nombre.pack() 

    boton_submit_highscore = tk.Button(ventana_actual, text="Guardar HighScore", command=lambda: agregar_score())
    boton_submit_highscore.pack()
    ventana_actual.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

def show_highscores():
    global juego_activo, ventana_actual, saved_highscores
    juego_activo = False
    show_highscore_pantalla = tk.Toplevel()
    ventana_actual = show_highscore_pantalla
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()
     
    #Config de la ventana : 
    ventana_actual.title("HighScores -- GatoAventuras")
    ventana_actual.geometry("600x800")

    try:
        for i in range(len(saved_highscores)):
            datos = saved_highscores[i]
            texto = f"{i+1}. {datos[0]} — {datos[1]} pts — {datos[2]}"
            label = tk.Label(ventana_actual, text=texto, font=("Arial", 12))
            label.pack()
    except:
        no_hay_hs =tk.Label(ventana_actual, text="No hay puntajes guardados :(")
        no_hay_hs.pack()

    cerrar_ventana = tk.Button(ventana_actual, text="Cerrar", command=lambda: ventana_actual.destroy())
    cerrar_ventana.pack(pady=10)
    

def verificar_nombre():
    global nombre_nuevo, digitar_nombre 
    nombre_nuevo = digitar_nombre.get()
    if "/" in nombre_nuevo or nombre_nuevo == "" or nombre_nuevo == "Inserte su nombre" or nombre_nuevo == "Digite un nombre válido":
        nombre_nuevo = "Digite un nombre válido"
        return nombre_nuevo 
    else :
        nombre_nuevo = nombre_nuevo
        return nombre_nuevo 
    
def verificar_top5():
    global saved_puntos, player_puntos_finales
    if len(saved_puntos) < 5: #Hay campo libre
        return True
    if player_puntos_finales > min(saved_puntos):
        return True  #Supera al puntaje minimo y luego tenemos que ver en que posicion escalo
    return False #No alcanzo 

def agregar_score():
    global ventana_actual, saved_puntos, player_puntos_finales, saved_highscores, mapa_actual, nuevo_nombre, digitar_nombre
    nuevo_nombre = digitar_nombre.get()
    ventana_actual.destroy() #destruimos el toplevel
    if len(saved_puntos) < 5: #entra de una
        saved_puntos.append(player_puntos_finales)
        saved_puntos = sorted(saved_puntos, reverse=True) #orden reverso sera de mayor a menor
        saved_highscores.append([nuevo_nombre, player_puntos_finales, mapa_actual])
        saved_highscores = sorted(saved_highscores, key= lambda x: int(x[1]), reverse=True)
    else : #Si tenemos los cinco espacios ocupados
        punto_a_eliminar = min(saved_puntos)#eliminamos el punto minimo
        index_a_eliminar = 0
        for i in range(len(saved_puntos)):
            if saved_highscores[i][1] == punto_a_eliminar:
                index_a_eliminar = i
                break
        
            # eliminar datos
        saved_puntos.pop(index_a_eliminar) #Usan el mismo ya que ambas comparten el mismo orden
        saved_highscores.pop(index_a_eliminar)  

        #Agregar nuevos datos 
        saved_puntos.append(player_puntos_finales)
        saved_puntos = sorted(saved_puntos, reverse=True) #orden reverso sera de mayor a menor
        saved_highscores.append([nuevo_nombre, player_puntos_finales, mapa_actual])
        saved_highscores = sorted(saved_highscores, key= lambda x: int(x[1]), reverse=True) # El key es en base a que, entonces llamamos una funcion lambda, que recorrera dentro de la matriz, la posicion 1, que son los datos
    
    escritura_highscores()
    mapa_actual = "" #Vamos a regresar al main menu

def escritura_highscores():
    global saved_highscores
    file = open("high_scores.txt", "w") # No lo vaciamos, ya que "w" se encarga de eso por nosotros
    for i in saved_highscores:
        file.write(f"{i[0]},{i[1]},{i[2]}\n") #f string, el {} es donde va el texto, lo demas es ttexto
    file.close()


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
    global matriz, casillas_reset, inicio_fila, inicio_col, matriz_original, filas_a_mantener, cols_a_mantener, direccion_a_mantener, player_fila, matriz, matriz_original, player_col, facing_right, objetos_a_recolectar, is_dashing, dash_restante, is_jumping, salto_extendido, salto_garantizado, paused_game, player_casillas_restantes, filas_balas_canon, cols_balas_canon, direccion_balas_canon
    matriz = copy.deepcopy(matriz_original)
    player_fila = inicio_fila
    player_col = inicio_col
    facing_right = True
    is_dashing = False
    dash_restante = 0
    is_jumping = False
    salto_garantizado = 0
    salto_extendido = 0
    player_casillas_restantes = casillas_reset 
    filas_balas_canon = [] 
    cols_balas_canon = []
    objetos_a_recolectar = 0
    direccion_balas_canon = []
    paused_game = False
    player_casillas_restantes = casillas_reset # Reworkear esto para futuro "Numero de Casillas"
    filas_a_mantener = []
    cols_a_mantener = []
    direccion_a_mantener = []
   
    #Llamar funciones
    encontrar_objetivos()
    encontrar_enemigos()
    dibujar_mapa()
    calculo_puntos_base()

def reintentar():
    global ventana_actual, objetos_a_recolectar, mapa_actual
    ventana_actual.destroy()
    objetos_a_recolectar = 0
    if mapa_actual == "Constructor":
        iniciar_juego_constructor()
    else: 
        iniciar_juego_default()

def finalizar_juego(): #salirnos del Juego
    pygame.mixer.music.load(canciones[0])
    pygame.mixer.music.play(-1)
    global player_hp, player_casillas_restantes, ventana_actual, objetos_a_recolectar, mapa_actual 
    player_hp = 3
    player_casillas_restantes = 90
    objetos_a_recolectar = 0
    if mapa_actual == "Constructor":
            limpiar_matriz_constructor()
    ventana_actual.destroy()

"""

▒█▄░▒█ ▀█▀ ▀█░█▀ █▀▀ █░░ 　 ▒█▀▀▄ █▀▀ █▀▀ █▀▀█ █░░█ █░░ ▀▀█▀▀ 
▒█▒█▒█ ▒█░ ░█▄█░ █▀▀ █░░ 　 ▒█░▒█ █▀▀ █▀▀ █▄▄█ █░░█ █░░ ░░█░░ 
▒█░░▀█ ▄█▄ ░░▀░░ ▀▀▀ ▀▀▀ 　 ▒█▄▄▀ ▀▀▀ ▀░░ ▀░░▀ ░▀▀▀ ▀▀▀ ░░▀░░
"""
def iniciar_juego_default():
    pygame.mixer.music.load(canciones[1])
    pygame.mixer.music.play(-1)
    global objetos_a_recolectar, filas_balas_canon, cols_balas_canon, direccion_balas_canon, inicio_col, inicio_fila, casillas_reset, mapa_actual, player_fila, player_col, matriz, matriz_default, matriz_original, mapa_actual, juego_activo, player_hp_label, player_puntos_label, player_casillas_restantes_label, player_objetivos_label, player_hp, player_casillas_restantes
    #Primero creamos un TopLevel
    global canvas, default_game 
    global ventana_actual
    default_game = tk.Toplevel()
    ventana_actual = default_game
    ventana_actual.title("Juego_Default!")
    ventana_actual.geometry("1700x900")
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()
    juego_activo = True
    #Bg Label 
    bg_label = tk.Label(ventana_actual, image=img_fondo_juego)
    bg_label.place(x=0,y=0)
    #Empezar cambiando la matriz a usar
    matriz = copy.deepcopy(matriz_default)
    matriz_original = copy.deepcopy(matriz_original_default)
    #Definir la posicion del jugador 
    player_fila = len(matriz) -1 
    player_col = 0
    inicio_fila = len(matriz) -1
    inicio_col = 0

    #Asegurarnos de que para el default si existan suficientes movimientos
    player_hp = 3
    player_casillas_restantes = 90
    casillas_reset = 90
    objetos_a_recolectar = 0 # Evitar bugs al reentrar a la ventana
    mapa_actual = "Predeterminado" #Esto nos servira para la escritura de highscores

    #Hacemos que la ventana actual sea la que se esta usando para poder tener la logica para el constructor de mapas

    #Creamos el Canvas
    canvas = tk.Canvas(
    ventana_actual, 
    width=len(matriz[0]) * TAM, #Se hace el canvas en base al tamaño de la matriz
    height=len(matriz) * TAM, 
    )
    canvas.place(relx= 0.03, anchor="nw")

    
    #Key Binds del game
    ventana_actual.bind("<KeyPress>", presionar_tecla)
    ventana_actual.bind("<KeyRelease>", soltar_tecla)

    filas_balas_canon = []
    cols_balas_canon = []
    direccion_balas_canon = []
    #Poblar lista de enemigos
    encontrar_enemigos()
    #Definir cuantos enemigos tenemos que encontrar
    encontrar_objetivos()
    #Definir puntos iniciales
    calculo_puntos_base()

    boton_musica = tk.Button(ventana_actual, text="Música", command=lambda: toggle_musica())
    boton_musica.place(relx=0.35, rely=0.95)
    
    # Crear botones y elementos
    fin_juego = tk.Button(ventana_actual, text="Salir a menú principal", command= lambda: finalizar_juego())
    fin_juego.place(relx=0.45, rely=0.95)

    #Creamos labels para mostrar la informacion 
    player_hp_label = tk.Label(ventana_actual, text=f"Vidas : {player_hp}", relief="groove")
    player_hp_label.place(relx= 0.1, rely = 0.9)
    
    player_casillas_restantes_label = tk.Label(ventana_actual, text=f"Energia : {player_casillas_restantes}", relief= "groove")
    player_casillas_restantes_label.place(relx = 0.3, rely = 0.9)

    player_puntos_label = tk.Label(ventana_actual, text=f"Puntos : {player_puntos}", relief="groove")
    player_puntos_label.place(relx= 0.5 , rely =0.9)
    
    player_objetivos_label = tk.Label(ventana_actual, text=f"Objetos por recolectar : {objetos_a_recolectar}", relief= "groove")
    player_objetivos_label.place(relx = 0.7, rely= 0.9)

    ventana_actual.protocol("WM_DELETE_WINDOW", lambda: root.destroy())


    #Llamar al loop del juego
    dibujar_mapa()

    game_loop() 


"""

░█████╗░░█████╗░███╗░░██╗░██████╗████████╗██████╗░██╗░░░██╗░█████╗░████████╗░█████╗░██████╗░  ██████╗░███████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░░░░██║░░░██████╔╝██║░░░██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝  ██║░░██║█████╗░░
██║░░██╗██║░░██║██║╚████║░╚═══██╗░░░██║░░░██╔══██╗██║░░░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗  ██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚███║██████╔╝░░░██║░░░██║░░██║╚██████╔╝╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║  ██████╔╝███████╗
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝

███╗░░░███╗░█████╗░██████╗░░█████╗░░██████╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██╔████╔██║███████║██████╔╝███████║╚█████╗░
██║╚██╔╝██║██╔══██║██╔═══╝░██╔══██║░╚═══██╗
██║░╚═╝░██║██║░░██║██║░░░░░██║░░██║██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░
"""
def iniciar_creador_de_mapas():
    pygame.mixer.music.load(canciones[2])
    pygame.mixer.music.play(-1)
    global  mapa_actual, canvas, entry_cambiar_energia,constructor_mapas,vidas_constructor, casillas_restantes_constructor, constructor_fila, constructor_col, ventana_actual, label_puntos_creador, entry_cambiar_vida
    constructor_mapas = tk.Toplevel()
    ventana_actual = constructor_mapas
    ventana_actual.title("Constructor de Mapas")
    ventana_actual.geometry("1700x900")
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()
    mapa_actual = "Constructor"
    
    #Bg Label 
    bg_label = tk.Label(ventana_actual, image=img_fondo_juego)
    bg_label.place(x=-10,y=0)

    #Creamos el Canvas
    canvas = tk.Canvas(
    ventana_actual, 
    width=len(matriz_constructor[0]) * TAM, #Se hace el canvas en base al tamaño de la matriz
    height=len(matriz_constructor) * TAM 
    )
    canvas.place(relx= 0.05, anchor="nw")

    #Luego de esto creamos los botones para cambiar las posiciones!!!
    poner_vacio = tk.Button(ventana_actual, text="Vacio", command=lambda: cambiar_bloque(0))
    poner_vacio.place(relx=0.0, rely=0.1)
    poner_bloque = tk.Button(ventana_actual, image=img_bloque, command=lambda: cambiar_bloque(1))
    poner_bloque.place(relx=0.0, rely=0.2)
    poner_escalera = tk.Button(ventana_actual, image=img_escalera, command=lambda: cambiar_bloque(2))
    poner_escalera.place(relx=0.0, rely=0.3)
    poner_trampa = tk.Button(ventana_actual, image=img_obstaculo, command=lambda: cambiar_bloque(3))
    poner_trampa.place(relx=0.0, rely=0.4)
    poner_enemigo = tk.Button(ventana_actual, image=img_enemigo, command=lambda: cambiar_bloque(4))
    poner_enemigo.place(relx=0.0, rely=0.5)
    poner_objetivo = tk.Button(ventana_actual, image=img_pescado, command=lambda: cambiar_bloque(5))
    poner_objetivo.place(relx=0.0, rely=0.6)
    poner_inicio = tk.Button(ventana_actual, text="Punto Inicio", command=lambda: cambiar_bloque(6))
    poner_inicio.place(relx=0.0, rely=0.7)
    borrar_todos = tk.Button(ventana_actual, text="Borrar Todo", command= lambda: limpiar_matriz_constructor())
    borrar_todos.place(relx=0.0, rely=0.8)
    
    boton_musica = tk.Button(ventana_actual, text="Música", command=lambda: toggle_musica())
    boton_musica.place(relx=0.28, rely=0.9)
    
    #Label que nos calcula los puntos del nivel 
    label_puntos_creador = tk.Label(ventana_actual, text="Aqui veras los puntos del mapa!")
    label_puntos_creador.place(relx =0.0, rely=0.9)

    #Entries para cambiar la vida y casillas
    entry_cambiar_vida = tk.Entry(ventana_actual)
    entry_cambiar_vida.config(font=("Arial, 14"), justify="center")
    entry_cambiar_vida.place(relx =0.5, rely = 0.9)
    entry_cambiar_vida.insert(0,f"Define Vidas, Actuales {vidas_constructor}")
    boton_cambiar_vida = tk.Button(ventana_actual, text="Vidas", command=lambda: config_vida())

    boton_cambiar_vida.place(relx=0.47, rely=0.9)

    entry_cambiar_energia = tk.Entry(ventana_actual)
    entry_cambiar_energia.config(font=("Arial, 14"), justify="center")
    entry_cambiar_energia.insert(0,f"Define Energia, Actual {casillas_restantes_constructor}")
    boton_cambiar_energia = tk.Button(ventana_actual, text= "Energia", command=lambda: config_energia())
    entry_cambiar_energia.place(relx=0.7, rely=0.9)
    boton_cambiar_energia.place(relx=0.66, rely=0.9)

    #Boton para empezar a jugar!!
    empezar_a_jugar = tk.Button(ventana_actual, text="Empezar a Jugar!!", command=lambda: jugar_el_nivel())
    empezar_a_jugar.place(relx= 0.14, rely=0.9)

    #Cargar mapas
    cargar_1 = tk.Button(ventana_actual, text="Cargar Slot 1", command=lambda: cargar_nivel(1))
    cargar_1.place(relx=0.07,rely=0.95, anchor="center")
    cargar_2 = tk.Button(ventana_actual, text="Cargar Slot 2", command=lambda: cargar_nivel(2))
    cargar_2.place(relx=0.14,rely=0.95, anchor="center")
    cargar_3 = tk.Button(ventana_actual, text="Cargar Slot 3", command=lambda: cargar_nivel(3))
    cargar_3.place(relx=0.21,rely=0.95, anchor="center")

    #Boton salir del constructor :(
    salir_constructor_boton = tk.Button(ventana_actual, text="Salir sin guardar", command=lambda: salir_constructor())
    salir_constructor_boton.place(relx =0.21, rely=0.9)
    ventana_actual.bind("<KeyPress>", mover_constructor)
    dibujar_mapa_constructor()
    ventana_actual.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

#Se ocupa definir un nuevo dibujo de mapas y nuevo movimiento
"""

▒█▀▀█ █▀▀█ █▀▀▄ ▀█░█▀ █▀▀█ █▀▀ ░░ █▀▀ █▀▀█ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀█ █░░█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 
▒█░░░ █▄▄█ █░░█ ░█▄█░ █▄▄█ ▀▀█ ▀▀ █░░ █░░█ █░░█ ▀▀█ ░░█░░ █▄▄▀ █░░█ █░░ ░░█░░ █░░█ █▄▄▀ 
▒█▄▄█ ▀░░▀ ▀░░▀ ░░▀░░ ▀░░▀ ▀▀▀ ░░ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ░▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀▀ ▀░▀▀
"""
def dibujar_mapa_constructor():
        global puntos_constructor, label_puntos_creador
        canvas.delete("all")
        canvas.create_image(0, 0, image=img_fondo_canvas, anchor=tk.NW)
        #recorremos la matriz para pinta cada 0,1,2 o 3
        for fila in range(len(matriz_constructor)):
                for col in range (len(matriz_constructor[fila])):
                        x1 = col * TAM          #0
                        y1 = fila * TAM         #0
                        x2 = x1 + TAM           #40
                        y2 = y1 + TAM           #40

                        #obtenemos el valor de la celda 0,1,2,3
                        
                        valor = matriz_constructor[fila][col]
                        color = ""
                        
                        if valor == 0:
                            canvas.create_rectangle(x1,y1,x2,y2, fill=color, outline = "black")
                        elif valor == 1:   # bloque por donde camina
                                canvas.create_image(x1, y1, anchor="nw", image=img_bloque)
                        elif valor == 2: #escalera
                                canvas.create_image(x1, y1, anchor="nw", image=img_escalera)
                        elif valor == 3: #bloque
                                canvas.create_image(x1, y1, anchor="nw", image=img_obstaculo)
                        elif valor == 4:
                                canvas.create_image(x1, y1, anchor="nw", image=img_enemigo)
                        elif valor == 5:
                                  canvas.create_image(x1, y1, anchor="nw", image=img_pescado)
                    
                        if valor == 6:
                             x1 = col * TAM + 5
                             y1 = fila * TAM + 5
                             x2 = x1 + TAM - 10
                             y2 = y1 + TAM - 10
                             canvas.create_oval(x1, y1, x2, y2, fill="Cyan", outline = "black")
                             canvas.create_text(
                                    col * TAM + TAM/2,
                                    fila * TAM + TAM/2,
                                    text = "I",
                                    fill = "White",
                                    font = ("Arial", 16, "bold")
                                    )
        dibujar_constructor()

def dibujar_constructor():
        x1 = constructor_col * TAM + 5
        y1 = constructor_fila * TAM + 5
        x2 = x1 + TAM - 10
        y2 = y1 + TAM - 10

        canvas.create_oval(x1,y1,x2,y2, fill="orange", outline = "black")
        canvas.create_text(
                constructor_col * TAM + TAM/2,
                constructor_fila * TAM + TAM/2,
                text = "C",
                fill = "white",
                font = ("Arial", 16, "bold")
        )


"""
█▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ ░░ █▀▀█ █░░█ ░▀░ ▀▀█▀▀ █▀▀█ █▀▀█ ░░ █▀▀▄ █░░ █▀▀█ █▀▀█ █░░█ █▀▀ █▀▀ 
█░░█ █░░█ █░░█ █▀▀ █▄▄▀ ▀▀ █░░█ █░░█ ▀█▀ ░░█░░ █▄▄█ █▄▄▀ ▀▀ █▀▀▄ █░░ █░░█ █░░█ █░░█ █▀▀ ▀▀█ 
█▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ░░ ▀▀▀█ ░▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ ▀░▀▀ ░░ ▀▀▀░ ▀▀▀ ▀▀▀▀ ▀▀▀█ ░▀▀▀ ▀▀▀ ▀▀▀
"""

def cambiar_bloque(id): #Le ponemos un ID que sera el bloque que queremos construir.
    global canvas, matriz_constructor, constructor_col, constructor_fila, puntos_constructor, label_puntos_creador
    if id == 6:
        if hay_punto_de_inicio(): #Evitar que se repitan
            eliminar_punto_de_inicio()
            poner_punto_de_inicio()
        else:
            poner_punto_de_inicio()

    else :
        matriz_constructor[constructor_fila][constructor_col] = id 
        if id == 1 or id == 2:
            puntos_constructor -= 2
        elif id == 3:
            puntos_constructor += 20
        elif id == 4:
            puntos_constructor += 50
    
    label_puntos_creador.config(text=f"Puntos Minimos : {puntos_constructor + 1*30}")

    dibujar_mapa_constructor()

def hay_punto_de_inicio(): #Ver si ya hay punto de inicio
    for i in range(len(matriz_constructor)):
        for j in range(len(matriz_constructor[0])):
            if matriz_constructor[i][j] == 6:
                return True
    return False

def eliminar_punto_de_inicio(): 
    global matriz_constructor
    for i in range(len(matriz_constructor)):
            for j in range(len(matriz_constructor[0])):
                if matriz_constructor[i][j] == 6:
                    matriz_constructor[i][j] = 0
                    return #Terminar el ciclado!! 
                    
def poner_punto_de_inicio():
    global matriz_constructor, constructor_col, constructor_fila   
    matriz_constructor[constructor_fila][constructor_col] = 6

def limpiar_matriz_constructor():
    global matriz_constructor, label_puntos_creador, puntos_constructor
    for i in range(len(matriz_constructor)):
        for j in range(len(matriz_constructor[0])):
            matriz_constructor[i][j] = 0
    puntos_constructor = 0 #Reseteamos los puntos
    dibujar_mapa_constructor()


"""
Configurar Vidas y Casillas
"""

def config_vida():
    global entry_cambiar_vida, vidas_constructor, label_puntos_creador #Esto nos sirve para hacer get
    try :
        vidas_constructor = int(entry_cambiar_vida.get())
        if vidas_constructor > 0:
            label_puntos_creador.config(text =f"Haz cambiado las vidas a {vidas_constructor}")
        else :
            vidas_constructor = 3
            label_puntos_creador.config(text =f"Valor no válido en vidas, cambiadas a {vidas_constructor}")
    except :
        vidas_constructor = 3
        label_puntos_creador.config(text =f"Valor no válido en vidas, cambiadas a {vidas_constructor}")

def config_energia():
    global entry_cambiar_energia, casillas_restantes_constructor, label_puntos_creador, puntos_creador#Esto nos sirve para hacer get
    try :
        casillas_restantes_constructor = int(entry_cambiar_energia.get())
        if casillas_restantes_constructor > 0:
            label_puntos_creador.config(text =f"Haz cambiado la energia a {casillas_restantes_constructor}, los puntos")
        else:
            casillas_restantes_constructor = 90
            label_puntos_creador.config(text =f"Valor no válido en energia, cambiada a {casillas_restantes_constructor}")
    except :
        casillas_restantes_constructor = 90
        label_puntos_creador.config(text =f"Valor no válido en energia, cambiada a {casillas_restantes_constructor}")
        

"""
▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀█ █░░█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ ░░ █▀▄▀█ █▀▀█ ▀█░█▀ █▀▀ █▀▀█ 
▒█░░░ █░░█ █░░█ ▀▀█ ░░█░░ █▄▄▀ █░░█ █░░ ░░█░░ █░░█ █▄▄▀ ▀▀ █░▀░█ █░░█ ░█▄█░ █▀▀ █▄▄▀ 
▒█▄▄█ ▀▀▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ░▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀▀ ▀░▀▀ ░░ ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀
"""


def mover_constructor (event):
        global constructor_fila, constructor_col   #indicarle al def que use las variables globales
        if isinstance(event.widget, tk.Entry):
            return

        nueva_fila = constructor_fila
        nueva_col =  constructor_col

        if event.keysym == "a":
                nueva_col -= 1
        elif event.keysym == "d":
                nueva_col += 1
        elif event.keysym == "w":
                nueva_fila -= 1
        elif event.keysym == "s":
                nueva_fila += 1
        else:
                return

        if puede_moverse_constructor(nueva_fila, nueva_col):
                constructor_fila = nueva_fila
                constructor_col =  nueva_col
        
        dibujar_mapa_constructor()

def puede_moverse_constructor (fila, col):
        #si se sale del borde superior o inferior
        if fila < 0 or fila >= len(matriz_constructor):
                return False
        #si se sale de bordes derecho o izquierdo
        if col < 0 or col >= len(matriz_constructor[0]):
                return False
        return True

"""

▒█░░▒█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█▀▀▀█ ░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▄░▒█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀█ ▒█░▒█ ▒█▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█ 
░▒█▒█░ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▀▀▀▄▄ ▀▀ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄▀ ▒█░▒█ ▒█░░░ ░▒█░░ ▒█░░▒█ ▒█▄▄▀ 
░░▀▄▀░ ▒█▄▄▄ ▒█░░▀█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█░▒█ ▒█▄▄▄█ ░░ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▀█ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ░▀▄▄▀ ▒█▄▄█ ░▒█░░ ▒█▄▄▄█ ▒█░▒█
"""
def salir_constructor():
    global vidas_constructor, casillas_restantes_constructor, puntos_constructor
    limpiar_matriz_constructor()
    vidas_constructor = 3
    casillas_restantes_constructor = 90
    puntos_constructor = 0
    ventana_actual.destroy()
    pygame.mixer.music.load(canciones[0])
    pygame.mixer.music.play(-1)

def volver_al_constructor():
    global juego_activo
    juego_activo = False
    ventana_actual.destroy()
    iniciar_creador_de_mapas()
"""
Guardar/Cargar Nivel
"""

def cargar_nivel(slot):
    global matriz_constructor 
    matriz_constructor = []
    if slot == 1:
        file = open("nivel1.txt", "r")
    elif slot == 2:
        file = open("nivel2.txt", "r")
    elif slot == 3:
        file = open("nivel3.txt", "r")
    
    try :
        for fila in file:
            datos = fila.strip().split(",") #Se cargan los datos
            fila = [int(x) for x in datos] # Expresion generadora
            matriz_constructor.append(fila)
        file.close()
        dibujar_mapa_constructor()
    except :
        pass 

def guardar_nivel(slot):
    global matriz_original
    if slot == 1:
        file = open("nivel1.txt", "w")
    elif slot == 2:
        file = open("nivel2.txt", "w")
    elif slot == 3:
        file = open("nivel3.txt", "w")
    
    for fila in matriz_original:
        file.write(",".join([str(x) for x in fila]) + "\n")#Join junta todo en un solo elemento
    file.close()

"""

░░▀ █░░█ █▀▀▀ █▀▀█ █▀▀█ 　 █▀▀ █░░ 　 █▀▀▄ ░▀░ ▀█░█▀ █▀▀ █░░ 
░░█ █░░█ █░▀█ █▄▄█ █▄▄▀ 　 █▀▀ █░░ 　 █░░█ ▀█▀ ░█▄█░ █▀▀ █░░ 
█▄█ ░▀▀▀ ▀▀▀▀ ▀░░▀ ▀░▀▀ 　 ▀▀▀ ▀▀▀ 　 ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀
"""

def hay_objetivo():
    for i in range(len(matriz_constructor)):
        for j in range(len(matriz_constructor[0])):
            if matriz_constructor[i][j] == 5:
                return True #Solo tiene que haber un objetvio
    return False

def guardar_pos_inicio():
    global inicio_fila, inicio_col, matriz_constructor
    for i in range(len(matriz_constructor)):
        for j in range(len(matriz_constructor[0])):
            if matriz_constructor[i][j] == 6:
                inicio_col = j
                inicio_fila = i

def jugar_el_nivel(): #Tiene que validar que el nivel sea posible 
    global casillas_reset, label_puntos_creador, matriz, matriz_original, player_hp, player_casillas_restantes, vidas_constructor, casillas_restantes_constructor
    if not hay_objetivo():
        label_puntos_creador.config(text="No hay objetivo, el nivel NO es jugable :(")
        return
    elif not hay_punto_de_inicio():
        label_puntos_creador.config(text="No hay un punto de inicio, el nivel NO es jugable :(")
        return 
    else : # Se cumplen ambas condiciones
        guardar_pos_inicio()
        matriz_original = copy.deepcopy(matriz_constructor)
        matriz = copy.deepcopy(matriz_constructor)
        player_hp = vidas_constructor
        player_casillas_restantes = casillas_restantes_constructor
        ventana_actual.unbind("KeyPress")
        ventana_actual.destroy()
        casillas_reset = casillas_restantes_constructor
        iniciar_juego_constructor()
        
        
def iniciar_juego_constructor():
    pygame.mixer.music.load(canciones[1])
    pygame.mixer.music.play(-1)
    global objetos_a_recolectar, filas_balas_canon, cols_balas_canon,direccion_balas_canon,player_hp, inicio_fila, inicio_col, player_fila, player_col, matriz, matriz_default, matriz_original, mapa_actual, juego_activo, player_hp_label, player_puntos_label, player_casillas_restantes_label, player_objetivos_label, player_hp, player_casillas_restantes
    global canvas, constructor_game
    global ventana_actual
    #Primero creamos un TopLevel
    constructor_game = tk.Toplevel()
    ventana_actual = constructor_game 
    ventana_actual.title("Juego_Constructor")
    ventana_actual.geometry("1700x900")
    ventana_actual.resizable(False,False)
    ventana_actual.grab_set()
    ventana_actual.focus()
    juego_activo = True

    #Bg Label 
    bg_label = tk.Label(ventana_actual, image=img_fondo_juego)
    bg_label.place(x=-10,y=0)
    
    mapa_actual = "Constructor" #Esto nos servira para la escritura de highscores

    #Hacemos que la ventana actual sea la que se esta usando para poder tener la logica para el constructor de mapas
    player_fila = inicio_fila
    player_col = inicio_col 

    player_hp = vidas_constructor

    
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

    #Evitar bugs de enemigos repetidos
    filas_balas_canon = []
    cols_balas_canon = []
    direccion_balas_canon = []

    #Poblar lista de enemigos
    encontrar_enemigos()

    objetos_a_recolectar = 0 # Evitar bug
    #Definir cuantos objetivos tenemos que encontrar
    encontrar_objetivos()
    #Definir puntos iniciales
    calculo_puntos_base() 

    fin_juego = tk.Button(ventana_actual, text="Salir a menú principal", command= lambda: finalizar_juego())
    fin_juego.place(relx=0.45, rely=0.95)

    #Creamos labels para mostrar la informacion 
    global player_hp_label, player_casillas_restantes_label, player_puntos_label, player_objetivos_label
    player_hp_label = tk.Label(ventana_actual, text=f"Vidas : {player_hp}", relief="groove")
    player_hp_label.place(relx= 0.1, rely = 0.9)
    
    player_casillas_restantes_label = tk.Label(ventana_actual, text=f"Energia : {player_casillas_restantes}", relief= "groove")
    player_casillas_restantes_label.place(relx = 0.3, rely = 0.9)

    player_puntos_label = tk.Label(ventana_actual, text=f"Puntos : {player_puntos}", relief="groove")
    player_puntos_label.place(relx= 0.5 , rely =0.9)
    
    player_objetivos_label = tk.Label(ventana_actual, text=f"Objetos por recolectar : {objetos_a_recolectar}", relief= "groove")
    player_objetivos_label.place(relx = 0.7, rely= 0.9)

    boton_musica = tk.Button(ventana_actual, text="Música", command=lambda: toggle_musica())
    boton_musica.place(relx=0.35, rely=0.95)
    #Llamar a game loop!
    game_loop()

    ventana_actual.protocol("WM_DELETE_WINDOW", lambda: root.destroy())


#Main window
boton_inicio_juego = tk.Button(root, text="Iniciar Juego Predeterminado",command= lambda: iniciar_juego_default())
boton_inicio_juego.place(relx=0.5, rely=0.55, anchor='center')
boton_constructor_mapas = tk.Button(root, text="Iniciar Constructor de Mapas", command= lambda:iniciar_creador_de_mapas())
boton_constructor_mapas.place(relx=0.5, rely=0.6, anchor='center')
boton_high_scores = tk.Button(root, text="HighScores",command=lambda: show_highscores())
boton_high_scores.place(relx=0.5, rely=0.65, anchor='center')
boton_musica = tk.Button(root, text="Música", command=lambda: toggle_musica())
boton_musica.place(relx=0.5, rely=0.7, anchor='center')
boton_salir = tk.Button(root, text="Salir del Juego", command=lambda: root.destroy())
boton_salir.place(relx= 0.5, rely=0.75, anchor='center')

root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

#Main loop
root.mainloop()

