import getpass

user = getpass.getuser()


def cteni(filename):
    file = open(filename, "r")
    cti_jeste = True
    soubor = []
    while cti_jeste:
        radek_str = file.readline()
        radek_str = radek_str.rstrip('\r\n')
        delka_radku = len(radek_str)

        if delka_radku == 0:
            cti_jeste = False
            continue

        if radek_str == "</settings>":
            cti_jeste = False

        soubor.append(radek_str)
    file.close()
    return soubor

def vycitani(soubor):
    delka = len(soubor)
    HLjazyk = 0
    VEjazyk = 0
    for x in range(0, delka):
        radek = soubor[x]
        delka_radku = len(radek)
        if radek.startswith('    <setting id="preferred_language"'):
            HLjazyk = radek[delka_radku-11]
        if radek.startswith('    <setting id="fallback_language"'):
            VEjazyk = radek[delka_radku-11]
    return HLjazyk, VEjazyk

def zmena(radek , jazyk, jazyk2):
    delka = len(radek)
    nov_radek = [0]*delka
    for x in range(0, delka):
        nov_radek[x] = radek[x]
    nov_radek[delka-12] = jazyk
    nov_radek[delka-11] = jazyk2
    str1 = ""    
    for ele in nov_radek:  
        str1 += ele
    return str1


def prepisovani(HLjazyk, VEjazyk, soubor):
    delka = len(soubor)
    for x in range(0, delka):
        radek = soubor[x]
        delka_radku = len(radek)
        if x == 1:
            print(type(delka_radku))
            print(type(radek))
        if radek.startswith('    <setting id="preferred_language"'):
            print(HLjazyk)
            if HLjazyk == "0":
                radek = zmena(radek , "c", "s")
                print(0)
            if HLjazyk == "2":
                radek = zmena(radek , "s", "k")
                print(1)
            if HLjazyk == "3":
                radek = zmena(radek , "e", "n")
                print(3)
        if radek.startswith('    <setting id="fallback_language"'):
            print(VEjazyk)
            if VEjazyk == "0":
                radek = zmena(radek , "c", "s")
                print(0)
            if VEjazyk == "2":
                radek = zmena(radek , "s", "k")
                print(1)
            if VEjazyk == "3":
                radek = zmena(radek , "e", "n")
        soubor[x] = radek
    return soubor, delka

def zapis(HLjazyk, VEjazyk, user):
    filename =("../../../Users/" + user + "/AppData/Roaming/Kodi/userdata/addon_data/skin.estuary.stream-cinema-2.leia/settings.xml")
    soubor = cteni(filename)
    soubor, delka = prepisovani(HLjazyk, VEjazyk, soubor)
    file = open(filename, "w")
    for x in range(0, delka):
        file.write(soubor[x])
        file.write('\n')
    file.close()

soubor = cteni("../../../Users/" + user + "/AppData/Roaming/Kodi/userdata/addon_data/plugin.video.stream-cinema-2-release/settings.xml")
HLjazyk, VEjazyk = vycitani(soubor)
zapis(HLjazyk, VEjazyk, user)


