import random
def feladat01() -> None:
    nev:str = str(input('Írd be kérlek a neved: '))
    kor:int = int(input('Írd be mikor születtél: '))
    karakterek:list[str] = ['@','&','#']

    nev_pasw:str = nev[0].upper() + nev[1:3].capitalize() #javítsd ki, hogy a jelszó az első karakternek adjon .upper-t és a következő 3-nak peddig picit!

    '''
    nev_pasw:str = nev[0].upper() + nev[1:4].lower() -> a karakterlánc 0.indexének a nagybetűs változata, és az azt követő 3 betűnek a kisbetűs változata (A[0] + bcd[1:4])
        VAGY
    nev_pasw:str = nev[0:4].capitalize() -> a karakterlánc visszaadja ugyan azt a stringet és átkonvertálja az első betűjét nagybetűsre (Abcd[0:4])
        a 8.sort csak túlkomplikáltad >-<
    '''

    #kor_pasw:int = int(kor[-2:])
    kor_pasw:int = kor % 100  #sajnos buta vagyok hozzá, és még a pysuli-val sem értetem, hogy ez miért jó....... :D

    '''
    ez a művelet azt jelenti, hogy az életkort elosztjuk 100-zal és megvizsgáljuk hogy mennyi lesz a maradék
    
        pl. ha valaki 35 éves, akkor a kor % 100 eredménye az ugyan úgy 35 lesz, de mivel a 35 nem osztható tökéletesen 100-zal 
            ezért lesz egy maradék és azt továbbra is fel tudod használni majd számításokban
    '''

    karakterek_pasw01:str = ''.join(random.choice(karakterek))
    karakterek_pasw02:str = ''.join(random.choice(karakterek))

    jelszo:str = nev_pasw + str(kor_pasw)  + karakterek_pasw01 + karakterek_pasw02 #itt a kor_pasw-nél írt egy hibát, mely ,,can only concatenate str (not "int") to str"

    '''
    a helyes sor:
    
    jelszo = nev_pasw + str(kor_pasw) + karakterek_pasw01 + karakterek_pasw02
        azért ír ki hibát, mert a kor_pasw az egész szám típusú, de azt egy karakterlánchoz (ez esetben nev_pasw) akarod hozzáadni
        a python nem engedi azt, hogy más típusokat adj össze, ezért a kor_pasw-t először át kell alakítanod hogy össze tudd fűzni többi karakterlánccal
    '''

    print(f'És a jelszavad nem más mint: {jelszo}')