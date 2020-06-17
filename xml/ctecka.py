import getpass
import sys

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
            HLjazyk_int = radek[delka_radku-11]
            if HLjazyk_int == "0":
                HLjazyk = "cs"

            if HLjazyk_int == "2":
                HLjazyk = "sk"

            if HLjazyk_int == "3":
                HLjazyk = "en"

        if radek.startswith('    <setting id="fallback_language"'):
            VEjazyk_int = radek[delka_radku-11]
            if VEjazyk_int == "0":
                VEjazyk = "cs"

            if VEjazyk_int == "2":
                VEjazyk = "sk"

            if VEjazyk_int == "3":
                VEjazyk = "en"

    return HLjazyk, VEjazyk

vstup = str(sys.argv)
soubor = cteni("../../../Users/" + user + "/AppData/Roaming/Kodi/userdata/addon_data/plugin.video.stream-cinema-2-release/settings.xml")
HLjazyk, VEjazyk = vycitani(soubor)
vraceni = "cs"

if vstup == "preferred_language":
    vraceni = HLjazyk

if vstup == "fallback_language":
    vraceni = VEjazyk

file = open("../../../Users/" + user + "/Downloads/vraceni.txt", "w")
file.write(vstup)
file.write("\r")
file.write(vraceni)
file.close()


sys.exit(vraceni)

