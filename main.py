"""
Aplikasi Pendeteksi Gempa terkini 
MODULARISASI DENGAN FUNCTION
"""
from Gempa_Terkini import ekstraksi_data, tampilkan_data  

if __name__ == "__main__":
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data(result)