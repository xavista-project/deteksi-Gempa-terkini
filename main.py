"""
Aplikasi deteksi gempa terkini
"""


def ekstraksi_data():
    """
    Tanggal : 30 Desember 2022
    Waktu : 19:10:47 WIB
    Magnitudo : 5.4
    Kedalaman : 10 km
    Lokasi : 8.24 LS - 129.07 BT
    Pusat Gempa : 142 km Tenggara MALUKUBRTDAYA 
    Dirasakan : tidak berpotensi TSUNAMI
    """
    hasil = dict()
    hasil["tanggal"] = "30 Desember 2022"
    hasil["waktu"] = "19:10:47 WIB"
    
    print(hasil)
    return hasil

def tampilkan_data(result):
    print(result)

def tampilkan_data():
    pass

if __name__ == '__main__ ':
    print("Aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)

print("Hello World!")