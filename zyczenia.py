import random as rnd

def generator_zyczen(imie):

    lista_cech =["pracowitość", "poczucie humoru", "optymizm","nieszablonowe myślenie","ciekawe anegdoty","otwartość"]

    cecha1 = rnd.choice(lista_cech)
    lista_cech.remove(cecha1)
    cecha2 = rnd.choice(lista_cech)
    lista_cech.remove(cecha2)
    cecha3 = rnd.choice(lista_cech)
    lista_cech.remove(cecha3)

    print("""
    %s

    Dziękujemy Ci.

    Za %s, wiele dla nas znaczy
    Za %s, bardzo nam wszystkim pomaga
    Za %s... To jest w Tobie najcenniejsze

    # obowiązuje pisownia obydwu członów wielkimi literami (Dzień Kobiet), 
    # ponieważ obydwa stanowią nomen proprium corocznego święta obchodzonego 
    # 8 marca (tak samo Dzień Matki, Dzień Ojca, Dzień Babci, Dzień Dziadka itp.). 
    # https://sjp.pwn.pl/poradnia/haslo/Dzien-Kobiet;18442.html
    Wszystkiego najlepszego z okazji Dnia Kobiet!""" % (imie,cecha1,cecha2,cecha3))
