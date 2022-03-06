import random as rnd

def generator_zyczen(imie):

    lista_cech =["pracowitość", "poczucie humoru", "optymizm","nieszablonowe myślenie","ciekawe anedgoty","otwartość"]

    cecha1 = rnd.choice(lista_cech)
    lista_cech.remove(cecha1)
    cecha2 = rnd.choice(lista_cech)
    lista_cech.remove(cecha2)
    cecha3 = rnd.choice(lista_cech)
    lista_cech.remove(cecha3)

    print("""%s

    Dziękujemy Ci.

    Za %s, wiele dla nas znaczy
    Za %s, bardzo nam wsyzstkim pomaga
    Za %s... To jest w Tobie najcenniejsze

    Wszystkiego najlepszego z okazji dnia kobiet!""" % (imie,cecha1,cecha2,cecha3))
