import time
import sys
from datetime import datetime

tilat = {
    "kaytetty": 0,
    "alotusaika": [],
    "lopetusaika": [],
    "opaika": [],
    "opaika_uus": [],

}

def sk():
    tilat["alotusaika"] = time.strftime("%H:%M:%S", time.localtime())
    #print(tilat["alotusaika"])
    menu2()

def menu():
    print("Teretulemast tähä sekuntikelloon")
    print("1. Aloittaa kellon")
    if int(input("Anna valinta: ")) == 1:
        sk()

def menu2():
    print("2. Pysäyttää kellon")
    valintaa = int(input("Anna valinta: "))
    if tilat["kaytetty"] == 1 and valintaa == 2:
        tilat["lopetusaika"] = time.strftime("%H:%M:%S", time.localtime())
        tilat["opaika_uus"] = tilat["opaika"] + datetime.strptime(tilat["lopetusaika"], '%H:%M:%S') - datetime.strptime(tilat["alotusaika"], '%H:%M:%S')
        tilat["opaika"] = tilat["opaika_uus"]
        print(tilat["opaika"])
        looppi()
    elif valintaa == 2:
        tilat["kaytetty"] = 1
        tilat["lopetusaika"] = time.strftime("%H:%M:%S", time.localtime())
        #print(tilat["lopetusaika"])
        tilat["opaika"] = datetime.strptime(tilat["lopetusaika"], '%H:%M:%S') - datetime.strptime(tilat["alotusaika"], '%H:%M:%S')
        print (tilat["opaika"])
        looppi()

def looppi():
    print("1. Jatkaa aikaa\n2. Lopettaa (ja tallentaa joskus tulevaisuudessa)")
    valinta = int(input("Anna valinta: "))
    if valinta == 1:
        sk()
    if valinta == 2:
        sys.exit()

        
if __name__ == "__main__":
    menu()