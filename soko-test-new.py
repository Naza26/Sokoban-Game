import pprint
import soko

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

def verificar_estado(desc, grilla):
    x = None
    y = None
    try:
        w, h = soko.dimensiones(grilla)
        assert (w, h) == (len(desc[0]), len(desc))
        for y in range(h):
            for x in range(w):
                c = desc[y][x]
                if c == '#':
                    assert soko.hay_pared(grilla, x, y)
                    assert not soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
                elif c == '.':
                    assert not soko.hay_pared(grilla, x, y)
                    assert soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
                elif c == '$':
                    assert not soko.hay_pared(grilla, x, y)
                    assert not soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert soko.hay_caja(grilla, x, y)
                elif c == '@':
                    assert not soko.hay_pared(grilla, x, y)
                    assert not soko.hay_objetivo(grilla, x, y)
                    assert soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
                elif c == '*':
                    assert not soko.hay_pared(grilla, x, y)
                    assert soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert soko.hay_caja(grilla, x, y)
                elif c == '+':
                    assert not soko.hay_pared(grilla, x, y)
                    assert soko.hay_objetivo(grilla, x, y)
                    assert soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
    except AssertionError as e:
        print('Estado esperado:')
        print('\n'.join(desc))
        print()
        print('Estado actual:')
        pprint.pprint(grilla)
        print()
        if x is not None and y is not None:
            print(f'Error en columna = {x}, fila = {y}:')
            print()
        raise

def test1():
    desc = [
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

def test2():
    desc = [
        '#####',
        '#+$ #',
        '#   #',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

def test3():
    desc = [
        '#####',
        '# * #',
        '#@  #',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert soko.juego_ganado(grilla)

def test4():
    desc = [
        '#####',
        '# *.#',
        '#@ $#',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

def test5():
    desc = [
        '#####',
        '# * #',
        '#@ *#',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert soko.juego_ganado(grilla)

def test6():
    desc1 = [
        '######',
        '#@ $.#',
        '######',
    ]
    desc2 = [
        '######',
        '# @$.#',
        '######',
    ]

    grilla1 = soko.crear_grilla(desc1)
    grilla2 = soko.mover(grilla1, ESTE)

    # Si el movimiento es válido, la función mover() debe devolver una grilla nueva
    # y NO modificar la grilla recibida.
    verificar_estado(desc1, grilla1)
    verificar_estado(desc2, grilla2)

def test7():
    desc = [
        '    ###   ',
        '    #.#   ',
        '    #$#   ',
        '   ##$####',
        '####@ $$.#',
        '#.$$  ####',
        '####$##   ',
        '   #$#    ',
        '   #.#    ',
        '   ###    ',
    ]
    grilla = soko.crear_grilla(desc)

    assert soko.mover(grilla, OESTE) == grilla
    assert soko.mover(grilla, NORTE) == grilla

    grilla = soko.mover(grilla, ESTE)

    assert soko.mover(grilla, ESTE) == grilla
    assert soko.mover(grilla, NORTE) == grilla

    grilla = soko.mover(grilla, SUR)

    assert soko.mover(grilla, ESTE) == grilla
    assert soko.mover(grilla, SUR) == grilla

    grilla = soko.mover(grilla, OESTE)

    assert soko.mover(grilla, OESTE) == grilla
    assert soko.mover(grilla, SUR) == grilla

def test8():
    desc = [
        '########',
        '#@ $ . #',
        '########',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

    for direction in (OESTE, NORTE, SUR):
        grilla = soko.mover(grilla, direction)
        verificar_estado(desc, grilla)
        assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, ESTE)
    desc = [
        '########',
        '# @$ . #',
        '########',
    ]
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

    for direction in (NORTE, SUR):
        grilla = soko.mover(grilla, direction)
        verificar_estado(desc, grilla)
        assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, ESTE)
    verificar_estado([
        '########',
        '#  @$. #',
        '########',
    ], grilla)
    assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, OESTE)
    verificar_estado([
        '########',
        '# @ $. #',
        '########',
    ], grilla)
    assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, ESTE)
    grilla = soko.mover(grilla, ESTE)
    verificar_estado([
        '########',
        '#   @* #',
        '########',
    ], grilla)
    assert soko.juego_ganado(grilla)


def test9():
    '''
    Prueba de que se pueda mover una caja hacia el objetivo
    '''
    desc1 = [
        '########',
        '#  @$. #',
        '#      #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)

    grilla2 = soko.mover(grilla1, ESTE)
    assert soko.juego_ganado(grilla2)
    assert grilla1 != grilla2



def test10():
    '''
    Prueba de que se pueda sacar una caja del objetivo
    '''
    desc1 = [
        '########',
        '#   @* #',
        '#      #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)

    grilla2 = soko.mover(grilla1, ESTE)
    assert not soko.juego_ganado(grilla2)
    assert grilla1 != grilla2


def test11():
    '''
    Prueba de que no se pueda mover una caja en objetivo adyacente a una pared
    '''
    desc1 = [
        '########',
        '#   @*##',
        '#      #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)

    grilla2 = soko.mover(grilla1, ESTE)
    assert soko.juego_ganado(grilla2)
    assert grilla1 == grilla2


def test12():
    '''
    Prueba de que no se pueda mover una caja fuera de objetivo adyacente a una pared
    '''
    desc1 = [
        '########',
        '#   @$##',
        '# .    #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)

    grilla2 = soko.mover(grilla1, ESTE)
    assert not soko.juego_ganado(grilla2)
    assert grilla1 == grilla2


def test13():
    '''
    Prueba de que no se pueda mover una caja fuera de objetivo adyacente a una de objetivo
    '''
    desc1 = [
        '########',
        '#   @$*#',
        '#  .   #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)

    grilla2 = soko.mover(grilla1, ESTE)
    assert not soko.juego_ganado(grilla2)
    assert grilla1 == grilla2



def test14():
    '''
    Prueba de que no se pueda mover una caja en objetivo adyacente a una fuera de objetivo
    '''
    desc1 = [
        '########',
        '#   @*$#',
        '#  .   #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)

    grilla2 = soko.mover(grilla1, ESTE)
    assert not soko.juego_ganado(grilla2)
    assert grilla1 == grilla2


def test15():
    '''
    Prueba de moverse a los limites del tablero
    '''
    desc1 = [
        '########',
        '#     @#',
        '#  *   #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)

    grilla2 = soko.mover(grilla1, ESTE)
    grilla3 = soko.mover(grilla1, NORTE)
    assert grilla1 == grilla3


def test16():
    '''
    Prueba de pisar el objetivo
    '''
    desc1 = [
        '########',
        '#    .@#',
        '#      #',
        '########',
    ]
    desc2 = [
        '########',
        '#    + #',
        '#      #',
        '########',
    ]
    desc3 = [
        '########',
        '#   @. #',
        '#      #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)
    grilla2 = soko.mover(grilla1, OESTE)
    grilla3 = soko.mover(grilla2, OESTE)
    verificar_estado(desc1, grilla1)
    verificar_estado(desc2, grilla2)
    verificar_estado(desc3, grilla3)


def test17():
    '''
    Prueba de mover una caja con objetivo hacia otro objetivo
    '''
    desc1 = [
        '########',
        '#   @*.#',
        '#      #',
        '########',
    ]
    desc2 = [
        '########',
        '#    +*#',
        '#      #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)
    grilla2 = soko.mover(grilla1, ESTE)
    verificar_estado(desc1, grilla1)
    verificar_estado(desc2, grilla2)



def test18():
    '''
    Prueba de un movimiento invalido con el jugador posicionado sobre un objetivo
    '''
    desc1 = [
        '########',
        '# $$+  #',
        '#      #',
        '########',
    ]
    grilla1 = soko.crear_grilla(desc1)
    grilla2 = soko.mover(grilla1, OESTE)
    verificar_estado(desc1, grilla2)




def test19():
    '''
    Prueba del primer nivel del TP2
    '''
    desc1 = [
        "####  ",
        "# .#  ",
        "#  ###",
        "#*   #",
        "#@ $ #",
        "#  ###",
        "####  "
    ]
    desc2 = [
        "####  ",
        "# .#  ",
        "#$ ###",
        "#+   #",
        "#  $ #",
        "#  ###",
        "####  "
    ]
    grilla1 = soko.crear_grilla(desc1)
    grilla2 = soko.mover(grilla1, NORTE)
    verificar_estado(desc2, grilla2)



def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()
    test16()
    test17()
    test18()
    test19()
    print("Todo OK :)")

main()
