import tkinter as tk
from sandwich_builder import SandwichBuilder

class SandwichBuilderApp:
    def __init__(self, Window):
        self.Window = Window
        self.Window.title("Sandwich Builder App")
        self.Window.resizable(False, False)
        self.sandwich_builder = SandwichBuilder()
        self.sandwich_list = []  # Lista para almacenar los sándwiches
        self.create_interface()


    def create_interface(self):
        global imgagre
        self.MenuCanvas = tk.Canvas(self.Window, width=1280, height=720)  # Se crea el Canvas para colocar las cosas
        self.MenuCanvas.place(x=0, y=0)

        self.Fondo = tk.PhotoImage(file="Imagenes/fondo.png")  # Establecer variable para imagen de fondo
        self.fnd = self.MenuCanvas.create_image(0, 0, anchor="nw", image=self.Fondo)  # Corrected 'self.Fondo'

        pavo_button = tk.Button(self.MenuCanvas, text="Pavo Sandwich 30cm",width=17, height=2,cursor="hand2",command=self.sandwich_builder.make_pavo_sandwich_30cm)
        pavo_button.place(x=30,y=300)

        pavo_button2 = tk.Button(self.Window, text="Pavo Sandwich 15cm",width=17, height=2,cursor="hand2",command=self.sandwich_builder.make_pavo_sandwich_15cm)
        pavo_button2.place(x=200,y=300)

        beef_button = tk.Button(self.MenuCanvas, text="Beef Sandwich 30cm", width=17, height=2, cursor="hand2",
                                command=self.sandwich_builder.make_beef_sandwich_30cm)
        beef_button.place(x=30, y=360)

        beef_button2 = tk.Button(self.Window, text="Beef Sandwich 15cm", width=17, height=2, cursor="hand2",
                                 command=self.sandwich_builder.make_beef_sandwich_15cm)
        beef_button2.place(x=200, y=360)

        vegg_button = tk.Button(self.MenuCanvas, text="Veggie Sandwich 30cm", width=17, height=2, cursor="hand2",
                                command=self.sandwich_builder.make_veggie_sandwich_30cm)
        vegg_button.place(x=30, y=420)

        vegg_button2 = tk.Button(self.Window, text="Veggie Sandwich 15cm", width=17, height=2, cursor="hand2",
                                 command=self.sandwich_builder.make_veggie_sandwich_15cm)
        vegg_button2.place(x=200, y=420)

        ita_button = tk.Button(self.MenuCanvas, text="Italiano Sandwich 30cm", width=17, height=2, cursor="hand2",
                                command=self.sandwich_builder.make_italiano_sandwich_30cm)
        ita_button.place(x=30, y=480)

        ita_button2 = tk.Button(self.Window, text="Italiano Sandwich 15cm", width=17, height=2, cursor="hand2",
                                 command=self.sandwich_builder.make_italiano_sandwich_15cm)
        ita_button2.place(x=200, y=480)

        atun_button = tk.Button(self.MenuCanvas, text="Atun Sandwich 30cm", width=17, height=2, cursor="hand2",
                                command=self.sandwich_builder.make_atun_sandwich_30cm)
        atun_button.place(x=30, y=540)

        atun_button2 = tk.Button(self.Window, text="Atun Sandwich 15cm", width=17, height=2, cursor="hand2",
                                 command=self.sandwich_builder.make_atun_sandwich_15cm)
        atun_button2.place(x=200, y=540)

        po_button = tk.Button(self.MenuCanvas, text="Pollo Sandwich 30cm", width=17, height=2, cursor="hand2",
                                command=self.sandwich_builder.make_pollo_sandwich_30cm)
        po_button.place(x=30, y=600)

        po_button2 = tk.Button(self.Window, text="Pollo Sandwich 15cm", width=17, height=2, cursor="hand2",
                                 command=self.sandwich_builder.make_pollo_sandwich_15cm)
        po_button2.place(x=200, y=600)
        # Decorator Buttons
        aguacate_button = tk.Button(self.Window, text="Aguacate", width=17, height=2,cursor="hand2",command=self.sandwich_builder.add_aguacate)
        aguacate_button.place(x=500, y=200)

        doble_button = tk.Button(self.Window, text="Doble Proteina", width=17, height=2,cursor="hand2",command=self.sandwich_builder.add_dobleproteina)
        doble_button.place(x=750, y=200)

        hongo_button = tk.Button(self.Window, text="Hongos", width=17, height=2,cursor="hand2",command=self.sandwich_builder.add_hongos)
        hongo_button.place(x=500, y=300)

        refresco_button = tk.Button(self.Window, text="Refresco", width=17, height=2,cursor="hand2",command=self.sandwich_builder.add_refresco)
        refresco_button.place(x=750, y=300)

        sopa_button = tk.Button(self.Window, text="Sopa", width=17, height=2,cursor="hand2",command=self.sandwich_builder.add_sopa)
        sopa_button.place(x=500, y=400)

        postre_button = tk.Button(self.Window, text="Postre", width=17, height=2,cursor="hand2",command=self.sandwich_builder.add_postre)
        postre_button.place(x=750, y=400)

        imgagre = tk.PhotoImage(file="Imagenes/agregar.png")
        add_to_list_button = tk.Button(self.Window, image= imgagre,cursor="hand2",command=self.add_to_list)
        add_to_list_button.place(x=1115, y=100)

        calculate_cost_button = tk.Button(self.Window, text="Pedir", width=17, height=2,cursor="hand2",command=self.calculate_total_cost)
        calculate_cost_button.place(x=1100,y=600)

        self.sandwich_builder.set_app(self)

        self.cost_label = tk.Label(self.Window, text="",font=("Arial", 20))
        self.cost_label.place(x=1190,y=670)


        self.update_costo()

    def add_to_list(self):
        if self.sandwich_builder.selected_sandwich:
            self.sandwich_list.append(self.sandwich_builder.selected_sandwich)


    def print_sandwich_details(self, sandwich_list, total_cost):
        print("=" * 70)
        for sandwich in sandwich_list:
            description = sandwich.get_descripcion()
            cost = sandwich.get_costo()
            print(f"{description} PRECIO ${cost}")
        print("=" * 70)
        print(f"TOTAL ${total_cost}")

    def calculate_total_cost(self):
        for i, sandwich in enumerate(self.sandwich_list, start=1):
            print(f"Sandwich {i}: {sandwich.get_descripcion()} - Costo: {sandwich.get_costo()}$")
        total_cost = sum(sandwich.get_costo() for sandwich in self.sandwich_list)
        self.print_sandwich_details(self.sandwich_list, total_cost)
        self.cost_label.config(text=f"{total_cost}$")

    def update_costo(self):
        self.sandwich_builder.update_costo()
        current_cost = self.sandwich_builder.get_current_costo()
        self.cost_label.config(text=f"{current_cost}$")


def main():
    Window = tk.Tk()
    Window.minsize(1280,720)
    app = SandwichBuilderApp(Window)
    Window.mainloop()

if __name__ == "__main__":
    main()
