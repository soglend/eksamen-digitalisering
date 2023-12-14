# OPPGAVE
# A) Slektsgranskning - a) vis slektstre av kongefamilien i Norge og gi valg om å få slektstilknytning til hver person

#####
# print, input, variable: int/float/string/boolean
# + - * / = > < == // ** % ! & | not and or
# def funksjon(inn-variabel) return ut-variabel main()
# if/else/elif:, for/in:, while:
# list [], tuple (), dictionary {:}, set {}, file/open/close/brwa/pickle
# class objekt:, __init__(self), __str__(self)
# objekt.globaledata, objekt.__lokaledata, objekt.funksjon()
# import python-bibliotek
#####

import csv
import pandas as pd
from graphviz import Digraph

class person:
    def __init__(self):
        self.__navn = None
        self.__far = None
        self.__mor = None
        self.__år = None
        self.__avkom = None

    def __str__(self):
        return self.__navn, self.__år
    
    def hent_data(self, csv_fil):
#        inn_fil = open(csv_fil, 'r', encoding='LATIN1')
#        type(csv_fil)
#        csv_data = csv.reader(inn_fil, delimiter='\t')
#        header = []
#        header = next(csv_data)
#        for indeks in range(len(header)):
#            header[indeks] = header[indeks].rstrip("\xa0")
#        print(header)

        data = pd.read_csv(csv_fil, encoding='LATIN1')
        self.__far = data["FAR" + "FARFØDT"] # Hent ut all data fra kolonnen FAR
        self.__mor = data["MOR" + "MORFØDT"]
        self.__avkom = data["AVKOM"]
        self.__år = data["FØDT"]
        barn1 = data["BARN1"]
        barn2 = data["BARN2"]
        barn3 = data["BARN3"]
        print(self.__far[2]) # skriv ut tredje i kolonnen (starter fra 0)
        print(self.__år[1])
        return self.__far, self.__mor, self.__avkom

    def finn_navn(self, fornavn):
        self.__navn = fornavn
        return self.__navn

    def finn_år(self):
        pass

kjør = person()
kjør.hent_data("data/slektstre_kongefamilien.csv")
