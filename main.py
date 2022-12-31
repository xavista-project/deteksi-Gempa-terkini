"""
Aplikasi Pendeteksi Gempa terkini 
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():


    """
    Tanggal : 30 Desember 2022
    Waktu :  19:10:47 WIB
    Magnitudo : 5.4
    Kedalaman : 10 km
    Lokasi : 8.24 LS - 129.07 BT
    Pusat Gempa : 142 km Tenggara MALUKUBRTDAYA
    Potensi : tidak berpotensi TSUNAMI
    """

    hasil = dict()
    hasil["Tanggal"] = "30 Desember 2022"
    hasil["Waktu"] = "19:10:47 WIB"
    hasil["Magnitudo"] = 5.4
    hasil["Kedalaman"] = "10 km"
    hasil["Lokasi"] = {"LS" : 8.24,  "BT" : 129.07 }
    hasil["Pusat Gempa"] = "142 km Tenggara MALUKUBRTDAYA"
    hasil["Potensi"] = "tidak berpotensi TSUNAMI"
    
    return hasil

def tampilkan_data(result):
    print("Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Kedalaman {result['Kedalaman']}")
    print(f"Lokasi : LS = {result['Lokasi']['LS']}, BT = {result['Lokasi']['BT']}")
    print(f"Pusat Gempa {result['Pusat Gempa']}")
    print(f"Potensi {result['Potensi']}")
    



if __name__ == "__main__":
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data(result)