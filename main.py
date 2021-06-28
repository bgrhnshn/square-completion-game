def oyunu_başlat():
    oyun = True
    while oyun:
        o1 = [" "]
        o2 = [" "]
        o1[0], o2[0], sa, su = veri_al()
        o1.append(0)
        o2.append(0)
        mp = harita_oluştur(sa, su)
        oyunalani_goster(mp, sa, su)
        while True:
            oyunalani_guncelle(mp, sa, su, o1)
            oyunalani_guncelle(mp, sa, su, o2)
            if o1[1] + o2[1] == len(sa) * len(su):
                break
        if o1[1] > o2[1]:
            print("Birinci oyuncu ({}) kazandi.".format(o1[0]))
        elif o1[1] == o2[1]:
            print("Berabere bitti.")
        else:
            print("İkinci oyuncu ({}) kazandi.".format(o2[0]))
        while True:
            devam = input("Tekrar oynamak istiyor musunuz? (E/H)")
            if devam == "H" or devam == "h":
                oyun = False
            elif devam == "e" or devam == "E":
                break


def oyunalani_guncelle(harita, satir_listesi, sutun_listesi, oyuncu):
    yer = tur_veri_alimi(harita, satir_listesi, sutun_listesi, oyuncu)
    while not yer:
        yer = tur_veri_alimi(harita, satir_listesi, sutun_listesi, oyuncu)
    harita[yer[0]][yer[1]] = yer[2]
    if yer[3] == "D" or yer[3] == "B" or yer[3] == "b" or yer[3] == "d":
        if harita[yer[0]][yer[1] - 1] == " ":
            if not (harita[yer[0]][yer[1] - 2] == " " or harita[yer[0] - 1][yer[1] - 1] == " " or
                    harita[yer[0] + 1][yer[1] - 1] == " "):
                harita[yer[0]][yer[1] - 1] = oyuncu[0]
                oyuncu[1] += 1
        if harita[yer[0]][yer[1] + 1] == " ":
            if not (harita[yer[0]][yer[1] + 2] == " " or harita[yer[0] - 1][yer[1] + 1] == " " or
                    harita[yer[0] + 1][yer[1] + 1] == " "):
                harita[yer[0]][yer[1] + 1] = oyuncu[0]
                oyuncu[1] += 1
    elif yer[3] == "K" or yer[3] == "G" or yer[3] == "k" or yer[3] == "g":
        if harita[yer[0] + 1][yer[1]] == " ":
            if not (harita[yer[0] + 2][yer[1]] == " " or harita[yer[0] + 1][yer[1] - 1] == " " or
                    harita[yer[0] + 1][yer[1] + 1] == " "):
                harita[yer[0] + 1][yer[1]] = oyuncu[0]
                oyuncu[1] += 1
        if harita[yer[0] - 1][yer[1]] == " ":
            if not (harita[yer[0] - 2][yer[1]] == " " or harita[yer[0] - 1][yer[1] - 1] == " " or
                    harita[yer[0] - 1][yer[1] + 1] == " "):
                harita[yer[0] - 1][yer[1]] = oyuncu[0]
                oyuncu[1] += 1

    oyunalani_goster(harita, satir_listesi, sutun_listesi)
    return harita


def tur_veri_alimi(harita, satir_listesi, sutun_listesi, oyuncu):
    print(oyuncu[0],
          "oyuncusunun sirasi aralarina boşluk koyarak satir, sutun ve yon bilgilerini giriniz.(Büyük harflerle ve yönler için K/G/D/B -> 2 B K )")
    girdi = input()
    satir, sutun, yon = girdi.split(sep=" ", maxsplit=2)
    if not (satir in satir_listesi):
        print("Yanliş giriş yaptiniz.1")
        return False
    if not (sutun in sutun_listesi):
        print("Yanliş giriş yaptiniz.2")
        return False
    if yon == "K" or yon == "k":
        yer = [-1, 0, "-", "K"]
    elif yon == "G" or yon == "g":
        yer = [1, 0, "-", "G"]
    elif yon == "D" or yon == "d":
        yer = [0, 1, "|", "D"]
    elif yon == "B" or yon == "b":
        yer = [0, -1, "|", "B"]
    else:
        print("Yanliş giriş yaptiniz.3")
        return False
    yer[0] = yer[0] + 2 * satir_listesi.index(satir) + 1
    yer[1] = yer[1] + 2 * sutun_listesi.index(sutun) + 1
    if harita[yer[0]][yer[1]] != " ":
        print("Dolu bir yer seçtiniz.")
        return False

    return yer


def oyunalani_goster(harita, satir, sutun):
    harita_temp = []
    for index, i in enumerate(harita):
        sira = []
        for jindex, j in enumerate(i):
            sira.append(j)
        harita_temp.append(sira)

    ilk_sira = []
    for column in range(2 * len(sutun) + 1):
        if column % 2 == 0:
            ilk_sira.append(" ")
        else:
            ilk_sira.append(sutun[(column - 1) // 2])
    harita_temp.insert(0, ilk_sira)

    for row in range(2 * (len(satir) + 1)):
        if row == 0 or row % 2 == 1:
            harita_temp[row].insert(0, " ")
        else:
            harita_temp[row].insert(0, satir[(row // 2) - 1])

    for row in harita_temp:
        for column in row:
            print(column, end="")
        print()
    return True


def harita_oluştur(satir, sutun):
    harita = []
    for row in range(2 * len(satir) + 1):
        sira = []
        if row == 0 or row == 2 * len(satir):
            for column in range(2 * len(sutun) - 1):
                sira.append("_")
            sira.insert(0, "*")
            sira.insert(2 * len(sutun) + 1, "*")
        else:
            for column in range(2 * len(sutun) - 1):
                sira.append(" ")
            sira.insert(0, "|")
            sira.insert(2 * len(sutun) + 1, "|")
        harita.append(sira)
    return harita


def karakter_kontrolu(string):
    if len(string) == 1 and string.isalpha():
        return True
    return False


def boyut_kontrolu(sayi, alt_sinir, ust_sinir):
    if sayi.isdigit():
        if ust_sinir >= int(sayi) >= alt_sinir:
            return 1
    return 0


def veri_al():
    sutun = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T"]
    # 1. oyuncu karakteri girişi
    oyuncu1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz: ")
    while not karakter_kontrolu(oyuncu1):
        oyuncu1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz: ")

    # 2. oyuncu karakter girişi
    oyuncu2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz: ")
    while (not karakter_kontrolu(oyuncu2)) or oyuncu2 == oyuncu1:
        oyuncu2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz: ")

    # Oyun alani satir girişi
    satir_sayisi = input("Oyun alaninin satir sayisini giriniz (3-7): ")
    while not boyut_kontrolu(satir_sayisi, 3, 7):
        satir_sayisi = input("Oyun alaninin satir sayisini giriniz (3-7): ")
    satir_sayisi = int(satir_sayisi)
    satir = ["{}".format(str(x)) for x in range(1, satir_sayisi + 1)]

    # Oyun alani sutun girişi
    sutun_sayisi = input("Oyun alaninin sutun sayisini giriniz (3-19): ")
    while not boyut_kontrolu(sutun_sayisi, 3, 19):
        sutun_sayisi = input("Oyun alaninin sutun sayisini giriniz (3-19): ")
    sutun_sayisi = int(sutun_sayisi)
    sutun = sutun[:sutun_sayisi]
    print()
    return oyuncu1, oyuncu2, satir, sutun




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    oyunu_başlat()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
