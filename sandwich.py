from abc import ABC, abstractmethod

# Clase abstracta que define la estructura del sándwich
class Sandwich(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def get_descripcion(self):
        pass

    @abstractmethod
    def get_costo(self):
        pass

# Clases concretas de sándwiches
class PavoSandwich(Sandwich):
    def __init__(self, size):
        super().__init__(size)
        self.precio = self.set_precio(size)

    def set_precio(self, size):
        if size == "15cm":
            return 12
        elif size == "30cm":
            return 18

    def get_descripcion(self):
        return f"{self.size} de Pavo ({self.precio}$)"

    def get_costo(self):
        return self.precio  # El costo ya refleja el precio ajustado según el tamaño

class ItalianoSandwich(Sandwich):
    def __init__(self, size):
        super().__init__(size)
        self.precio = self.set_precio(size)

    def set_precio(self, size):
        if size == "15cm":
            return 9
        elif size == "30cm":
            return 16

    def get_descripcion(self):
        return f"{self.size} de Italiano ({self.precio}$)"

    def get_costo(self):
        return self.precio  # El costo ya refleja el precio ajustado según el tamaño

class BeefSandwich(Sandwich):
    def __init__(self, size):
        super().__init__(size)
        self.precio = self.set_precio(size)

    def set_precio(self, size):
        if size == "15cm":
            return 10
        elif size == "30cm":
            return 16

    def get_descripcion(self):
        return f"{self.size} de Beef ({self.precio}$)"

    def get_costo(self):
        return self.precio  # El costo ya refleja el precio ajustado según el tamaño

class VeggieSandwich(Sandwich):
    def __init__(self, size):
        super().__init__(size)
        self.precio = self.set_precio(size)

    def set_precio(self, size):
        if size == "15cm":
            return 8
        elif size == "30cm":
            return 14

    def get_descripcion(self):
        return f"{self.size} de Veggie ({self.precio}$)"

    def get_costo(self):
        return self.precio  # El costo ya refleja el precio ajustado según el tamaño

class AtunSandwich(Sandwich):
    def __init__(self, size):
        super().__init__(size)
        self.precio = self.set_precio(size)

    def set_precio(self, size):
        if size == "15cm":
            return 11
        elif size == "30cm":
            return 17

    def get_descripcion(self):
        return f"{self.size} de Atun ({self.precio}$)"

    def get_costo(self):
        return self.precio  # El costo ya refleja el precio ajustado según el tamaño

class PolloSandwich(Sandwich):
    def __init__(self, size):
        super().__init__(size)
        self.precio = self.set_precio(size)

    def set_precio(self, size):
        if size == "15cm":
            return 12
        elif size == "30cm":
            return 18

    def get_descripcion(self):
        return f"{self.size} de Pollo ({self.precio}$)"

    def get_costo(self):
        return self.precio  # El costo ya refleja el precio ajustado según el tamaño