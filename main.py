from sandwich import PavoSandwich,BeefSandwich,VeggieSandwich,ItalianoSandwich,AtunSandwich,PolloSandwich
from decoradores import Aguacate, DobleProteina,Hongos,Sopa,Postre,Refresco

def verDetalle(sandwich):
    print(f"{sandwich.get_descripcion()}    TOTAL = {sandwich.get_costo()}$")

if __name__ == "__main__":
    san1 = PavoSandwich("30cm")
    verDetalle(san1)
    san2 = Aguacate(san1)
    verDetalle(san2)
    san3 = DobleProteina(san2)
    verDetalle(san3)


    san1 = PavoSandwich("15cm")
    verDetalle(san1)
    san2 = Aguacate(san1)
    verDetalle(san2)
    san3 = DobleProteina(san2)
    verDetalle(san3)
    san4 = Sopa(san3)
    verDetalle(san4)
    san5 = Sopa(san4)
    verDetalle(san5)



