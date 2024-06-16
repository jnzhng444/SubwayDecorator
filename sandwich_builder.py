from sandwich import PavoSandwich, BeefSandwich, VeggieSandwich, ItalianoSandwich, AtunSandwich, PolloSandwich

from decoradores import Aguacate, DobleProteina, Hongos, Sopa, Postre, Refresco

class SandwichBuilder:
    def __init__(self):
        self.selected_sandwich = None
        self.current_costo = 0

    def verDetalle(self):
        if self.selected_sandwich:
            print(f"{self.selected_sandwich.get_descripcion()}    TOTAL = {self.selected_sandwich.get_costo()}$")

    def make_pavo_sandwich_30cm(self):
        self.selected_sandwich = PavoSandwich("30cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_pavo_sandwich_15cm(self):
        self.selected_sandwich = PavoSandwich("15cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_beef_sandwich_30cm(self):
        self.selected_sandwich = BeefSandwich("30cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_beef_sandwich_15cm(self):
        self.selected_sandwich = BeefSandwich("15cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_veggie_sandwich_30cm(self):
        self.selected_sandwich = VeggieSandwich("30cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_veggie_sandwich_15cm(self):
        self.selected_sandwich = VeggieSandwich("15cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_italiano_sandwich_30cm(self):
        self.selected_sandwich = ItalianoSandwich("30cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_italiano_sandwich_15cm(self):
        self.selected_sandwich = ItalianoSandwich("15cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_atun_sandwich_30cm(self):
        self.selected_sandwich = AtunSandwich("30cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_atun_sandwich_15cm(self):
        self.selected_sandwich = AtunSandwich("15cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_pollo_sandwich_30cm(self):
        self.selected_sandwich = PolloSandwich("30cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def make_pollo_sandwich_15cm(self):
        self.selected_sandwich = PolloSandwich("15cm")
        self.verDetalle()
        self.update_costo()
        self.app.update_costo()

    def add_aguacate(self):
        if self.selected_sandwich:
            self.selected_sandwich = Aguacate(self.selected_sandwich)
            self.verDetalle()
            self.update_costo()
            self.app.update_costo()

    def add_dobleproteina(self):
        if self.selected_sandwich:
            self.selected_sandwich = DobleProteina(self.selected_sandwich)
            self.verDetalle()
            self.update_costo()
            self.app.update_costo()

    def add_hongos(self):
        if self.selected_sandwich:
            self.selected_sandwich = Hongos(self.selected_sandwich)
            self.verDetalle()
            self.update_costo()
            self.app.update_costo()

    def add_refresco(self):
        if self.selected_sandwich:
            self.selected_sandwich = Refresco(self.selected_sandwich)
            self.verDetalle()
            self.update_costo()
            self.app.update_costo()

    def add_sopa(self):
        if self.selected_sandwich:
            self.selected_sandwich = Sopa(self.selected_sandwich)
            self.verDetalle()
            self.update_costo()
            self.app.update_costo()

    def add_postre(self):
        if self.selected_sandwich:
            self.selected_sandwich = Postre(self.selected_sandwich)
            self.verDetalle()
            self.update_costo()
            self.app.update_costo()


    def update_costo(self):
        if self.selected_sandwich:
            self.current_costo = self.selected_sandwich.get_costo()

    def get_current_costo(self):
        return self.current_costo

    def set_app(self, app):
        self.app = app

