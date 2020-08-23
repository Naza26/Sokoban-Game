import soko
import gamelib
import math

PX_CELDA = 60

class PilaMovimiento:

    def __init__(self):
        self.items = []

    def esta_vacia(self):

        '''Devuelve True si la lista esta vacia, False en caso contrario'''

        return len(self.items) == 0

    def apilar(self, x):

        '''Apila el elemento x'''

        self.items.append(x)

    def desapilar(self):

        '''Devulve el elemento tope y lo elimina. Si la pila esta vacia levanta una excepcion'''

        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        else:
            return self.items.pop()


class ColaPista:

    """Representa a una cola, con operaciones de encolar y desencolar. 
    El primero en ser encolado es también el primero en ser desencolado."""


    def __init__(self):

        """Crea una cola vacía."""

        self.items = []

    def __repr__(self):
        return f"{self.items}"

    def encolar(self, x):

        """Agrega el elemento x como último de la cola."""

        self.items.append(x)

    def desencolar(self):

        """Desencola el primer elemento y devuelve su
        valor. Si la cola está vacía, levanta ValueError."""

        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self.items.pop(0)

    def esta_vacia(self):

        """Devuelve True si la cola esta vacía, False si no."""

        return len(self.items) == 0



def obtengo_coordenadas_soko(grilla):

    '''Esta funcion mappea coordenadas al soko'''

    pos_jugador = soko.encontrar_jugador(grilla)

    return {'NORTE': soko.NORTE, 'OESTE': soko.OESTE, 'ESTE': soko.ESTE, 'SUR': soko.SUR, 'REINICIAR': pos_jugador}

def controles(ruta, grilla):

    '''Esta funcion lee los controles del juego'''

    dic_teclas = {}
    lista_lineas = []
    coordenadas = obtengo_coordenadas_soko(grilla)

    with open("teclas.txt") as archivo_teclas:
        for linea in archivo_teclas:
            linea = linea.rstrip("\n")
            if linea.startswith(" "):
                archivo_teclas.next()
            else:
              lista_lineas.append(linea)
         
        for i in lista_lineas:
            separacion = i.split("=")
            tecla = separacion[0].rstrip()
            transformacion_coordenada_0 = coordenadas.get(separacion[0].strip(), separacion[0].rstrip())
            transformacion_coordenada_1 = coordenadas.get(separacion[-1].strip(), separacion[1].rstrip())

            dic_teclas[tecla] = dic_teclas.get(transformacion_coordenada_0, transformacion_coordenada_1)

    for tecla, coordenada in dic_teclas.items():
        if coordenada in coordenadas:
            dic_teclas[tecla] = coordenadas[coordenada]

    return dic_teclas


def coordenadas_teclas(tecla, grilla):

    '''Esta funcion recibe una tecla y mappea esa tecla a un valor en coordenadas x e y'''

    pos_jugador = soko.encontrar_jugador(grilla)

    dic_teclas = controles("teclas.txt", grilla)

    for t in dic_teclas:

        if t == tecla:
            return dic_teclas[t]


def dibujo_juego(grilla):

    '''Esta funcion recibe una grilla y dibuja el juego'''
 
    x_total, y_total = cargar_tamaño(grilla) #Tupla con el total de de px por pantalla

    x = 0

    y = 0

    casilleros_maximos_horizontales = y_total / PX_CELDA
    
    for fila in range(len(grilla)):
        for columna in range(int(casilleros_maximos_horizontales)+PX_CELDA):
            if columna  < len(grilla[fila]):
                gamelib.draw_image('img/ground.gif', x_total, y_total) 
                celda = grilla[fila][columna]
                if soko.hay_pared(grilla, columna, fila):
                    gamelib.draw_image('img/wall.gif', x, y)
                elif soko.hay_jugador(grilla, columna, fila):
                    gamelib.draw_image('img/player.gif', x, y)
                elif celda == " ":
                    gamelib.draw_image('img/ground.gif', x, y)
                elif soko.hay_caja(grilla, columna, fila):
                    gamelib.draw_image('img/box.gif', x, y)
                elif soko.hay_objetivo(grilla, columna, fila):
                    gamelib.draw_image('img/goal.gif', x, y)
            else:
                gamelib.draw_image('img/ground.gif', x, y)
            x = x + PX_CELDA
        x = 0
        y = y + PX_CELDA
 

def cargar_tamaño(grilla):

    '''Esta funcion recibe una grilla y devuelve el tamaño en px que esta ocupa'''
    
    len_maxima_fila = len(grilla[0])

    for i in range(0,len(grilla)):
        largo_fila = len(grilla[i])
        if largo_fila > len_maxima_fila:
            len_maxima_fila = largo_fila
    return (len_maxima_fila*PX_CELDA, (len(grilla)*PX_CELDA) - PX_CELDA) #Le resto 60px porque tengo una fila vacia que es la que me indica el cambio de linea



def leer_niveles(ruta):

    '''Esta funcion debe leer el archivo con los niveles y cargarlos en la memoria del programa. Esto debe ocurrir al comienzo del juego'''
    dic_niveles = {}

    with open("niveles.txt") as archivo_niveles:
        for linea in archivo_niveles:
            linea = linea.rstrip("\n")
            if linea.startswith("Level "):
                linea_nivel = linea
                linea_nivel_lista = linea_nivel.split(" ")
                linea_nivel_lista = int(linea_nivel_lista[-1]) 
                dic_niveles[linea_nivel_lista] = dic_niveles.get(linea_nivel_lista, [])
            elif linea.startswith("'"):
                next(archivo_niveles)
            else:
                if linea != " ":
                    dic_niveles[linea_nivel_lista].append(list(linea))
    return dic_niveles

dic_niveles = leer_niveles("niveles.txt")

def pasar_nivel(grilla, dic_niveles_grilla, nivel_inicial):

    '''Esta funcion recibe los niveles con sus respectivas grillas y si el nivel esta ganado, devuelve el nuevo nivel con su respectiva grilla.'''

    if soko.juego_ganado(grilla) and nivel_inicial <= len(dic_niveles_grilla):
        nivel_inicial += 1
        print(f"Usted avanzo al nivel {nivel_inicial}")
        return dic_niveles_grilla[nivel_inicial], nivel_inicial

    print(f"No paso de nivel, esta en el nivel {nivel_inicial}")    
    return grilla, nivel_inicial

def printgrilla(grilla):
    for linea in grilla:
        print(''.join(linea))

def convertir_a_inmutable(estado_grilla):

    '''Convierto mi lista de listas que representa mi grilla o tablero del juego en una cadena'''

    cadena = ''
    for fila in estado_grilla:
        cadena = cadena + ''.join(fila)
    return cadena


def buscar_solucion(estado_inicial, nivel_inicial):

    '''Wrapper del bactrack'''

    visitados = {}
    print("Buscando pista...")
    gamelib.draw_text('Buscando pista', 350, 350, fill='red', anchor='nw')
    return backtrack(estado_inicial, visitados, nivel_inicial)

movs_tuplas = ((1,0), (-1,0), (0,1), (0,-1)) # Asi no cuento el reiniciar de mi dic

def backtrack(estado, visitados, nivel_inicial):

    '''Recorro diferentes posibles estados para resolver un movimiento y devuelvo una solucion'''

    dic_niveles_grilla = leer_niveles("niveles.txt")

    visitados[convertir_a_inmutable(estado)] = visitados.get(convertir_a_inmutable(estado), True)

    if soko.juego_ganado(estado):
        return True, []
    else:
        for mov in movs_tuplas:
            printgrilla(estado)
            print(mov)
            print()
            nuevo_estado_grilla = soko.mover(estado, mov)
            printgrilla(nuevo_estado_grilla)
            if convertir_a_inmutable(nuevo_estado_grilla) in visitados:
                print("Ya recorrido...")
                continue
            else:
                print("Utilizando pista...")
                solucion_encontrada, acciones = backtrack(nuevo_estado_grilla, visitados, nivel_inicial)
                if solucion_encontrada:
                    return True, acciones + [mov] 
        return False, None
            

def main():
    # Inicializar el estado del juego

    nivel_inicial = 1

    dic_niveles_grilla = leer_niveles("niveles.txt")

    grilla = dic_niveles_grilla[nivel_inicial]

    tablero_mov = PilaMovimiento()

    cola_pista = ColaPista()

    tamaño = cargar_tamaño(grilla)

    x, y = tamaño

    cont_indices = 0

    if x > 300 or y > 300:
        gamelib.resize(x * 5, y * 5) # Agrando la pantalla en base a gamelib(300 px) dividido la cant de px que tengo por celda (60px) = 5

    else:

        gamelib.resize(300, 300)

    while gamelib.is_alive():

        gamelib.draw_begin()
        # Dibujar la pantalla
        dibujo_juego(grilla)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)

        if not ev:
            break

        tecla = ev.key

        # Actualizar el estado del juego, según la `tecla` presionada

        if ev.type == gamelib.EventType.KeyPress and tecla == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.KeyPress and tecla == 'w':
            # El usuario presiono la tecla w, mover hacia arriba.
            grilla = soko.mover(grilla, coordenadas_teclas('w', grilla))
            grilla, nivel_inicial = pasar_nivel(grilla, dic_niveles_grilla, nivel_inicial)
            tablero_mov.apilar(grilla)

        if ev.type == gamelib.EventType.KeyPress and tecla == 's':
            # El usuario presiono la tecla s, mover hacia abajo
            grilla = soko.mover(grilla, coordenadas_teclas('s', grilla))
            grilla, nivel_inicial = pasar_nivel(grilla, dic_niveles_grilla, nivel_inicial)
            tablero_mov.apilar(grilla)

        if ev.type == gamelib.EventType.KeyPress and tecla == 'd':
            # El usuario presiono la tecla d, mover hacia la derecha
            grilla = soko.mover(grilla, coordenadas_teclas('d', grilla))
            grilla, nivel_inicial = pasar_nivel(grilla, dic_niveles_grilla, nivel_inicial)
            tablero_mov.apilar(grilla)

        if ev.type == gamelib.EventType.KeyPress and tecla == 'a':
            #El usuario presiono la tecla a, mover hacia la izquierda
            grilla = soko.mover(grilla, coordenadas_teclas('a', grilla))
            grilla, nivel_inicial = pasar_nivel(grilla, dic_niveles_grilla, nivel_inicial)
            tablero_mov.apilar(grilla)

        if ev.type == gamelib.EventType.KeyPress and tecla == 'r':
            #El usuario presiono la tecla r, reiniciar la posicion
            grilla = dic_niveles_grilla[nivel_inicial]
            tablero_mov.apilar(grilla)

        if ev.type == gamelib.EventType.KeyPress and tecla == 'u':
            #El usuario presiono la tecla u, deshacer la posicion
            if tablero_mov.esta_vacia():
                grilla = dic_niveles_grilla[nivel_inicial]
            else:
                grilla = tablero_mov.desapilar()
           
        if ev.type == gamelib.EventType.KeyPress and tecla == 'c':
            #El usuario presiono la tecla c, dar pista
            if not cola_pista.esta_vacia():
                mov = cola_pista.desencolar()
                grilla = soko.mover(grilla, mov)
                grilla, nivel_inicial = pasar_nivel(grilla, dic_niveles_grilla, nivel_inicial)
            else:
                pista, movs = buscar_solucion(dic_niveles_grilla[nivel_inicial], nivel_inicial)
                for mov in movs[::-1]:
                    cola_pista.encolar(mov)
                    
gamelib.init(main)


