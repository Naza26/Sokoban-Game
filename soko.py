'''
# pared
$ caja
@ jugador
. objetivo
* objetivo + caja
+ objetivo + jugador
'''

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

def crear_grilla(desc):
  matrix = []
  for x in desc:
    row = [char for char in x]
    matrix.append(row)
  return matrix
 
grilla = crear_grilla(['#####','#.$ #','#@  #','#####'])

def print_grilla(grilla):
  for x in grilla:
    print (''.join(x))

def dimensiones(grilla):
  fila = len(grilla)
  columna = len(grilla[0][:])
  total = columna, fila
  return total
     
def hay_pared(grilla, c, f):

  return grilla[f][c] == '#'

def hay_objetivo(grilla, c, f):

  return grilla[f][c] == "." or grilla[f][c] == "*"  or grilla[f][c] == "+" 

def hay_caja(grilla, c, f):

  return grilla[f][c] == "$" or grilla[f][c] == "*" 


def hay_jugador(grilla, c, f):

  return grilla[f][c] == "@" or grilla[f][c] == "+" 

def juego_ganado(grilla):
  """Esta funcion recibe una grilla y devuelve true si el juegoe esta ganado"""
  #fila = len(grilla)
  #columna = len(grilla[0])
  for y in range(len(grilla)):
    for x in range(len(grilla[y])):
      t = grilla[y][x]
      if t == "." or t == "+": 
        return False
  return True


def encontrar_jugador(grilla):
  """Esta funcion recibe una grilla y devuelve la posicion del jugador con sus coordenadas"""  
  x = None
  y = None
  #fila = len(grilla)
  #columna = len(grilla[0])
  for y in range(len(grilla)):
    for x in range(len(grilla[y])):
    #recorro toda la lista
      t = grilla[y][x]
      if t == "@" or t == '+': #Encuentro jugador
        return y, x #Devuelvo coordenadas del jugador(tupla)

def representacion_jugador_arroba(nueva_grilla,mov_jug_a,mov_jug_b):
    jugador_arroba = nueva_grilla[mov_jug_a][mov_jug_b] = "@"
    return jugador_arroba

def representacion_caja(nueva_grilla,mov_caja_c,mov_caja_d):
  caja = nueva_grilla[mov_caja_c][mov_caja_d] = "$"
  return caja

def representacion_jugador_mas(nueva_grilla,mov_jug_a,mov_jug_b):
  jugador_arroba = nueva_grilla[mov_jug_a][mov_jug_b] = "+"
  return jugador_arroba

def ni_pared_ni_caja_ni_objcaja(nueva_grilla, mov_caja_c,mov_caja_d):
  bloqueos = nueva_grilla[mov_caja_c][mov_caja_d] != "#" and nueva_grilla[mov_caja_c][mov_caja_d] != "$" and nueva_grilla[mov_caja_c][mov_caja_d] != "*" #Si no hay una pared, ni caja, hago lo siguiente:
  return bloqueos

def borrar_jugador(nueva_grilla,y,x):
  borrado = nueva_grilla[y][x] = " "
  return borrado

def objetivo_mas_caja(nueva_grilla,mov_caja_c,mov_caja_d):
  obj_caja = nueva_grilla[mov_caja_c][mov_caja_d] = "*"
  return obj_caja

def mover(grilla, direccion):
  nueva_grilla = [x[:] for x in grilla]
  """Esta funcion recibe una grilla y una direccion y devuelve una nueva grilla con el movimiento actualizado"""
  juego_ganado(nueva_grilla)
  #print(nueva_grilla)
  x2, y2 = direccion # desempaqueto la direccion
  y, x = encontrar_jugador(grilla) # desempaqueto la posic jugador
  casillero_mov = (y + y2, x + x2) #Movimiento desde el jugador
  mov_jug_a, mov_jug_b = casillero_mov # desempaqueto el mov del jugador
  x3, y3 = direccion #La que voy a usar para calcular el mov de la caja
  casillero_mov_caja = (y + y3 * 2, x + x3 * 2)
  mov_caja_c, mov_caja_d = casillero_mov_caja #Desempaqueto el mov del jugador para el mov doble de la caja

  # condiciones si el jugador es @

  if hay_jugador(nueva_grilla,x,y) and nueva_grilla[y][x] == '@':

    if nueva_grilla[mov_jug_a][mov_jug_b] == " ":
      representacion_jugador_arroba(nueva_grilla,mov_jug_a,mov_jug_b)
      borrar_jugador(nueva_grilla,y,x)
      return nueva_grilla

    if hay_caja(nueva_grilla,mov_jug_b,mov_jug_a):

      if nueva_grilla[mov_jug_a][mov_jug_b] == "$":
        representacion_jugador_arroba(nueva_grilla,mov_jug_a,mov_jug_b)
        borrar_jugador(nueva_grilla,y,x)
      if nueva_grilla[mov_jug_a][mov_jug_b] == "*":
        representacion_jugador_mas(nueva_grilla,mov_jug_a,mov_jug_b)
        borrar_jugador(nueva_grilla,y,x)
      if ni_pared_ni_caja_ni_objcaja(nueva_grilla, mov_caja_c,mov_caja_d):
        if nueva_grilla[mov_caja_c][mov_caja_d] == " ":
          representacion_caja(nueva_grilla,mov_caja_c,mov_caja_d)
          return nueva_grilla
        if nueva_grilla[mov_caja_c][mov_caja_d] == ".":
          objetivo_mas_caja(nueva_grilla,mov_caja_c,mov_caja_d)
          return nueva_grilla

    if hay_objetivo(nueva_grilla,mov_jug_b,mov_jug_a):

      if nueva_grilla[mov_jug_a][mov_jug_b] == ".":
        nueva_grilla[mov_jug_a][mov_jug_b] = "+" 
        borrar_jugador(nueva_grilla,y,x)
        #nueva_grilla[y][x] = "."
        return nueva_grilla
      if ni_pared_ni_caja_ni_objcaja(nueva_grilla, mov_caja_c,mov_caja_d):
        if nueva_grilla[mov_caja_c][mov_caja_d] == " ":
          representacion_caja(nueva_grilla,mov_caja_c,mov_caja_d) 
          return nueva_grilla
        if nueva_grilla[mov_caja_c][mov_caja_d] == ".":
          objetivo_mas_caja(nueva_grilla,mov_caja_c,mov_caja_d)
          return nueva_grilla

    if hay_objetivo(nueva_grilla,mov_jug_b,mov_jug_a):

      if nueva_grilla[mov_jug_a][mov_jug_b] == ".":
        nueva_grilla[mov_jug_a][mov_jug_b] = "+"
        borrar_jugador(nueva_grilla,y,x)
        return nueva_grilla

  # condiciones si el jugador es +

  if hay_jugador(nueva_grilla,x,y) and nueva_grilla[y][x] == '+':

    if nueva_grilla[mov_jug_a][mov_jug_b] == " ":
      representacion_jugador_arroba(nueva_grilla,mov_jug_a,mov_jug_b)
      nueva_grilla[y][x] = "."
      return nueva_grilla

    if hay_caja(nueva_grilla,mov_jug_b,mov_jug_a):

      if nueva_grilla[mov_jug_a][mov_jug_b] == "$":
        representacion_jugador_arroba(nueva_grilla,mov_jug_a,mov_jug_b)
        nueva_grilla[y][x] = "."
      if nueva_grilla[mov_jug_a][mov_jug_b] == "*":
        representacion_jugador_mas(nueva_grilla,mov_jug_a,mov_jug_b)
        borrar_jugador(nueva_grilla,y,x)
      if ni_pared_ni_caja_ni_objcaja(nueva_grilla, mov_caja_c,mov_caja_d):
        if nueva_grilla[mov_caja_c][mov_caja_d] == " ":
          representacion_caja(nueva_grilla,mov_caja_c,mov_caja_d)
          return nueva_grilla
        if nueva_grilla[mov_caja_c][mov_caja_d] == ".":
          objetivo_mas_caja(nueva_grilla,mov_caja_c,mov_caja_d)
          return nueva_grilla

    if hay_objetivo(nueva_grilla,mov_jug_b,mov_jug_a):

      if nueva_grilla[mov_jug_a][mov_jug_b] == ".":
        nueva_grilla[mov_jug_a][mov_jug_b] = "+"
        borrar_jugador(nueva_grilla,y,x)
        #nueva_grilla[y][x] = "."
        return nueva_grilla
      if ni_pared_ni_caja_ni_objcaja(nueva_grilla, mov_caja_c,mov_caja_d):
        if nueva_grilla[mov_caja_c][mov_caja_d] == " ":
          representacion_caja(nueva_grilla,mov_caja_c,mov_caja_d)
          return nueva_grilla
        if nueva_grilla[mov_caja_c][mov_caja_d] == ".":
          objetivo_mas_caja(nueva_grilla,mov_caja_c,mov_caja_d)
          return nueva_grilla

    if hay_objetivo(nueva_grilla,mov_jug_b,mov_jug_a):

      if nueva_grilla[mov_jug_a][mov_jug_b] == ".":
        nueva_grilla[mov_jug_a][mov_jug_b] = "+" 
        borrar_jugador(nueva_grilla,y,x)
        return nueva_grilla
      
  return grilla[:]
