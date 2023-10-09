# Importujeme potrebné knižnice
import csv
import math
import numpy as np
import matplotlib.pyplot as plt

# Otvoríme CSV súbor - uložený v rovnakom priečinku ako skript
with open('matlabmja.csv', 'r') as file:
    # Vytvoríme inštanciu čítača, ktorý vytvorí "list listov" s ; ako oddeľovačom
    reader = csv.reader(file, delimiter=';')
    # Uložíme dáta
    data_list = list(reader)
    # Odstránime prvý "riadok" (u , y)
    data_list = data_list[1:]

# Súbor sa uzavrie automaticky pri opustení bloku 'with'

# Vytvoríme listy pre údaje 'u' a 'y'
list_u = [float(sublist[0]) for sublist in data_list]
list_y = [float(sublist[1]) for sublist in data_list]


# Definujeme funkciu na výpočet strednej hodnoty
def spocitaj_strednu_hodnotu(list):
    """
    Vypočíta a vráti strednú hodnotu (priemer) listu čísel.

    Args:
        list: List čísel, pre ktorý chceme vypočítať strednú hodnotu.

    Returns:
        float: Stredná hodnota listu.
    """
    stredna_hodnota = 0
    suma = 0
    for i in range(len(list)):
        suma += list[i]

    stredna_hodnota = (1 / len(list)) * suma

    return stredna_hodnota


# Definujeme funkciu na výpočet rozptylu
def spocitaj_rozptyl(list, stredna_hodnota):
    """
    Vypočíta a vráti rozptyl listu čísel.

    Args:
        list: List čísel, pre ktorý chceme vypočítať rozptyl.
        stredna_hodnota: Stredná hodnota listu.

    Returns:
        float: Rozptyl listu.
    """
    rozptyl = 0
    suma = 0
    for i in range(len(list)):
        suma += pow((list[i] - stredna_hodnota), 2)

    rozptyl = (1 / len(list)) * suma

    return rozptyl


# Definujeme funkciu na výpočet kovariácie
def spocitaj_kovariaciu(list1, list2, stredna_hodnota1, stredna_hodnota2):
    """
    Vypočíta a vráti kovariáciu medzi dvoma listami čísel.

    Args:
        list1: Prvý list čísel.
        list2: Druhý list čísel.
        stredna_hodnota1: Stredná hodnota prvého listu.
        stredna_hodnota2: Stredná hodnota druhého listu.

    Returns:
        float: Kovariácia medzi listami.
    """
    suma = 0
    for i in range(len(list1)):
        suma += (list1[i] - stredna_hodnota1) * (list2[i] - stredna_hodnota2)

    kovariacia = (1 / len(list1)) * suma

    return kovariacia


# Definujeme funkciu na výpočet koeficientu korelácie
def spocitaj_koeficient_korelacie(kovariacia, smer_odchylka1, smer_odchylka2):
    """
    Vypočíta a vráti koeficient korelácie medzi dvoma listmi čísel.

    Args:
        kovariacia: Kovariácia medzi listami.
        smer_odchylka1: Smerodajná odchýlka prvého listu.
        smer_odchylka2: Smerodajná odchýlka druhého listu.

    Returns:
        float: Koeficient korelácie.
    """
    koeficient_korelacie = kovariacia / (smer_odchylka1 * smer_odchylka2)

    return koeficient_korelacie


# Definujeme funkciu na výpočet autokorelačnej funkcie
def spocitaj_autokorelacnu_funkciu(list):
    """
    Vypočíta a vráti autokorelačnú funkciu pre zadaný list hodnôt.

    Args:
        list: List hodnôt.

    Returns:
        list: Autokorelačná funkcia.
    """
    vysledok = []
    suma = 0
    maximalny_posun = int(0.1 * len(list))
    for i in range(maximalny_posun):
        for k in range(len(list) - maximalny_posun):
            suma += list[k] * list[k + i]

        suma = (1 / (len(list) - i)) * suma
        vysledok.append(suma)

    return vysledok


# Definujeme funkciu na výpočet vzájomnej korelacnej funkcie
def spocitaj_vzajomne_korelacnu_funkciu(list1, list2):
    """
    Vypočíta a vráti vzájomnú korelačnú funkciu medzi dvoma listami hodnôt.

    Args:
        list1: Prvý list hodnôt.
        list2: Druhý list hodnôt.

    Returns:
        list: Vzájomne korelačná funkcia.
    """
    vysledok = []
    suma = 0
    maximalny_posun = int(0.1 * len(list1))
    for i in range(maximalny_posun):
        for k in range(len(list1) - maximalny_posun):
            suma += list1[k] * list2[k + i]

        suma = (1 / (len(list1) - i)) * suma
        vysledok.append(suma)

    return vysledok


def plot_histogram(data, filename):
    """
    Vytvorí histogram z dát v liste a uloží ho ako obrázok.

    Args:
        data (list): List hodnôt, pre ktorý sa má vytvoriť histogram.
        filename (str): Názov súboru pre uloženie obrázku histogramu.

    Returns:
        None
    """
    # Vytvor histogram
    plt.hist(data, bins=10, edgecolor='black', alpha=0.7)

    # Pridaj popisky
    plt.xlabel('Hodnota')
    plt.ylabel('Frekvencia výskytu')
    plt.title(filename)

    # Ulož graf
    plt.savefig(f"./Plots/{filename}.png")
    plt.clf()


def plot_diskr_dist_func(list, filename):
    """
    Vytvorí distribučnú funkciu pre diskrétne dáta a uloží ju ako obrázok.

    Args:
        data (list): List diskrétnych hodnôt.
        filename (str): Názov súboru pre uloženie obrázku distribučnej funkcie.

    Returns:
        None
    """
    # Vzorové dáta
    data = list

    # Usporiadané dáta
    usporiadane_data = sorted(data)

    # Vytvorenie poľa s kumulatívnymi pravdepodobnosťami
    cdf = np.arange(1, len(usporiadane_data) + 1) / len(usporiadane_data)

    # Počet intervalov
    pocet_intervalov = 20

    # Rozdelenie dát do intervalov
    hist, bin_edges = np.histogram(usporiadane_data, bins=pocet_intervalov)

    # Vytvorenie poľa s kumulatívnymi pravdepodobnosťami z intervalového histogramu
    cdf_intervalov = np.cumsum(hist) / len(usporiadane_data)

    # Vytvorenie CDF grafu
    plt.step(bin_edges[:-1], cdf_intervalov, where='post')

    # Pridaj vertikalnu ciaru v x=0
    plt.axvline(x=0, color='black', linestyle=':', label='Vertical Line at 0')

    # Pridaj horizontalnu ciaru v  y=1
    plt.axhline(y=1, color='black', linestyle=':', label='Horizontal Line at 1')

    # Nastavenie popisov osí
    plt.xlabel('Hodnota')
    plt.ylabel('Kumulatívna pravdepodobnosť')
    plt.title(filename + " 20 intervalov")

    # Uloz graf
    plt.savefig(f"./Plots/{filename}.png")
    plt.clf()

def plot_priebeh_funkcie(list, filename, x_axis_label, y_axis_label):
    """
    Vytvorí graf priebehu funkcie z dát a uloží ho ako obrázok.

    Args:
        data (list): List hodnôt pre graf.
        filename (str): Názov súboru pre uloženie obrázku grafu.
        x_axis_label (str): Popis osi x.
        y_axis_label (str): Popis osi y.

    Returns:
        None
    """
    # Vzorové dáta
    data = list

    # Vytvorenie grafu s čiernymi bodmi a spojnicami k y=0
    x = np.arange(len(data))

    # Adjust marker size (e.g., set marker size to 6)
    marker_size = 6
    plt.figure(figsize=(8, 6))  # Increase the figure size (adjust as needed)
    plt.scatter(x, data, color='blue', marker='o', s=marker_size)
    plt.plot([x, x], [np.zeros(len(data)), data], 'b',alpha=0.5)

    # Nastavenie popisov osí
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(filename)

    # Pridaj horizontalnu ciaru v y=0
    plt.axhline(y=0, color='black', linestyle=':', label='Horizontal Line at 0')

    # Zobrazenie grafu
    plt.savefig(f"./Plots/{filename}.png")
    plt.clf()


def vytvor_maticu(a, b, c, d):
    matica = [[a, b], [c, d]]
    return matica


def uloz_data_do_suboru(data):
    # Open the text file in append mode ('a')
    with open("output.txt", "a") as file:
        # Append the new data to the file
        file.write(data)


# Spočítame stredné hodnoty pre 'u' a 'y'
stredna_hodnota_u = spocitaj_strednu_hodnotu(list_u)
stredna_hodnota_y = spocitaj_strednu_hodnotu(list_y)
uloz_data_do_suboru("Stredna Hodnota U = " + str(stredna_hodnota_u) + "\n\n")
uloz_data_do_suboru("Stredna Hodnota Y = " + str(stredna_hodnota_y) + "\n\n")

# Spočítame rozptyly pre 'u' a 'y'
rozptyl_u = spocitaj_rozptyl(list_u, stredna_hodnota_u)
rozptyl_y = spocitaj_rozptyl(list_y, stredna_hodnota_y)
uloz_data_do_suboru("Rozptyl U = " + str(rozptyl_u) + "\n\n")
uloz_data_do_suboru("Rozptyl Y = " + str(rozptyl_y) + "\n\n")

# Spočítame smerodajné odchýlky pre 'u' a 'y'
smer_odchylka_u = math.sqrt(rozptyl_u)
smer_odchylka_y = math.sqrt(rozptyl_y)
uloz_data_do_suboru("Smerodajna Odchylka U = " + str(smer_odchylka_u) + "\n\n")
uloz_data_do_suboru("Smerodajna Odchylka Y = " + str(smer_odchylka_y) + "\n\n")

# Spočítame kovariáciu medzi 'u' a 'y'
kovariacia_u_y = spocitaj_kovariaciu(list_u, list_y, stredna_hodnota_u, stredna_hodnota_y)
kovariacia_y_u = spocitaj_kovariaciu(list_y, list_u, stredna_hodnota_y, stredna_hodnota_u)
uloz_data_do_suboru("Kovariacia_u_y = " + str(kovariacia_u_y) + "\n\n")

print("Kovariacia_u_y : ", kovariacia_u_y)
print("Kovariacia_y_u : ", kovariacia_y_u)

# Vytvorime kovariačnú maticu
matica = vytvor_maticu(smer_odchylka_u, kovariacia_u_y, kovariacia_y_u, smer_odchylka_y)
print(matica[0])
print(matica[1])

uloz_data_do_suboru("Matica - Spocitana = \n" + str(matica[0]) + "\n" + str(matica[1]) + "\n\n")

# Spočítame koeficient korelácie
koeficient_korelacie = spocitaj_koeficient_korelacie(kovariacia_u_y, smer_odchylka_u, smer_odchylka_y)
uloz_data_do_suboru("Koeficient Korelacie " + str(koeficient_korelacie) + "\n\n")

# Vypíšeme výsledky
print("Korelačný koeficient - Spočítaný        :", koeficient_korelacie)

# Porovnáme so vstavanou funkciou
correlation_coefficient = np.corrcoef(list_u, list_y)[0, 1]
print("Korelačný koeficient - Vstavaná Funkcia :", correlation_coefficient)
uloz_data_do_suboru("Korelačný koeficient - Vstavaná Funkcia (numpy.corrcoef) :"  + str(correlation_coefficient) + "\n\n")

autokorelacna_func_u = spocitaj_autokorelacnu_funkciu(list_u)
autokorelacna_func_y = spocitaj_autokorelacnu_funkciu(list_y)

print("Autokorelačná funkcia - u :", autokorelacna_func_u)
print("Autokorelačná funkcia - y :", autokorelacna_func_y)
uloz_data_do_suboru("Autokorelačná funkcia - U :" + str(autokorelacna_func_u) + "\n\n")
uloz_data_do_suboru("Autokorelačná funkcia - Y :" + str(autokorelacna_func_y) + "\n\n")


vzajomne_korelacna_func_u_y = spocitaj_vzajomne_korelacnu_funkciu(list_u, list_y)
uloz_data_do_suboru("Vzajomne Korelacna Funkcia U Y :" + str(vzajomne_korelacna_func_u_y) + "\n\n")

print("Vzájomne korelačná funkcia:", vzajomne_korelacna_func_u_y)

plot_histogram(list_u, "Histogram - U")
plot_histogram(list_y, "Histogram - Y")

plot_diskr_dist_func(list_u, "Diskrétna distribučná funkcia - U")
plot_diskr_dist_func(list_u, "Diskrétna distribučná funkcia - Y")

plot_priebeh_funkcie(list_u, "Priebeh - U", "Iteracia", "Hodnota")
plot_priebeh_funkcie(list_y, "Priebeh - Y", "Iteracia", "Hodnota")

plot_priebeh_funkcie(autokorelacna_func_u, "Autokorelacna Funkcia - U", "Prvok", "Hodnota")
plot_priebeh_funkcie(autokorelacna_func_y, "Autokorelacna Funkcia - Y", "Prvok", "Hodnota")
plot_priebeh_funkcie(vzajomne_korelacna_func_u_y, "Vzajomne korelacna Funkcia", "Prvok", "Hodnota")




