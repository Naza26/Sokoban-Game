class PilaMovimiento:

    def __init__(self):
        self.items = []

    def esta_vacia(self):
        '''Devuelve True si la lista esta vacia, False en caso contrario'''
        return len(self.items) == 0

    def apilar(self, x):
        '''
        Apila el elemento x
        '''
        self.items.append(x)

    def desapilar(self):
        '''Devulve el elemento tope y lo elimina. Si la pila esta vacia levanta una excepcion'''
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        else:
            print(self.items)
            return self.items.pop()


class PilaCoordenada:
    def __init__(self):
        self.movimientos = []

    def esta_vacia(self):
        '''Devuelve True si la lista esta vacia, False en caso contrario'''
        return len(self.movimientos) == 0

    def apilar(self, x):
        '''Apila el elemento x'''
        self.movimientos.append(x)

    def desapilar(self):
        '''Devulve el elemento tope y lo elimina. Si la pila esta vacia levanta una excepcion'''
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        else:
            print(self.movimientos)
            return self.movimientos.pop()

class ColaPista:
    """Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero
    en ser desencolado."""

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