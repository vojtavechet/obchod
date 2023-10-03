celkem_cene = []
polozky = []

plzen = [30,"plzen"]
kozel = [28,"kozel"]
branik = [15,"branik"]

cerene = [159,"cervene"]
bile = [120,"bile"]
krabicak = [54,"krabicak"]


zelena = [199,"zelena"]
rum = [399,"rum"]
becherovka = [359,"becherovka"]

pivok = True
vinok = True
tvrdok = True



notFinished = True
while notFinished:
    pivok = True
    vinok = True
    tvrdok = True
    print("""VYBERTE KATEGORII
    1 - PIVO
    2 - VINO
    3 - DESTILAT
    4 - KASA
                """)

    menu = int(input("zadejte cislo kategorie "))

    if(menu == 1):
        print("""VYBERTE PRODUKT
        1 - PLZEN - 30kc
        2 - KOZEL - 28kc
        3 - BRANIK - 15kc
        4 - ZPET NA VYBER KATEGORIE
                """)
    
        while pivok:
        
            pivo = int(input("zadejte cislo produktu "))
            if (pivo == 1):
                celkem_cene.append(plzen[0])
                polozky.append(plzen[1])
            
            if (pivo == 2):
                celkem_cene.append(kozel[0])
                polozky.append(kozel[1])
            if (pivo == 3):
                celkem_cene.append(branik[0])
                polozky.append(branik[1])
            if (pivo == 4):
                pivok=False

    if(menu == 2):
         print("""VYBERTE PRODUKT
         1 - ČERVENÉ - 159kc
         2 - BÍLÉ - 120kc
         3 - KRABIČIČÁK - 54kc
         4 - ZPET NA VYBER KATEGORIE
                """)
    
         while vinok:        
            vino = int(input("zadejte cislo produktu "))
            if (vino == 1):
                celkem_cene.append(cerene[0])
                polozky.append(cerene[1])
            
            if (vino == 2):
                celkem_cene.append(bile[0])
                polozky.append(bile[1])
            if (vino == 3):
                celkem_cene.append(krabicak[0])
                polozky.append(krabicak[1])
            if (vino == 4):
                vinok = False              
       
    if(menu == 3):
         print("""VYBERTE PRODUKT
         1 - ZELENÁ - 199kc
         2 - RUM - 399kc
         3 - BECHEROVKA - 359kc
         4 - ZPET NA VYBER KATEGORIE
                """)
    
         while tvrdok:        
            tvrdy = int(input("zadejte cislo produktu "))
            if (tvrdy == 1):
                celkem_cene.append(zelena[0])
                polozky.append(zelena[1])
            
            if (tvrdy == 2):
                celkem_cene.append(rum[0])
                polozky.append(rum[1])
            if (tvrdy == 3):
                celkem_cene.append(becherovka[0])
                polozky.append(becherovka[1])
            if (tvrdy == 4):
                tvrdok = False              
       


    
    if (menu == 4):
        print( polozky)
        soucet = sum(celkem_cene)
        print(soucet)
        notFinished = False


    elif ():
        print("neplatne cislo")
        continue

