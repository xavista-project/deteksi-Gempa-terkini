"""
Aplikasi Pendeteksi Gempa terkini 
MODULARISASI DENGAN FUNCTION
"""

import Gempa_Terkini

if __name__ == "__main__":
    print("Aplikasi Utama")
    result = Gempa_Terkini.ekstraksi_data()
    Gempa_Terkini.tampilkan_data(result)