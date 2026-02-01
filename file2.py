# Tanpa modules, kita harus menulis function yang sama berulang kali:
# file2.py

def hitung_nilai_persegi(sisi): # Menulis ulang function yang sama!
    return sisi * sisi

luas = hitung_nilai_persegi(10)
print("Luas Persegi = ",luas)