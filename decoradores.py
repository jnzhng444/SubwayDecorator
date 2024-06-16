from sandwich import Sandwich

class Aguacate(Sandwich):
    def __init__(self, sandwich):
        super().__init__(sandwich.size)
        self.sandwich = sandwich
        self.base_precio_15cm = 1.5
        self.base_precio_30cm = 2.5

    def get_precio(self):
        size = self.sandwich.size
        if size == "15cm":
            return self.sandwich.get_costo() + self.base_precio_15cm
        elif size == "30cm":
            return self.sandwich.get_costo() + self.base_precio_30cm
        else:
            return self.sandwich.get_costo()

    def get_descripcion(self):
        return f"{self.sandwich.get_descripcion()} + Aguacate ({self.base_precio_15cm if self.sandwich.size == '15cm' else self.base_precio_30cm}$)"

    def get_costo(self):
        return self.get_precio()


class DobleProteina(Sandwich):
    def __init__(self, sandwich):
        super().__init__(sandwich.size)
        self.sandwich = sandwich
        self.base_precio_15cm = 4.5
        self.base_precio_30cm = 8

    def get_precio(self):
        size = self.sandwich.size
        if size == "15cm":
            return self.sandwich.get_costo() + self.base_precio_15cm
        elif size == "30cm":
            return self.sandwich.get_costo() + self.base_precio_30cm
        else:
            return self.sandwich.get_costo()

    def get_descripcion(self):
        return f"{self.sandwich.get_descripcion()} + Doble proteina ({self.base_precio_15cm if self.sandwich.size == '15cm' else self.base_precio_30cm}$)"

    def get_costo(self):
        return self.get_precio()

class Hongos(Sandwich):
    def __init__(self, sandwich):
        super().__init__(sandwich.size)
        self.sandwich = sandwich
        self.base_precio_15cm = 0.85
        self.base_precio_30cm = 1.45

    def get_precio(self):
        size = self.sandwich.size
        if size == "15cm":
            return self.sandwich.get_costo() + self.base_precio_15cm
        elif size == "30cm":
            return self.sandwich.get_costo() + self.base_precio_30cm
        else:
            return self.sandwich.get_costo()

    def get_descripcion(self):
        return f"{self.sandwich.get_descripcion()} + Hongos ({self.base_precio_15cm if self.sandwich.size == '15cm' else self.base_precio_30cm}$)"

    def get_costo(self):
        return self.get_precio()

class Refresco(Sandwich):
    def __init__(self, sandwich):
        super().__init__(sandwich.size)
        self.sandwich = sandwich
        self.base_precio_15cm = 1
        self.base_precio_30cm = 1

    def get_precio(self):
        size = self.sandwich.size
        if size == "15cm":
            return self.sandwich.get_costo() + self.base_precio_15cm
        elif size == "30cm":
            return self.sandwich.get_costo() + self.base_precio_30cm
        else:
            return self.sandwich.get_costo()

    def get_descripcion(self):
        return f"{self.sandwich.get_descripcion()} + Refresco ({self.base_precio_15cm if self.sandwich.size == '15cm' else self.base_precio_30cm}$)"

    def get_costo(self):
        return self.get_precio()

class Sopa(Sandwich):
    def __init__(self, sandwich):
        super().__init__(sandwich.size)
        self.sandwich = sandwich
        self.base_precio_15cm = 4.2
        self.base_precio_30cm = 4.2

    def get_precio(self):
        size = self.sandwich.size
        if size == "15cm":
            return self.sandwich.get_costo() + self.base_precio_15cm
        elif size == "30cm":
            return self.sandwich.get_costo() + self.base_precio_30cm
        else:
            return self.sandwich.get_costo()

    def get_descripcion(self):
        return f"{self.sandwich.get_descripcion()} + Sopa ({self.base_precio_15cm if self.sandwich.size == '15cm' else self.base_precio_30cm}$)"

    def get_costo(self):
        return self.get_precio()

class Postre(Sandwich):
    def __init__(self, sandwich):
        super().__init__(sandwich.size)
        self.sandwich = sandwich
        self.base_precio_15cm = 3.5
        self.base_precio_30cm = 3.5

    def get_precio(self):
        size = self.sandwich.size
        if size == "15cm":
            return self.sandwich.get_costo() + self.base_precio_15cm
        elif size == "30cm":
            return self.sandwich.get_costo() + self.base_precio_30cm
        else:
            return self.sandwich.get_costo()

    def get_descripcion(self):
        return f"{self.sandwich.get_descripcion()} + Postre ({self.base_precio_15cm if self.sandwich.size == '15cm' else self.base_precio_30cm}$)"

    def get_costo(self):
        return self.get_precio()

