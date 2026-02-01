# matematika.py

def tambah(a, b):
    """Fungsi ini digunakan untuk menjumlahkan dua angka"""
    return a + b

def kurang(a, b):
    """Fungsi ini digunakan untuk mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Fungsi ini digunakan untuk mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Fungsi ini digunakan untuk membagi dua angka"""
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol tidak diizinkan"

# Variable yang bisa digunakan
PI = 3.14159
NAMA_PEMBUAT = "Mahmuddin"

if __name__ == "__main__":
    print("Program ini tidak bisa dijalankan sebagai module!")