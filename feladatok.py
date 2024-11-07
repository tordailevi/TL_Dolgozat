import random

def feladat1():
    i:int=1
    while not(i % 2 == 0):
        i:int=int(input("Adjon meg egy páros számot: "))
        if(i % 2 != 0):
            print(f"A(z) {i} nem egy páros szám!")

def feladat2():
    i:int=0
    e:int=0
    harommaloszthato:int=0
    lista=[]
    for i in range(0,13,1):
        randomszam:int=int(random.random()*(150-10))
        lista.append(randomszam)
        print(randomszam)

        if (lista[i] % 3 == 0):
            harommaloszthato += 1
    print(f"A számok között {harommaloszthato} db 3-mal osztható van.")

def feladat3(text, N):
    if len(text) < N:
        print("Nincs N. karakter!")
    else:
        karakter=text[N - 1].upper()  
        print(karakter * 3)  

def feladat4():
    i:int=0
    kilepojel:str=" "
    while not (kilepojel == "@"):
        kilepojel:str=str(input("Adjon meg neveket: "))
        i+=1
        if (kilepojel=="@"):
            print(f"A felhasználó {i-1} nevet adott meg.")
    
def feladat5():
    tipp:str=" "
    while not(tipp=="Kő" or tipp== "Papír" or tipp== "Olló" ):
        tipp:str=str(input("Kő-Papír-Olló?! Add meg a tipped: "))
        gep:int=int(random.random()*3+1)

    felhasznalo_tippje:str=tipp.casefold()
    if(gep==1):
        gep_tippje:str="kő"
    elif(gep==2):
        gep_tippje:str="papír"
    elif(gep==3):
        gep_tippje:str="olló"

    if(felhasznalo_tippje == gep_tippje):
        print("Döntetlen!")

    elif(felhasznalo_tippje=="kő" and gep_tippje=="papír"):
        print("Vesztettél!")

    elif(felhasznalo_tippje=="papír" and gep_tippje=="olló"):
        print("Vesztettél!")

    elif (felhasznalo_tippje=="olló" and gep_tippje=="kő"):
        print("Vesztettél!")

    elif(felhasznalo_tippje=="papír" and gep_tippje=="kő"):
        print("Győztél!")

    elif(felhasznalo_tippje=="olló" and gep_tippje=="papír"):
        print("Győztél!")

    elif (felhasznalo_tippje=="kő" and gep_tippje=="olló"):
        print("Győztél!")